"""Centered Taylor-model certificate prototype for compact theta boxes."""

from decimal import Decimal as D
import argparse
import json
import math
from pathlib import Path

from theta_compact_endpoint_decimal_interval import (
    Interval,
    extrapolated_simpson_jets,
    formal_simpson_remainder_bounds,
    formal_tail_bounds,
)


def hull(a, b):
    return Interval(min(a.lo, b.lo), max(a.hi, b.hi))


def symmetric(radius):
    return Interval((-radius).next_minus(), radius.next_plus())


def certified_source_jets(x, steps, jet_count):
    empirical, _ = extrapolated_simpson_jets(
        x=x, steps=steps, jet_count=jet_count
    )
    simpson = formal_simpson_remainder_bounds(
        x=x, steps=steps, jet_count=jet_count
    )
    contour, labels = formal_tail_bounds(x=x, jet_count=jet_count)
    result = []
    for order, value in enumerate(empirical):
        midpoint = (value.lo + value.hi) / 2
        rounding = (value.hi - value.lo) / 2
        radius = rounding + simpson[order] + contour[order] + labels[order]
        result.append(Interval((midpoint - radius).next_minus(),
                               (midpoint + radius).next_plus()))
    return result


class TaylorModel:
    """Interval polynomial in one shared delta plus a uniform remainder."""

    radius = None
    degree = None

    def __init__(self, coefficients, remainder=None):
        values = [value if isinstance(value, Interval) else Interval(value)
                  for value in coefficients]
        self.c = values[: self.degree + 1] + [Interval(0)] * (
            self.degree + 1 - len(values)
        )
        self.rem = remainder or Interval(0)

    @classmethod
    def constant(cls, value):
        return cls([value])

    def polynomial_range(self):
        delta = Interval(-self.radius, self.radius)
        value = self.c[-1]
        for coefficient in reversed(self.c[:-1]):
            value = value * delta + coefficient
        return value

    def range(self):
        return self.polynomial_range() + self.rem

    def __neg__(self):
        return TaylorModel([-v for v in self.c], -self.rem)

    def __add__(self, other):
        other = tm(other)
        return TaylorModel([a + b for a, b in zip(self.c, other.c)],
                           self.rem + other.rem)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-tm(other))

    def __rsub__(self, other):
        return tm(other) - self

    def __mul__(self, other):
        other = tm(other)
        full = [Interval(0) for _ in range(2 * self.degree + 1)]
        for i, left in enumerate(self.c):
            for j, right in enumerate(other.c):
                full[i + j] = full[i + j] + left * right
        kept = full[: self.degree + 1]
        discarded = Interval(0)
        radius_power = self.radius ** (self.degree + 1)
        for power in range(self.degree + 1, len(full)):
            discarded = discarded + full[power] * symmetric(radius_power)
            radius_power *= self.radius
        p_range = self.polynomial_range()
        q_range = other.polynomial_range()
        remainder = (
            discarded
            + p_range * other.rem
            + q_range * self.rem
            + self.rem * other.rem
        )
        return TaylorModel(kept, remainder)

    __rmul__ = __mul__

    def reciprocal(self):
        whole = self.range()
        if whole.lo <= 0 <= whole.hi:
            raise ZeroDivisionError("Taylor-model range contains zero")
        q = [Interval(0) for _ in range(self.degree + 1)]
        q[0] = self.c[0].reciprocal()
        for n in range(1, self.degree + 1):
            convolution = Interval(0)
            for k in range(1, n + 1):
                convolution = convolution + self.c[k] * q[n - k]
            q[n] = -q[0] * convolution
        candidate = TaylorModel(q)
        residual = TaylorModel.constant(1) - self * candidate
        # 1/self - candidate = residual/self.  Keeping this as a uniform
        # remainder is rigorous and preserves all computed polynomial terms.
        correction = residual.range() / whole
        return TaylorModel(q, correction)

    def __truediv__(self, other):
        return self * tm(other).reciprocal()

    def __rtruediv__(self, other):
        return tm(other) / self


def tm(value):
    return value if isinstance(value, TaylorModel) else TaylorModel.constant(value)


def logarithmic_taylor_jets(values):
    normalized = [value / values[0] for value in values]
    logarithmic = [TaylorModel.constant(0)]
    for order in range(1, len(values)):
        correction = TaylorModel.constant(0)
        for index in range(1, order):
            correction = correction + (
                math.comb(order - 1, index - 1)
                * logarithmic[index]
                * normalized[order - index]
            )
        logarithmic.append(normalized[order] - correction)
    return logarithmic[1:]


def evaluate_box(x_lo, x_hi, steps, degree):
    if not (D("0.25") <= x_lo < x_hi <= D(400)):
        raise ValueError("require 0.25 <= x_lo < x_hi <= 400")
    if steps <= 0 or steps % 2:
        raise ValueError("steps must be a positive even integer")
    if degree < 1:
        raise ValueError("degree must be positive")

    center = (x_lo + x_hi) / 2
    radius = (x_hi - x_lo) / 2
    TaylorModel.radius = radius
    TaylorModel.degree = degree
    jet_count = 5 + degree + 2
    center_jets = certified_source_jets(center, steps, jet_count)
    right_jets = certified_source_jets(x_hi, steps, jet_count)

    source_models = []
    for derivative in range(6):
        coefficients = [
            center_jets[derivative + power] / Interval(math.factorial(power))
            for power in range(degree + 1)
        ]
        next_derivative = right_jets[derivative + degree + 1]
        remainder_radius = (
            next_derivative.hi
            * radius ** (degree + 1)
            / D(math.factorial(degree + 1))
        ).next_plus()
        source_models.append(TaylorModel(coefficients, symmetric(remainder_radius)))

    l1, l2, l3, l4, l5 = logarithmic_taylor_jets(source_models)
    delta = TaylorModel([Interval(0), Interval(1)])
    displacement = TaylorModel.constant(center - D("0.25")) + delta
    h1 = l1 + displacement * l2
    h2 = 2 * l2 + displacement * l3
    h3 = 3 * l3 + displacement * l4
    h4 = 4 * l4 + displacement * l5
    numerator = 2 * h1 * h3 - 3 * h2 * h2
    numerator_prime = 2 * h1 * h4 - 4 * h2 * h3
    n_range = numerator.range()
    np_range = numerator_prime.range()
    return {
        "x_box": [str(x_lo), str(x_hi)],
        "center": str(center),
        "radius": str(radius),
        "degree": degree,
        "simpson_steps": steps,
        "source_derivative_count": jet_count,
        "schwarzian_numerator": n_range.encode(),
        "schwarzian_numerator_prime": np_range.encode(),
        "numerator_polynomial_coefficients": [v.encode() for v in numerator.c],
        "numerator_model_remainder": numerator.rem.encode(),
        "box_numerator_strictly_positive": n_range.lo > 0,
        "box_numerator_prime_strictly_negative": np_range.hi < 0,
        "centered_correlated_taylor_model": True,
        "compact_interval_certified": False,
        "rh_proved_or_disproved": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-lo", required=True)
    parser.add_argument("--x-hi", required=True)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--degree", type=int, default=4)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = evaluate_box(D(args.x_lo), D(args.x_hi), args.steps, args.degree)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
