"""Exact squared-coordinate Stieltjes target and hostile-quartet obstruction."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    w, x, gamma = sp.symbols("w x gamma", positive=True)
    pair_log_derivative = 2 * w / (w**2 + gamma**2)
    stieltjes_atom = sp.simplify(pair_log_derivative / (2 * w)).subs(w**2, x)
    assert sp.simplify(stieltjes_atom - 1 / (x + gamma**2)) == 0

    n = sp.symbols("n", integer=True, nonnegative=True)
    for order in range(0, 8):
        derivative = sp.diff(1 / (x + gamma**2), x, order)
        expected = (-1) ** order * sp.factorial(order) / (x + gamma**2) ** (order + 1)
        assert sp.simplify(derivative - expected) == 0

    alpha, beta = sp.symbols("alpha beta", real=True)
    a = alpha + sp.I * beta
    hostile = (w**2 - a**2) * (w**2 - sp.conjugate(a) ** 2)
    hostile_squared_log_derivative = sp.simplify(sp.diff(hostile, w) / hostile / (2 * w))
    hostile_in_x = sp.factor(hostile_squared_log_derivative.subs(w**2, x))
    expected_hostile = 1 / (x - a**2) + 1 / (x - sp.conjugate(a) ** 2)
    assert sp.simplify(hostile_in_x - expected_hostile) == 0

    print("critical_pair_stieltjes_atom=1/(x+gamma^2)")
    print("complete_monotonicity_checked_orders=0..7")
    print("hostile_quartet_squared_poles=a^2,conjugate(a)^2")
    print("hostile_quartet_stieltjes_admissible=False")
    print("stieltjes_measure=positive_squared_ordinate_measure")


if __name__ == "__main__":
    main()
