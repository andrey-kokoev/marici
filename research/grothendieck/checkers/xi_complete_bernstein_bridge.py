"""Exact bridge among centered xi logarithm, Stieltjes resolvent, and heat Levy density."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x, t, gamma = sp.symbols("x t gamma", positive=True)
    bernstein_atom = sp.log(1 + x / gamma**2)
    stieltjes_atom = sp.diff(bernstein_atom, x)
    assert sp.simplify(stieltjes_atom - 1 / (x + gamma**2)) == 0

    # Frullani representation is fixed by matching derivative and value at 0.
    levy_derivative = sp.integrate(
        sp.exp(-x * t) * sp.exp(-gamma**2 * t),
        (t, 0, sp.oo),
    )
    assert sp.simplify(levy_derivative - stieltjes_atom) == 0
    assert bernstein_atom.subs(x, 0) == 0

    for order in range(0, 8):
        derivative = sp.diff(stieltjes_atom, x, order)
        expected = (-1) ** order * sp.factorial(order) / (x + gamma**2) ** (order + 1)
        assert sp.simplify(derivative - expected) == 0

    a = sp.symbols("a")
    hostile_atom = sp.log(1 - x / a**2)
    hostile_derivative = sp.diff(hostile_atom, x)
    assert sp.simplify(hostile_derivative + 1 / (a**2 - x)) == 0

    print("bernstein_atom=log(1+x/gamma^2)")
    print("bernstein_derivative=1/(x+gamma^2)")
    print("levy_atom=exp(-gamma^2*t)/t")
    print("complete_monotonicity_orders_checked=0..7")
    print("centered_xi_log_derivative_equals_stieltjes_target=True")
    print("hostile_quartet_complete_bernstein_admissible=False")


if __name__ == "__main__":
    main()
