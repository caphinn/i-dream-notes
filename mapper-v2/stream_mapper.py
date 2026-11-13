"""Streaming version of mapper v2: consumes ONE row at a time (rows of a trip arrive in time order) and keeps only
bounded state. Uses only the current and past rows, so its output must equal mapper.py (batch). See test_batch_equals_stream.py."""
from collections import deque
import math
from mapper import Config

def _v(row, k):
    x = row.get(k, 0)
    return 0.0 if x is None or (isinstance(x, float) and math.isnan(x)) else x

class StreamMapper:
    EV = ("tailgating", "yawn", "eye_close", "eye_off_road", "phone")
    def __init__(self, cfg=Config()):
        self.cfg = cfg
        self.trip = {}     # trip id -> state
        self.drv = {}      # driver id -> [acc, partial, prev_moving_ts]

    def _trip_state(self, tid):
        if tid not in self.trip:
            self.trip[tid] = dict(h2=deque(maxlen=1), hb=deque(maxlen=1), sp=deque(maxlen=1), ped=deque(maxlen=1),
                                  f={k: deque(maxlen=2) for k in self.EV},          # previous in-state flags (incl. moving)
                                  ev=deque(maxlen=1), evy=deque(maxlen=1), eve=deque(maxlen=1),
                                  tot=deque(maxlen=9), trig={k: deque(maxlen=9) for k in ("y", "e", "p", "t")},
                                  tg=deque(maxlen=9))
        return self.trip[tid]

    def update(self, row):
        c = self.cfg; z = lambda k: _v(row, k)
        st = self._trip_state(row["trip_uuid_"])
        spd = z("ME_Car_speed_mean"); moving = spd > c.moving_kmh
        # --- drive_since_break (per driver, moving rows only)
        dsb = None
        if moving:
            d = self.drv.setdefault(row["driver_uuid_"], [0, False, None]); ts = row["ts"]
            if d[2] is not None:
                stop = (ts - d[2]).total_seconds() / 60 - 1
                if stop >= 45: d[0], d[1] = 0, False
                elif stop >= 30 and d[1]: d[0], d[1] = 0, False
                elif stop >= 15: d[1] = True
            d[0] += 1; d[2] = ts; dsb = d[0]
        # --- row-level signals
        H = [z(f"iDreams_Headway_Map_level_{l}_sum") for l in (-1, 0, 1, 2, 3)]; H3 = H[4]
        F1 = z("iDreams_Fatigue_Map_level_1_sum") + z("iDreams_Fatigue_Map_level_2_sum") + z("iDreams_Fatigue_Map_level_3_sum") > 0
        F2 = z("iDreams_Fatigue_Map_level_2_sum") + z("iDreams_Fatigue_Map_level_3_sum") > 0
        night = row.get("ME_AWS_time_indicator_median") == c.night_indicator
        tail = {"gt0": H3 > 0, "ge30": H3 >= 30, "dominant": H3 > 0 and H3 >= max(H[:4])}[c.tailgating]
        h2 = (H[3] + H3) > 0; sp = (z("iDreams_Speeding_Map_level_2_sum") + z("iDreams_Speeding_Map_level_3_sum")) > 0
        hb = sum(z(f"DEM_evt_hb_lvl_{l}_sum") for l in c.harsh_levels) > 0; ped = z("ME_AWS_pedestrian_dz_mean") > 0
        danger = int(h2 or any(st["h2"])) + int(hb or any(st["hb"])) + int(sp or any(st["sp"]))
        ped_w = ped or any(st["ped"])
        for k, v in (("h2", h2), ("hb", hb), ("sp", sp), ("ped", ped)): st[k].append(v)
        state = {"tailgating": tail and spd >= c.tailgate_kmh,
                 "yawn": F1 or (dsb is not None and dsb >= c.yawn_min),
                 "eye_close": F2 and night,
                 "eye_off_road": danger >= 2, "phone": danger >= 3 or (danger >= 2 and ped_w)}
        out = {}
        for k in self.EV:
            f = bool(state[k] and moving); h = st["f"][k]
            p1 = not (len(h) >= 1 and h[-1]); p2 = not (len(h) >= 2 and h[-2])
            if k in ("yawn", "eye_close") and c.fatigue_emit == "per_minute": e = f
            elif k in ("yawn", "eye_close") and c.fatigue_emit == "first2":   e = f and (p1 or p2)
            else:                                                              e = f and p1
            h.append(f); out[k] = bool(e)
        # --- 10-minute status and priority alerts (same definitions as mapper.status_10min / alerts)
        total = sum(out.values()); r10 = total + sum(st["tot"]); st["tot"].append(total)
        out["status_r10"] = r10
        yaw2 = out["yawn"] + (st["evy"][-1] if st["evy"] else 0); eye2 = out["eye_close"] + (st["eve"][-1] if st["eve"] else 0)
        st["evy"].append(out["yawn"]); st["eve"].append(out["eye_close"])
        tg_buf = list(st["tg"]) + [out["tailgating"]]; tg10 = sum(tg_buf[-10:]); st["tg"].append(out["tailgating"])
        trigs = {"y": yaw2 >= 2, "e": eye2 >= 2, "p": out["phone"], "t": tg10 >= 2}
        for k, t in trigs.items():
            out["alert_" + k] = bool(t and not any(st["trig"][k])); st["trig"][k].append(bool(t))
        out["drive_since_break"] = dsb; out["moving"] = moving
        return out
