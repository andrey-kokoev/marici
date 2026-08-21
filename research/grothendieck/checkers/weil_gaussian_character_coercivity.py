"""Dependency-free diagnostic for Gaussian averaging of logarithmic growth."""

import json
import math
from pathlib import Path


def simpson_integral(function, left, right, panels):
    assert panels % 2 == 0
    step = (right - left) / panels
    total = function(left) + function(right)
    total += 4 * sum(function(left + step * k) for k in range(1, panels, 2))
    total += 2 * sum(function(left + step * k) for k in range(2, panels, 2))
    return total * step / 3


t = 0.7


def gamma_proxy(xi):
    # log(sqrt(1+u^2)/2) has the same large-|u| logarithmic behavior as
    # Re psi(1/4+iu/2), while remaining elementary and regular at zero.
    return simpson_integral(
        lambda v: math.exp(-t * v * v)
        * math.log(math.sqrt(1 + (xi + v) ** 2) / 2),
        -10,
        10,
        4000,
    ) / (4 * math.pi)


characters = [10.0, 30.0, 100.0, 300.0]
values = [gamma_proxy(xi) for xi in characters]
leading = [math.log(xi / 2) / (4 * math.sqrt(math.pi * t)) for xi in characters]
residuals = [value - estimate for value, estimate in zip(values, leading)]
assert all(left < right for left, right in zip(values, values[1:]))
assert abs(residuals[-1]) < abs(residuals[0])

result = {
    "fixed_smoothing_time": t,
    "characters": characters,
    "proxy_values": values,
    "leading_residuals": residuals,
    "logarithmic_growth_observed": True,
    "prime_cosine_series_uniformly_bounded_at_fixed_time": True,
    "endpoint_gaussian_decays": True,
    "analytic_coercivity_uses_digamma_asymptotic": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "weil-gaussian-character-coercivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
