"""Equivalence test: batch mapper (vectorised) vs streaming mapper (row by row) must agree on every row."""
import sys, numpy as np, pandas as pd
from dataclasses import replace
from mapper import *
from stream_mapper import StreamMapper
df = load(sys.argv[1]); trip = df.trip_uuid_
cols = ["trip_uuid_", "driver_uuid_", "ts", "ME_Car_speed_mean", "ME_AWS_time_indicator_median", "ME_AWS_pedestrian_dz_mean"] + \
       [c for c in df.columns if c.startswith(("iDreams_Headway_Map_level_", "iDreams_Fatigue_Map_level_", "iDreams_Speeding_Map_level_", "DEM_evt_hb_lvl_")) and c.endswith("_sum")]
rows = df[cols].to_dict("records")
order = sorted(range(len(df)), key=lambda i: (rows[i]["ts"], i))      # global arrival order by time (stable)
ok_all = True
for name, cfg in [("default (ge30, first2)", Config()), ("dominant/first2", replace(Config(), tailgating="dominant")),
                  ("gt0/episode", replace(Config(), tailgating="gt0", fatigue_emit="episode")),
                  ("ge30/per_minute", replace(Config(), fatigue_emit="per_minute"))]:
    ev, state, aux, _ = map_events(df, cfg); r10, _ = status_10min(ev, trip, cfg); al = alerts(ev, trip, cfg)
    sm = StreamMapper(cfg); res = [None] * len(df)
    for i in order: res[i] = sm.update(rows[i])
    S = pd.DataFrame(res)
    diffs = {k: int((S[k].values != ev[k].values).sum()) for k in ev.columns}
    diffs["status_r10"] = int((S.status_r10.values != r10.values).sum())
    for a, b in [("alert_y", "yawn>=2/2min"), ("alert_e", "eye_close>=2/2min"), ("alert_p", "phone x1"), ("alert_t", "tailgating>=2/10min")]:
        diffs[b] = int((S[a].values != al[b].values).sum())
    m = aux.moving.values; dsb_b = aux.drive_since_break.values[m]; dsb_s = S.drive_since_break.values[m].astype(float)
    diffs["drive_since_break"] = int((dsb_b != dsb_s).sum())
    ok = all(v == 0 for v in diffs.values()); ok_all &= ok
    print(f"{name:26s} rows={len(df)} events(batch)={int(ev.sum().sum())} alerts(batch)={int(al.sum().sum())} mismatches={diffs} -> {'PASS' if ok else 'FAIL'}")
print("ALL PASS" if ok_all else "SOME FAILED"); sys.exit(0 if ok_all else 1)
