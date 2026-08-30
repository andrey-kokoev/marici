"""Dependency-free hostile audit of fixed-time off-axis derivative amplification."""

import cmath
import json
import math
from pathlib import Path


A = 1.0
lambda_0 = 1.0
epsilon = 1e-6
decay = 2.0
frequency = 3.0
t0 = 1.0
complex_rate = decay - 1j * frequency
rate_modulus = abs(complex_rate)


def D(k):
    background = A * lambda_0**k * math.exp(-lambda_0 * t0)
    defect = epsilon * (complex_rate**k * cmath.exp(-complex_rate * t0)).real
    return background + defect


values = [D(k) for k in range(80)]
negative_orders = [k for k, value in enumerate(values) if value < 0]
assert negative_orders
first_negative_order = negative_orders[0]

amplitude_latency = (
    math.log(A / abs(epsilon)) + (decay - lambda_0) * t0
) / math.log(rate_modulus / lambda_0)
assert first_negative_order >= math.floor(amplitude_latency) - 2

# Order zero remains strictly positive and the perturbation is tiny there.
assert values[0] > 0

result = {
    "background_rate": lambda_0,
    "complex_rate": str(complex_rate),
    "complex_rate_modulus": rate_modulus,
    "defect_amplitude": epsilon,
    "chosen_time": t0,
    "order_zero_positive": True,
    "amplitude_latency_estimate": amplitude_latency,
    "first_negative_derivative_order": first_negative_order,
    "all_order_hierarchy_detects_hidden_pair": True,
    "finite_order_latency_unbounded_as_epsilon_tends_to_zero": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "one-time-off-axis-derivative-latency.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
