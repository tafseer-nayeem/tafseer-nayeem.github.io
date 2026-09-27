from __future__ import annotations

import pandas as pd

from .axis import pair_level_gaps, summarize_gaps


def estimate_support_prior(dev_scores: pd.DataFrame) -> pd.DataFrame:
    gaps = pair_level_gaps(dev_scores)
    return (
        gaps.groupby(["model", "task", "evidence"], dropna=False)["gap_atomic_minus_fragmented"]
        .mean()
        .reset_index()
        .rename(columns={"gap_atomic_minus_fragmented": "support_prior"})
    )


def apply_prior_correction(eval_scores: pd.DataFrame, prior: pd.DataFrame, strength: float = 1.0) -> pd.DataFrame:
    gaps = pair_level_gaps(eval_scores)
    merged = gaps.merge(prior, on=["model", "task", "evidence"], how="left")
    merged["support_prior"] = merged["support_prior"].fillna(0.0)
    merged["gap_adjusted"] = merged["gap_atomic_minus_fragmented"] - strength * merged["support_prior"]
    return merged


def summarize_correction(adjusted: pd.DataFrame) -> pd.DataFrame:
    raw = adjusted.rename(columns={"gap_atomic_minus_fragmented": "gap"}).copy()
    adj = adjusted.rename(columns={"gap_adjusted": "gap"}).copy()
    raw_summary = summarize_gaps(
        raw.rename(columns={"gap": "gap_atomic_minus_fragmented"}),
        ["task"],
    ).rename(columns={"mean_gap": "raw_gap", "ci_low": "raw_ci_low", "ci_high": "raw_ci_high"})
    adj_summary = summarize_gaps(
        adj.rename(columns={"gap": "gap_atomic_minus_fragmented"}),
        ["task"],
    ).rename(columns={"mean_gap": "adjusted_gap", "ci_low": "adjusted_ci_low", "ci_high": "adjusted_ci_high"})
    return raw_summary[["task", "raw_gap", "raw_ci_low", "raw_ci_high"]].merge(
        adj_summary[["task", "adjusted_gap", "adjusted_ci_low", "adjusted_ci_high"]],
        on="task",
    )
