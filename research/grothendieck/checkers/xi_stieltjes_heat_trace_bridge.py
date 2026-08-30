"""Exact Laplace bridge between the squared Stieltjes resolvent and heat trace."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x, t, gamma = sp.symbols("x t gamma", positive=True)
    laplace_atom = sp.integrate(sp.exp(-x * t) * sp.exp(-gamma**2 * t), (t, 0, sp.oo))
    assert sp.simplify(laplace_atom - 1 / (x + gamma**2)) == 0

    for order in range(0, 8):
        resolvent_derivative = sp.diff(1 / (x + gamma**2), x, order)
        heat_moment = sp.integrate(
            (-t) ** order * sp.exp(-x * t) * sp.exp(-gamma**2 * t),
            (t, 0, sp.oo),
        )
        assert sp.simplify(resolvent_derivative - heat_moment) == 0

    alpha, beta = sp.symbols("alpha beta", real=True)
    a = alpha + sp.I * beta
    hostile_kernel = sp.exp(a**2 * t) + sp.exp(sp.conjugate(a) ** 2 * t)
    hostile_real_form = sp.simplify(sp.expand_complex(hostile_kernel))
    expected_hostile = 2 * sp.exp((alpha**2 - beta**2) * t) * sp.cos(2 * alpha * beta * t)
    assert sp.simplify(hostile_real_form - expected_hostile) == 0

    print("stieltjes_atom_laplace_residual=0")
    print("derivative_heat_moment_residuals_zero_orders=0..7")
    print("critical_heat_atom=exp(-gamma^2*t)")
    print("hostile_heat_pair=2*exp((alpha^2-beta^2)*t)*cos(2*alpha*beta*t)")
    print("hostile_heat_pair_positive_for_all_t=False")


if __name__ == "__main__":
    main()
