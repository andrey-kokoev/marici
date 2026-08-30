#!/usr/bin/env python3
"""Identify the Leray-soft relational residue with the top conductor row."""

import json
from fractions import Fraction
from pathlib import Path


K = [
    [0, 0, 1, -1],
    [0, 1, 0, -1],
    [1, -1, -1, 1],
]
J = [
    [2, 0, 1],
    [0, 2, 1],
    [0, 0, 1],
]
phi_exc = [
    [1, -1, 1, -1],
    [1, 1, -1, -1],
    [1, -1, -1, 1],
]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def column(matrix, j):
    return [row[j] for row in matrix]


relational_flat = [-1, 1, 1, -1]
top_conductor_row = K[2]
diagonal = [1, 1, 1, 1]
K_diagonal = [sum(row[j] * diagonal[j] for j in range(4)) for row in K]

wall_1 = column(J, 0)
wall_2 = column(J, 1)
top = column(J, 2)
common_e6 = [
    top[i] - Fraction(1, 2) * wall_1[i] - Fraction(1, 2) * wall_2[i]
    for i in range(3)
]

checks = {
    "relational_residue_is_oriented_top_row": top_conductor_row
    == [-value for value in relational_flat],
    "diagonal_occurrence_is_killed": K_diagonal == [0, 0, 0],
    "source_factorization_phi_equals_JK": matmul(J, K) == phi_exc,
    "top_minus_half_walls_is_e6": common_e6
    == [Fraction(0), Fraction(0), Fraction(1)],
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.relational_residue_conductor_realization.v1",
    "corner_order": ["++", "+-", "-+", "--"],
    "relational_residue_flat": relational_flat,
    "K": K,
    "J": J,
    "Phi_exc": phi_exc,
    "top_conductor_row": top_conductor_row,
    "orientation_relation": "K_top=-R_fb",
    "common_e6_coordinate": [str(value) for value in common_e6],
    "checks": checks,
    "verdict": (
        "The primitive Leray-soft relational residue is already present, up "
        "to the forced orientation sign, as the top row of the source-derived "
        "unimodular occurrence quotient K. Through J, its top conductor image "
        "reduces to the common e6 bridge after removing the two wall legs."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "relational_residue_conductor_realization.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
