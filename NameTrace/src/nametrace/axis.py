from __future__ import annotations

import numpy as np
import pandas as pd


def bootstrap_ci(values: np.ndarray, n_boot: int = 2000, seed: int = 17) -> tuple[float, float]:
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    if len(values) == 0:
        return float("nan"), float("nan")
    draws = rng.choice(values, size=(n_boot, len(values)), replace=True).mean(axis=1)
    return tuple(np.quantile(draws, [0.025, 0.975]))


def pair_level_gaps(scores: pd.DataFrame) -> pd.DataFrame:
    required = {"pair_id", "model", "task", "evidence", "support_class", "axis_score"}
    missing = required.difference(scores.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    wide = scores.pivot_table(
        index=["pair_id", "model", "task", "evidence"],
        columns="support_class",
        values="axis_score",
        aggfunc="mean",
    ).reset_index()
    wide["gap_atomic_minus_fragmented"] = wide["atomic"] - wide["short_fragmented"]
    return wide


def summarize_gaps(gaps: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for key, grp in gaps.groupby(group_cols, dropna=False):
        key = key if isinstance(key, tuple) else (key,)
        vals = grp["gap_atomic_minus_fragmented"].to_numpy(float)
        lo, hi = bootstrap_ci(vals)
        row = dict(zip(group_cols, key))
        row.update(
            {
                "n": int(len(vals)),
                "mean_gap": float(vals.mean()),
                "ci_low": float(lo),
                "ci_high": float(hi),
                "share_positive": float((vals > 0).mean()),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def task_conditioned_name_support_score(gaps: pd.DataFrame) -> pd.DataFrame:
    return summarize_gaps(gaps, ["model", "task"])
