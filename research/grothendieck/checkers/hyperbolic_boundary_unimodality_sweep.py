"""Hostile sweep for unimodality of the upper bang--bang margin."""

from __future__ import annotations

import collections
import math
import random


def boundary_margin(p: float, q: float, holding: float) -> float:
    up, uq = math.atanh(p), math.atanh(q)
    descent = up - uq
    descent_image = 0.5 * math.log((1.0 - q * q) / (1.0 - p * p))
    t = math.tanh((descent + holding) / 2.0)
    r = math.tanh((descent_image + p * holding) / 2.0)
    linear = t * (p + q)
    quadratic = 1.0 - 2.0 * t * t - t * t * p * q
    return t * t * (t * t + p * q) - linear * r + quadratic * r * r + linear * r**3


def boundary_derivative(p: float, q: float, holding: float) -> float:
    up, uq = math.atanh(p), math.atanh(q)
    descent = up - uq
    descent_image = 0.5 * math.log((1.0 - q * q) / (1.0 - p * p))
    t = math.tanh((descent + holding) / 2.0)
    r = math.tanh((descent_image + p * holding) / 2.0)
    slope_sum, slope_product = p + q, p * q
    n_t = (
        4.0 * t**3 + 2.0 * t * slope_product
        - 2.0 * t * (2.0 + slope_product) * r * r
        - slope_sum * r * (1.0 - r * r)
    )
    n_r = (
        -t * slope_sum
        + 2.0 * (1.0 - 2.0 * t * t - t * t * slope_product) * r
        + 3.0 * t * slope_sum * r * r
    )
    return 0.5 * ((1.0 - t * t) * n_t + p * (1.0 - r * r) * n_r)


def main() -> None:
    generator = random.Random(20260820)
    patterns: collections.Counter[tuple[int, ...]] = collections.Counter()
    pairs = 20_000
    for _ in range(pairs):
        p = generator.random()
        q = generator.random() * p
        holdings = [10.0 ** (-5.0 + 7.0 * index / 99.0) for index in range(100)]
        values = [boundary_margin(p, q, holding) for holding in holdings]
        derivatives = [boundary_derivative(p, q, holding) for holding in holdings]
        signs: list[int] = []
        for derivative in derivatives:
            sign = 1 if derivative > 1e-12 else -1 if derivative < -1e-12 else 0
            if sign and (not signs or sign != signs[-1]):
                signs.append(sign)
        patterns[tuple(signs)] += 1
    print(f"pairs={pairs}")
    print(f"derivative_sign_patterns={dict(patterns)}")
    print(f"all_unimodal={patterns == collections.Counter({(1, -1): pairs})}")


if __name__ == "__main__":
    main()
