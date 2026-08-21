"""Exact endpoint pole audit for the Möbius-pulled Li rational-square cone."""

from __future__ import annotations

import sympy as sp


def valuation_at(expr: sp.Expr, variable: sp.Symbol, point: int) -> int:
    shifted = sp.cancel(expr.subs(variable, variable + point))
    numerator, denominator = sp.fraction(shifted)
    numerator_poly = sp.Poly(numerator, variable)
    denominator_poly = sp.Poly(denominator, variable)
    numerator_order = min(monomial[0] for monomial, coefficient in numerator_poly.terms() if coefficient != 0)
    denominator_order = min(monomial[0] for monomial, coefficient in denominator_poly.terms() if coefficient != 0)
    return numerator_order - denominator_order


def main() -> None:
    s, z = sp.symbols("s z")
    u = (s - 1) / s

    for degree in range(0, 9):
        # Generic enough to keep nonzero constant and leading coefficients and
        # avoid accidental endpoint cancellations.
        polynomial = sum((j + 1) * z**j for j in range(degree + 1))
        test = sp.cancel(
            polynomial.subs(z, u)
            * polynomial.subs(z, 1 / u)
            / (s * (1 - s))
        )
        order_zero = valuation_at(test, s, 0)
        order_one = valuation_at(test, s, 1)
        assert order_zero == -(degree + 1)
        assert order_one == -(degree + 1)
        assert sp.simplify(test.subs(s, 1 - s) - test) == 0
        print(
            f"degree={degree} pole_order_at_0={-order_zero} "
            f"pole_order_at_1={-order_one}"
        )

    print("generic_endpoint_pole_order=degree+1")
    print("ordinary_holomorphic_test_class_admissible=False")
    print("canonical_endpoint_regularization_required=True")


if __name__ == "__main__":
    main()
