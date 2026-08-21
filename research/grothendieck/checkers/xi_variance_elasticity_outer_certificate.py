"""Directed outer certificate for (y K''(y))' > 0."""

from __future__ import annotations

from decimal import Decimal
from math import factorial

from theta_inner_interval_certificate import I, scale
from xi_fourth_cumulant_outer_certificate import log_interval


def log_power_integral(s: I, start: int, power: int) -> I:
    log_start = log_interval(start)
    factor = I.point(0)
    for index in range(power + 1):
        coefficient = factorial(power) // factorial(power - index)
        factor = factor + scale(log_start.power(power - index), coefficient) / (
            s - I.point(1)
        ).power(index + 1)
    return ((I.point(1) - s) * log_start).exp() * factor


def elasticity_lower(s: I) -> I:
    y = s - I.point("0.5")
    pole = s / (s - I.point(1)).power(3)
    gamma = I.point(1) / scale(s + I.point(2), 2)
    gamma = gamma - (scale(s, 2) - I.point(1)) * (
        (s + I.point(2)).power(3).reciprocal()
        + I.point(1) / scale((s + I.point(2)).power(2), 4)
    )
    log_two = log_interval(2)
    prime_upper = y * (
        log_two.power(3) * (-s * log_two).exp() + log_power_integral(s, 2, 3)
    )
    return pole + gamma - prime_upper


def main() -> None:
    left = Decimal(8)
    right = Decimal(100)
    cells = 4096
    minimum = None
    worst = None
    evaluated = 0
    for index in range(cells):
        a = left + (right - left) * Decimal(index) / Decimal(cells)
        b = left + (right - left) * Decimal(index + 1) / Decimal(cells)
        stack = [(a, b, 0)]
        while stack:
            x, z, depth = stack.pop()
            enclosure = elasticity_lower(I(x, z))
            evaluated += 1
            if enclosure.lo <= 0:
                assert depth < 20, (x, z, enclosure)
                midpoint = (x + z) / Decimal(2)
                stack.extend([(x, midpoint, depth + 1), (midpoint, z, depth + 1)])
                continue
            if minimum is None or enclosure.lo < minimum:
                minimum = enclosure.lo
                worst = (index, x, z, enclosure)
    print(f"evaluated_enclosures={evaluated}")
    print(f"certified_lower_bound={minimum}")
    print(f"worst_cell={worst}")
    assert minimum is not None and minimum > 0


if __name__ == "__main__":
    main()
