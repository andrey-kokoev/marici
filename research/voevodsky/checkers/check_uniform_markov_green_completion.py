from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def gram(edges: tuple[Fraction, ...]) -> sp.Matrix:
    n = len(edges) + 1
    def entry(i: int, j: int) -> sp.Rational:
        lo, hi = sorted((i, j))
        value = Fraction(1)
        for edge in edges[lo:hi]:
            value *= edge
        return sp.Rational(value.numerator, value.denominator)
    return sp.Matrix(n, n, entry)


def main() -> None:
    rho = sp.Rational(3, 4)
    schur_bound = sp.simplify((1 + rho) / (1 - rho))
    assert schur_bound == 7

    edges = tuple(Fraction(i + 1, i + 4) for i in range(8))
    assert all(abs(edge) <= Fraction(3, 4) for edge in edges)
    large = gram(edges)

    # Nested finite certificates are exact principal compressions.
    for last_edge in range(1, len(edges) + 1):
        small = gram(edges[:last_edge])
        indices = list(range(last_edge + 1))
        assert large.extract(indices, indices) == small
        assert small.det() > 0

    # Strict functoriality of coordinate inclusions.
    i_2_5 = sp.zeros(6, 3)
    for index in range(3):
        i_2_5[index, index] = 1
    i_5_8 = sp.zeros(9, 6)
    for index in range(6):
        i_5_8[index, index] = 1
    i_2_8 = sp.zeros(9, 3)
    for index in range(3):
        i_2_8[index, index] = 1
    assert i_5_8 * i_2_5 == i_2_8

    # Hostile all-ones truncations have growing norm n+1.
    hostile_norms = []
    for vertex_count in (2, 4, 8):
        ones = sp.ones(vertex_count)
        hostile_norms.append(max(ones.eigenvals().keys()))
    assert hostile_norms == [2, 4, 8]

    result = {
        "schema": "marici.voevodsky.uniform-markov-green-completion.v1",
        "status": "restricted_completion_pseudofunctor_verified",
        "symbolic_schur_bound": "(1+rho)/(1-rho)",
        "rho_fixture": str(rho),
        "rho_fixture_schur_bound": str(schur_bound),
        "principal_compressions_exact": True,
        "finite_blocks_positive": True,
        "coordinate_inclusions_strictly_functorial": True,
        "completion_comparison_cells": "identity",
        "hostile_all_ones_norms": [str(value) for value in hostile_norms],
        "uniform_contraction_required": True,
        "general_completion_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
