"""Exact pullback of circle polynomial squares to reflection-invariant rational tests."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s = sp.symbols("s")
    u = 1 - 1 / s
    reflected_u = sp.simplify(u.subs(s, 1 - s))
    assert sp.simplify(reflected_u - 1 / u) == 0

    weight = sp.simplify((1 - u) * (1 - 1 / u))
    assert sp.simplify(weight - 1 / (s * (1 - s))) == 0

    degree = 5
    coefficients = sp.symbols(f"a0:{degree + 1}")
    z = sp.symbols("z")
    polynomial = sum(coefficients[j] * z**j for j in range(degree + 1))
    test = sp.cancel(
        polynomial.subs(z, u)
        * polynomial.subs(z, 1 / u)
        / (s * (1 - s))
    )
    reflected_test = sp.cancel(test.subs(s, 1 - s))
    assert sp.simplify(test - reflected_test) == 0

    sigma, gamma = sp.symbols("sigma gamma", real=True)
    critical = sp.Rational(1, 2) + sp.I * gamma
    critical_u = sp.simplify(u.subs(s, critical))
    assert sp.simplify(critical_u * sp.conjugate(critical_u) - 1) == 0
    assert sp.simplify(
        (1 / (s * (1 - s))).subs(s, critical) - 1 / (sp.Rational(1, 4) + gamma**2)
    ) == 0

    print(f"checked_polynomial_degree={degree}")
    print("functional_reflection_maps_u_to_inverse=True")
    print("rational_test_reflection_residual=0")
    print("critical_line_phase_unitary=True")
    print("critical_line_weight=1/abs(s)^2")


if __name__ == "__main__":
    main()
