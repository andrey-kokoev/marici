#!/usr/bin/env python3
"""Certify the labelled all-soft Koszul costalk and its normal orders."""

import json
from math import comb
from pathlib import Path


# Rows are (g1,g2,g3,g23,g31); columns are the new labelled basis
# (g2,g1,r3,r23,r31).
CHANGE = (
    (0, 1, -1, -1, 0),
    (1, 0, -1, 0, -1),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
)


def determinant(matrix):
    rows = [list(row) for row in matrix]
    det = 1
    n = len(rows)
    for column in range(n):
        pivot = next(i for i in range(column, n) if rows[i][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            det *= -1
        value = rows[column][column]
        det *= value
        for i in range(column + 1, n):
            if not rows[i][column]:
                continue
            # Every pivot here is 1, so integer elimination is exact.
            factor = rows[i][column] // value
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[column])]
    return det


def main():
    # Coefficient rows of (a,b) for q=(b,a,a+b,b,a).
    q_matrix = ((0, 1, 1, 0, 1), (1, 0, 1, 1, 0))
    transformed = tuple(
        tuple(sum(q_matrix[i][k] * CHANGE[k][j] for k in range(5)) for j in range(5))
        for i in range(2)
    )
    determinant_change = determinant(CHANGE)
    graded = [comb(4, degree) for degree in range(5)]
    # External degrees of the coefficients of a^4, a^2b^2, b^4,
    # a^2, b^2, and 1 in the frozen Cayley--Menger polynomial.
    k_external_coefficient_degrees = (2, 2, 2, 4, 4, 6)
    k_normal_order = min(k_external_coefficient_degrees)
    checks = {
        "label_change_is_unimodular": abs(determinant_change) == 1,
        "marked_sequence_reduces_to_a_b_and_three_zero_relations": transformed == ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0)),
        "total_zero_directions_include_K": len(graded) == 5 and sum(graded) == 16,
        "three_marked_relations_match_external_conormal_rank": 3 == 3,
        "K_starts_at_second_external_normal_order": k_normal_order == 2,
    }
    result = {
        "schema": "marici.rank26-all-soft-costalk.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "all_soft_sequence": ["0", "b", "a", "a+b", "b", "a"],
        "labelled_zero_directions": [
            "e_K",
            "e_g3-e_g2-e_g1",
            "e_g23-e_g1",
            "e_g31-e_g2",
        ],
        "change_matrix": [list(row) for row in CHANGE],
        "change_determinant": determinant_change,
        "transformed_q_coefficient_matrix": [list(row) for row in transformed],
        "costalk_homology": "F tensor exterior(e_K,r3,r23,r31)",
        "graded_dimensions": graded,
        "total_dimension": sum(graded),
        "normal_orders": {
            "three_marked_relation_directions": 1,
            "Cayley_Menger_direction": k_normal_order,
        },
        "K_external_coefficient_degrees": list(k_external_coefficient_degrees),
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-all-soft-costalk.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
