from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from nametrace.tokenization import TokenizerAuditConfig, audit_names, summarize_atomic_access


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--names", required=True)
    parser.add_argument("--models", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    names = pd.read_csv(args.names)["name"].dropna().astype(str).tolist()
    models = pd.read_csv(args.models)
    configs = [
        TokenizerAuditConfig(model_id=row.model_id, display_name=row.model_label)
        for row in models.itertuples(index=False)
    ]
    audit = audit_names(names, configs)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    audit.to_csv(out / "tokenizer_audit.csv", index=False)
    summarize_atomic_access(audit).to_csv(out / "tokenizer_summary.csv", index=False)


if __name__ == "__main__":
    main()
