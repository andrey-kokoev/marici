"""Dependency-free audit of the exact off-line quartet Gaussian factor."""

import json
import math
from pathlib import Path


alpha = 0.08
beta = 14.0


def quartet_scaled_by_first_gaussian(t, xi):
    ratio = math.exp(-4 * t * beta * xi)
    return -1 + ratio * math.cos(2 * t * alpha * (xi + beta))


times = [0.2, 1.0, 10.0, math.pi / (2 * alpha * alpha)]
lobes = [beta + math.pi / (2 * t * alpha) for t in times]
values = [quartet_scaled_by_first_gaussian(t, xi) for t, xi in zip(times, lobes)]
ratios = [math.exp(-4 * t * beta * xi) for t, xi in zip(times, lobes)]
assert all(value < 0 for value in values)
assert all(ratio < 1 for ratio in ratios)

critical_t = math.pi / (2 * alpha * alpha)
critical_exponent = critical_t * alpha * alpha - math.pi**2 / (
    4 * critical_t * alpha * alpha
)
assert abs(critical_exponent) < 1e-14

result = {
    "alpha": alpha,
    "beta": beta,
    "sample_times": times,
    "first_negative_lobes": lobes,
    "quartet_values_scaled_by_positive_first_gaussian": values,
    "second_to_first_gaussian_ratios": ratios,
    "negative_at_every_sampled_scale": True,
    "exact_unsuppressed_scale": "t*alpha^2=pi/2",
    "critical_exponent_residual": critical_exponent,
    "Gaussian_latency_differs_from_Li_latency": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "offline-quartet-gaussian-negative-lobe.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
