#!/usr/bin/env python3
"""Exact rational outward intervals and angle-margin certificates."""

import json
from fractions import Fraction as F
from pathlib import Path


def interval(low, high):
    assert low <= high
    return low, high

def add(x, y): return x[0] + y[0], x[1] + y[1]
def mul(x, y):
    products = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(products), max(products)
def contains(x, value): return x[0] <= value <= x[1]
def width(x): return x[1] - x[0]

def sin_interval(x):
    assert 0 <= x <= 1
    upper = x - x**3 / 6 + x**5 / 120
    lower = upper - x**7 / 5040
    return interval(lower, upper)
def cos_interval(x):
    assert 0 <= x <= 1
    upper = 1 - x**2 / 2 + x**4 / 24
    lower = upper - x**6 / 720
    return interval(lower, upper)

x = F(1, 3)
s = sin_interval(x)
c = cos_interval(x)
norm_interval = add(mul(s, s), mul(c, c))
effect_00 = mul(c, c)
effect_01 = mul(c, s)
effect_11 = mul(s, s)
trace_interval = add(effect_00, effect_11)

nominal_margin = F(1, 20)
weights = (F(1), F(1))
radii = (F(1, 100), F(1, 100))
perturbation_budget = sum(weight * radius for weight, radius in zip(weights, radii))
residual_margin = nominal_margin - perturbation_budget
hostile_radii = (F(1, 20), F(1, 20))
hostile_budget = sum(weight * radius for weight, radius in zip(weights, hostile_radii))
hostile_residual = nominal_margin - hostile_budget
checks = {
    "sine_interval_is_ordered": s[0] <= s[1],
    "cosine_interval_is_ordered": c[0] <= c[1],
    "alternating_remainders_are_nonzero": width(s) == x**7 / 5040 and width(c) == x**6 / 720,
    "structural_norm_value_is_enclosed": contains(norm_interval, F(1)),
    "effect_trace_interval_encloses_one": contains(trace_interval, F(1)),
    "effect_entry_intervals_are_nonnegative": effect_00[0] >= 0 and effect_01[0] >= 0 and effect_11[0] >= 0,
    "angle_perturbation_budget_is_exact": perturbation_budget == F(1, 50),
    "positive_margin_is_certified": residual_margin == F(3, 100) and residual_margin > 0,
    "hostile_budget_exceeds_margin": hostile_budget == F(1, 10) and hostile_budget > nominal_margin,
    "hostile_certificate_is_rejected": hostile_residual == F(-1, 20) and hostile_residual < 0,
    "dependency_inflation_is_retained": width(norm_interval) > 0,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.outward-interval-arbitrary-angles.v1", "status": "passed", "checks": checks, "angle": str(x), "sin_interval": [str(value) for value in s], "cos_interval": [str(value) for value in c], "norm_interval": [str(value) for value in norm_interval], "residual_margin": str(residual_margin), "hostile_residual": str(hostile_residual), "claim_boundary": "Rational Taylor enclosure for |angle|<=1 and Lipschitz slack margin; not general transcendental interval arithmetic."}
output = Path(__file__).parents[1] / "results" / "outward_interval_arbitrary_angles.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "residual_margin": str(residual_margin), "hostile_residual": str(hostile_residual)}, sort_keys=True))
