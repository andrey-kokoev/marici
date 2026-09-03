from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/rank-two-common-center-coupled-cone-v1.json")


def d2(x: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
    return sp.expand(x[0] * x[2] - x[1] ** 2)


def centered(x: tuple[sp.Expr, sp.Expr, sp.Expr], r: sp.Expr) -> sp.Expr:
    return sp.expand(x[2] - 2 * r * x[1] + r**2 * x[0])


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    A0, A1, A2, r = sp.symbols("A0 A1 A2 r", real=True)
    A = (A0, A1, A2)
    assert sp.expand(d2(A) - (A0 * centered(A, r) - (A1 - r * A0) ** 2)) == 0

    g0, g1, g2, p0, p1, p2 = sp.symbols("g0 g1 g2 p0 p1 p2", real=True)
    g, p = (g0, g1, g2), (p0, p1, p2)
    total = tuple(g[k] + p[k] for k in range(3))
    assert sp.expand(centered(total, r) - centered(g, r) - centered(p, r)) == 0

    # One sector has negative zeroth moment, but the total cone passes.
    gamma = (sp.Rational(-1, 5), sp.Rational(-1, 10), sp.Rational(-1, 25))
    prime = (sp.Rational(6, 5), sp.Rational(7, 10), sp.Rational(3, 5))
    coupled = tuple(gamma[k] + prime[k] for k in range(3))
    assert gamma[0] < 0 < coupled[0]
    assert d2(coupled) > 0

    optimal = sp.Rational(coupled[1], coupled[0])
    assert sp.simplify(coupled[1] - optimal * coupled[0]) == 0
    assert sp.simplify(d2(coupled) - coupled[0] * centered(coupled, optimal)) == 0

    # A nearby rational center preserves the exact positive certificate with a residual square.
    rational_center = optimal + sp.Rational(1, 100)
    lhs = coupled[0] * centered(coupled, rational_center)
    residual_square = (coupled[1] - rational_center * coupled[0]) ** 2
    assert sp.simplify(lhs - residual_square - d2(coupled)) == 0
    assert lhs > residual_square

    result = {
        "schema":"marici.voevodsky.rank-two-common-center-coupled-cone-check.v1",
        "status":"common_center_coupled_identity_verified",
        "arbitrary_center_identity":True,
        "sector_centered_linearization":True,
        "negative_sector_mass_fixture":True,
        "rational_center_stability_fixture":True,
        "source_interval_enclosure":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
