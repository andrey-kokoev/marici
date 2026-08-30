"""Exact labelled normal expansion of the generic three-site CM kernel."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    c, a, b = sp.symbols("c a b")
    x1, x2, x3 = sp.symbols("X1 X2 X3")
    n1, n2, n3 = sp.symbols("nu1 nu2 nu3")

    p1sq, p2sq, p3sq = x1**2 + n1, x2**2 + n2, x3**2 + n3
    cm = sp.Matrix([
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, p2sq, p1sq],
        [1, a**2, p2sq, 0, p3sq],
        [1, b**2, p1sq, p3sq, 0],
    ])
    kernel = sp.expand(-cm.det() / 2)
    polynomial = sp.Poly(kernel, n1, n2, n3)
    coefficients = {monomial: sp.factor(value) for monomial, value in polynomial.terms()}

    expected_monomials = {
        (0, 0, 0),
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (2, 0, 0), (0, 2, 0), (0, 0, 2),
        (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 1, 1),
    }
    assert set(coefficients) == expected_monomials
    assert polynomial.total_degree() == 3

    expected_quadratic = {
        (2, 0, 0): a**2,
        (0, 2, 0): b**2,
        (0, 0, 2): c**2,
        (1, 1, 0): x3**2 - a**2 - b**2,
        (1, 0, 1): x2**2 - a**2 - c**2,
        (0, 1, 1): x1**2 - b**2 - c**2,
    }
    for monomial, value in expected_quadratic.items():
        assert sp.simplify(coefficients[monomial] - value) == 0
    assert coefficients[(1, 1, 1)] == 1

    # No cubic other than the fully labelled product, and no higher grade.
    assert [m for m in coefficients if sum(m) == 3] == [(1, 1, 1)]
    assert not [m for m in coefficients if sum(m) > 3]

    # The complete kernel is covariant under cyclic occurrence transport.
    cyclic = {
        x1: x2, x2: x3, x3: x1,
        n1: n2, n2: n3, n3: n1,
        a: b, b: c, c: a,
    }
    assert sp.expand(kernel.xreplace(cyclic) - kernel) == 0

    linear = {
        "nu1": str(coefficients[(1, 0, 0)]),
        "nu2": str(coefficients[(0, 1, 0)]),
        "nu3": str(coefficients[(0, 0, 1)]),
    }
    quadratic = {
        "nu1^2": str(coefficients[(2, 0, 0)]),
        "nu2^2": str(coefficients[(0, 2, 0)]),
        "nu3^2": str(coefficients[(0, 0, 2)]),
        "nu1*nu2": str(coefficients[(1, 1, 0)]),
        "nu1*nu3": str(coefficients[(1, 0, 1)]),
        "nu2*nu3": str(coefficients[(0, 1, 1)]),
    }
    packet = {
        "schema": "marici.benincasa.generic-six-scale-kernel-normal-tower.v1",
        "source_kernel": "K=-det(CM)/2 with P_i^2=X_i^2+nu_i",
        "normal_grade_dimensions": {"0": 1, "1": 3, "2": 6, "3": 1},
        "normal_degree": polynomial.total_degree(),
        "linear_coefficients": linear,
        "quadratic_coefficients": quadratic,
        "cubic_coefficients": {"nu1*nu2*nu3": "1"},
        "other_cubic_coefficients": 0,
        "higher_normal_coefficients": 0,
        "cyclic_map": "(X1,X2,X3;nu1,nu2,nu3;a,b,c)->(X2,X3,X1;nu2,nu3,nu1;b,c,a)",
        "cyclic_covariance": True,
        "classification": (
            "finite labelled nonhomogeneous scalar interaction tower over "
            "the existing Cayley-Menger carrier"
        ),
        "new_carrier_datum": False,
        "scope": "kernel-level theorem before Gauss-Manin pushforward and physical readout",
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
