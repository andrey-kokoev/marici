"""Hostile two-scale sweep of the p,q -> 1 critical-curvature chart."""

from __future__ import annotations

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature, state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


def critical_curvature(p: float, q: float) -> tuple[float, float]:
    left, right = 1e-9, 1.0
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
    normalized = -directional_curvature(t, r, p, q) / (p*p*(1.0-p*p)**2)
    return holding, normalized


def main() -> None:
    ks = (0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0)
    for epsilon in (1e-3, 1e-4, 1e-5):
        p = 1.0 - epsilon
        values = []
        for k in ks:
            q = max(0.0, 1.0 - (1.0 + k) * epsilon)
            values.append((k, *critical_curvature(p, q)))
        monotone = all(values[index][2] <= values[index+1][2] for index in range(len(values)-1))
        print(f"epsilon={epsilon} monotone_in_k={monotone}")
        print(values)


if __name__ == "__main__":
    main()
