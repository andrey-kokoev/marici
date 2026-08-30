"""Evaluate the exact coalescing-unit-slope limiting curvature function."""

from __future__ import annotations

import math


def limit_margin(x: float) -> float:
    t = math.tanh(x)
    s = 1.0 - t * t
    return t * t * s - 2.0 * x * t * s * s + (1.0 + 3.0 * t * t) * x * x * s * s


def derivative(x: float, step: float = 1e-5) -> float:
    return (limit_margin(x + step) - limit_margin(x - step)) / (2.0 * step)


def second_derivative(x: float, step: float = 2e-4) -> float:
    return (limit_margin(x + step) - 2.0 * limit_margin(x) + limit_margin(x - step)) / (step * step)


def main() -> None:
    left, right = 0.5, 2.0
    for _ in range(70):
        midpoint = (left + right) / 2.0
        if derivative(midpoint) > 0.0:
            left = midpoint
        else:
            right = midpoint
    x_star = (left + right) / 2.0
    curvature = -second_derivative(x_star) / 4.0
    print(f"x_star={x_star:.15g}")
    print(f"L_star={2.0*x_star:.15g}")
    print(f"limit_margin={limit_margin(x_star):.15g}")
    print(f"normalized_negative_curvature={curvature:.15g}")


if __name__ == "__main__":
    main()
