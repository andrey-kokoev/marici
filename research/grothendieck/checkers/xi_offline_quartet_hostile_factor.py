"""Exact hostile factor preserving reflection and critical-boundary sign while adding off-line zeros."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    w = sp.symbols("w")
    alpha, beta, t = sp.symbols("alpha beta t", real=True)
    a = alpha + sp.I * beta
    factor = sp.expand((w**2 - a**2) * (w**2 - sp.conjugate(a) ** 2))

    assert sp.simplify(factor.subs(w, -w) - factor) == 0
    assert sp.simplify(sp.conjugate(factor).subs(sp.conjugate(w), w) - factor) == 0

    boundary = sp.factor(factor.subs(w, sp.I * t))
    expected_boundary = sp.expand(
        (t**2 + a**2) * (t**2 + sp.conjugate(a) ** 2)
    )
    assert sp.simplify(boundary - expected_boundary) == 0
    assert sp.simplify(expected_boundary - sp.Abs(t**2 + a**2) ** 2) == 0

    log_derivative = sp.diff(factor, w) / factor
    boundary_log_derivative = sp.simplify(log_derivative.subs(w, sp.I * t))
    assert sp.simplify(sp.re(boundary_log_derivative)) == 0

    roots = (a, -a, sp.conjugate(a), -sp.conjugate(a))
    assert all(sp.simplify(factor.subs(w, root)) == 0 for root in roots)

    print("hostile_factor=(w^2-a^2)*(w^2-conjugate(a)^2)")
    print("reflection_even=True")
    print("real_structure=True")
    print("critical_boundary_factor=abs(t^2+a^2)^2")
    print("critical_boundary_sign_preserved=True")
    print("boundary_log_derivative_real_part=0")
    print("inserted_zero_quartet=a,-a,conjugate(a),-conjugate(a)")
    print("symmetry_and_boundary_sign_exclude_offline_zeros=False")


if __name__ == "__main__":
    main()
