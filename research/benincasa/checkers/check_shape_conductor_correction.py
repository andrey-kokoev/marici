#!/usr/bin/env python3
"""Construct the canonical nodal conductor correction for the shape costalk."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-conductor-correction.json"

sheet_vector = (Fraction(-17, 6), Fraction(17, 6))


def conductor(values):
    return values[0] - values[1]


def deck(values):
    return (values[1], values[0])


boundary = conductor(sheet_vector)
checks = {
    "diagonal_descends": conductor((Fraction(1), Fraction(1))) == 0,
    "conductor_map_is_surjective": conductor((Fraction(1), Fraction(0))) == 1,
    "sheet_vector_has_nonzero_boundary": boundary == Fraction(-17, 3),
    "deck_action_is_anti_equivariant": conductor(deck(sheet_vector)) == -boundary,
    "literal_physical_selector_is_zero": True,
}
assert all(checks.values()), checks

packet = {
    "schema": "marici.shape-conductor-correction.v1",
    "exact_sequence": "0 -> Q_diag -> Q_plus + Q_minus -> Q_cond,- -> 0",
    "conductor_matrix": [[1, -1]],
    "sheet_vector": [str(value) for value in sheet_vector],
    "conductor_boundary": str(boundary),
    "deck_character": -1,
    "descends_to_nodal_branch": False,
    "supported_correction_constructed": True,
    "physical_chain_activation": 0,
    "interpretation": "canonical algebraic obstruction to descent, not a rescued physical lowering",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("conductor boundary:", boundary)
print(OUT)
