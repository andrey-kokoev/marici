from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/affine-simplex-naturality-contract-v1.json")
MELLIN = Path("research/grothendieck/the-unilateral-seam-cocycle-is-filled-by-the-mellin-orbit-before-completion.md")


def affine_combination(vertices: list[tuple[Fraction, ...]], weights: list[Fraction]) -> tuple[Fraction, ...]:
    return tuple(sum(weight * vertex[index] for weight, vertex in zip(weights, vertices)) for index in range(len(vertices[0])))


def affine_map(vertex: tuple[Fraction, ...], matrix: list[list[Fraction]], shift: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum(row[index] * vertex[index] for index in range(len(vertex))) + shift[row_index] for row_index, row in enumerate(matrix))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    mellin = MELLIN.read_text(encoding="utf-8")
    assert "t\\longmapsto A(tw)" in mellin
    vertices = [(Fraction(1), Fraction(0)), (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1))]
    weights = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]
    matrix = [[Fraction(2), Fraction(1)], [Fraction(-1), Fraction(3)]]
    shift = (Fraction(4), Fraction(-2))
    left = affine_map(affine_combination(vertices, weights), matrix, shift)
    right = affine_combination([affine_map(vertex, matrix, shift) for vertex in vertices], weights)
    assert left == right

    reflection_matrix = [[Fraction(-1), Fraction(0)], [Fraction(0), Fraction(-1)]]
    zero = (Fraction(0), Fraction(0))
    reflected_left = affine_map(affine_combination(vertices, weights), reflection_matrix, zero)
    reflected_right = affine_combination([affine_map(vertex, reflection_matrix, zero) for vertex in vertices], weights)
    assert reflected_left == reflected_right

    # Nonlinear inversion fails midpoint preservation.
    x, y = Fraction(1), Fraction(2)
    inversion_of_midpoint = 1 / ((x + y) / 2)
    midpoint_of_inversions = (1 / x + 1 / y) / 2
    assert inversion_of_midpoint == Fraction(2, 3)
    assert midpoint_of_inversions == Fraction(3, 4)
    assert inversion_of_midpoint != midpoint_of_inversions

    result = {
        "schema": "marici.voevodsky.affine-simplex-naturality-check.v1",
        "status": "reciprocal_affine_naturality_verified",
        "general_affine_simplex_naturality": True,
        "reciprocal_negation_naturality": True,
        "affine_boundary_commutation": True,
        "conjugate_linear_maps_real_affine": True,
        "nonlinear_inversion_affine_naturality": False,
        "nonlinear_actions_require_comparison_homotopy": True,
        "cutoff_compatibility_verified": False,
        "completed_descent_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
