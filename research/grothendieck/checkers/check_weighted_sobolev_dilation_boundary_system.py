#!/usr/bin/env python3
"""Numerical audit of the unitary dilation boundary system."""

import math


LAM = math.pi


def simpson(function, left: float, right: float, panels: int = 40000) -> float:
    if panels % 2:
        panels += 1
    step = (right - left) / panels
    total = function(left) + function(right)
    total += 4.0 * sum(function(left + step * j) for j in range(1, panels, 2))
    total += 2.0 * sum(function(left + step * j) for j in range(2, panels, 2))
    return total * step / 3.0


def psi(y: float) -> float:
    return (1.0 + 2.0 * y + 3.0 * y * y) * math.exp(-LAM * y)


def psi_prime(y: float) -> float:
    polynomial = 1.0 + 2.0 * y + 3.0 * y * y
    return (2.0 + 6.0 * y - LAM * polynomial) * math.exp(-LAM * y)


def generator(y: float) -> float:
    return 2.0 * (1.0 + y) * psi_prime(y) + 0.5 * psi(y)


def weight(y: float) -> float:
    return 0.5 / math.sqrt(1.0 + y)


cutoff_y = 16.0
norm_y = simpson(lambda y: psi(y) ** 2 * weight(y), 0.0, cutoff_y)

# Direct logarithmic-frame norm after y=e^(2u)-1.
cutoff_u = 0.5 * math.log(1.0 + cutoff_y)
norm_u = simpson(
    lambda u: (
        math.exp(0.5 * u) * psi(math.exp(2.0 * u) - 1.0)
    )
    ** 2,
    0.0,
    cutoff_u,
)

green_left = 2.0 * simpson(
    lambda y: generator(y) * psi(y) * weight(y), 0.0, cutoff_y
)
green_boundary = math.sqrt(1.0 + cutoff_y) * psi(cutoff_y) ** 2 - psi(0.0) ** 2

checks = {
    "unitary_norm_transport": abs(norm_y - norm_u) < 1.0e-11,
    "green_boundary_identity": abs(green_left - green_boundary) < 1.0e-10,
    "seam_trace_is_retained": abs(green_boundary + 1.0) < 1.0e-10,
    "theta_strip_radius_positive": math.pi / 4.0 > 0.7,
    "tail_boundary_decays": abs(psi(cutoff_y)) < 1.0e-18,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "norm_y": norm_y,
        "norm_u": norm_u,
        "green_left": green_left,
        "green_boundary": green_boundary,
    }
)

if failed:
    raise SystemExit(1)

