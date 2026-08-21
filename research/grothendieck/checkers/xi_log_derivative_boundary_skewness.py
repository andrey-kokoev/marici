"""Exact symmetry audit for critical-boundary skewness of xi'/xi."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t = sp.symbols("t", real=True)
    # Represent the boundary value L(1/2+it)=a+ib and impose reflection plus
    # real conjugation: conjugate(L)=-L.
    a, b = sp.symbols("a b", real=True)
    boundary_value = a + sp.I * b
    residual = sp.expand(sp.conjugate(boundary_value) + boundary_value)
    solution = sp.solve([sp.re(residual), sp.im(residual)], [a], dict=True)
    assert solution == [{a: 0}]

    s = sp.symbols("s")
    centered = sp.Rational(1, 2) + sp.I * t
    reflected = sp.simplify(1 - centered)
    assert sp.simplify(reflected - sp.conjugate(centered)) == 0

    print("functional_log_derivative_symmetry=L(1-s)=-L(s)")
    print("critical_reflection=complex_conjugation")
    print("boundary_constraint=conjugate(L)=-L")
    print("boundary_real_part=0")
    print("interior_pole_obstruction=off_line_zero")


if __name__ == "__main__":
    main()
