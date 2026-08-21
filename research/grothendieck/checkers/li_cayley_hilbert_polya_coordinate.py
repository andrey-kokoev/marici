"""Exact Cayley recovery of the centered zero ordinate from the rigid Li phase."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, u, gamma = sp.symbols("s u gamma", real=False)
    phase = 1 - 1 / s
    inverse = sp.solve(sp.Eq(u, phase), s)[0]
    assert sp.simplify(inverse - 1 / (1 - u)) == 0

    centered = sp.simplify((2 * inverse - 1) / (2 * sp.I))
    cayley = sp.simplify((1 + u) / (2 * sp.I * (1 - u)))
    assert sp.simplify(centered - cayley) == 0

    critical_s = sp.Rational(1, 2) + sp.I * gamma
    critical_u = sp.simplify(phase.subs(s, critical_s))
    recovered = sp.simplify(cayley.subs(u, critical_u))
    assert sp.simplify(recovered - gamma) == 0

    print("inverse_mobius=s=1/(1-u)")
    print("centered_cayley=(1+u)/(2*i*(1-u))")
    print("critical_ordinate_recovery_residual=0")
    print("singular_phase=u=1")


if __name__ == "__main__":
    main()
