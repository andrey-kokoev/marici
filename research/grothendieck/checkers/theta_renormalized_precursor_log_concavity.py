"""Hostile PF2/log-concavity scan for the renormalized theta precursor."""

import json
import math
from pathlib import Path


def precursor_jet(u, order, max_label=12):
    """Return K and its first two derivatives for u >= 0."""
    if order not in (0, 1, 2):
        raise ValueError("only jets through order two are implemented")

    # K(u) = exp(-u/2)/2 - sum_n exp(u/2-pi*n^2*exp(2u)).
    base = 0.5 * ((-0.5) ** order) * math.exp(-0.5 * u)
    x_scale = math.exp(2.0 * u)
    total = base
    for n in range(1, max_label + 1):
        x = math.pi * n * n * x_scale
        value = math.exp(0.5 * u - x)
        if order == 0:
            jet = value
        elif order == 1:
            jet = (0.5 - 2.0 * x) * value
        else:
            jet = ((0.5 - 2.0 * x) ** 2 - 4.0 * x) * value
        total -= jet
    return total


def row(u):
    k0 = precursor_jet(u, 0)
    k1 = precursor_jet(u, 1)
    k2 = precursor_jet(u, 2)
    numerator = k0 * k2 - k1 * k1
    return {
        "u": u,
        "K": k0,
        "K_prime": k1,
        "K_second": k2,
        "log_curvature_numerator_KKsecond_minus_Kprime_squared": numerator,
        "log_concave_at_sample": k0 > 0.0 and numerator <= 0.0,
    }


sample_points = [index / 100.0 for index in range(0, 401)]
rows = [row(u) for u in sample_points]
positive_curvature_rows = [
    item
    for item in rows
    if item["log_curvature_numerator_KKsecond_minus_Kprime_squared"] > 0.0
]

result = {
    "source": "K(u)=cosh(u/2)-exp(u/2)*Theta(exp(2u))/2",
    "sample_interval": [0.0, 4.0],
    "sample_step": 0.01,
    "max_theta_label": 12,
    "all_sampled_K_positive": all(item["K"] > 0.0 for item in rows),
    "all_samples_log_concave": not positive_curvature_rows,
    "first_positive_log_curvature_sample": positive_curvature_rows[0] if positive_curvature_rows else None,
    "largest_log_curvature_numerator_sample": max(
        rows,
        key=lambda item: item["log_curvature_numerator_KKsecond_minus_Kprime_squared"],
    ),
    "smallest_log_curvature_numerator_sample": min(
        rows,
        key=lambda item: item["log_curvature_numerator_KKsecond_minus_Kprime_squared"],
    ),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-renormalized-precursor-log-concavity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
