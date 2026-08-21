"""Hostile stationary-point sweep for the reachable hyperbolic cubic."""

from __future__ import annotations

import json
import math
import random


def cubic(t: float, r: float, p: float, q: float) -> float:
    return (
        t * t * (t * t + p * q)
        - t * (p + q) * r
        + (1.0 - 2.0 * t * t - t * t * p * q) * r * r
        + t * (p + q) * r**3
    )


def main() -> None:
    generator = random.Random(20260820)
    trials = 1_000_000
    minimum = (1.0, None)
    stationary_roots = 0
    failures = 0
    negative_stationary_below = 0
    negative_stationary_above = 0
    for _ in range(trials):
        length = 10.0 ** generator.uniform(-3.0, 2.0)
        left_u = generator.random() * 10.0
        right_u = max(0.0, left_u - generator.random() * min(left_u, length))
        p, q = math.tanh(left_u), math.tanh(right_u)
        descent = left_u - right_u
        integral = math.log(math.cosh(left_u) / math.cosh(right_u))
        h_min = integral + q * (length - descent)
        h_max = p * (length - descent) + integral
        r_min, r_max = math.tanh(h_min / 2.0), math.tanh(h_max / 2.0)
        t = math.tanh(length / 2.0)
        linear = t * (p + q)
        quadratic = 1.0 - 2.0 * t * t - t * t * p * q
        candidates = [r_min, r_max]
        if linear > 1e-15:
            discriminant = 4.0 * quadratic * quadratic + 12.0 * linear * linear
            root = (-2.0 * quadratic + math.sqrt(discriminant)) / (6.0 * linear)
            root_value = cubic(t, root, p, q)
            if root_value < -1e-12 and root < r_min:
                negative_stationary_below += 1
            if root_value < -1e-12 and root > r_max:
                negative_stationary_above += 1
            if r_min <= root <= r_max:
                candidates.append(root)
                stationary_roots += 1
        for r in candidates:
            value = cubic(t, r, p, q)
            if value < minimum[0]:
                minimum = (value, (length, left_u, right_u, h_min, h_max, r))
            if value < -1e-12:
                failures += 1
                break
        if failures:
            break
    print(json.dumps({
        "trials": trials,
        "stationary_roots_in_reachable_interval": stationary_roots,
        "negative_stationary_below_reachable_interval": negative_stationary_below,
        "negative_stationary_above_reachable_interval": negative_stationary_above,
        "failures_below_minus_1e_12": failures,
        "minimum": minimum,
    }, indent=2))


if __name__ == "__main__":
    main()
