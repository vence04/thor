"""Train the hyperlocal correction ("offset") model with data-volume warm-up gates.

Builds (forecast, actual) pairs per variable from day-0 archives + previous-runs
(leads 1-7 d), then bakes off three correctors against raw pass-through:

  raw   — no correction (always the fallback)
  bias  — mean error by lead bucket (+ hour-of-day once enough data)
  ridge — linear model on forecast value + time harmonics + lead
  lgbm  — LightGBM on the same features (gated: needs >= 90 days AND a full year of
          span, because a tree cannot extrapolate past the range it has seen)

Winner per variable = lowest MAE under rolling-origin cross-validation, and must
beat raw by >2% or raw ships. Writes model/model.json (+ lgbm boosters) and
reports/backtest.md. Rerun weekly; models upgrade themselves as data accumulates.
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

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = MODEL_DIR
OUTDOOR_START = pd.Timestamp("2026-07-13T19:00:00Z")
# The outdoor temperature/humidity sensor (WH26) was moved on 2026-10-21 and its new
# position is permanent (Lloyd, 2026-10-26). The station reported nothing on 19 and 20
# October, read 58F against 41F from every model on the 21st, and has run 3.5-5.6F
# warmer than the models since: a different site, so its variables start a new record
# on 22 October and nothing before it is evidence about where the sensor is now. The
# wind array keeps its history: the wind correction still scored 66% better than raw in
# the week after the move, so whatever moved did not change what it measures.
SENSOR_MOVED = pd.Timestamp("2026-10-22T00:00:00Z")
SITE_START = {"temp_f": SENSOR_MOVED, "humidity_pct": SENSOR_MOVED, "dewpoint_f": SENSOR_MOVED}
INHG_TO_HPA = 33.8639


def site_start(var: str) -> pd.Timestamp:
    """The first hour of the station record that speaks for this variable's sensor
    where it is today."""
    return SITE_START.get(var, OUTDOOR_START)

SOURCE_MODEL = "best_match"   # fallback only; the per-variable choice comes from the bake-off

# The bake-off has always ranked the seven models against the station, and nothing read
# the result: every variable came from best_match, which on 2026-10-12 lost on all of
# them (pressure by 41%, gusts 28%, wind 27%, dew point 22%, humidity 9%, temp 7%).
# Each variable now comes from the model that actually forecasts it best here.

# actual col -> (day0/forecast col, uses_full_history)
VARS = {
    "temp_f": ("temperature_2m", False),
    "humidity_pct": ("relative_humidity_2m", False),
    "dewpoint_f": ("dew_point_2m", False),
    "wind_mph": ("wind_speed_10m", False),
    "gust_mph": ("wind_gusts_10m", False),
    "pressure_abs_hpa": ("surface_pressure", True),
}
GATE_BIAS_H = 14 * 24      # pairs needed before bias correction
GATE_RIDGE_H = 45 * 24
GATE_LGBM_H = 90 * 24
MIN_IMPROVEMENT = 0.02     # must beat raw MAE by 2%

# A sensor that has not moved at all for this long is frozen, not becalmed. The WH26
# and WH68 sat at a constant 58.6F from 2026-08-15 to 2026-08-26 and a model trained
# on that span learned to predict 58.6 forever. Frozen hours are excluded from
# training and reported loudly; they are NOT deleted from the parquet.
STALE_WINDOW_H = 24

# Two things need a full seasonal cycle before they are safe, for the same underlying
# reason: a tree cannot predict outside the range it was trained on.
#
#  - sin_doy/cos_doy are meant to carry seasonality, but over a span shorter than a
#    year they are monotonic - a plain time index. A tree splits on them to memorise
#    the level per date, then clamps at the edge, collapsing the forecast to one value.
#  - lgbm itself clamps. Trained on 13 Jul - 15 Aug 2026 (station min 51.6F) it floored
#    the corrected overnight low at 53F while the regional model called 38F. ridge and
#    bias extend linearly and stay honest outside the observed range, so they are the
#    right correctors until the station has actually lived through a year.
SEASONAL_SPAN_D = 365

# Cross-validation above runs over the whole history, which is mostly summer, so a
# corrector can win it while failing on the season it is actually being used in. On
# 2026-09-21, scored against four days of live September readings, the ridge temperature
# model was 7.6F too warm (MAE 7.58 vs raw 3.01): its slope on the regional forecast was
# 0.67, pulling every forecast toward a 65.6F summer average. So the winner must also
# beat raw on the most recent week, fitted only on data from before that week.
RECENT_HOLDOUT_D = 7

# The holdout above scores candidates on ARCHIVED forecasts. What readers actually get
# is the published forecast, at the mix of lead times the page shows, and the two
# disagree: on 2026-10-12 the archive holdout said the temperature offset beat raw
# (4.08 vs 4.41) while the published record said it had run 20% worse and +2.23F too
# warm over 28 days. The published record wins - it is the real outcome - so where the
# scorecard has enough evidence about THIS method, it can veto shipping it.
# Newest window first. 28 days alone has a blind spot: when a correction or a source
# model changes, the 28-day window stays dominated by the OLD method for weeks, its
# share of that window falls below PUBLISHED_MIN_SHARE, and the gate goes quiet for
# exactly the period the new method most needs watching. Measured 2026-10-17: after the
# 2026-10-12 source switch, humidity's bias correction had produced 70% of the last
# 116 published hours and was running 11% WORSE than raw, yet over 28 days it held only
# 28% of the hours, so the gate saw nothing.
PUBLISHED_WINDOWS = ("last_7_days", "last_28_days")
PUBLISHED_MIN_SHARE = 0.5    # the method must have produced most of those forecasts
PUBLISHED_MIN_HOURS = 72     # ...over at least this many hours, or it is not evidence


def source_models() -> dict:
    """Which model each variable is taken from, as decided by the latest bake-off."""
    path = REPORTS_DIR / "source_models.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("by_variable", {})
    except (json.JSONDecodeError, OSError):
        return {}


def _archive(model: str) -> pd.DataFrame | None:
    """One model's day-0 and previous-runs archives, stacked, keyed by ts and lead."""
    d0path = FORECAST_DIR / f"day0_{model}.parquet"
    if not d0path.exists():
        return None
    frames = [pd.read_parquet(d0path).assign(lead_d=0).reset_index()]
    prev = FORECAST_DIR / f"prevruns_{model}.parquet"
    if prev.exists():
        frames.append(pd.read_parquet(prev).drop(columns=["model"], errors="ignore"))
    fc = C.numeric(pd.concat(frames, ignore_index=True))
    fc["ts"] = pd.to_datetime(fc["ts"], utc=True)
    return fc.groupby(["ts", "lead_d"], as_index=False).first()


def load_pairs(source: str = SOURCE_MODEL) -> pd.DataFrame:
    """(forecast, actual) pairs for one source - a single model, or a blend of them.

    A blend is averaged per timestamp and lead before it meets the actuals, so the
    corrector is fitted on exactly the series predict.py will publish. Members with no
    archive are skipped; if none has one, the caller gets an empty frame and falls
    back the same way it would for a model with no data.
    """
    a = pd.read_parquet(ACTUALS_PARQUET)
    a["pressure_abs_hpa"] = a["pressure_abs_inhg"] * INHG_TO_HPA

    w = C.weights(source)
    parts = {m: f for m, f in ((m, _archive(m)) for m in w) if f is not None}
    if not parts:
        return pd.DataFrame()
    if len(parts) == 1:
        fc = next(iter(parts.values()))
    else:
        # a stack's members carry their learned weights; a blend's are equal
        stacked = pd.concat([f.assign(_w=w[m]) for m, f in parts.items()], ignore_index=True)
        num = [c for c in stacked.columns if c not in ("ts", "lead_d", "model", "_w")]
        keys = [stacked["ts"], stacked["lead_d"]]
        out = {}
        for c in num:
            present = stacked["_w"].where(stacked[c].notna(), 0.0)
            out[c] = ((stacked[c].fillna(0.0) * stacked["_w"]).groupby(keys).sum()
                      / present.groupby(keys).sum())
        fc = pd.DataFrame(out).reset_index()
    return fc.merge(a, left_on="ts", right_index=True, how="inner")


def published_verdict(actual_col: str, method: str) -> dict | None:
    """What the last scorecard says about THIS correction, as published.

    Returns None unless the scorecard covers enough hours and the method being
    considered is the one that actually produced most of those forecasts - a result
    earned by `raw` says nothing about whether `ridge` should ship.
    """
    path = REPORTS_DIR / "scorecard.json"
    if not path.exists():
        return None
    try:
        card = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    for window in PUBLISHED_WINDOWS:
        try:
            s = card["windows"][window][actual_col]
        except (KeyError, TypeError):
            continue
        share = (s.get("published_methods") or {}).get(method, 0)
        if s.get("hours", 0) < PUBLISHED_MIN_HOURS or share < PUBLISHED_MIN_SHARE:
            continue
        return {"improvement_pct": s.get("improvement_pct"), "hours": s["hours"],
                "share": share, "window": window,
                "bespoke_mae": s.get("bespoke_mae"), "raw_mae": s.get("raw_mae")}
    return None


def frozen_hours(actuals: pd.DataFrame, col: str) -> pd.DatetimeIndex:
    """Hours where `col` did not change at all across the trailing STALE_WINDOW_H."""
    s = actuals[col].dropna()
    if len(s) < STALE_WINDOW_H:
        return pd.DatetimeIndex([])
    # peak-to-peak, not std: std of identical floats can return ~1e-15, and 58.64 vs
    # 58.64000000000001 in the WH26 freeze was enough to slip past an == 0 test.
    ptp = s.rolling(STALE_WINDOW_H).max() - s.rolling(STALE_WINDOW_H).min()
    flat = (ptp <= 1e-9).fillna(False)
    bad = set()
    for pos in np.flatnonzero(flat.to_numpy()):
        bad.update(s.index[pos - STALE_WINDOW_H + 1:pos + 1])
    return pd.DatetimeIndex(sorted(bad))


def features(df: pd.DataFrame, fc_col: str, use_doy: bool = False) -> pd.DataFrame:
    hour = df["ts"].dt.hour + df["ts"].dt.minute / 60
    doy = df["ts"].dt.dayofyear
    X = pd.DataFrame({
        "fc": df[fc_col].values,
        "lead_d": df["lead_d"].values,
        "sin_h": np.sin(2 * np.pi * hour / 24), "cos_h": np.cos(2 * np.pi * hour / 24),
    }, index=df.index)
    if use_doy:
        X["sin_doy"] = np.sin(2 * np.pi * doy / 365)
        X["cos_doy"] = np.cos(2 * np.pi * doy / 365)
    if "cloud_cover" in df:
        X["cloud"] = df["cloud_cover"].fillna(50).values
    return X


def cv_score(df, fc_col, actual_col, fit_predict, folds=4):
    """Rolling-origin CV: train on past, test on the next chunk. Returns MAE."""
    df = df.sort_values("ts")
    n = len(df)
    errs = []
    for k in range(1, folds + 1):
        split = int(n * (0.4 + 0.15 * (k - 1)))
        end = int(n * (0.4 + 0.15 * k))
        tr, te = df.iloc[:split], df.iloc[split:end]
        if len(tr) < 48 or len(te) < 12:
            continue
        pred = fit_predict(tr, te)
        errs.append((pred - te[actual_col].values))
    if not errs:
        return np.inf
    return float(np.abs(np.concatenate(errs)).mean())


def make_bias(fc_col, actual_col, by_hour):
    def fit_predict(tr, te):
        err = tr[fc_col] - tr[actual_col]
        lead_bias = err.groupby(tr["lead_d"]).mean()
        base = te["lead_d"].map(lead_bias).fillna(err.mean()).values
        if by_hour:
            hb = err.groupby(tr["ts"].dt.hour).mean()
            base = base + te["ts"].dt.hour.map(hb).fillna(0).values * 0.5
        return te[fc_col].values - base
    return fit_predict


def make_ridge(fc_col, actual_col, use_doy):
    from sklearn.linear_model import Ridge
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    def fit_predict(tr, te):
        m = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
        m.fit(features(tr, fc_col, use_doy), tr[actual_col])
        return m.predict(features(te, fc_col, use_doy))
    return fit_predict


def make_lgbm(fc_col, actual_col, use_doy):
    import lightgbm as lgb
    def fit_predict(tr, te):
        m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=15,
                              min_child_samples=40, verbose=-1)
        m.fit(features(tr, fc_col, use_doy), tr[actual_col])
        return m.predict(features(te, fc_col, use_doy))
    return fit_predict


def fit_final(method, df, fc_col, actual_col, use_doy=False):
    """Fit chosen method on ALL data; return serializable params."""
    if method == "bias":
        err = df[fc_col] - df[actual_col]
        by_lead = err.groupby(df["lead_d"]).mean().round(3).to_dict()
        by_hour = (err.groupby(df["ts"].dt.hour).mean() * 0.5).round(3).to_dict() \
            if len(df) >= GATE_BIAS_H * 2 else {}
        return {"bias_by_lead": {str(k): v for k, v in by_lead.items()},
                "bias_by_hour": {str(k): v for k, v in by_hour.items()},
                "bias_global": round(float(err.mean()), 3)}
    if method == "ridge":
        from sklearn.linear_model import Ridge
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import make_pipeline
        X = features(df, fc_col, use_doy)
        m = make_pipeline(StandardScaler(), Ridge(alpha=1.0)).fit(X, df[actual_col])
        scaler, ridge = m.named_steps["standardscaler"], m.named_steps["ridge"]
        return {"features": list(X.columns),
                "scale_mean": scaler.mean_.round(6).tolist(),
                "scale_std": scaler.scale_.round(6).tolist(),
                "coef": ridge.coef_.round(6).tolist(),
                "intercept": round(float(ridge.intercept_), 6)}
    if method == "lgbm":
        import lightgbm as lgb
        X = features(df, fc_col, use_doy)
        m = lgb.LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=15,
                              min_child_samples=40, verbose=-1).fit(X, df[actual_col])
        path = MODEL_DIR / f"lgbm_{actual_col}.txt"
        m.booster_.save_model(str(path))
        return {"features": list(X.columns), "booster_file": path.name}
    return {}


def residual_bands(method_params, method, df, fc_col, actual_col):
    """P10/P90 of residuals per lead bucket for uncertainty bands."""
    err = (df[fc_col] - df[actual_col]).dropna()
    if len(err) < 100:
        return {}
    q = err.groupby(df.loc[err.index, "lead_d"]).quantile([0.1, 0.9]).unstack()
    return {str(k): [round(v[0.1], 2), round(v[0.9], 2)] for k, v in q.iterrows()}


def main() -> None:
    chosen = source_models()
    pair_cache: dict[str, pd.DataFrame] = {}

    def pairs_for(variable: str) -> tuple[pd.DataFrame, str]:
        source = chosen.get(variable, SOURCE_MODEL)
        # a blend is usable as long as ANY member has an archive; load_pairs averages
        # whatever is there. A source with nothing behind it falls back to the default.
        if not any((FORECAST_DIR / f"day0_{m}.parquet").exists()
                   for m in C.members(source)):
            source = SOURCE_MODEL
        if source not in pair_cache:
            pair_cache[source] = load_pairs(source)
        return pair_cache[source], source

    pairs = load_pairs()
    actuals = pd.read_parquet(ACTUALS_PARQUET)
    actuals["pressure_abs_hpa"] = actuals["pressure_abs_inhg"] * INHG_TO_HPA
    ensure_dirs()
    stale_notes = []
    result = {"trained_at": pd.Timestamp.now("UTC").isoformat(),
              "source_model": SOURCE_MODEL, "outdoor_start": str(OUTDOOR_START),
              "site_start": {k: str(v) for k, v in SITE_START.items()},
              "variables": {}}
    report = ["# Offset model backtest", "",
              f"Source model: `{SOURCE_MODEL}`. Rolling-origin CV, 4 folds. "
              f"Winner must beat raw MAE by >{MIN_IMPROVEMENT:.0%}.", ""]

    for actual_col, (fc_col, full_hist) in VARS.items():
        pairs, src = pairs_for(actual_col)
        df = pairs[["ts", "lead_d", fc_col, actual_col]
                   + (["cloud_cover"] if "cloud_cover" in pairs else [])].dropna(
                       subset=[fc_col, actual_col])
        if not full_hist:
            df = df[df["ts"] >= site_start(actual_col)]

        # A frozen sensor is not data. Drop those hours and say so.
        frozen = frozen_hours(actuals, actual_col)
        if len(frozen):
            before = len(df)
            df = df[~df["ts"].isin(frozen)]
            dropped = before - len(df)
            if dropped:
                note = (f"{actual_col}: dropped {dropped} pairs from {len(frozen)} frozen "
                        f"hours ({frozen.min():%Y-%m-%d %H:%M} to {frozen.max():%Y-%m-%d %H:%M} UTC) "
                        f"- sensor value did not change for {STALE_WINDOW_H}h+")
                stale_notes.append(note)
                print(f"  !! {note}")

        # see SEASONAL_SPAN_D: doy harmonics and lgbm both need a full year first
        span_d = (df["ts"].max() - df["ts"].min()).days if len(df) else 0
        seasoned = span_d >= SEASONAL_SPAN_D
        use_doy = seasoned

        n = len(df)
        raw_mae = float((df[fc_col] - df[actual_col]).abs().mean()) if n else float("nan")
        cand = {"raw": raw_mae}
        if n >= GATE_BIAS_H:
            cand["bias"] = cv_score(df, fc_col, actual_col,
                                    make_bias(fc_col, actual_col, n >= GATE_BIAS_H * 2))
        if n >= GATE_RIDGE_H:
            cand["ridge"] = cv_score(df, fc_col, actual_col,
                                     make_ridge(fc_col, actual_col, use_doy))
        if n >= GATE_LGBM_H and seasoned:
            cand["lgbm"] = cv_score(df, fc_col, actual_col,
                                    make_lgbm(fc_col, actual_col, use_doy))

        best = min(cand, key=cand.get)
        if best != "raw" and cand[best] > raw_mae * (1 - MIN_IMPROVEMENT):
            best = "raw"

        recent = None
        if best != "raw":
            cut = df["ts"].max() - pd.Timedelta(days=RECENT_HOLDOUT_D)
            tr, te = df[df["ts"] < cut], df[df["ts"] >= cut]
            if len(te) >= 24 and len(tr) >= GATE_BIAS_H:
                fit_predict = {
                    "bias": lambda: make_bias(fc_col, actual_col, len(tr) >= GATE_BIAS_H * 2),
                    "ridge": lambda: make_ridge(fc_col, actual_col, use_doy),
                    "lgbm": lambda: make_lgbm(fc_col, actual_col, use_doy),
                }[best]()
                rec_mae = float(np.abs(fit_predict(tr, te) - te[actual_col].values).mean())
                rec_raw = float((te[fc_col] - te[actual_col]).abs().mean())
                recent = {"method": best, "mae": round(rec_mae, 3), "raw_mae": round(rec_raw, 3),
                          "n": len(te)}
                if rec_mae > rec_raw * (1 - MIN_IMPROVEMENT):
                    print(f"  !! {actual_col}: {best} loses to raw over the last "
                          f"{RECENT_HOLDOUT_D} days ({rec_mae:.2f} vs {rec_raw:.2f}) - shipping raw")
                    best = "raw"

        # Published record overrules the archive holdout where it has evidence on this method
        published = published_verdict(actual_col, best) if best != "raw" else None
        if published and (published["improvement_pct"] or 0) < MIN_IMPROVEMENT * 100:
            print(f"  !! {actual_col}: {best} was published for "
                  f"{published['share']:.0%} of the {published['window'].replace('last_','').replace('_',' ')} "
                  f"and scored {published['improvement_pct']:+.1f}% against raw "
                  f"({published['bespoke_mae']} vs {published['raw_mae']}, "
                  f"{published['hours']}h) - shipping raw")
            best = "raw"
            recent = dict(recent or {}, published=published)
        params = fit_final(best, df, fc_col, actual_col, use_doy)
        result["variables"][actual_col] = {
            "fc_col": fc_col, "method": best, "n_train": n,
            "source_model": src,
            "span_days": span_d, "use_doy": use_doy, "lgbm_eligible": seasoned,
            "recent_holdout": recent,
            "last_actual": str(df["ts"].max()) if n else None,
            "cv_mae": {k: (None if np.isinf(v) else round(v, 3)) for k, v in cand.items()},
            "params": params,
            "bands": residual_bands(params, best, df, fc_col, actual_col),
        }
        report.append(f"## {actual_col}  (n={n}, method=**{best}**)")
        report.append("| method | CV MAE |")
        report.append("|--------|--------|")
        for k, v in cand.items():
            report.append(f"| {k} | {v:.3f} |")
        report.append("")
        print(f"{actual_col:18s} [{src:14s}] n={n:6d} span={span_d:4d}d doy={int(use_doy)} -> {best:5s}  " +
              " ".join(f"{k}={v:.3f}" for k, v in cand.items() if not np.isinf(v)))

    (MODEL_DIR / "model.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (REPORTS_DIR / "backtest.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
