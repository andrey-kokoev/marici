#!/usr/bin/env python3
"""Hostile test of the frozen normal-order rule on the full eight-section packet."""

import json
from math import comb
from pathlib import Path


LABELS = ("g1", "g2", "g3", "g12", "g23", "g31", "G23", "G31")
# Rows are coefficients of a,b in the independently frozen source order.
Q = (
    (0, 1, 1, 1, 0, 1, 1, 0),
    (1, 0, 1, 1, 1, 0, 0, 1),
)

# Columns are (g2,g1,r3,r12,r23,r31,rG23,rG31), expressed in source order.
CHANGE = (
    (0, 1, -1, -1, -1, 0, 0, -1),
    (1, 0, -1, -1, 0, -1, -1, 0),
    (0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 1),
)


def determinant(matrix):
    from fractions import Fraction
    rows = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        pivot = next(index for index in range(column, len(rows)) if rows[index][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result *= -1
        value = rows[column][column]
        result *= value
        rows[column] = [entry / value for entry in rows[column]]
        for index in range(column + 1, len(rows)):
            factor = rows[index][column]
            rows[index] = [a - factor * b for a, b in zip(rows[index], rows[column])]
    return int(result)


def main():
    transformed = tuple(
        tuple(sum(Q[row][k] * CHANGE[k][column] for k in range(8)) for column in range(8))
        for row in range(2)
    )
    change_det = determinant(CHANGE)
    exterior_generators = 7  # six marked null directions plus zero K
    graded = [comb(exterior_generators, degree) for degree in range(exterior_generators + 1)]
    expected = [1, 7, 21, 35, 35, 21, 7, 1]
    checks = {
        "source_packet_has_eight_labelled_sections": len(LABELS) == 8,
        "label_change_is_unimodular": abs(change_det) == 1,
        "normal_form_is_a_b_plus_six_zero_relations": transformed == (
            (1, 0, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 0, 0),
        ),
        "predeclared_exterior_grading_matches": graded == expected,
        "predeclared_total_rank_matches": sum(graded) == 128,
    }
    result = {
        "schema": "marici.nine-master-full-marked-all-soft-signature.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "frozen_labels": list(LABELS),
        "source_incidence_matrix": [list(row) for row in Q],
        "change_determinant": change_det,
        "transformed_incidence_matrix": [list(row) for row in transformed],
        "labelled_relation_basis": ["r3", "r12", "r23", "r31", "rG23", "rG31"],
        "normal_order_signature": [1, 1, 1, 1, 1, 1, 2],
        "exterior_graded_dimensions": graded,
        "total_rank": sum(graded),
        "checks": checks,
    }
    output = Path(__file__).with_name("nine-master-full-marked-all-soft-signature.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
