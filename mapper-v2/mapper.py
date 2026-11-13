"""Mapper v2: i-DREAMS per-minute rows -> G7-style events. Deterministic (no randomness).
Spec: idream-notes/21-mapper-spec-v2.md. Every constant lives in Config with its source."""
from dataclasses import dataclass
import numpy as np, pandas as pd

@dataclass(frozen=True)
class Config:
    moving_kmh: float = 5.0        # team convention, no external source (spec sec.4); sensitivity reported
    tailgate_kmh: float = 50.0     # SCGJWD tailgating definition
    yawn_min: int = 120            # D3.6 Table 6: drive < 2 h = normal
    night_indicator: int = 3       # D6.1 Table 2 (ME_AWS_time_indicator)
    window: int = 2                # Track 1 / priority-alert window (minutes)
    status_window: int = 10        # seniors' 10-minute status rule
    tailgating: str = "ge30"        # 'ge30' (L3 >= half the minute, precision 96%) | 'dominant' | 'gt0'
    fatigue_emit: str = "first2"   # 'first2' | 'episode' | 'per_minute'  (team design choice, see spec)
    harsh_levels: tuple = ("M", "H")

def load(path):
    df = pd.read_csv(path, usecols=lambda c: not c.startswith("Unnamed"))
    df = df.loc[:, [c for c in df.columns if c.lower() != "check"]]
    df["ts"] = pd.to_datetime(df.trip_start_.astype(str) + " " + df.tirp_start_time.astype(str).str[:8],
                              dayfirst=True, errors="coerce") + pd.to_timedelta(df.grpby_seconds, unit="s")
    df = df.sort_values(["trip_uuid_", "grpby_seconds"]).reset_index(drop=True)
    df["vday"] = df.vehicle_uuid_ + "|" + df.trip_start_.astype(str)
    return df

def trailing_sum(x, trip, k):
    """sum of the last k rows (incl. current) inside the same trip"""
    x = x.astype(int); c = x.groupby(trip).cumsum()
    return c - c.groupby(trip).shift(k).fillna(0)

def drive_since_break(df, moving):
    """minutes driven (moving rows) since last complete break, per driver.
    complete break = stop >=45 min, or a stop >=15 min followed by a stop >=30 min (EU 561/2006 Art.7)."""
    d = pd.DataFrame({"drv": df.driver_uuid_, "ts": df.ts, "i": df.index})[moving.values].sort_values(["drv", "ts"])
    out = {}
    for _, g in d.groupby("drv"):
        ts, idx = g.ts.values, g.i.values
        acc, partial, prev = 0, False, None
        for k in range(len(g)):
            if prev is not None:
                stop = (ts[k] - prev) / np.timedelta64(1, "m") - 1
                if stop >= 45: acc, partial = 0, False
                elif stop >= 30 and partial: acc, partial = 0, False
                elif stop >= 15: partial = True
            acc += 1; out[idx[k]] = acc; prev = ts[k]
    return pd.Series(out).reindex(df.index)

def map_events(df, cfg=Config()):
    z = lambda c: df[c].fillna(0)
    P = lambda p, l: z(f"iDreams_{p}_Map_level_{l}_sum")
    spd, trip = df.ME_Car_speed_mean.fillna(0), df.trip_uuid_
    moving = spd > cfg.moving_kmh
    dsb = drive_since_break(df, moving)
    F1 = (P("Fatigue", 1) + P("Fatigue", 2) + P("Fatigue", 3)) > 0
    F2 = (P("Fatigue", 2) + P("Fatigue", 3)) > 0
    night = df.ME_AWS_time_indicator_median == cfg.night_indicator
    H = pd.concat([P("Headway", l) for l in (-1, 0, 1, 2, 3)], axis=1); H3 = H.iloc[:, 4]
    tail = {"gt0": H3 > 0, "ge30": H3 >= 30,
            "dominant": (H3 > 0) & (H3 >= H.iloc[:, :4].max(axis=1))}[cfg.tailgating]
    H2 = (P("Headway", 2) + P("Headway", 3)) > 0
    SP = (P("Speeding", 2) + P("Speeding", 3)) > 0
    HB = sum(z(f"DEM_evt_hb_lvl_{l}_sum") for l in cfg.harsh_levels) > 0
    PED = z("ME_AWS_pedestrian_dz_mean") > 0
    w = cfg.window
    danger = (trailing_sum(H2, trip, w) > 0).astype(int) + (trailing_sum(HB, trip, w) > 0).astype(int) \
             + (trailing_sum(SP, trip, w) > 0).astype(int)
    ped_w = trailing_sum(PED, trip, w) > 0
    state = {  # per-minute state (True while the rule holds)
        "tailgating":   tail & (spd >= cfg.tailgate_kmh),
        "yawn":         F1 | (dsb >= cfg.yawn_min),
        "eye_close":    F2 & night,
        "eye_off_road": danger >= 2,
        "phone":        (danger >= 3) | ((danger >= 2) & ped_w)}
    provenance = {"tailgating": "direct", "yawn": "derived-weak", "eye_close": "derived-weak",
                  "eye_off_road": "proxy-weak", "phone": "proxy-weak"}
    ev = pd.DataFrame(index=df.index)
    for k, s in state.items():
        f = s & moving
        p1 = f.astype(int).groupby(trip).shift(1).fillna(0) == 0   # previous minute not in state
        p2 = f.astype(int).groupby(trip).shift(2).fillna(0) == 0
        if k in ("yawn", "eye_close") and cfg.fatigue_emit == "per_minute": ev[k] = f
        elif k in ("yawn", "eye_close") and cfg.fatigue_emit == "first2":   ev[k] = f & (p1 | p2)
        else:                                                                 ev[k] = f & p1
    aux = pd.DataFrame({"moving": moving, "drive_since_break": dsb, "danger_2m": danger,
                        "night": night, "speed": spd})
    return ev, state, aux, provenance

def status_10min(ev, trip, cfg=Config()):
    total = sum(ev[c].astype(int) for c in ev.columns)
    r = trailing_sum(total, trip, cfg.status_window)
    return r, np.where(r >= 6, "HIGH", np.where(r >= 3, "MEDIUM", "LOW"))

def alerts(ev, trip, cfg=Config()):
    """seniors' priority alerts; an alert is counted once per 10 rows (expires after 10 min, re-trigger resets)"""
    def first(trig):
        t = trig.astype(int); return (t == 1) & ((trailing_sum(t, trip, 10) - t) == 0)
    return pd.DataFrame({
        "yawn>=2/2min":        first(trailing_sum(ev.yawn, trip, 2) >= 2),
        "eye_close>=2/2min":   first(trailing_sum(ev.eye_close, trip, 2) >= 2),
        "phone x1":            first(ev.phone),
        "tailgating>=2/10min": first(trailing_sum(ev.tailgating, trip, 10) >= 2)})
