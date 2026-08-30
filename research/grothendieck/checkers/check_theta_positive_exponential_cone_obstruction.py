#!/usr/bin/env python3
"""Audit the seam-jet obstruction to positive exponential membership."""

import math


def moment(k: int, cutoff: int = 12) -> float:
    return sum(
        (math.pi * n * n) ** k * math.exp(-math.pi * n * n)
        for n in range(1, cutoff + 1)
    )


moments = [moment(k) for k in range(5)]
m1, m2, m3, m4 = moments[1], moments[2], moments[3], moments[4]

phi = 4.0 * m2 - 6.0 * m1
phi_prime = 30.0 * m2 - 15.0 * m1 - 8.0 * m3
phi_second = 165.0 * m2 - 112.0 * m3 + 16.0 * m4 - 37.5 * m1
curvature = phi * phi_second - phi_prime * phi_prime

# A representative positive exponential packet must have nonnegative
# logarithmic curvature.
alphas = [0.5, 1.25, 3.0]
coefficients = [1.0, 0.7, 2.0]
f0 = sum(coefficients)
f1 = -sum(c * alpha for c, alpha in zip(coefficients, alphas))
f2 = sum(c * alpha * alpha for c, alpha in zip(coefficients, alphas))
positive_mode_curvature = f0 * f2 - f1 * f1

checks = {
    "theta_value_positive": phi > 0.8,
    "modular_evenness_visible_in_first_jet": abs(phi_prime) < 1.0e-12,
    "theta_second_jet_negative": phi_second < -16.0,
    "theta_log_curvature_negative": curvature < -14.0,
    "positive_mode_log_curvature_positive": positive_mode_curvature > 0.0,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "theta": {
            "phi": phi,
            "phi_prime": phi_prime,
            "phi_second": phi_second,
            "log_curvature_numerator": curvature,
        },
        "positive_mode_curvature": positive_mode_curvature,
    }
)

if failed:
    raise SystemExit(1)

