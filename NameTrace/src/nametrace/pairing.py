from __future__ import annotations

import math

import pandas as pd


def match_score(row: pd.Series) -> float:
    first_char_mismatch = 0.0 if bool(row["first_char_match"]) else 1.0
    return (
        abs(float(row["high_log_count"]) - float(row["low_log_count"]))
        + 0.25 * abs(float(row["high_name_length"]) - float(row["low_name_length"]))
        + 1.5 * abs(float(row["high_race_share"]) - float(row["low_race_share"]))
        + 1.5 * abs(float(row["high_gender_share"]) - float(row["low_gender_share"]))
        + 0.25 * first_char_mismatch
    )


def build_candidate_pairs(names: pd.DataFrame) -> pd.DataFrame:
    required = {
        "name",
        "support_class",
        "race_group",
        "gender_group",
        "count",
        "race_share",
        "gender_share",
    }
    missing = required.difference(names.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")

    rows: list[dict[str, object]] = []
    high = names[names["support_class"].eq("atomic")].copy()
    low = names[names["support_class"].eq("short_fragmented")].copy()
    for (race, gender), hgrp in high.groupby(["race_group", "gender_group"]):
        lgrp = low[low["race_group"].eq(race) & low["gender_group"].eq(gender)]
        for _, h in hgrp.iterrows():
            for _, l in lgrp.iterrows():
                row = {
                    "race_group": race,
                    "gender_group": gender,
                    "high_name": h["name"],
                    "low_name": l["name"],
                    "high_log_count": math.log(float(h["count"])),
                    "low_log_count": math.log(float(l["count"])),
                    "high_name_length": len(str(h["name"])),
                    "low_name_length": len(str(l["name"])),
                    "high_race_share": float(h["race_share"]),
                    "low_race_share": float(l["race_share"]),
                    "high_gender_share": float(h["gender_share"]),
                    "low_gender_share": float(l["gender_share"]),
                    "first_char_match": str(h["name"])[0].lower() == str(l["name"])[0].lower(),
                }
                row["match_score"] = match_score(pd.Series(row))
                rows.append(row)
    return pd.DataFrame(rows).sort_values(["race_group", "gender_group", "match_score"])


def select_nonoverlapping_pairs(candidates: pd.DataFrame, per_group: int) -> pd.DataFrame:
    selected: list[pd.DataFrame] = []
    for group, grp in candidates.groupby(["race_group", "gender_group"], sort=True):
        used: set[str] = set()
        kept: list[pd.Series] = []
        for _, row in grp.sort_values("match_score").iterrows():
            h = str(row["high_name"]).lower()
            l = str(row["low_name"]).lower()
            if h in used or l in used:
                continue
            kept.append(row)
            used.update([h, l])
            if len(kept) == per_group:
                break
        out = pd.DataFrame(kept)
        out["match_group"] = f"{group[0]}|{group[1]}"
        selected.append(out)
    result = pd.concat(selected, ignore_index=True)
    result.insert(0, "pair_id", [f"name_pair_{i + 1:04d}" for i in range(len(result))])
    return result


def alternating_split(pairs: pd.DataFrame) -> pd.DataFrame:
    out = pairs.copy()
    out["split"] = "heldout"
    for _, idx in out.groupby("match_group").groups.items():
        ordered = list(idx)
        out.loc[ordered[::2], "split"] = "development"
    return out
