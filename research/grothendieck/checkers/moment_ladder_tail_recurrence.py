"""Exact elimination audit for the theta moment-to-tail recurrence."""

import json
from pathlib import Path

import sympy as sp


z, F0, m0, m1 = sp.symbols("z F0 m0 m1")
F1 = ((z + sp.Rational(1, 2)) * F0 + m0) / 2
F2 = ((z + sp.Rational(5, 2)) * F1 + m1) / 2
physical = sp.expand(4 * F2 - 6 * F1)
expected = sp.expand((z**2 - sp.Rational(1, 4)) * F0 + (z - sp.Rational(1, 2)) * m0 + 2 * m1)

F0_minus = sp.symbols("F0_minus")
bilateral = sp.expand(physical + physical.subs({z: -z, F0: F0_minus}))
bilateral_expected = sp.expand((z**2 - sp.Rational(1, 4)) * (F0 + F0_minus) - m0 + 4 * m1)

checks = {
    "half_transform_elimination": sp.simplify(physical - expected) == 0,
    "bilateral_sewing": sp.simplify(bilateral - bilateral_expected) == 0,
    "odd_seam_coefficient_cancels": sp.expand(bilateral).coeff(z, 1) == 0,
}

result = {
    "schema": "marici.grothendieck.moment_ladder_tail_recurrence.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "half_transform": str(expected),
    "bilateral_transform": str(bilateral_expected),
    "zero_level_set": "(z^2-1/4)X0(z)=M0(0)-4M1(0)",
}

output = Path(__file__).parents[1] / "results" / "moment_ladder_tail_recurrence.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

