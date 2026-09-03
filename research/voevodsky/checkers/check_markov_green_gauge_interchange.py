from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def gram(edges: tuple[Fraction, ...]) -> sp.Matrix:
    n = len(edges) + 1
    def entry(i: int, j: int) -> sp.Rational:
        if i == j:
            return sp.Integer(1)
        lo, hi = sorted((i, j))
        value = Fraction(1)
        for edge in edges[lo:hi]:
            value *= edge
        return sp.Rational(value.numerator, value.denominator)
    return sp.Matrix(n, n, entry)


def transform_edges(edges: tuple[Fraction, ...], signs: tuple[int, ...]) -> tuple[Fraction, ...]:
    assert len(signs) == len(edges) + 1
    return tuple(signs[i] * signs[i + 1] * edge for i, edge in enumerate(edges))


def concat_signs(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...] | None:
    if left[-1] != right[0]:
        return None
    return left + right[1:]


def diagonal(signs: tuple[int, ...]) -> sp.Matrix:
    return sp.diag(*signs)


def main() -> None:
    left_edges = (Fraction(1, 2), Fraction(2, 3))
    right_edges = (Fraction(3, 4), Fraction(4, 5))
    left_signs = (1, -1, 1)
    right_signs = (1, -1, -1)
    combined_signs = concat_signs(left_signs, right_signs)
    assert combined_signs is not None

    gauge_then_concat_edges = transform_edges(left_edges, left_signs) + transform_edges(right_edges, right_signs)
    concat_then_gauge_edges = transform_edges(left_edges + right_edges, combined_signs)
    assert gauge_then_concat_edges == concat_then_gauge_edges

    original = gram(left_edges + right_edges)
    route_matrix = gram(gauge_then_concat_edges)
    direct_matrix = diagonal(combined_signs) * original * diagonal(combined_signs)
    assert route_matrix == direct_matrix

    # Vertical composition: pointwise sign multiplication.
    second_signs = (1, 1, -1, -1, 1)
    composed_signs = tuple(a * b for a, b in zip(combined_signs, second_signs))
    twice = diagonal(second_signs) * direct_matrix * diagonal(second_signs)
    once = diagonal(composed_signs) * original * diagonal(composed_signs)
    assert twice == once

    incompatible_right = (-1, -1, 1)
    assert concat_signs(left_signs, incompatible_right) is None

    result = {
        "schema": "marici.voevodsky.markov-green-gauge-interchange.v1",
        "status": "restricted_analytic_interchange_verified",
        "gauge_then_concat_equals_concat_then_gauge": True,
        "full_gram_matrix_equality": True,
        "vertical_composition_pointwise": True,
        "interchange_cell": "identity_isometry",
        "shared_vertex_mismatch_rejected": True,
        "general_vertical_interchange_verified": False,
        "gauge_quotient_interchange_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
