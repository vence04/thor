"""Source bake-off: which forecast - which model, or which blend of models - should
each variable be taken from at Bear Paw Trail?

Two records are used, because neither can answer the question alone.

  SITE      the Ecowitt station, hourly, outdoors since 2026-07-13. The only record
            that knows what happens in this hollow, and the one that decides. Three
            months long, summer and autumn, no winter at all.
  REGIONAL  KHIE, Mount Washington Regional at Whitefield, 16 km east: hourly public
            observations since 2024, every season, 13k hours against every model.
            It cannot know the site. It can rank models with real statistical power,
            and it has seen two Januaries.

So the regional record SHORTLISTS and the site record CHOOSES. The shortlist is the
union of the regional top few, the site's own top few and the incumbent, which means
regional evidence can only ever add a candidate the site would not have considered -
never remove the one the site prefers. That matters most for wind, where the two
stations correlate only 0.57 (measured 2026-10-17 over 1,410 overlapping hours;
temperature 0.88, dew point 0.92) because this site is sheltered and KHIE is an
airfield.

Candidates include blends as well as single models - see candidates.py.

Produces reports/source_bakeoff.md and reports/source_models.json.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import candidates as C  # noqa: E402
from paths import (ACTUALS_DIR, ACTUALS_PARQUET, FORECAST_DIR, MODEL_DIR,
                   MODEL_JSON, REPORTS_DIR, ensure_dirs)  # noqa: E402
from train import VARS as TRAIN_VARS, make_bias, make_ridge, site_start  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FC = FORECAST_DIR
INHG_TO_HPA = 33.8639

# Before this the sensors sat indoors (discovered 2026-07-13: Jan "outdoor" temp ~70F,
# wind 0.0 for 4954h, no solar signal). Only pressure is valid earlier.
OUTDOOR_START = pd.Timestamp("2026-07-13T19:00:00Z")

# A candidate is only switched to when it wins over the WHOLE site record AND over the
# last two weeks. Picking on all-history alone is how temperature and dew point were
# moved on 2026-10-12 to models that then did worse on the published record. The
# incumbent keeps the slot unless a challenger beats it on both windows.
RECENT_D = 14
FULL_HISTORY_VARS = {"pressure_abs_hpa"}

# Candidates are ranked by how good they are AFTER correction, out of sample, not by
# their raw error. Raw error rewards a model whose scale happens to suit the site and
# punishes one that tracks the weather better but runs high - and scale is the one
# thing the offset layer removes. Measured 2026-10-17: meteofrance_seamless had the
# best raw wind error here (1.56 against 2.43 for gem_seamless) and the WORST
# correlation of all thirteen models (0.54 against 0.70), purely because every other
# model forecasts an open grid cell and over-predicts wind in this hollow by 1.4x to
# 2.2x. Choosing it on raw error would have thrown away the signal and kept the shape.
CORRECTED_HOLDOUT = 0.30   # the last 30% of the site record, never fitted on
MIN_HOLDOUT_H = 200
# A challenger must be clearly better, not better by a rounding error. Two runs 45
# minutes apart on 2026-10-17 swapped dew point between ncep_nbm_conus and a blend
# containing it, and gusts between two blends differing by 0.07 mph. Switching source
# costs a week of the corrector being fitted to something else, so a tie should stay
# put. Measured on the same holdout, the top six temperature candidates sit inside
# 0.1F of each other - that is the regime this guards.
SWITCH_MARGIN = 0.03       # 3% better, on the criterion in use

# The site record can only speak for seasons it has lived through. See season_veto().
SEASON_LOOKAHEAD_D = 14    # judge the season a fortnight out, not today's
SEASON_EVIDENCE_H = 240    # site hours in that season before its verdict stands alone
# Loose on purpose. At 15% this left one or two candidates out of thirteen, which
# makes the regional record the decider rather than a guard. 25% ruled out ECMWF for
# winter temperature - which is the real finding, it is 48% worse than NBM across two
# regional Januaries - while leaving seven candidates for the site to choose between.
#
# Loose also because of a circularity: ncep_nbm_conus is NOAA's blend, calibrated
# against ASOS observations, and KHIE is an ASOS. It is being marked by its own
# examiner there, so some of its regional lead will not transfer to a hollow 16 km
# away with no instrument feeding NOAA. That is a reason to use this record to exclude
# the clearly bad, never to crown a winner.
SEASON_VETO = 0.25
# ...and never cut below this many, however far ahead the leader is. On winter
# humidity NBM beat everything else by more than 25% at KHIE, which would have left
# the site a choice of one - the regional record deciding outright, which is what the
# circularity above says it must not do.
SEASON_MIN_KEPT = 4

REGIONAL_DIR = FORECAST_DIR / "regional"
REGIONAL_OBS = ACTUALS_DIR / "obs_hie.parquet"
SHORTLIST_REGIONAL = 3    # how many of the regional ranking to put in front of the site
SHORTLIST_SITE = 2        # ...alongside this many of the site's own favourites
BLEND_SIZES = (2, 3, 5)   # blends of the N best regional models are also candidates
# A stack's weights are fitted on the training part of the site record only (the same
# split corrected_skill uses), by non-negative least squares shrunk gently towards equal
# weights so twelve correlated columns cannot swing wildly week to week.
STACK_SHRINK = 0.02       # as a share of the design's scale; 0 would be plain NNLS
STACK_MIN_MEMBERS = 3     # fewer models with a full record than this: no stack

# best_match is what an app gets by default. At this point it is byte-identical to
# gfs_seamless (checked 2026-10-17 against both the archive and the live API), so it
# rides along as the baseline to beat and is excluded from blends, where it would
# simply double-weight GFS.
BASELINE = "best_match"

# actual column -> forecast column
VARMAP = {
    "temp_f": "temperature_2m",
    "humidity_pct": "relative_humidity_2m",
    "dewpoint_f": "dew_point_2m",
    "wind_mph": "wind_speed_10m",
    "gust_mph": "wind_gusts_10m",
    "pressure_abs_hpa": "surface_pressure",
    "precip_in": "precipitation",
}
# KHIE reports sea-level pressure and no rain gauge total we can difference, so those
# two are ranked on the site record alone.
REGIONAL_VARMAP = {k: v for k, v in VARMAP.items()
                   if k not in ("pressure_abs_hpa", "precip_in")}
SEASONS = {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
           6: "summer", 7: "summer", 8: "summer", 9: "fall", 10: "fall", 11: "fall"}


def load_actuals() -> pd.DataFrame:
    a = pd.read_parquet(ACTUALS_PARQUET)
    a["pressure_abs_hpa"] = a["pressure_abs_inhg"] * INHG_TO_HPA
    # hourly precip from cumulative daily rain: increments within each local day
    daily = a["rain_daily_in"]
    inc = daily.diff()
    inc[inc < 0] = daily[inc < 0]  # day rollover: counter resets, new value IS the increment
    a["precip_in"] = inc
    return a


def score(frames: dict, truth: pd.DataFrame, cands: list[str], varmap: dict,
          outdoor_only: bool = True, recent_d: int | None = None,
          seasons: bool = False) -> tuple[pd.DataFrame, pd.DataFrame]:
    """MAE/bias of every candidate against a truth record, per variable."""
    rows, srows = [], []
    for cand in cands:
        for av, fv in varmap.items():
            if av not in truth:
                continue
            f = C.series(cand, frames, fv)
            if f is None:
                continue
            d = (f - truth[av]).dropna()
            if outdoor_only and av not in FULL_HISTORY_VARS:
                d = d[d.index >= site_start(av)]
            if len(d) < 24:
                continue
            row = {"candidate": cand, "variable": av, "n": len(d),
                   "mae": d.abs().mean(), "bias": d.mean(), "rmse": (d ** 2).mean() ** 0.5}
            if recent_d:
                r = d[d.index >= d.index.max() - pd.Timedelta(days=recent_d)]
                row["recent_n"] = len(r)
                row["recent_mae"] = r.abs().mean() if len(r) >= 24 else float("nan")
            rows.append(row)
            if seasons:
                for season, g in d.groupby(d.index.month.map(SEASONS)):
                    srows.append({"candidate": cand, "variable": av, "season": season,
                                  "n": len(g), "mae": g.abs().mean(), "bias": g.mean()})
    return pd.DataFrame(rows), pd.DataFrame(srows)


def corrected_skill(cand: str, frames: dict, actuals: pd.DataFrame,
                    actual_col: str, fc_col: str) -> dict:
    """How well a candidate does on the site AFTER correction, out of sample.

    The last CORRECTED_HOLDOUT of the record is held out. Which corrector to use and
    its parameters are both decided on the earlier part, so the holdout number is an
    honest estimate of what this candidate would actually publish. `raw` is always a
    contender, so a candidate that needs no correction is not penalised.
    """
    f = C.series(cand, frames, fc_col)
    if f is None:
        return {}
    j = pd.concat([f.rename(fc_col), actuals[actual_col].rename(actual_col)],
                  axis=1, sort=False).dropna().sort_index()
    if actual_col not in FULL_HISTORY_VARS:
        j = j[j.index >= site_start(actual_col)]
    if len(j) < MIN_HOLDOUT_H * 3:
        return {}
    j = j.reset_index().rename(columns={"index": "ts", j.columns.name or "ts": "ts"})
    j["ts"] = pd.to_datetime(j["ts"], utc=True)
    j["lead_d"] = 0                       # day-0 archives; leads come from prevruns
    cut = j["ts"].quantile(1 - CORRECTED_HOLDOUT)
    tr, te = j[j["ts"] < cut], j[j["ts"] >= cut]
    if len(te) < MIN_HOLDOUT_H or len(tr) < MIN_HOLDOUT_H:
        return {}

    # choose the corrector on an inner split of the training part only
    inner = tr["ts"].quantile(0.75)
    itr, iva = tr[tr["ts"] < inner], tr[tr["ts"] >= inner]
    use_doy = TRAIN_VARS.get(actual_col, (None, False))[1]
    options = {"raw": None, "bias": make_bias(fc_col, actual_col, True),
               "ridge": make_ridge(fc_col, actual_col, use_doy)}
    inner_scores = {}
    for name, fp in options.items():
        if len(itr) < 50 or len(iva) < 50:
            continue
        try:
            pred = iva[fc_col].values if fp is None else fp(itr, iva)
            inner_scores[name] = float((pred - iva[actual_col]).abs().mean())
        except Exception:                                      # noqa: BLE001
            continue
    if not inner_scores:
        return {}
    method = min(inner_scores, key=inner_scores.get)
    fp = options[method]
    pred = te[fc_col].values if fp is None else fp(tr, te)
    err = pd.Series(pred - te[actual_col].values, index=te["ts"].values)
    recent = err[err.index >= err.index.max() - pd.Timedelta(days=RECENT_D)]
    return {"corrected_mae": float(err.abs().mean()), "corrected_method": method,
            "holdout_n": len(te), "corrected_bias": float(err.mean()),
            "corrected_recent_mae": float(recent.abs().mean()) if len(recent) >= 24
            else float("nan"),
            "corr": float(pd.Series(te[fc_col].values).corr(
                pd.Series(te[actual_col].values)))}


def fit_stack(frames: dict, actuals: pd.DataFrame, actual_col: str, fc_col: str,
              exclude: set[str] | None = None) -> str | None:
    """Learn one weight per model for this variable, on the part of the site record
    that corrected_skill will fit on, and return the stack's name - or None.

    The split must be the one corrected_skill uses, or the holdout would have seen the
    weights. Its cut is a quantile of the hours where the candidate and the station
    both have a value; a stack has a value wherever ANY member does, which is the same
    set of hours whatever the weights, so the cut is taken on the equal-weight blend of
    the same members and is therefore identical.

    The weights are used as proportions: candidates.weighted_mean renormalises them
    over the members present in each hour, so a stack is a weighted average, never a
    scale correction. Scale (a sheltered site's wind at a third of the models') is the
    corrector's job, and the corrector is judged on the same holdout.
    """
    from scipy.optimize import nnls
    exclude = exclude or set()
    names = [m for m in sorted(frames) if m != BASELINE and m not in exclude
             and fc_col in frames[m] and frames[m][fc_col].notna().any()]
    if len(names) < STACK_MIN_MEMBERS:
        return None
    eq = C.series(C.make_blend(names), frames, fc_col)
    j = pd.concat([eq.rename("eq"), actuals[actual_col].rename("y")], axis=1,
                  sort=False).dropna().sort_index()
    if actual_col not in FULL_HISTORY_VARS:
        j = j[j.index >= site_start(actual_col)]
    if len(j) < MIN_HOLDOUT_H * 3:
        return None
    cut = pd.Series(j.index).quantile(1 - CORRECTED_HOLDOUT)
    X = pd.concat([frames[m][fc_col].rename(m) for m in names], axis=1, sort=False)
    X = X.reindex(j.index[j.index < cut]).dropna(how="any")
    y = actuals[actual_col].reindex(X.index)
    if len(X) < MIN_HOLDOUT_H:
        return None
    k = len(names)
    scale = float(np.sqrt((X.values ** 2).mean())) or 1.0
    lam = STACK_SHRINK * scale * np.sqrt(len(X))
    A = np.vstack([X.values, lam * np.eye(k)])
    b = np.concatenate([y.values, np.full(k, lam / k)])
    w, _ = nnls(A, b)
    return C.make_stack(dict(zip(names, w)))


def score_leads(actuals: pd.DataFrame) -> pd.DataFrame:
    rows = []
    lead_map = {"temp_f": "temperature_2m", "wind_mph": "wind_speed_10m",
                "gust_mph": "wind_gusts_10m", "humidity_pct": "relative_humidity_2m"}
    for f in sorted(FC.glob("prevruns_*.parquet")):
        model = f.stem.replace("prevruns_", "")
        fc = pd.read_parquet(f)
        for lead, g in fc.groupby("lead_d"):
            g = g.set_index("ts")
            j = actuals.join(g, how="inner", rsuffix="_fc")
            for av, fv in lead_map.items():
                d = (j[fv] - j[av]).dropna()
                if av not in FULL_HISTORY_VARS:
                    d = d[d.index >= site_start(av)]
                if len(d) < 24:
                    continue
                rows.append({"model": model, "variable": av, "lead_d": lead,
                             "n": len(d), "mae": d.abs().mean(), "bias": d.mean()})
    return pd.DataFrame(rows)


def incumbents() -> dict:
    path = REPORTS_DIR / "source_models.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("by_variable", {})
    except (json.JSONDecodeError, OSError):
        return {}


def coming_season(now: pd.Timestamp | None = None) -> str:
    """The season a fortnight out, so a guard engages before the season arrives."""
    now = now or pd.Timestamp.now("UTC")
    return SEASONS[(now + pd.Timedelta(days=SEASON_LOOKAHEAD_D)).month]


def season_veto(var: str, season: str, site_season_h: int,
                regional_seasonal: pd.DataFrame) -> set[str]:
    """Candidates that are bad in the coming season where the site cannot tell.

    The site record decides everything, but it can only speak for seasons it has
    lived through. It went outdoors on 2026-07-13, so on the day this was written it
    had 1,649 hours of summer and autumn and not one hour of winter, while KHIE had
    5,706 winter hours against every model. Without this, the first cold snap would be
    forecast by whichever model happened to suit an October afternoon.

    This only ever REMOVES a candidate that the regional record says is clearly poor in
    the coming season, and only while the site has too little of that season to judge
    for itself. It cannot promote anything, and it switches itself off as the site
    accumulates its own evidence - by next autumn it will do nothing at all.
    """
    if regional_seasonal.empty or site_season_h >= SEASON_EVIDENCE_H:
        return set()
    g = regional_seasonal[(regional_seasonal.variable == var)
                          & (regional_seasonal.season == season)]
    if g.empty or g["mae"].min() <= 0:
        return set()
    limit = g["mae"].min() * (1 + SEASON_VETO)
    keep = set(g.nsmallest(SEASON_MIN_KEPT, "mae")["candidate"])
    return set(g.loc[g["mae"] > limit, "candidate"]) - keep


def shortlist(var: str, regional: pd.DataFrame, site_models: pd.DataFrame,
              incumbent: str, vetoed: set[str] | None = None) -> list[str]:
    """Which candidates the site record gets to choose between, and why each is there."""
    vetoed = vetoed or set()
    picks = []
    if not regional.empty:
        rg = regional[regional.variable == var].sort_values("mae")
        best = [c for c in rg.candidate
                if not C.is_blend(c) and c != BASELINE and c not in vetoed]
        picks += best[:SHORTLIST_REGIONAL]
        for n in BLEND_SIZES:
            if len(best) >= n:
                picks.append(C.make_blend(best[:n]))
    sg = site_models[site_models.variable == var].sort_values("mae")
    picks += [c for c in sg.candidate
              if c != BASELINE and c not in vetoed][:SHORTLIST_SITE]
    picks += [incumbent, BASELINE]
    seen, out = set(), []
    for p in picks:
        if p and p not in seen:
            seen.add(p)
            out.append(p)
    return out


def choose_sources(site: pd.DataFrame, regional: pd.DataFrame, current: dict,
                   vetoes: dict | None = None) -> dict:
    """Pick each variable's source on corrected, out-of-sample skill at the site.

    Falls back to raw error only where the corrected scorer could not judge: too
    little history, or a variable the trainer does not model.
    """
    chosen, notes = {}, []
    for var, g in site.groupby("variable"):
        g = g.set_index("candidate")
        judged = (g["corrected_mae"].notna() if "corrected_mae" in g
                  else pd.Series(False, index=g.index))
        col, rcol = (("corrected_mae", "corrected_recent_mae") if judged.any()
                     else ("mae", "recent_mae"))
        basis = "corrected" if col == "corrected_mae" else "raw"
        pool = g[judged] if judged.any() else g
        # A candidate the coming season rules out is not eligible, incumbent included -
        # otherwise the switch margin would protect a source that regional winters say
        # is poor and the site cannot yet contradict. Never empty the pool.
        out = (vetoes or {}).get(var, (0, set()))[1]
        if out and not pool.index.difference(list(out)).empty:
            pool = pool.drop(index=[c for c in out if c in pool.index])
        incumbent = current.get(var, BASELINE)
        if incumbent not in pool.index:
            incumbent = pool[col].idxmin()
        challenger = pool[col].idxmin()
        rg = (regional[regional.variable == var].set_index("candidate")["mae"]
              if not regional.empty else pd.Series(dtype=float))
        seen = f", {rg.at[challenger]:.2f} regionally" if challenger in rg.index else ""
        if challenger == incumbent:
            chosen[var] = incumbent
            notes.append(f"{var}: keeping {C.label(incumbent)} "
                         f"({pool.at[incumbent, col]:.2f} {basis}{seen})")
            continue
        r_new, r_old = pool.at[challenger, rcol], pool.at[incumbent, rcol]
        gain = 1 - pool.at[challenger, col] / pool.at[incumbent, col]             if pool.at[incumbent, col] else 0
        if gain < SWITCH_MARGIN:
            chosen[var] = incumbent
            notes.append(f"{var}: keeping {C.label(incumbent)} "
                         f"({pool.at[incumbent, col]:.2f} {basis}); {C.label(challenger)} "
                         f"is only {gain:.1%} better, under the {SWITCH_MARGIN:.0%} margin")
            continue
        if pd.notna(r_new) and pd.notna(r_old) and r_new < r_old:
            chosen[var] = challenger
            notes.append(f"{var}: switching {C.label(incumbent)} -> {C.label(challenger)} "
                         f"({basis} {pool.at[incumbent, col]:.2f} -> "
                         f"{pool.at[challenger, col]:.2f}{seen}; "
                         f"last {RECENT_D}d {r_old:.2f} -> {r_new:.2f})")
        else:
            chosen[var] = incumbent
            why = ("no recent data" if pd.isna(r_new) or pd.isna(r_old)
                   else f"last {RECENT_D}d {r_new:.2f} vs incumbent {r_old:.2f}")
            notes.append(f"{var}: keeping {C.label(incumbent)}; {C.label(challenger)} wins "
                         f"on {basis} skill over the whole record but not recently ({why})")
    for n in notes:
        print("  " + n)
    return chosen


def main() -> None:
    ensure_dirs()
    actuals = load_actuals()
    site_frames = C.load_frames(FC, "day0")
    singles = sorted(site_frames)
    print(f"{len(singles)} models archived: {', '.join(singles)}")

    # 1. the regional record: every model, every season, ranked with real power
    regional, regional_seasonal = pd.DataFrame(), pd.DataFrame()
    if REGIONAL_OBS.exists() and REGIONAL_DIR.is_dir():
        robs = pd.read_parquet(REGIONAL_OBS)
        rframes = C.load_frames(REGIONAL_DIR, "regional")
        rsingles = [m for m in sorted(rframes) if m != BASELINE]
        rcands = rsingles + [C.make_blend(rsingles[:n]) for n in BLEND_SIZES
                             if len(rsingles) >= n] + [BASELINE]
        regional, regional_seasonal = score(rframes, robs, rcands, REGIONAL_VARMAP,
                                            outdoor_only=False, seasons=True)
        # rank the blends by the models that are actually good, not alphabetically
        if not regional.empty:
            better = {}
            for var, g in regional[~regional.candidate.str.startswith(C.BLEND)] \
                    .groupby("variable"):
                order = [c for c in g.sort_values("mae").candidate if c != BASELINE]
                better[var] = [C.make_blend(order[:n]) for n in BLEND_SIZES
                               if len(order) >= n]
            extra = sorted({b for bs in better.values() for b in bs} - set(rcands))
            if extra:
                more, more_s = score(rframes, robs, extra, REGIONAL_VARMAP,
                                     outdoor_only=False, seasons=True)
                regional = pd.concat([regional, more], ignore_index=True)
                regional_seasonal = pd.concat([regional_seasonal, more_s], ignore_index=True)
        print(f"regional record: {len(robs)} hours, "
              f"{robs.index.min():%Y-%m-%d} to {robs.index.max():%Y-%m-%d}")
    else:
        print("regional record not present - ranking on the site alone "
              "(run scripts/fetch_public_obs.py and fetch_archived_forecasts.py)")

    # 2. the site record: single models first, to build each variable's shortlist
    site_models, _ = score(site_frames, actuals, singles, VARMAP, recent_d=RECENT_D)

    # 3. score every shortlisted candidate on the site, and let the site choose
    current = incumbents()
    season = coming_season()
    wanted, vetoes = set(), {}
    for var in VARMAP:
        if var in actuals:
            s = actuals[var].dropna()
            s = s[s.index >= site_start(var)] if var not in FULL_HISTORY_VARS else s
            season_h = int((s.index.month.map(SEASONS) == season).sum())
        else:
            season_h = 0
        out = season_veto(var, season, season_h, regional_seasonal)
        if out:
            vetoes[var] = (season_h, out)
        wanted |= set(shortlist(var, regional, site_models,
                                current.get(var, BASELINE), out))
        # ...plus a stack fitted for this variable, judged like everything else
        if var in TRAIN_VARS:
            stk = fit_stack(site_frames, actuals, var, VARMAP[var], out)
            if stk:
                wanted.add(stk)
    if vetoes:
        print(f"coming season is {season}; the site cannot judge it yet, so the "
              f"regional record rules out what is clearly poor there:")
        for var, (season_h, out) in sorted(vetoes.items()):
            print(f"  {var}: {season_h}h of {season} on site, "
                  f"{len(out)} candidate(s) ruled out")
    site, site_seasonal = score(site_frames, actuals, sorted(wanted), VARMAP,
                                recent_d=RECENT_D, seasons=True)
    # ...then score that shortlist the way the choice is actually made: after
    # correction, on a holdout the corrector never saw.
    extra = [{"candidate": row.candidate, "variable": row.variable,
              **corrected_skill(row.candidate, site_frames, actuals,
                                row.variable, VARMAP[row.variable])}
             for row in site.itertuples() if row.variable in TRAIN_VARS]
    if extra:
        site = site.merge(pd.DataFrame(extra), on=["candidate", "variable"], how="left")
    winners = choose_sources(site, regional, current, vetoes)

    # 4. the report
    out = ["# Source bake-off — Bear Paw Lodge (44.3206, -71.7439)", "",
           f"Site actuals: Ecowitt hourly means, "
           f"{actuals['temp_f'].dropna().index.min():%Y-%m-%d} to "
           f"{actuals['temp_f'].dropna().index.max():%Y-%m-%d}.",
           "Day-0 = archived freshest-run forecasts (Open-Meteo Historical Forecast API).", ""]

    out += ["## Source in use, per variable", "", "| variable | source |", "|---|---|"]
    out += [f"| {v} | {C.label(m)} |" for v, m in sorted(winners.items())]
    out.append("")
    if vetoes:
        out += [f"The coming season is **{season}**, and the Bear Paw station has not "
                f"lived through enough of it to judge, so candidates the Whitefield "
                f"record shows are clearly poor in {season} are not eligible. This "
                f"switches itself off per variable as the station accumulates its own "
                f"{season} hours.", "",
                f"| variable | {season} hours on site | candidates ruled out |",
                "|---|---|---|"]
        out += [f"| {v} | {h} | {len(o)} |" for v, (h, o) in sorted(vetoes.items())]
        out.append("")

    out.append("## Site skill, shortlisted candidates (lower MAE = better)\n")
    for var, g in (site.groupby("variable") if not site.empty else []):
        out += [f"### {var}\n",
                g.sort_values("corrected_mae" if g.get("corrected_mae") is not None
                              and g["corrected_mae"].notna().any() else "mae")[
                    [c for c in ("candidate", "n", "mae", "bias", "corr",
                                 "corrected_method", "corrected_mae", "holdout_n",
                                 "corrected_recent_mae") if c in g]]
                 .to_markdown(index=False, floatfmt=".2f"), ""]

    if not regional.empty:
        out += ["## Regional skill — KHIE, Whitefield NH, every season\n",
                "Ranks models with 13k hours and two winters; the site record above "
                "decides. KHIE is 16 km east and is not this hollow: over the hours "
                "both stations recorded, temperature correlates 0.88 and dew point "
                "0.92, but wind only 0.57.\n"]
        for var, g in regional.groupby("variable"):
            out += [f"### {var}\n",
                    g.sort_values("mae")[["candidate", "n", "mae", "bias", "rmse"]]
                     .to_markdown(index=False, floatfmt=".2f"), ""]
        out.append("## Regional MAE by season (temperature)\n")
        st = regional_seasonal[regional_seasonal.variable == "temp_f"].pivot_table(
            index="candidate", columns="season", values="mae")
        out += [st.to_markdown(floatfmt=".2f"), ""]

    leads = score_leads(actuals)
    out.append("## MAE by lead time, days 1-7 (previous-runs, site)\n")
    if leads.empty:
        out.append("_Not enough outdoor-era data yet._\n")
    for var, g in (leads.groupby("variable") if not leads.empty else []):
        out += [f"### {var}\n",
                g.pivot_table(index="model", columns="lead_d", values="mae")
                 .to_markdown(floatfmt=".2f"), ""]

    (REPORTS_DIR / "source_bakeoff.md").write_text("\n".join(out), encoding="utf-8")
    site.to_csv(REPORTS_DIR / "day0_scores.csv", index=False)
    if not regional.empty:
        regional.to_csv(REPORTS_DIR / "regional_scores.csv", index=False)
    leads.to_csv(REPORTS_DIR / "lead_scores.csv", index=False)
    (REPORTS_DIR / "source_models.json").write_text(
        json.dumps({"chosen_at": pd.Timestamp.now("UTC").isoformat(),
                    "by_variable": winners}, indent=2), encoding="utf-8")
    print("source in use, per variable:")
    for v, m in sorted(winners.items()):
        print(f"  {v}: {C.label(m)}")


if __name__ == "__main__":
    main()
