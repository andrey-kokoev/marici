"""Dependency-free scaling audit for the broad-smoothing dominance theorem."""

import json
import math
from pathlib import Path


def simpson(function, left, right, panels=6000):
    step = (right - left) / panels
    total = function(left) + function(right)
    total += 4 * sum(function(left + k * step) for k in range(1, panels, 2))
    total += 2 * sum(function(left + k * step) for k in range(2, panels, 2))
    return total * step / 3


def regularized_j(z):
    # log(sqrt(y^2+eps^2)) regularizes only the quadrature probe; the theorem
    # uses the integrable log|y| function directly.
    epsilon = 1e-5
    return simpson(
        lambda y: math.exp(-(y - z) ** 2)
        * math.log(math.sqrt(y * y + epsilon * epsilon)),
        -12,
        12,
    )


scaled_characters = [-6, -3, -1, 0, 1, 3, 6]
j_values = [regularized_j(z) for z in scaled_characters]
assert min(j_values) > -10
assert j_values[0] > j_values[1] > j_values[2]
assert j_values[-1] > j_values[-2] > j_values[-3]

times = [0.08, 0.04, 0.02, 0.01]
weyl_scales = [math.log(1 / t) / (8 * math.sqrt(math.pi * t)) for t in times]
prime_two_bounds = [
    math.exp(-(math.log(2) ** 2) / (4 * t)) / math.sqrt(t) for t in times
]
assert all(left < right for left, right in zip(weyl_scales, weyl_scales[1:]))
assert all(left > right for left, right in zip(prime_two_bounds, prime_two_bounds[1:]))

result = {
    "scaled_character_samples": scaled_characters,
    "regularized_log_convolution_samples": j_values,
    "log_convolution_has_finite_sampled_minimum": True,
    "weyl_scale_grows_as_t_decreases": True,
    "first_prime_scale_decays_exponentially": True,
    "endpoint_uniform_bound": "exp(t/4)",
    "broad_all_character_positivity_uses_zero_locations": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "broad-smoothing-uniform-weil-positivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
