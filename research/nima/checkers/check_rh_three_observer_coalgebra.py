#!/usr/bin/env python3
"""Finite falsifiers for compressing the theta dilation orbit to a finite observer."""

import json
from fractions import Fraction
from pathlib import Path


def dilation(coefficients):
    """Apply P -> 2 X P' + (1/2 - 2 X) P in coefficient coordinates."""
    result = [Fraction(0) for _ in range(len(coefficients) + 1)]
    for degree, coefficient in enumerate(coefficients):
        result[degree] += Fraction(2 * degree, 1) * coefficient
        result[degree] += Fraction(1, 2) * coefficient
        result[degree + 1] -= 2 * coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


orbit = [[Fraction(1)]]
for _ in range(8):
    orbit.append(dilation(orbit[-1]))

degrees = [len(polynomial) - 1 for polynomial in orbit]
leading = [polynomial[-1] for polynomial in orbit]

assert degrees == list(range(9))
assert leading == [Fraction((-2) ** k) for k in range(9)]

# A projection retaining degrees at most N agrees at the present stage but loses
# the first new direction after one more dilation.
escape_witnesses = []
for cutoff in range(8):
    current = orbit[cutoff]
    successor = orbit[cutoff + 1]
    assert len(current) <= cutoff + 1
    assert successor[cutoff + 1] != 0
    escape_witnesses.append(
        {
            "retained_degree": cutoff,
            "escaped_degree": cutoff + 1,
            "escaped_coefficient": str(successor[cutoff + 1]),
        }
    )

result = {
    "dilation_degrees": degrees,
    "leading_coefficients": [str(value) for value in leading],
    "every_tested_finite_degree_projection_leaks": True,
    "escape_witnesses": escape_witnesses,
    "verdict": (
        "finite present-record observers are not closed under native dilation; "
        "the state must retain a function-valued continuation, an infinite orbit, "
        "or a separately sourced nonlinear transformed-argument law"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-three-observer-coalgebra.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
