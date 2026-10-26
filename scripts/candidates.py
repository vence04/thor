"""Forecast candidates: a single model, or a blend of several.

A candidate is a string. "ecmwf_ifs025" is that model; "blend:ecmwf_ifs025+gem_seamless"
is the hour-by-hour mean of those two. Blends are here because averaging several
models cancels errors no single model avoids, which is what Apple, the Weather Channel
and the National Weather Service all do and what this pipeline did not: measured on a
30-day holdout on 2026-10-17, an equal-weight blend of the families Apple credits beat
our best single model by 35% on humidity and 8% on dew point, while single-model
selection stayed ahead on wind and pressure. Neither approach wins everywhere, so the
bake-off now scores both and lets the station decide per variable.

A third kind, "stack:icon_seamless=0.3+knmi_seamless=0.7", is a blend whose weights were
learned by regressing the station's readings on every model at once (a "stacked" or
"superensemble" forecast). Tested 2026-10-18 on a 30% holdout against the best single
model after correction: 21% better on wind and 27% on humidity, where the models
disagree about scale and the regression learns whom to trust, and 17% WORSE on
temperature, where twelve near-identical columns overfit about 1,200 training hours.
So a stack is never imposed: bakeoff.py fits one per variable, with non-negative
weights, and puts it in front of the same holdout gate as every other candidate. The
weights live in the name so that train.py and predict.py apply exactly what was judged.

Shared by bakeoff.py (scoring), train.py (building pairs) and predict.py (publishing),
so that a candidate means exactly the same thing in all three.
"""
from __future__ import annotations

import pandas as pd

BLEND = "blend:"
STACK = "stack:"


def is_blend(cand: str) -> bool:
    return cand.startswith(BLEND)


def is_stack(cand: str) -> bool:
    return cand.startswith(STACK)


def members(cand: str) -> list[str]:
    """The models a candidate draws on - one for a plain model, several for a blend."""
    if is_stack(cand):
        return [p.split("=")[0] for p in cand[len(STACK):].split("+")]
    return cand[len(BLEND):].split("+") if is_blend(cand) else [cand]


def weights(cand: str) -> dict[str, float]:
    """Each member's weight: learned for a stack, equal for a blend or a plain model."""
    if is_stack(cand):
        return {p.split("=")[0]: float(p.split("=")[1]) for p in cand[len(STACK):].split("+")}
    ms = members(cand)
    return {m: 1.0 / len(ms) for m in ms}


def make_blend(models) -> str:
    """Name a blend. Members are sorted so the same set always gets the same name."""
    uniq = sorted(set(models))
    return uniq[0] if len(uniq) == 1 else BLEND + "+".join(uniq)


def make_stack(w: dict[str, float]) -> str | None:
    """Name a stack from learned weights: members sorted, weights to three places, a
    member weighing nothing dropped. One surviving member is just that model."""
    keep = {m: round(float(v), 3) for m, v in sorted(w.items()) if v >= 0.0005}
    if not keep:
        return None
    if len(keep) == 1:
        return next(iter(keep))
    # Weights the data could not tell apart (pressure, where every model agrees) come
    # back equal: that is a plain blend, and is named as one so it reads honestly.
    if max(keep.values()) <= 1.05 * min(keep.values()):
        return make_blend(keep)
    return STACK + "+".join(f"{m}={v}" for m, v in keep.items())


def label(cand: str) -> str:
    """How a candidate reads on the page and in the report."""
    if is_stack(cand):
        return "weighted blend of " + ", ".join(f"{m} ({v:.2f})" for m, v in weights(cand).items())
    return ("blend of " + ", ".join(members(cand))) if is_blend(cand) else cand


def weighted_mean(df: pd.DataFrame, w: dict[str, float]) -> pd.Series:
    """Row-wise weighted mean of the columns in `w`, renormalising over the columns
    that have a value in that row. With equal weights this is a plain skipna mean."""
    wt = pd.Series({c: w[c] for c in df.columns if c in w})
    d = df[wt.index]
    num = d.fillna(0.0).mul(wt, axis=1).sum(axis=1)
    den = d.notna().mul(wt, axis=1).sum(axis=1)
    return (num / den).where(den > 0)


def series(cand: str, frames: dict[str, pd.DataFrame], col: str) -> pd.Series | None:
    """One column of a candidate's forecast, averaging the members of a blend (by their
    learned weights for a stack).

    `frames` maps model name -> a frame indexed by timestamp. A member that is missing,
    or that lacks this column, is skipped rather than turning the whole blend to NaN:
    not every model serves every variable, and a blend of the two that do is still a
    better answer than nothing.
    """
    w = weights(cand)
    cols = {m: frames[m][col] for m in w
            if m in frames and col in frames[m] and frames[m][col].notna().any()}
    if not cols:
        return None
    if len(cols) == 1:
        return next(iter(cols.values()))
    return weighted_mean(pd.concat(cols, axis=1), w)


def numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Force every forecast column to a number.

    Open-Meteo sometimes serves a variable a model does not carry as nulls, and the
    column lands in parquet as object dtype. Averaging then silently drops it: on
    2026-10-17 the gust blend lost wind_gusts_10m and surface_pressure exactly this
    way, and the training run failed on a missing column rather than on a wrong one,
    which is the only reason it was noticed.
    """
    out = df.copy()
    for c in out.columns:
        if c not in ("ts", "lead_d", "model") and out[c].dtype == object:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


def load_frames(directory, tag: str) -> dict[str, pd.DataFrame]:
    """Every <tag>_<model>.parquet in a directory, keyed by model name."""
    out = {}
    for f in sorted(directory.glob(f"{tag}_*.parquet")):
        out[f.stem[len(tag) + 1:]] = numeric(pd.read_parquet(f))
    return out
