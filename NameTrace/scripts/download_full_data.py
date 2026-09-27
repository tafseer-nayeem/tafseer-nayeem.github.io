from __future__ import annotations

import argparse
import os
from pathlib import Path

from huggingface_hub import snapshot_download

DEFAULT_REPO_ID = "tafseer-nayeem/NameTrace"


def main() -> None:
    parser = argparse.ArgumentParser(description="Download the NameTrace full data bundle from Hugging Face.")
    parser.add_argument(
        "--repo-id",
        default=os.environ.get("NAMETRACE_HF_DATASET", DEFAULT_REPO_ID),
    )
    parser.add_argument("--revision", default=None)
    parser.add_argument("--output", default="data/full")
    args = parser.parse_args()

    if not args.repo_id:
        raise SystemExit("Pass --repo-id <namespace>/NameTrace or set NAMETRACE_HF_DATASET.")

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    snapshot_download(
        repo_id=args.repo_id,
        repo_type="dataset",
        revision=args.revision,
        local_dir=out,
        allow_patterns=["README.md", "data/**"],
    )
    print(f"Downloaded {args.repo_id} to {out}")


if __name__ == "__main__":
    main()
