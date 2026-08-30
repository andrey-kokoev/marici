#!/usr/bin/env python3
"""Verify that the C9 seam carrier data has no pure Gram-normal residue."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "nine-site-maximal-orbit-universal-jacobians.json"
TARGET = ROOT / "results" / "c9-seam-gram-normal-gate.json"


def has_gram_symbol(value) -> bool:
    if isinstance(value, str):
        tokens = value.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").replace("(", " ").replace(")", " ").split()
        return "k" in tokens or "l" in tokens
    if isinstance(value, list):
        return any(has_gram_symbol(item) for item in value)
    if isinstance(value, dict):
        return any(has_gram_symbol(item) for item in value.values())
    return False


def main() -> None:
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = []
    for item in packet["classes"]:
        carrier_data = {
            "labels": item["labels"],
            "wall_solution": item["wall_solution"],
            "base_relations": item["base_relations"],
        }
        gram_dependent = has_gram_symbol(carrier_data)
        rows.append({"canonical_key": item["canonical_key"], "carrier_wall_data_gram_dependent": gram_dependent})
    assert len(rows) == 480
    assert not any(row["carrier_wall_data_gram_dependent"] for row in rows)
    result = {
        "schema": "marici.c9_seam_gram_normal_gate.v1",
        "class_count": 480,
        "all_labelled_carrier_wall_data_independent_of_k_l": True,
        "partial_k_alpha_C": "0",
        "gram_normal_transgression_T_k": "0",
        "residue_dk_over_k_of_H": "0",
        "pure_gram_costalk_activation": False,
        "remaining_scope": "proper finite Landau-wall intersections require the source-labelled seam restriction map",
        "records": rows,
    }
    TARGET.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"classes": 480, "gram_normal_residue": 0, "pure_gram_activation": False}))


if __name__ == "__main__":
    main()
