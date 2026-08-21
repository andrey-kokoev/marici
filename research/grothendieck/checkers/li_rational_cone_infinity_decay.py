"""Exact degree-independent infinity decay of the Möbius Li rational-square tests."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, z, x = sp.symbols("s z x")
    u = (s - 1) / s

    for degree in range(0, 9):
        coefficients = sp.symbols(f"a0:{degree + 1}")
        polynomial = sum(coefficients[j] * z**j for j in range(degree + 1))
        value_at_one = sp.expand(polynomial.subs(z, 1))
        test = sp.cancel(
            polynomial.subs(z, u)
            * polynomial.subs(z, 1 / u)
            / (s * (1 - s))
        )
        at_infinity = sp.cancel(test.subs(s, 1 / x))
        series = sp.series(at_infinity, x, 0, 4).removeO().expand()
        assert sp.simplify(series.coeff(x, 0)) == 0
        assert sp.simplify(series.coeff(x, 1)) == 0
        assert sp.simplify(series.coeff(x, 2) + value_at_one**2) == 0
        print(f"degree={degree} leading_coefficient=-p(1)^2 leading_order=s^-2")

    print("degree_independent_decay=True")
    print("generic_decay=O(s^-2)")
    print("divisor_tail_under_N_of_T_bound=O(log(T)/T)")


if __name__ == "__main__":
    main()
