#!/usr/bin/env python3
"""Compare the bounded five-mark presentation at generic and physical twist."""
from __future__ import annotations
import contextlib
import importlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
with contextlib.redirect_stdout(io.StringIO()):
    base = importlib.import_module("physical_four_mark_residue_twisted_derham")

def canonical_reduce(row, pivots):
    """Eliminate every pivot before projecting to free quotient coordinates."""
    row = dict(row)
    while True:
        active = [column for column in row if column in pivots]
        if not active:
            return row
        pivot = max(active)
        coefficient = row[pivot]
        for column, value in pivots[pivot].items():
            base.add_value(row, column, -coefficient * value)

base.reduce_row = canonical_reduce

OUT_DIR = Path(__file__).resolve().parents[1] / "results"

def presentation(gamma: int, ambient: int = 14, cutoff: int = 7):
    low, _columns, pivots, free = base.presentation(
        ("g1", "g2", "g3", "g23", "g31"), gamma, ambient, cutoff,
        minimum_q_level=1,
    )
    assert len(low) >= len(free)
    relations = [dict(row) for pivot, row in pivots.items() if pivot < len(low)]
    return low, free, relations

def relation_rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for row in rows:
        base.add_pivot(dict(row), pivots)
    return len(pivots)

def main() -> None:
    p = base.PRIME
    generic_low, generic_free, generic_relations = presentation(5)
    half_low, half_free, half_relations = presentation((-pow(2, p - 2, p)) % p)
    assert generic_low == half_low
    generic = len(generic_free)
    half = len(half_free)
    generic_relation_rank = relation_rank(generic_relations)
    half_relation_rank = relation_rank(half_relations)
    joint_relation_rank = relation_rank(generic_relations + half_relations)
    generic_union = base.unsplit_union_census(5, 14, 7)
    physical_union = base.unsplit_union_census((-pow(2, p - 2, p)) % p, 14, 7)
    payload = {
        "schema": "marici.rank26-half-twist-specialization-gate.v1",
        "prime": p,
        "ambient_relation_degree": 14,
        "cutoff": 7,
        "marked_poles": ["g1", "g2", "g3", "g23", "g31"],
        "generic_gamma": 5,
        "generic_dimension": generic,
        "physical_gamma": "-1/2",
        "physical_bounded_dimension": half,
        "literal_specialization_preserves_rank26": half == generic == 26,
        "generic_relation_rank": generic_relation_rank,
        "physical_relation_rank": half_relation_rank,
        "joint_relation_rank": joint_relation_rank,
        "bounded_quotient_relation_spaces_equal": joint_relation_rank == generic_relation_rank == half_relation_rank,
        "generic_unsplit_source_saturation_rank": generic_union["unsplit_source_horizontal_saturation_rank"],
        "physical_unsplit_source_saturation_rank": physical_union["unsplit_source_horizontal_saturation_rank"],
        "same_unsplit_source_is_cyclic_in_both_bounded_fibers": generic_union["unsplit_source_horizontal_saturation_rank"] == physical_union["unsplit_source_horizontal_saturation_rank"] == 26,
        "scope": "bounded pole-depth-two presentation; not a complete resonant Betti census",
    }
    payload["passed"] = generic == 26
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"rank26_half_twist_specialization_gate_p{p}.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2), flush=True)
    if not payload["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
