"""Measured check of tailgating definitions against SCGJWD's own definition (speed >= 50 km/h AND distance <= 20 m).
distance (m) = ME_AWS_hw_measurement_mean (headway, seconds) * speed (km/h) / 3.6 ; only minutes with a clean headway
measurement (not NaN, < 10 s) can be checked, so 'checkable' is reported next to every precision."""
import sys, numpy as np, pandas as pd
from mapper import load
df = load(sys.argv[1]); z = lambda c: df[c].fillna(0)
H = pd.concat([z(f"iDreams_Headway_Map_level_{l}_sum") for l in (-1, 0, 1, 2, 3)], axis=1); H3 = H.iloc[:, 4]
spd = df.ME_Car_speed_mean.fillna(0); hw = df.ME_AWS_hw_measurement_mean
clean = hw.notna() & (hw < 10); dist = hw * spd / 3.6; s50 = spd >= 50
dom = (H3 > 0) & (H3 >= H.iloc[:, :4].max(axis=1))
sets = {"L3>0 (D-08)": H3 > 0, "dominant": dom, "L3>=30 s": H3 >= 30,
        "dominant but L3<30 (the 34 extra minutes)": dom & (H3 < 30), "L3>0 but not dominant": (H3 > 0) & ~dom}
def wilson(k, n, z_=1.96):
    if n == 0: return (np.nan, np.nan)
    p = k / n; d = 1 + z_**2 / n; c = p + z_**2 / (2 * n); m = z_ * np.sqrt(p * (1 - p) / n + z_**2 / (4 * n**2))
    return (c - m) / d, (c + m) / d
print(f"{'definition':45s} {'flagged':>8s} {'checkable':>10s} {'<=20 m':>7s} {'precision':>10s}  95% CI (Wilson)   median dist")
for k, m in sets.items():
    f = m & s50; c = f & clean; hit = int(((dist <= 20) & c).sum()); n = int(c.sum()); lo, hi = wilson(hit, n)
    print(f"{k:45s} {int(f.sum()):8d} {n:10d} {hit:7d} {hit/max(n,1)*100:9.1f}%  [{lo*100:4.0f}, {hi*100:4.0f}]%   {dist[c].median():5.1f} m")
# baseline: how often is dist<=20 among ALL checkable minutes at >=50 km/h (what a random flagged minute would score)
b = s50 & clean; print(f"\nbaseline: all checkable minutes at >=50 km/h: n={int(b.sum())}, <=20 m = {((dist<=20)&b).sum()/b.sum()*100:.1f}%")
