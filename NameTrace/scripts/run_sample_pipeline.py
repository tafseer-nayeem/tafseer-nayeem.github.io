from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nametrace.axis import pair_level_gaps, summarize_gaps, task_conditioned_name_support_score
from nametrace.correction import apply_prior_correction, estimate_support_prior, summarize_correction


def main() -> None:
    out = ROOT / "outputs" / "sample"
    out.mkdir(parents=True, exist_ok=True)

    dev = pd.read_csv(ROOT / "data" / "sample" / "sample_dev_scores.csv")
    heldout = pd.read_csv(ROOT / "data" / "sample" / "sample_heldout_scores.csv")

    heldout_gaps = pair_level_gaps(heldout)
    heldout_gaps.to_csv(out / "pair_gaps.csv", index=False)
    task_conditioned_name_support_score(heldout_gaps).to_csv(out / "task_conditioned_scores.csv", index=False)
    summarize_gaps(heldout_gaps, ["task"]).to_csv(out / "pooled_task_scores.csv", index=False)

    prior = estimate_support_prior(dev)
    adjusted = apply_prior_correction(heldout, prior, strength=1.0)
    summarize_correction(adjusted).to_csv(out / "prior_correction.csv", index=False)

    print(f"Wrote sample outputs to {out}")


if __name__ == "__main__":
    main()
