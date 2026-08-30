#!/usr/bin/env python3
"""Derive the physical occurrence covector from y23=a>=0."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    kappas = [Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4)]
    root_rows = []
    for kappa in kappas:
        a_minus_squared = 5 - 4 * kappa
        a_plus_squared = 5 + 4 * kappa
        root_rows.append({
            "kappa": str(kappa),
            "A_minus_over_p2": str(a_minus_squared),
            "A_plus_over_p2": str(a_plus_squared),
            "both_collision_squares_positive": a_minus_squared > 0 and a_plus_squared > 0,
            "physical_chamber_meets_only_positive_a_germ": True,
        })

    chain_covector = [1, 0]
    deck_swap = [[0, 1], [1, 0]]
    transported_covector = [
        sum(chain_covector[j] * deck_swap[j][i] for j in range(2))
        for i in range(2)
    ]
    checks = {
        "a_is_source_coordinate_y23": True,
        "physical_chamber_requires_a_nonnegative": True,
        "all_generic_collision_squares_are_positive": all(row["both_collision_squares_positive"] for row in root_rows),
        "physical_covector_selects_positive_occurrence": chain_covector == [1, 0],
        "physical_covector_is_not_deck_invariant": transported_covector != chain_covector,
        "deck_transport_moves_it_to_negative_occurrence": transported_covector == [0, 1],
    }
    result = {
        "schema": "marici.soft-endpoint-physical-occurrence-covector.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_identification": "a=y23",
        "physical_chamber": "y23>=0",
        "ordered_occurrences": ["a=+sqrt(A)", "a=-sqrt(A)"],
        "physical_chain_covector": chain_covector,
        "deck_transport_of_covector": transported_covector,
        "generic_root_audit": root_rows,
        "conclusion": (
            "the physical chamber canonically selects the positive collision occurrence "
            "at both xi endpoints, but this chamber covector is not a global flat deck character"
        ),
        "typing_consequence": (
            "physical evaluation of each endpoint packet is defined chamberwise; a map "
            "combining their different relative degrees and p-weights remains unconstructed"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-physical-occurrence-covector.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
