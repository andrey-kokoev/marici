#!/usr/bin/env python3
"""Exact finite separation of orientation, chamber monoid, and completion."""

import json
from fractions import Fraction
from pathlib import Path


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def matrix(q):
    return (
        ((1 + q) / 2, (1 - q) / 2),
        ((1 - q) / 2, (1 + q) / 2),
    )


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def main():
    quarter_turn = ((0, -1), (1, 0))
    assert determinant(quarter_turn) == 1
    selected_quarter_turn_coefficient = quarter_turn[0][0]
    assert selected_quarter_turn_coefficient == 0

    q1 = Fraction(1, 2)
    q2 = Fraction(1, 3)
    m1 = matrix(q1)
    m2 = matrix(q2)
    composed = multiply(m1, m2)
    expected = matrix(q1 * q2)
    assert composed == expected
    assert all(entry > 0 for row in composed for entry in row)
    assert determinant(composed) == q1 * q2 > 0

    q = Fraction(1, 2)
    finite_selected = [q**n for n in range(1, 13)]
    assert all(value > 0 for value in finite_selected)
    assert all(finite_selected[i + 1] < finite_selected[i] for i in range(11))
    assert finite_selected[-1] == Fraction(1, 4096)

    result = {
        "schema": "marici.rh-chamber-monoid-completion.v1",
        "status": "pass",
        "quarter_turn_orientation_preserved": determinant(quarter_turn) > 0,
        "quarter_turn_selected_coefficient": selected_quarter_turn_coefficient,
        "positive_monoid_composition_exact": composed == expected,
        "composed_determinant": [determinant(composed).numerator, determinant(composed).denominator],
        "all_finite_diagonal_coefficients_positive": all(value > 0 for value in finite_selected),
        "twelfth_diagonal_coefficient": [finite_selected[-1].numerator, finite_selected[-1].denominator],
        "completion_margin_not_implied": True,
        "disposition": "orientation, positive composition, and completion margin are independent gates",
    }
    out = Path(__file__).parents[1] / "results" / "rh-chamber-monoid-completion.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
