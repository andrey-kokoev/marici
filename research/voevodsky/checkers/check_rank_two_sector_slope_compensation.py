from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/rank-two-sector-slope-compensation-v1.json")


def determinant(x: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
    return sp.expand(x[0] * x[2] - x[1] ** 2)


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2", nonzero=True, real=True)
    a = (a0, a1, a2)
    b = (b0, b1, b2)
    total = tuple(a[i] + b[i] for i in range(3))
    cross = a0 * b2 + a2 * b0 - 2 * a1 * b1
    assert sp.expand(determinant(total) - determinant(a) - determinant(b) - cross) == 0

    mu_a, mu_b = a1 / a0, b1 / b0
    delta_a, delta_b = determinant(a) / a0**2, determinant(b) / b0**2
    normalized = (a0 + b0) * (a0 * delta_a + b0 * delta_b) + a0 * b0 * (mu_a - mu_b) ** 2
    assert sp.simplify(determinant(total) - normalized) == 0

    # Both sectors fail, while separation of slopes makes the sum pass.
    sector_a = (sp.Rational(1), sp.Rational(0), sp.Rational(-1, 10))
    sector_b = (sp.Rational(1), sp.Rational(1), sp.Rational(9, 10))
    assert determinant(sector_a) < 0
    assert determinant(sector_b) < 0
    combined = tuple(sector_a[i] + sector_b[i] for i in range(3))
    assert determinant(combined) > 0

    # Equal slopes remove the separation resource and preserve a negative result.
    hostile_a = (sp.Rational(1), sp.Rational(1, 2), sp.Rational(1, 5))
    hostile_b = (sp.Rational(2), sp.Rational(1), sp.Rational(2, 5))
    assert hostile_a[1] / hostile_a[0] == hostile_b[1] / hostile_b[0]
    assert determinant(hostile_a) < 0 and determinant(hostile_b) < 0
    hostile_total = tuple(hostile_a[i] + hostile_b[i] for i in range(3))
    assert determinant(hostile_total) < 0

    result = {
        "schema":"marici.voevodsky.rank-two-sector-slope-compensation-check.v1",
        "status":"sector_slope_compensation_identity_verified",
        "polarization_identity":True,
        "normalized_identity":True,
        "double_negative_compensation_fixture":True,
        "equal_slope_hostile_fixture":True,
        "source_interval_bound":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
