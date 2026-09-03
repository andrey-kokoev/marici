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


def restrict_contiguous(matrix: sp.Matrix, first_vertex: int, last_vertex: int) -> sp.Matrix:
    assert 0 <= first_vertex <= last_vertex < matrix.rows
    indices = list(range(first_vertex, last_vertex + 1))
    return matrix.extract(indices, indices)


def main() -> None:
    left = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4))
    right = (Fraction(4, 5), Fraction(5, 6), Fraction(6, 7))
    full_edges = left + right
    full = gram(full_edges)

    # Cross-seam target vertices 2..5 retains edges indices 2..4.
    route_complete_then_restrict = restrict_contiguous(full, 2, 5)
    retained_edges = full_edges[2:5]
    route_restrict_then_complete = gram(retained_edges)
    assert route_complete_then_restrict == route_restrict_then_complete

    det_expected = sp.prod(1 - sp.Rational(e.numerator, e.denominator) ** 2 for e in retained_edges)
    assert sp.factor(route_complete_then_restrict.det() - det_expected) == 0

    # Strict pasting of nested contiguous restrictions.
    first_restriction = restrict_contiguous(full, 1, 6)
    nested = restrict_contiguous(first_restriction, 2, 4)
    direct = restrict_contiguous(full, 3, 5)
    assert nested == direct

    # Noncontiguous selection has the same dimension as a three-vertex
    # contiguous chain but is outside this constructor's interface type.
    noncontiguous_indices = [0, 2, 5]
    hostile = full.extract(noncontiguous_indices, noncontiguous_indices)
    contiguous_same_dimension = restrict_contiguous(full, 0, 2)
    assert hostile.shape == contiguous_same_dimension.shape
    assert hostile != contiguous_same_dimension

    result = {
        "schema": "marici.voevodsky.markov-green-contiguous-beck-chevalley.v1",
        "status": "restricted_invertible_beck_chevalley_verified",
        "cross_seam_route_equality": True,
        "full_gram_certificate_preserved": True,
        "determinant_certificate_preserved": True,
        "beck_chevalley_cell": "identity_isometry",
        "beck_chevalley_invertible": True,
        "nested_pasting_strict": True,
        "noncontiguous_equal_dimension_fixture_rejected": True,
        "general_pullback_beck_chevalley_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
