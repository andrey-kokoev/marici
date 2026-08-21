"""Dependency-free counterexample to positive-heat-implies-Stieltjes."""

import cmath
import json
import math
from pathlib import Path


epsilon = 0.5
frequency = 4.0


def theta(t):
    return math.exp(-t) * (1 + epsilon * math.cos(frequency * t))


assert 1 - epsilon > 0
assert all(theta(k / 20) > 0 for k in range(201))

# -Theta'=e^-t[1+epsilon*cos(bt)+epsilon*b*sin(bt)].
phase = math.atan2(-epsilon * frequency, -epsilon) % (2 * math.pi)
t_bad = phase / frequency
minus_first_derivative = math.exp(-t_bad) * (
    1
    + epsilon * math.cos(frequency * t_bad)
    + epsilon * frequency * math.sin(frequency * t_bad)
)
assert minus_first_derivative < 0

poles = [-1 + 1j * frequency, -1 - 1j * frequency]
assert all(abs(pole.imag) > 0 for pole in poles)

result = {
    "heat_kernel": "exp(-t)*(1+epsilon*cos(b*t))",
    "epsilon": epsilon,
    "frequency": frequency,
    "strictly_positive_for_all_t": True,
    "bad_derivative_time": t_bad,
    "minus_first_derivative_at_bad_time": minus_first_derivative,
    "completely_monotone_in_t": False,
    "Laplace_transform_off_axis_poles": [str(pole) for pole in poles],
    "Stieltjes": False,
    "pointwise_heat_positivity_implies_RH": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "scalar-heat-positivity-not-stieltjes.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
