"""Directed interval-x prototype for compact Schwarzian boxes.

This deliberately hostile checker evaluates the completed theta source with
the spectral coordinate x left as an interval.  It tests whether ordinary
interval propagation retains enough correlation to certify N>0 throughout a
box.  Failure is diagnostic: it requests a Taylor-model refinement, not a
claim that N changes sign.
"""

from decimal import Decimal as D
import argparse
import json
import math
from pathlib import Path

from theta_compact_endpoint_decimal_interval import (
    Interval,
    formal_simpson_remainder_bounds,
    formal_tail_bounds,
    logarithmic_jets,
    phi_bounds,
)


def kernel_derivative_interval(x, u, order, terms=220):
    """Positive power-series enclosure for d_x^order cosh(sqrt(x) u)."""
    k = order
    coefficient = D(math.factorial(k)) / D(math.factorial(2 * k))
    term = Interval(coefficient * (D(1) if k == 0 else u ** (2 * k)))
    total = term
    u_squared = u * u
    for _ in range(terms - 1):
        scalar = (
            x
            * Interval(u_squared)
            * Interval(k + 1)
            / Interval(k + 1 - order)
            / Interval(2 * k + 1)
            / Interval(2 * k + 2)
        )
        term = term * scalar
        total = total + term
        k += 1

    # On the admitted domain x<=400 and u<=2, the ratio after 220 terms is
    # below 0.012.  A factor two on the last positive term encloses the tail.
    total = Interval(total.lo, (total.hi + D(2) * term.hi).next_plus())
    return total


def simpson_box_jets(x, cutoff=D(2), steps=4000):
    width = cutoff / steps
    sums = [Interval(0) for _ in range(6)]
    for index in range(steps + 1):
        u = width * index
        source = phi_bounds(u, u)
        weight = 1 if index in (0, steps) else (4 if index % 2 else 2)
        for order in range(6):
            kernel = kernel_derivative_interval(x, u, order)
            sums[order] = sums[order] + source * kernel * Interval(weight)
    return [value * Interval(width / 3) for value in sums]


def evaluate_box(x_lo, x_hi, steps):
    if not (D("0.25") <= x_lo < x_hi <= D(400)):
        raise ValueError("require 0.25 <= x_lo < x_hi <= 400")
    if steps <= 0 or steps % 2:
        raise ValueError("steps must be a positive even integer")

    x = Interval(x_lo, x_hi)
    midpoint = (x_lo + x_hi) / 2
    displacement = x - Interval(D("0.25"))
    quadrature = simpson_box_jets(x, steps=steps)

    # The u-Peano remainder is monotone in positive x-series coefficients;
    # evaluating its interval-jet majorant on the whole x box retains that
    # dependence.  Tail maxima occur at x_hi.
    simpson_errors = formal_simpson_remainder_bounds(x=x, steps=steps)
    contour_tails, label_tails = formal_tail_bounds(x=x_hi)
    c_jets = []
    for order, value in enumerate(quadrature):
        radius = simpson_errors[order] + contour_tails[order] + label_tails[order]
        c_jets.append(Interval((value.lo - radius).next_minus(),
                                (value.hi + radius).next_plus()))

    l1, l2, l3, l4, l5 = logarithmic_jets(c_jets)
    h1 = l1 + displacement * l2
    h2 = Interval(2) * l2 + displacement * l3
    h3 = Interval(3) * l3 + displacement * l4
    h4 = Interval(4) * l4 + displacement * l5
    numerator = Interval(2) * h1 * h3 - Interval(3) * h2 * h2
    numerator_prime = Interval(2) * h1 * h4 - Interval(4) * h2 * h3

    return {
        "x_box": [str(x_lo), str(x_hi)],
        "x_midpoint": str(midpoint),
        "simpson_steps": steps,
        "C_jets": [value.encode() for value in c_jets],
        "H_jets": [value.encode() for value in (h1, h2, h3, h4)],
        "schwarzian_numerator": numerator.encode(),
        "schwarzian_numerator_prime": numerator_prime.encode(),
        "box_numerator_strictly_positive": numerator.lo > 0,
        "box_numerator_prime_strictly_negative": numerator_prime.hi < 0,
        "direct_interval_x_propagation": True,
        "formal_Simpson_remainder_bounds": [str(v) for v in simpson_errors],
        "formal_contour_tail_bounds": [str(v) for v in contour_tails],
        "formal_label_tail_bounds": [str(v) for v in label_tails],
        "compact_interval_certified": False,
        "rh_proved_or_disproved": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-lo", required=True)
    parser.add_argument("--x-hi", required=True)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = evaluate_box(D(args.x_lo), D(args.x_hi), args.steps)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
