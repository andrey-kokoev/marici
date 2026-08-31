#!/usr/bin/env python3
"""Numerical scout for the normalized theta-plane compression tau.

This checks the explicit theta series on the even half-line. It is not an
interval-certified proof and does not identify the ledger incidence columns.
"""

from __future__ import annotations

import json
import math


def phi_and_derivative(u: float) -> tuple[float, float]:
    eu = math.exp(2.0 * u)
    prefactor = math.exp(0.5 * u)
    phi = 0.0
    derivative = 0.0
    for n in range(1, 1000):
        x = math.pi * n * n * eu
        if x > 745.0:
            break
        exponential = math.exp(-x)
        phi += prefactor * exponential * (4.0 * x * x - 6.0 * x)
        derivative -= prefactor * exponential * x * (
            8.0 * x * x - 30.0 * x + 15.0
        )
    return phi, derivative


def simpson_square(component: int, endpoint: float, panels: int) -> float:
    assert panels % 2 == 0
    step = endpoint / panels
    total = 0.0
    for index in range(panels + 1):
        value = phi_and_derivative(index * step)[component]
        weight = 1 if index in (0, panels) else 4 if index % 2 else 2
        total += weight * value * value
    # Phi is even and Phi' odd, so double the positive-half-line integral.
    return 2.0 * step * total / 3.0


def main() -> None:
    endpoint = 4.0
    coarse_panels = 20_000
    fine_panels = 40_000
    coarse = (
        simpson_square(0, endpoint, coarse_panels),
        simpson_square(1, endpoint, coarse_panels),
    )
    fine = (
        simpson_square(0, endpoint, fine_panels),
        simpson_square(1, endpoint, fine_panels),
    )
    relative_changes = tuple(
        abs(a - b) / max(abs(b), 1e-300) for a, b in zip(coarse, fine)
    )
    assert max(relative_changes) < 1e-10
    tau = -math.sqrt(fine[0] / fine[1])
    assert -1.0 < tau < 0.0
    print(
        json.dumps(
            {
                "schema": "marici.nima.rh_theta_tau_compression_numeric.v1",
                "scope": "numerical_scout_not_interval_proof",
                "integration_endpoint": endpoint,
                "fine_panels": fine_panels,
                "phi_l2_squared": fine[0],
                "phi_derivative_l2_squared": fine[1],
                "tau_theta": tau,
                "coarse_fine_relative_changes": relative_changes,
                "normalized_scalar_margin": 1.0 - abs(tau),
                "ledger_incidence_columns_identified": False,
                "verdict": "normalized_theta_plane_tau_is_negative_and_strictly_inside_unit_interval_numerically",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
