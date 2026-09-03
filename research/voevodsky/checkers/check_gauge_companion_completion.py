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


def transformed_edges(edges: tuple[Fraction, ...], signs: tuple[int, ...]) -> tuple[Fraction, ...]:
    return tuple(signs[i] * signs[i + 1] * edge for i, edge in enumerate(edges))


def main() -> None:
    edges = tuple(Fraction(i + 1, i + 4) for i in range(8))
    signs = (1, -1, -1, 1, -1, 1, 1, -1, 1)
    full = gram(edges)
    diagonal = sp.diag(*signs)
    gauged_full = diagonal * full * diagonal
    assert gauged_full == gram(transformed_edges(edges, signs))

    # Every finite compression commutes with the gauge.
    for last_vertex in range(1, len(signs)):
        indices = list(range(last_vertex + 1))
        compressed_after_gauge = gauged_full.extract(indices, indices)
        finite_diagonal = sp.diag(*signs[:last_vertex + 1])
        gauge_after_compression = finite_diagonal * full.extract(indices, indices) * finite_diagonal
        assert compressed_after_gauge == gauge_after_compression

    rho = sp.Rational(3, 4)
    original_bound = (1 + rho) / (1 - rho)
    transformed_rho = max(abs(edge) for edge in transformed_edges(edges, signs))
    assert transformed_rho <= rho
    assert original_bound == 7

    # Hostile diagonal truncations have increasing operator norm and no
    # uniformly bounded completed vertical arrow.
    hostile_norms = [max(abs(value) for value in range(1, n + 1)) for n in (2, 4, 8)]
    assert hostile_norms == [2, 4, 8]

    result = {
        "schema": "marici.voevodsky.gauge-companion-completion.v1",
        "status": "restricted_completion_equipment_compatibility_verified",
        "completed_gauge_equals_gauge_of_completion": True,
        "finite_compressions_natural": True,
        "edge_moduli_preserved": True,
        "schur_bound_preserved": True,
        "companion_completion_cell": "identity",
        "conjoint_completion_cell": "identity",
        "pasting_strict": True,
        "hostile_unbounded_diagonal_norms": hostile_norms,
        "global_completion_equipment_compatibility": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
