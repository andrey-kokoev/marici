"""Dependency-free exact-threshold audit for a signed three-atom measure."""

import json
import math
from pathlib import Path


sigma_threshold = 1 / (4 * math.log(2))
t_threshold = math.log(2)


def normalized_bracket(sigma, x):
    return 2 * math.exp(-1 / (4 * sigma)) * math.cosh(x / (2 * sigma)) - 1


assert abs(normalized_bracket(sigma_threshold, 0.0)) < 1e-15
assert normalized_bracket(sigma_threshold * 0.9, 0.0) < 0
assert normalized_bracket(sigma_threshold * 1.1, 0.0) > 0

for factor in [1.0, 1.1, 2.0, 10.0]:
    sigma = sigma_threshold * factor
    samples = [normalized_bracket(sigma, x / 4) for x in range(-40, 41)]
    assert min(samples) >= -1e-15
    assert abs(min(samples) - normalized_bracket(sigma, 0.0)) < 1e-15

result = {
    "signed_measure": "delta_-1+delta_1-delta_0",
    "sigma_threshold": sigma_threshold,
    "exact_sigma_threshold": "1/(4 log 2)",
    "exact_inverse_time_threshold": "log 2",
    "broad_smoothing_positive": True,
    "narrow_smoothing_detects_negative_atom": True,
    "positivity_propagates_to_larger_variance": True,
    "positivity_propagates_to_larger_inverse_time": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "weil-gaussian-positivity-threshold.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
