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
    size = 5
    matrix = [
        [Fraction(1) if i == j else Fraction(1 if (i + j) % 2 == 0 else -1, 10) for j in range(size)]
        for i in range(size)
    ]
    radii = [sum(abs(matrix[i][j]) for j in range(size) if j != i) for i in range(size)]
    margins = [matrix[i][i] - radii[i] for i in range(size)]
    leading_determinants = [determinant([row[:n] for row in matrix[:n]]) for n in range(1, size + 1)]

    assert all(radius == Fraction(2, 5) for radius in radii)
    assert all(margin == Fraction(3, 5) for margin in margins)
    assert all(value > 0 for value in leading_determinants)

    positive_non_dominant_r = Fraction(1, 2)
    positive_non_dominant_radius = 3 * positive_non_dominant_r
    positive_non_dominant_eigenvalues = [1 - positive_non_dominant_r, 1 + 3 * positive_non_dominant_r]
    assert positive_non_dominant_radius > 1
    assert all(value > 0 for value in positive_non_dominant_eigenvalues)

    result = {
        "schema": "marici.voevodsky.diagonal-dominance-green-certificate.v1",
        "status": "uniform_sufficient_certificate_verified",
        "certified_size": size,
        "row_radii": [render(value) for value in radii],
        "gershgorin_lower_margins": [render(value) for value in margins],
        "leading_principal_determinants": [render(value) for value in leading_determinants],
        "certificate_is_necessary": False,
        "positive_non_dominant_example": {
            "size": 4,
            "correlation": render(positive_non_dominant_r),
            "row_radius": render(positive_non_dominant_radius),
            "eigenvalues": [render(value) for value in positive_non_dominant_eigenvalues],
        },
        "promotion_gate": "source-derived row bounds for the actual Green blocks",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
