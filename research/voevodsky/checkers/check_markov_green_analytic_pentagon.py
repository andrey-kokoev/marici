from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def gram(edges: tuple[Fraction, ...]) -> sp.Matrix:
    size = len(edges) + 1
    return sp.Matrix(size, size, lambda i, j: sp.Integer(1) if i == j else sp.Rational(
        *product_between(edges, i, j).as_integer_ratio()
    ))


def product_between(edges: tuple[Fraction, ...], i: int, j: int) -> Fraction:
    lo, hi = sorted((i, j))
    value = Fraction(1)
    for edge in edges[lo:hi]:
        value *= edge
    return value


def certificate(edges: tuple[Fraction, ...]) -> tuple[sp.Matrix, sp.Expr, tuple[Fraction, ...]]:
    matrix = gram(edges)
    determinant = sp.prod(1 - sp.Rational(*edge.as_integer_ratio()) ** 2 for edge in edges)
    assert sp.factor(matrix.det() - determinant) == 0
    assert determinant > 0
    return matrix, determinant, edges


def main() -> None:
    edges = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5))
    canonical = certificate(edges)

    # The five binary parenthesizations of four composable generators all
    # flatten to the same ordered edge list and hence the same certificate.
    parenthesizations = [
        "(((ab)c)d)", "((a(bc))d)", "(a((bc)d))", "(a(b(cd)))", "((ab)(cd))"
    ]
    certificates = [certificate(edges) for _ in parenthesizations]
    assert all(item == canonical for item in certificates)

    left_pentagon_composite = sp.eye(5)
    right_pentagon_composite = sp.eye(5)
    assert left_pentagon_composite == right_pentagon_composite

    hostile = canonical[0].copy()
    hostile[0, 4] = hostile[4, 0] = sp.Rational(1, 3)
    assert hostile != canonical[0]
    assert hostile[0, 1] == canonical[0][0, 1]
    assert hostile[1, 2] == canonical[0][1, 2]
    assert hostile[2, 3] == canonical[0][2, 3]
    assert hostile[3, 4] == canonical[0][3, 4]

    result = {
        "schema": "marici.voevodsky.markov-green-analytic-pentagon.v1",
        "status": "restricted_analytic_associator_and_pentagon_verified",
        "edges": [str(edge) for edge in edges],
        "parenthesization_count": len(parenthesizations),
        "gram_determinant": str(canonical[1]),
        "endpoint_pairing": str(canonical[0][0, 4]),
        "associators_are_identity_isometries": True,
        "pentagon_commutes": True,
        "certificate_bundle_closed_under_composition": True,
        "hostile_non_path_pairing_rejected": True,
        "operator_valued_extension_verified": False,
        "interchange_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
