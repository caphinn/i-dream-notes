"""Per-feature deep dive for the advisor brief (section 3.5 numbers + one test graph per feature).
Usage: python feature_deepdive.py <i-Dream-Sample_dataset.csv>   -> figures/g1..g5, deepdive.json
Deterministic; reads the same Config/rules as mapper.py (no new constants)."""
import sys, json, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from mapper import *
OUT = "figures/"; INK, GRID = "#0b0b0b", "#e6e5e1"
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]; GRAY = "#b9b8b3"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#8a8984",
                     "axes.labelcolor": "#52514e", "xtick.color": "#52514e", "ytick.color": "#52514e",
                     "axes.grid": True, "grid.color": GRID, "axes.axisbelow": True})
cfg = Config(); df = load(sys.argv[1]); trip = df.trip_uuid_
ev, state, aux, _ = map_events(df, cfg); mv = aux.moving; hrs = mv.sum() / 60
z = lambda c: df[c].fillna(0); P = lambda p, l: z(f"iDreams_{p}_Map_level_{l}_sum")
F1 = (P("Fatigue", 1) + P("Fatigue", 2) + P("Fatigue", 3)) > 0; F2 = (P("Fatigue", 2) + P("Fatigue", 3)) > 0
dsb, night = aux.drive_since_break, aux.night
pct = lambda m: float(m[mv].mean() * 100); R = {"moving_minutes": int(mv.sum()), "moving_hours": round(hrs, 1)}
def wilson(k, n, zz=1.96):
    p = k / n; d = 1 + zz**2 / n; c = p + zz**2 / (2 * n); m = zz * np.sqrt(p * (1 - p) / n + zz**2 / (4 * n**2)); return (c - m) / d, (c + m) / d
def bar_h(ax, labels, vals, colors, fmt="{:.1f}", xmax=None):
    ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.55)
    for y, x in enumerate(vals[::-1]): ax.text(x + (xmax or max(vals)) * 0.01, y, fmt.format(x), va="center", color=INK, fontsize=9)
    ax.grid(axis="y", visible=False)

# ---- g1 tailgating: precision vs SCGJWD (<=20 m) -------------------------------------------------
H = pd.concat([P("Headway", l) for l in (-1, 0, 1, 2, 3)], axis=1); H3 = H.iloc[:, 4]
spd, hw = aux.speed, df.ME_AWS_hw_measurement_mean; clean = hw.notna() & (hw < 10); dist = hw * spd / 3.6; s50 = spd >= 50
dom = (H3 > 0) & (H3 >= H.iloc[:, :4].max(axis=1))
defs = {"L3 > 0 (old)": H3 > 0, "L3 dominant": dom, "L3 >= 30 s (used)": H3 >= 30}
rows = []
for k, m in defs.items():
    f = m & s50 & clean; n = int(f.sum()); h = int(((dist <= 20) & f).sum()); lo, hi = wilson(h, n)
    rows.append((k, h / n * 100, lo * 100, hi * 100, n)); R[f"tailgating[{k}]"] = dict(checkable=n, within20m=h, precision=round(h / n * 100, 1), ci=[round(lo * 100), round(hi * 100)])
b = s50 & clean; base_p = float(((dist <= 20) & b).sum() / b.sum() * 100); R["tailgating_baseline_pct"] = round(base_p, 1)
fig, ax = plt.subplots(figsize=(7.5, 2.9)); y = np.arange(len(rows))[::-1]
ax.barh(y, [r[1] for r in rows], color=[GRAY, GRAY, C[0]], height=0.5)
ax.errorbar([r[1] for r in rows], y, xerr=[[r[1] - r[2] for r in rows], [r[3] - r[1] for r in rows]], fmt="none", ecolor=INK, capsize=3, lw=1)
for yy, r in zip(y, rows): ax.text(101, yy, f"{r[1]:.1f}%  (n={r[4]})", va="center", fontsize=9, color=INK)
ax.axvline(base_p, color="#8a8984", ls="--", lw=1); ax.text(base_p + 1, 1.5, f"baseline {base_p:.1f}%", fontsize=8, color="#52514e")
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows]); ax.set_xlim(0, 100); ax.set_xlabel("% of checkable flagged minutes with real distance <= 20 m (95% CI)")
ax.set_title("tailgating: precision against SCGJWD's own definition", loc="left", color=INK, fontsize=11); ax.grid(axis="y", visible=False)
fig.subplots_adjust(right=0.78, left=0.2, bottom=0.2); fig.savefig(OUT + "g1_tailgating_precision.png", dpi=160); plt.close()

# ---- g2 yawn: two paths are different signals -----------------------------------------------------
A, B = F1, dsb >= cfg.yawn_min
both, onlyA, onlyB = A & B, A & ~B, ~A & B
R["yawn_minutes_pct"] = dict(path_fatigue=round(pct(A), 1), path_drive120=round(pct(B), 1), either=round(pct(A | B), 1), only_fatigue=round(pct(onlyA), 1), only_drive120=round(pct(onlyB), 1), both=round(pct(both), 1))
R["yawn_overlap"] = dict(drive120_without_fatigue=round(float((B & ~A)[mv & B].mean() * 100), 1), fatigue_without_drive120=round(float((A & ~B)[mv & A].mean() * 100), 1))
e = ev.yawn; R["yawn_events"] = dict(total=int(e.sum()), from_fatigue=int((e & A).sum()), only_drive120=int((e & ~A & B).sum()), share_only_drive120_pct=round(float((e & ~A & B).sum() / e.sum() * 100)))
fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.0), gridspec_kw={"width_ratios": [1.1, 1]})
bar_h(axs[0], ["only Fatigue >= L1", "both", "only drive >= 120 min"], [pct(onlyA), pct(both), pct(onlyB)], [C[1], GRAY, C[1]], "{:.1f}%", 12)
axs[0].set_xlabel("% of moving minutes"); axs[0].set_title("minutes in yawn state", loc="left", fontsize=10, color=INK)
bar_h(axs[1], ["Fatigue path", "drive >= 120 only"], [R["yawn_events"]["from_fatigue"], R["yawn_events"]["only_drive120"]], [C[1], GRAY], "{:.0f}", 1200)
axs[1].set_xlabel("events"); axs[1].set_title(f"{int(e.sum()):,} yawn events by origin", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(OUT + "g2_yawn_paths.png", dpi=160); plt.close()

# ---- g3 eye_close: two ingredients (Fatigue >= L2, night) ------------------------------------------
e = ev.eye_close; both = F2 & night & mv
R["eye_close"] = dict(night_pct=round(pct(night), 1), fatigue_ge2_pct=round(pct(F2), 1), both_pct=round(pct(F2 & night), 1), events=int(e.sum()),
                      events_fatigue_ge2_all=int(((ev.yawn & F2)).sum()))
fig, ax = plt.subplots(figsize=(7.5, 2.6))
bar_h(ax, ["night (time_indicator = 3)", "Fatigue >= L2", "both = eye_close state"], [pct(night), pct(F2), pct(F2 & night)], [GRAY, GRAY, C[2]], "{:.1f}%", 50)
ax.set_xlabel("% of moving minutes"); ax.set_title(f"eye_close = Fatigue >= L2 AND night  ({int(e.sum())} events)", loc="left", color=INK, fontsize=11)
fig.tight_layout(); fig.savefig(OUT + "g3_eye_close_paths.png", dpi=160); plt.close()

# ---- g4 eye_off_road: danger_2m distribution + which signals ---------------------------------------
w = cfg.window
H2 = (P("Headway", 2) + P("Headway", 3)) > 0; SP = (P("Speeding", 2) + P("Speeding", 3)) > 0
HB = sum(z(f"DEM_evt_hb_lvl_{l}_sum") for l in cfg.harsh_levels) > 0
sh, sb, ss = (trailing_sum(x, trip, w) > 0 for x in (H2, HB, SP)); d = aux.danger_2m
dist_d = [float((d[mv] == k).mean() * 100) for k in range(4)]; R["danger_2m_pct"] = [round(x, 1) for x in dist_d]
R["signal_rate_pct"] = dict(headway_ge_L2=round(pct(H2), 1), harsh_MH=round(pct(HB), 1), speeding_ge_L2=round(pct(SP), 1))
m2 = (d >= 2) & mv; n2 = int(m2.sum()); hs = int((m2 & sh & ss & ~sb).sum())
R["eye_off_road_minutes"] = dict(n=n2, headway_speeding_only=hs, share_headway_speeding_only_pct=round(hs / n2 * 100), involving_harsh_brake=int((m2 & sb).sum()))
combos = {"headway + speeding": int((m2 & sh & ss & ~sb).sum()), "headway + harsh brake": int((m2 & sh & sb & ~ss).sum()),
          "speeding + harsh brake": int((m2 & ss & sb & ~sh).sum()), "all three": int((m2 & (d == 3)).sum())}; R["eye_off_road_combos"] = combos
fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.0), gridspec_kw={"width_ratios": [1, 1.15]})
axs[0].bar(["0", "1", "2", "3"], dist_d, color=[GRAY, GRAY, C[3], C[3]], width=0.6)
for i, v in enumerate(dist_d): axs[0].text(i, v + 1, f"{v:.1f}%", ha="center", fontsize=9, color=INK)
axs[0].set_xlabel("danger_2m (signals in last 2 min)"); axs[0].set_ylabel("% of moving minutes"); axs[0].set_title("rule fires at >= 2", loc="left", fontsize=10, color=INK); axs[0].grid(axis="x", visible=False)
bar_h(axs[1], list(combos), list(combos.values()), [C[3], GRAY, GRAY, C[3]], "{:.0f}", 2100); axs[1].set_xlabel("minutes")
axs[1].set_title(f"what the {n2:,} firing minutes consist of", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(OUT + "g4_eye_off_road_signals.png", dpi=160); plt.close()

# ---- g5 phone: nested in eye_off_road, two paths ---------------------------------------------------
PED = z("ME_AWS_pedestrian_dz_mean") > 0; pw = trailing_sum(PED, trip, w) > 0
pa, pb = (d >= 3) & mv, (d >= 2) & pw & (d < 3) & mv
R["phone"] = dict(minutes=int((pa | pb).sum()), path_all3=int(pa.sum()), path_ped=int(pb.sum()), ped_pct=round(pct(PED), 1),
                  rate_phone=round(float(ev.phone.sum() / hrs), 2), rate_eye_off_road=round(float(ev.eye_off_road.sum() / hrs), 2),
                  subset_of_eye_off_road=bool((state["phone"] & mv & ~(state["eye_off_road"] & mv)).sum() == 0))
fig, axs = plt.subplots(1, 2, figsize=(8.5, 2.7), gridspec_kw={"width_ratios": [1, 1.15]})
bar_h(axs[0], ["eye_off_road", "phone"], [R["phone"]["rate_eye_off_road"], R["phone"]["rate_phone"]], [C[3], C[4]], "{:.2f}", 1.6)
axs[0].set_xlabel("events per moving hour"); axs[0].set_title("phone is much rarer (subset)", loc="left", fontsize=10, color=INK)
bar_h(axs[1], ["danger_2m = 3", "danger_2m >= 2 & pedestrian"], [R["phone"]["path_all3"], R["phone"]["path_ped"]], [C[4], GRAY], "{:.0f}", 100)
axs[1].set_xlabel("minutes"); axs[1].set_title(f"{R['phone']['minutes']} firing minutes by path", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(OUT + "g5_phone_paths.png", dpi=160); plt.close()
json.dump(R, open("deepdive.json", "w"), indent=1, ensure_ascii=False); print(json.dumps(R, indent=1, ensure_ascii=False))

# ---- trailing-window rates (the quantities danger_2m actually counts) -------------------------------
R2 = dict(headway_2m=round(pct(sh), 1), harsh_2m=round(pct(sb), 1), speeding_2m=round(pct(ss), 1), pedestrian_2m=round(pct(pw), 1))
R["signal_rate_trailing2m_pct"] = R2; json.dump(R, open("deepdive.json", "w"), indent=1, ensure_ascii=False); print(R2)

# ---- g6 danger_2m: why the 2-minute window matters (signal rate per minute vs in trailing 2 min) -----
raw = dict(zip(["Headway >= L2", "harsh brake M/H", "Speeding >= L2"], [pct(H2), pct(HB), pct(SP)]))
trl = dict(zip(raw, [pct(sh), pct(sb), pct(ss)]))
fig, ax = plt.subplots(figsize=(7.5, 2.9)); y = np.arange(3)[::-1]
ax.barh(y + 0.17, list(raw.values()), height=0.32, color=GRAY, label="in this minute only")
ax.barh(y - 0.17, list(trl.values()), height=0.32, color=C[3], label="in last 2 minutes (used)")
for yy, a, b_ in zip(y, raw.values(), trl.values()):
    ax.text(a + 0.5, yy + 0.17, f"{a:.1f}%", va="center", fontsize=9, color=INK); ax.text(b_ + 0.5, yy - 0.17, f"{b_:.1f}%", va="center", fontsize=9, color=INK)
ax.set_yticks(y); ax.set_yticklabels(list(raw)); ax.set_xlim(0, 38); ax.set_xlabel("% of moving minutes where the signal is present"); ax.grid(axis="y", visible=False)
ax.legend(frameon=False, loc="lower right"); ax.set_title("three signals that make up danger_2m", loc="left", color=INK, fontsize=11)
fig.tight_layout(); fig.savefig(OUT + "g6_danger_2m_signals.png", dpi=160); plt.close()
R["signal_rate_raw_pct"] = {k: round(v, 1) for k, v in raw.items()}; json.dump(R, open("deepdive.json", "w"), indent=1, ensure_ascii=False)
