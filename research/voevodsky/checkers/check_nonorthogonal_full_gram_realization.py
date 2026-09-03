from __future__ import annotations

import json
from fractions import Fraction
from itertools import permutations


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    total = Fraction(0)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j] for i in range(size) for j in range(i + 1, size))
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    matrix = [
        [Fraction(2), Fraction(1, 2), Fraction(1, 3)],
        [Fraction(1, 2), Fraction(1), Fraction(1, 4)],
        [Fraction(1, 3), Fraction(1, 4), Fraction(1)],
    ]
    leading = [determinant([row[:size] for row in matrix[:size]]) for size in range(1, 4)]
    assert all(value > 0 for value in leading)

    # Eliminate k first.
    u_after_k = matrix[1][1] - matrix[1][0] * matrix[0][1] / matrix[0][0]
    x_after_k = matrix[2][2] - matrix[2][0] * matrix[0][2] / matrix[0][0]
    ux_after_k = matrix[1][2] - matrix[1][0] * matrix[0][2] / matrix[0][0]
    assert u_after_k == Fraction(7, 8)
    assert x_after_k == Fraction(17, 18)
    assert ux_after_k == Fraction(1, 6)
    successive = x_after_k - ux_after_k**2 / u_after_k

    # Eliminate the joint (k,u) block directly.
    a, b, d = matrix[0][0], matrix[0][1], matrix[1][1]
    block_det = a * d - b * b
    inverse = [[d / block_det, -b / block_det], [-b / block_det, a / block_det]]
    coupling = [matrix[2][0], matrix[2][1]]
    correction = sum(coupling[i] * inverse[i][j] * coupling[j] for i in range(2) for j in range(2))
    direct = matrix[2][2] - correction
    assert successive == direct == Fraction(115, 126)

    raw_cross_reuse = matrix[1][2]
    wrong_successive = x_after_k - raw_cross_reuse**2 / u_after_k
    assert wrong_successive != direct

    result = {
        "schema": "marici.voevodsky.nonorthogonal-full-gram-realization.v1",
        "status": "finite_nonorthogonal_partial_equipment_realized",
        "leading_principal_determinants": [render(value) for value in leading],
        "transported_cross_after_first_elimination": render(ux_after_k),
        "successive_schur_quotient": render(successive),
        "direct_joint_schur_quotient": render(direct),
        "schur_composition_associative": successive == direct,
        "raw_cross_reuse_quotient": render(wrong_successive),
        "raw_cross_reuse_valid": False,
        "beck_chevalley_requires_transported_cross_certificate": True,
        "finite_completion_strict": True,
        "unbounded_completion_realized": False,
        "next_gate": "embed sourced enlarged Green and gauge fixtures with source-selected quotient conventions",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
