"""Hostile exact-derivative sweep at critical points of the boundary margin."""

from __future__ import annotations

import json
import math
import random

from hyperbolic_boundary_unimodality_sweep import boundary_derivative


def state(p: float, q: float, holding: float) -> tuple[float, float]:
    up, uq = math.atanh(p), math.atanh(q)
    descent = up - uq
    image = 0.5 * math.log((1.0 - q * q) / (1.0 - p * p))
    return math.tanh((descent + holding) / 2.0), math.tanh((image + p * holding) / 2.0)


def directional_curvature(t: float, r: float, p: float, q: float) -> float:
    slope_sum, slope_product = p + q, p * q
    b = 1.0 - 2.0 * t * t - t * t * slope_product
    n_t = (
        4.0 * t**3 + 2.0 * t * slope_product
        - 2.0 * t * (2.0 + slope_product) * r * r
        - slope_sum * r * (1.0 - r * r)
    )
    n_r = -t * slope_sum + 2.0 * b * r + 3.0 * t * slope_sum * r * r
    n_tt = 12.0 * t * t + 2.0 * slope_product - 2.0 * (2.0 + slope_product) * r * r
    n_tr = -4.0 * t * (2.0 + slope_product) * r - slope_sum * (1.0 - 3.0 * r * r)
    n_rr = 2.0 * b + 6.0 * t * slope_sum * r
    vt, vr = 1.0 - t * t, p * (1.0 - r * r)
    return (
        -2.0 * t * vt * n_t - 2.0 * p * r * vr * n_r
        + vt * vt * n_tt + 2.0 * vt * vr * n_tr + vr * vr * n_rr
    )


def main() -> None:
    generator = random.Random(20260821)
    trials = 100_000
    largest = (-math.inf, None)
    normalized_minimum = (math.inf, None)
    failures = 0
    roots = 0
    for _ in range(trials):
        p = generator.random()
        q = generator.random() * p
        grid = [10.0 ** (-6.0 + 9.0 * index / 119.0) for index in range(120)]
        derivatives = [boundary_derivative(p, q, holding) for holding in grid]
        for index in range(len(grid) - 1):
            if not (derivatives[index] > 0.0 and derivatives[index + 1] < 0.0):
                continue
            left, right = grid[index], grid[index + 1]
            for _ in range(50):
                midpoint = (left + right) / 2.0
                if boundary_derivative(p, q, midpoint) > 0.0:
                    left = midpoint
                else:
                    right = midpoint
            holding = (left + right) / 2.0
            t, r = state(p, q, holding)
            curvature = directional_curvature(t, r, p, q)
            roots += 1
            if curvature > largest[0]:
                largest = (curvature, (p, q, holding, t, r))
            normalizer = p * p * (1.0 - p * p) ** 2
            if normalizer > 0.0:
                normalized = -curvature / normalizer
                if normalized < normalized_minimum[0]:
                    normalized_minimum = (normalized, (p, q, holding, t, r))
            if curvature >= 1e-10:
                failures += 1
            break
    print(json.dumps({
        "trials": trials,
        "critical_points_found": roots,
        "nonnegative_above_1e-10": failures,
        "largest_directional_curvature": largest,
        "minimum_normalized_negative_curvature": normalized_minimum,
    }, indent=2))


if __name__ == "__main__":
    main()
