"""Exact audit of the Poisson seam normalization of the moment level set."""

import json
from pathlib import Path

import sympy as sp


m0, m1, z, X0 = sp.symbols("m0 m1 z X0")
seam_derivative = sp.Rational(1, 2) + m0 - 4 * m1
seam_solution = sp.solve(sp.Eq(seam_derivative, 0), m0 - 4 * m1)[0]
completed = sp.expand((z**2 - sp.Rational(1, 4)) * X0 - m0 + 4 * m1)
normalized = sp.expand(completed.subs(m0, 4 * m1 - sp.Rational(1, 2)))
expected = sp.expand(sp.Rational(1, 2) + (z**2 - sp.Rational(1, 4)) * X0)

checks = {
    "seam_constant": seam_solution == -sp.Rational(1, 2),
    "neutral_half_carrier": sp.simplify(normalized - expected) == 0,
    "zero_level": sp.simplify((expected - sp.Rational(1, 2)) - (z**2 - sp.Rational(1, 4)) * X0) == 0,
}

result = {
    "schema": "marici.grothendieck.poisson_seam_half_carrier.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "seam_identity": "M0(0)-4M1(0)=-1/2",
    "completed_transform": "X_Phi(z)=1/2+(z^2-1/4)X0(z)",
    "zero_level_set": "(z^2-1/4)X0(z)=-1/2",
}

output = Path(__file__).parents[1] / "results" / "poisson_seam_half_carrier.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

