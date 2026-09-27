from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class TokenizerAuditConfig:
    model_id: str
    display_name: str | None = None
    add_prefix_space: bool = False


def load_tokenizer(model_id: str):
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)


def surface_variants(name: str) -> dict[str, str]:
    return {
        "plain": name,
        "leading_space": f" {name}",
        "title": name.title(),
        "title_leading_space": f" {name.title()}",
    }


def audit_names(names: Iterable[str], configs: Iterable[TokenizerAuditConfig]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    names = list(dict.fromkeys(str(n).strip() for n in names if str(n).strip()))
    for cfg in configs:
        tok = load_tokenizer(cfg.model_id)
        label = cfg.display_name or cfg.model_id
        for name in names:
            for variant, surface in surface_variants(name).items():
                ids = tok(surface, add_special_tokens=False).input_ids
                decoded = tok.decode(ids) if ids else ""
                rows.append(
                    {
                        "model_id": cfg.model_id,
                        "model_label": label,
                        "name": name,
                        "variant": variant,
                        "surface": surface,
                        "num_tokens": len(ids),
                        "single_token": int(len(ids) == 1 and decoded == surface),
                        "token_ids": " ".join(map(str, ids)),
                    }
                )
    return pd.DataFrame(rows)


def summarize_atomic_access(audit: pd.DataFrame, group_cols: list[str] | None = None) -> pd.DataFrame:
    keys = ["model_label"]
    if group_cols:
        keys.extend(group_cols)
    return (
        audit.groupby(keys, dropna=False)
        .agg(
            n_surfaces=("surface", "count"),
            n_single_token=("single_token", "sum"),
            single_token_rate=("single_token", "mean"),
        )
        .reset_index()
    )
