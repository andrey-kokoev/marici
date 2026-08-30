"""Hostile sweep for the tilted Riemann-theta third cumulant.

This is a double-precision diagnostic, not a proof. It has no third-party
dependencies and evaluates the theta source with log-stabilized summands.
"""

from __future__ import annotations

import json
import math


def log_cosh(x: float) -> float:
    x = abs(x)
    return x + math.log1p(math.exp(-2.0 * x)) - math.log(2.0)


def log_sinh_positive(x: float) -> float:
    if x == 0.0:
        return -math.inf
    return math.log(math.sinh(x)) if x <= 20.0 else x - math.log(2.0) + math.log1p(-math.exp(-2.0 * x))


def weighted_integrand(u: float, y: float, order: int, log_scale: float = 0.0) -> float:
    """Return Phi(u) u^order cosh/sinh(yu) without overflow."""
    if u == 0.0 and order:
        return 0.0
    e2u = math.exp(2.0 * u)
    log_power = 0.0 if order == 0 else order * math.log(u)
    log_hyperbolic = log_cosh(y * u) if order % 2 == 0 else log_sinh_positive(y * u)
    total = 0.0
    for n in range(1, 40):
        n2 = float(n * n)
        bracket = 2.0 * math.pi * n2 * e2u - 3.0
        log_coefficient = math.log(2.0 * math.pi * n2) + 2.5 * u + math.log(bracket)
        exponent = log_coefficient - math.pi * n2 * e2u + log_power + log_hyperbolic - log_scale
        term = 0.0 if exponent < -745.0 else math.exp(exponent)
        total += term
        if n >= 4 and term <= 1e-16 * max(total, 1e-300):
            break
    return total


def raw_moment(y: float, order: int, intervals: int = 12000) -> float:
    # Fixed composite Simpson is intentionally predictable and shares no
    # recursion overhead.  N=12000 is ample for this smooth super-exponential
    # integrand; the checker below is diagnostic rather than certified.
    right = 6.0
    assert intervals > 0 and intervals % 2 == 0
    step = right / intervals
    # All orders at a fixed height use the same scale, so it cancels from
    # moment ratios.  A coarse source scan is sufficient to prevent overflow;
    # the added margin absorbs the grid displacement and polynomial factors.
    scale_scan = max(
        -math.pi * math.exp(2.0 * index / 200.0)
        + 4.5 * index / 200.0
        + log_cosh(y * index / 200.0)
        for index in range(1201)
    )
    log_scale = max(0.0, scale_scan + 20.0)
    total = weighted_integrand(0.0, y, order, log_scale) + weighted_integrand(right, y, order, log_scale)
    for index in range(1, intervals):
        weight = 4.0 if index % 2 else 2.0
        total += weight * weighted_integrand(index * step, y, order, log_scale)
    return total * step / 3.0


def sample(y: float) -> dict[str, float]:
    moments = [raw_moment(y, order) for order in range(4)]
    mean = moments[1] / moments[0]
    second = moments[2] / moments[0]
    variance = second - mean * mean
    third_cumulant = moments[3] / moments[0] - 3.0 * mean * second + 2.0 * mean**3
    target_residual = mean - y * variance
    return {
        "y": y,
        "mean": mean,
        "variance": variance,
        "third_cumulant": third_cumulant,
        "target_residual": target_residual,
    }


def main() -> None:
    heights = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
    print(
        json.dumps(
            {
                "arithmetic": "IEEE-754 double; 12000-panel composite Simpson",
                "criterion": "third_cumulant <= 0 is sufficient; target_residual >= 0 is exact",
                "samples": [sample(y) for y in heights],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
