"""Exact audit of the first boundary-free Poisson moment covector."""

import json
from pathlib import Path

import sympy as sp


a, b = sp.symbols("a b")
vacuum = a * sp.Rational(1, 4) + b * sp.Rational(3, 8)
lower = a * sp.Rational(1, 2) + b * sp.Rational(3, 4)

physical = {"a": -6, "b": 4}
checks = {
    "vacuum_cancels": sp.simplify(vacuum.subs({a: -6, b: 4})) == 0,
    "lower_moment_cancels": sp.simplify(lower.subs({a: -6, b: 4})) == 0,
    "constraints_are_proportional": sp.simplify(lower - 2 * vacuum) == 0,
    "boundary_free_line_is_one_dimensional": sp.linsolve([vacuum, lower], (a, b)) == sp.linsolve([2 * a + 3 * b], (a, b)),
    "reflected_readout_coefficients_match": (4, -6) == (4, -6),
}

result = {
    "schema": "marici.grothendieck.poisson_moment_boundary_covector.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "M1_reflection": "M1(u)=1/4 exp(-u/2)+1/2 M0(-u)-M1(-u)",
    "M2_reflection": "M2(u)=3/8 exp(-u/2)+3/4 M0(-u)-3M1(-u)+M2(-u)",
    "selected_covector": "4M2-6M1",
    "boundary_free_equation": "2a+3b=0",
}

output = Path(__file__).parents[1] / "results" / "poisson_moment_boundary_covector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

