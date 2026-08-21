"""Exact Gaussian-log integral behind the completed-xi short-time heat Weyl law."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t, gamma, a = sp.symbols("t gamma a", positive=True)
    moment_family = sp.gamma((a + 1) / 2) / (2 * t ** ((a + 1) / 2))
    gaussian = sp.simplify(moment_family.subs(a, 0))
    gaussian_log = sp.simplify(sp.diff(moment_family, a).subs(a, 0))

    assert sp.simplify(gaussian - sp.sqrt(sp.pi) / (2 * sp.sqrt(t))) == 0
    expected_log = gaussian * (
        -sp.EulerGamma / 2 - sp.log(2) - sp.log(t) / 2
    )
    assert sp.simplify(sp.expand_func(gaussian_log) - expected_log) == 0

    density_integral = sp.simplify(
        (gaussian_log - sp.log(2 * sp.pi) * gaussian) / (2 * sp.pi)
    )
    expected_density = sp.simplify(
        1
        / (4 * sp.sqrt(sp.pi * t))
        * (-sp.log(t) / 2 - sp.EulerGamma / 2 - sp.log(4 * sp.pi))
    )
    assert sp.simplify(sp.expand_log(density_integral, force=True) - expected_density) == 0

    alpha, beta = sp.symbols("alpha beta", real=True)
    hostile_pair = 2 * sp.exp((alpha**2 - beta**2) * t) * sp.cos(2 * alpha * beta * t)
    assert sp.limit(hostile_pair, t, 0, dir="+") == 2

    print("gaussian_integral=sqrt(pi)/(2*sqrt(t))")
    print("gaussian_log_integral_exact=True")
    print("heat_leading_log_coefficient=1/(8*sqrt(pi*t))")
    print("heat_next_weyl_coefficient=-(EulerGamma/2+log(4*pi))/(4*sqrt(pi*t))")
    print("finite_hostile_pair_short_time_order=O(1)")
    print("leading_weyl_law_excludes_finite_offline_quartets=False")


if __name__ == "__main__":
    main()
