#!/usr/bin/env python3
"""Hostile showing that pseudoscalar preservation does not preserve Clifford scalars."""

import json
from fractions import Fraction
from pathlib import Path


def determinant_diagonal(diagonal):
    result = Fraction(1)
    for entry in diagonal:
        result *= entry
    return result


def quadratic(diagonal_metric, vector):
    return sum(metric * coordinate * coordinate for metric, coordinate in zip(diagonal_metric, vector))


metric = (Fraction(1), Fraction(1), Fraction(1), Fraction(1))
squeeze = (Fraction(2), Fraction(1, 2), Fraction(1), Fraction(1))
assert determinant_diagonal(squeeze) == 1

x = (Fraction(1), Fraction(1), Fraction(0), Fraction(0))
sx = tuple(scale * coordinate for scale, coordinate in zip(squeeze, x))
q_before = quadratic(metric, x)
q_after = quadratic(metric, sx)
assert q_before == 2
assert q_after == Fraction(17, 4)

# Conformal preservation would require every squared scale to equal one common lambda.
squared_scales = tuple(scale * scale for scale in squeeze)
conformal = len(set(squared_scales)) == 1
assert not conformal

# A uniform scale is conformal and separates scale from orientation.
uniform = (Fraction(3),) * 4
uniform_squared = tuple(scale * scale for scale in uniform)
assert len(set(uniform_squared)) == 1

result = {
    "squeeze_determinant": str(determinant_diagonal(squeeze)),
    "pseudoscalar_preserved": True,
    "quadratic_before": str(q_before),
    "quadratic_after": str(q_after),
    "squeeze_is_conformal": conformal,
    "uniform_scale_conformal_factor": str(uniform_squared[0]),
    "verdict": (
        "top-grade preservation does not control the Clifford scalar channel; source "
        "transport must satisfy a metric or conformal-Clifford law"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-clifford-conformal-gate.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
