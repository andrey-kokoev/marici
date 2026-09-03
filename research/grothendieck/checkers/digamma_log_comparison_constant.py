"""Verify the algebraic maximizer in the explicit digamma-log bound."""

import json
from pathlib import Path

import sympy as sp

u = sp.symbols("u", nonnegative=True)
ratio_squared = (1 + u) ** 2 / (sp.Rational(1, 16) + u**2 / 4)
derivative_numerator = sp.factor(sp.together(sp.diff(ratio_squared, u))).as_numer_denom()[0]
critical_value = sp.Rational(1, 4)
checks = {
    "critical_point_is_one_quarter": sp.simplify(derivative_numerator.subs(u, critical_value)) == 0,
    "ratio_squared_at_critical_point_is_twenty": sp.simplify(ratio_squared.subs(u, critical_value)) == 20,
    "endpoint_ratio_squared_is_sixteen": ratio_squared.subs(u, 0) == 16,
    "infinite_ratio_squared_limit_is_four": sp.limit(ratio_squared, u, sp.oo) == 4,
}
result = {
    "schema": "marici.grothendieck.digamma-log-comparison-constant.v1",
    "derivative_numerator": str(derivative_numerator),
    "max_ratio_squared": 20,
    "digamma_minus_log1p_bound": "4 + log(20)/2",
    **checks,
    "all_verified": all(checks.values()),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "digamma-log-comparison-constant.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
