"""Exact hostile test for varying the limiting critical branch.

The selected branch must have Q_L=-sqrt(discriminant).  Replacing it by the
other algebraic root reverses the transverse sign and therefore selects a
minimum instead of the source-required maximum.
"""

from __future__ import annotations

import sympy as sp

from hyperbolic_inward_monotonicity_symbolic import generate, k, l, t


def main() -> None:
    _, _, q, _ = generate()
    polynomial = sp.Poly(q, l)
    q2 = sp.factor(polynomial.coeff_monomial(l**2))
    q1 = polynomial.coeff_monomial(l)
    discriminant = sp.factor(sp.discriminant(q, l))
    square_root = sp.sqrt(discriminant)

    maximum_root = sp.cancel((-q1 - square_root) / (2 * q2))
    opposite_root = sp.cancel((-q1 + square_root) / (2 * q2))
    transverse = sp.diff(q, l)

    maximum_residual = sp.simplify(transverse.subs(l, maximum_root) + square_root)
    opposite_residual = sp.simplify(transverse.subs(l, opposite_root) - square_root)
    maximum_critical_residual = sp.simplify(q.subs(l, maximum_root))
    opposite_critical_residual = sp.simplify(q.subs(l, opposite_root))

    expected_q2 = t * (t - 1) * (t + 1) * (3 * t - 1) * (3 * t + 1) / 4
    assert sp.expand(q2 - expected_q2) == 0
    assert maximum_residual == 0
    assert opposite_residual == 0
    assert maximum_critical_residual == 0
    assert opposite_critical_residual == 0

    print(f"q2_factor={q2}")
    print("q2_negative_on_one_third_lt_t_lt_one=True")
    print("maximum_branch_Q_L=-sqrt(discriminant)")
    print("opposite_branch_Q_L=+sqrt(discriminant)")
    print("maximum_critical_residual=0")
    print("opposite_critical_residual=0")
    print("opposite_branch_is_maximum=False")
    print("deliberate_failure_exhibited=True")


if __name__ == "__main__":
    main()
