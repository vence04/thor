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
from paths import (ACTUALS_DIR, ACTUALS_PARQUET, FORECAST_DIR, MODEL_DIR,
                   MODEL_JSON, REPORTS_DIR, ensure_dirs)  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = MODEL_DIR
OUTDOOR_START = pd.Timestamp("2026-07-13T19:00:00Z")
INHG_TO_HPA = 33.8639

SOURCE_MODEL = "best_match"  # per-variable override comes from bakeoff once data suffices

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


def load_pairs() -> pd.DataFrame:
    a = pd.read_parquet(ACTUALS_PARQUET)
    a["pressure_abs_hpa"] = a["pressure_abs_inhg"] * INHG_TO_HPA

    frames = []
    d0 = pd.read_parquet(FORECAST_DIR / f"day0_{SOURCE_MODEL}.parquet")
    d0 = d0.assign(lead_d=0)
    frames.append(d0.reset_index())
    prev = FORECAST_DIR / f"prevruns_{SOURCE_MODEL}.parquet"
    if prev.exists():
        frames.append(pd.read_parquet(prev).drop(columns=["model"], errors="ignore"))
    fc = pd.concat(frames, ignore_index=True)
    fc["ts"] = pd.to_datetime(fc["ts"], utc=True)
    return fc.merge(a, left_on="ts", right_index=True, how="inner")


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
    pairs = load_pairs()
    actuals = pd.read_parquet(ACTUALS_PARQUET)
    actuals["pressure_abs_hpa"] = actuals["pressure_abs_inhg"] * INHG_TO_HPA
    ensure_dirs()
    stale_notes = []
    result = {"trained_at": pd.Timestamp.now("UTC").isoformat(),
              "source_model": SOURCE_MODEL, "outdoor_start": str(OUTDOOR_START),
              "variables": {}}
    report = ["# Offset model backtest", "",
              f"Source model: `{SOURCE_MODEL}`. Rolling-origin CV, 4 folds. "
              f"Winner must beat raw MAE by >{MIN_IMPROVEMENT:.0%}.", ""]

    for actual_col, (fc_col, full_hist) in VARS.items():
        df = pairs[["ts", "lead_d", fc_col, actual_col]
                   + (["cloud_cover"] if "cloud_cover" in pairs else [])].dropna(
                       subset=[fc_col, actual_col])
        if not full_hist:
            df = df[df["ts"] >= OUTDOOR_START]

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
        params = fit_final(best, df, fc_col, actual_col, use_doy)
        result["variables"][actual_col] = {
            "fc_col": fc_col, "method": best, "n_train": n,
            "span_days": span_d, "use_doy": use_doy, "lgbm_eligible": seasoned,
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
        print(f"{actual_col:18s} n={n:6d} span={span_d:4d}d doy={int(use_doy)} -> {best:5s}  " +
              " ".join(f"{k}={v:.3f}" for k, v in cand.items() if not np.isinf(v)))

    (MODEL_DIR / "model.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (REPORTS_DIR / "backtest.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
