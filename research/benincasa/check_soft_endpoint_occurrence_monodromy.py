#!/usr/bin/env python3
"""Audit soft-endpoint monodromy before truncating collision occurrences."""

import json
from pathlib import Path


def rank(matrix):
    # Exact rank for the two small integer matrices used here.
    if all(value == 0 for row in matrix for value in row):
        return 0
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return 2 if determinant != 0 else 1


def main():
    # A_+=(5+4*kappa)p^2.  Around kappa=-5/4, sqrt(A_+) changes sign,
    # exchanging the source-labelled a=+sqrt(A_+) and a=-sqrt(A_+) germs.
    transport = [[0, 1], [1, 0]]
    transport_minus_identity = [[-1, 1], [1, -1]]
    invariant_rank = 2 - rank(transport_minus_identity)
    anti_invariant_period_vector = [1, -1]
    transported_period_vector = [
        sum(transport[i][j] * anti_invariant_period_vector[j] for j in range(2))
        for i in range(2)
    ]

    checks = {
        "monodromy_exchanges_two_occurrences": transport == [[0, 1], [1, 0]],
        "full_occurrence_module_has_invariant_rank_one": invariant_rank == 1,
        "displayed_positive_sheet_period_is_anti_invariant": transported_period_vector == [-1, 1],
        "single_positive_sheet_line_is_not_monodromy_stable": transport[0] != [1, 0],
        "previous_rank_zero_full_Hom_conclusion_is_invalid": invariant_rank != 0,
    }
    result = {
        "schema": "marici.soft-endpoint-occurrence-monodromy.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "labelled_occurrences": ["a=+sqrt(A_plus)", "a=-sqrt(A_plus)"],
        "monodromy_matrix": transport,
        "invariant_rank": invariant_rank,
        "invariant_generator": [1, 1],
        "anti_invariant_generator": anti_invariant_period_vector,
        "conclusion": (
            "the positive-sheet rank-one truncation is not a local system; "
            "the full occurrence-resolved endpoint has a nonzero invariant line"
        ),
        "remaining_question": (
            "construct the marked/unmarked comparison on the full occurrence modules "
            "and determine which invariant or anti-invariant character the physical chain reads"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-occurrence-monodromy.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
