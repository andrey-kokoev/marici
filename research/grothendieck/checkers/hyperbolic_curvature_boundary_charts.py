"""Diagnostic boundary charts for the normalized critical curvature."""

from __future__ import annotations

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature, state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


def critical_point(p: float, q: float) -> tuple[float, float]:
    left, right = 1e-10, 1.0
    while boundary_derivative(p, q, right) > 0.0:
        right *= 2.0
    for _ in range(70):
        midpoint = (left + right) / 2.0
        if boundary_derivative(p, q, midpoint) > 0.0:
            left = midpoint
        else:
            right = midpoint
    holding = (left + right) / 2.0
    t, r = state(p, q, holding)
    normalized = -directional_curvature(t, r, p, q) / (p * p * (1.0 - p * p) ** 2)
    return holding, normalized


def main() -> None:
    print("coalescing_unit_slope_chart")
    for epsilon in (1e-2, 1e-3, 1e-4, 1e-5):
        p = 1.0 - epsilon
        print(epsilon, critical_point(p, p))
    print("small_slope_chart_q_over_p_one_half")
    for p in (1e-2, 1e-3, 1e-4, 1e-5):
        print(p, critical_point(p, p / 2.0))


if __name__ == "__main__":
    main()
