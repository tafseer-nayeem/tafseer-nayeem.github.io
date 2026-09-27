from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nametrace.pairing import alternating_split, build_candidate_pairs, select_nonoverlapping_pairs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--names", required=True)
    parser.add_argument("--per-group", type=int, default=2)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    names = pd.read_csv(args.names)
    candidates = build_candidate_pairs(names)
    pairs = alternating_split(select_nonoverlapping_pairs(candidates, args.per_group))
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    candidates.to_csv(out / "candidate_pairs.csv", index=False)
    pairs.to_csv(out / "selected_pairs.csv", index=False)


if __name__ == "__main__":
    main()
