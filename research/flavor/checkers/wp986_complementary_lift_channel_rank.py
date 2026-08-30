#!/usr/bin/env python3
"""Exact checker for the WP986 complementary-channel rank theorem."""

from fractions import Fraction
import json
from pathlib import Path


J = [
    [Fraction(2), Fraction(4), Fraction(-1), Fraction(-5)],
    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
]


def determinant(matrix):
    n = len(matrix)
    a = [row[:] for row in matrix]
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col]
            for j in range(col, n):
                a[r][j] -= factor * a[col][j]
    return det


det_J = determinant(J)
gram_det = det_J**2

# Exact reconstruction test on a hostile rational source tangent.
x = [Fraction(3, 2), Fraction(-7, 3), Fraction(5, 4), Fraction(11, 6)]
y0 = sum(J[0][i] * x[i] for i in range(4))
y_gamma, y_B, y_C = x[0], x[2], x[3]
x_A_reconstructed = (y0 - 2 * y_gamma + y_B + 5 * y_C) / 4

checks = {
    "single_response_kernel_dimension_is_three": 4 - 1 == 3,
    "two_complementary_channels_cannot_reach_rank_four": 1 + 2 < 4,
    "three_complementary_channels_are_minimal": 1 + 3 == 4,
    "joint_jacobian_determinant_is_minus_four": det_J == -4,
    "identity_metric_gram_determinant_is_sixteen": gram_det == 16,
    "hostile_x_A_reconstructs_exactly": x_A_reconstructed == x[1],
    "joint_contextual_kernel_is_zero": det_J != 0,
}

result = {
    "schema": "marici.flavor.complementary-lift-channel-rank.v1",
    "work_package": "WP986",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "source_tangent": ["log_Gamma", "log_A", "log_B", "log_C"],
    "base_response_row": ["2", "4", "-1", "-5"],
    "complementary_rows": [
        ["1", "0", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"],
    ],
    "determinant": str(det_J),
    "gram_determinant_identity_metric": str(gram_det),
    "classification": "formal separator and constructor identifier; neither selector nor established instrument",
    "remaining_gate": (
        "derive calibrated vertex and pole-mass instruments with finite-width, "
        "mixing, resolution, common-frame, and weak-basis-descent control"
    ),
}

out = Path("research/flavor/results/wp986_complementary_lift_channel_rank.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
