"""Forecast candidates: a single model, or a blend of several.

A candidate is a string. "ecmwf_ifs025" is that model; "blend:ecmwf_ifs025+gem_seamless"
is the hour-by-hour mean of those two. Blends are here because averaging several
models cancels errors no single model avoids, which is what Apple, the Weather Channel
and the National Weather Service all do and what this pipeline did not: measured on a
30-day holdout on 2026-10-17, an equal-weight blend of the families Apple credits beat
our best single model by 35% on humidity and 8% on dew point, while single-model
selection stayed ahead on wind and pressure. Neither approach wins everywhere, so the
bake-off now scores both and lets the station decide per variable.

Shared by bakeoff.py (scoring), train.py (building pairs) and predict.py (publishing),
so that a candidate means exactly the same thing in all three.
"""
from __future__ import annotations

import pandas as pd

BLEND = "blend:"


def is_blend(cand: str) -> bool:
    return cand.startswith(BLEND)


def members(cand: str) -> list[str]:
    """The models a candidate draws on - one for a plain model, several for a blend."""
    return cand[len(BLEND):].split("+") if is_blend(cand) else [cand]


def make_blend(models) -> str:
    """Name a blend. Members are sorted so the same set always gets the same name."""
    uniq = sorted(set(models))
    return uniq[0] if len(uniq) == 1 else BLEND + "+".join(uniq)


def label(cand: str) -> str:
    """How a candidate reads on the page and in the report."""
    return ("blend of " + ", ".join(members(cand))) if is_blend(cand) else cand


def series(cand: str, frames: dict[str, pd.DataFrame], col: str) -> pd.Series | None:
    """One column of a candidate's forecast, averaging the members of a blend.

    `frames` maps model name -> a frame indexed by timestamp. A member that is missing,
    or that lacks this column, is skipped rather than turning the whole blend to NaN:
    not every model serves every variable, and a blend of the two that do is still a
    better answer than nothing.
    """
    cols = [frames[m][col] for m in members(cand)
            if m in frames and col in frames[m] and frames[m][col].notna().any()]
    if not cols:
        return None
    if len(cols) == 1:
        return cols[0]
    return pd.concat(cols, axis=1).mean(axis=1, skipna=True)


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
