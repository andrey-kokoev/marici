"""Exact-rational interval propagation for the first Hausdorff localizers.

This proves robustness conditional on the stated input boxes.  It does not
certify that the analytic constants lie in those boxes.
"""

import json
from fractions import Fraction
from pathlib import Path


Interval = tuple[Fraction, Fraction]


def add(*xs: Interval) -> Interval:
    return sum(x[0] for x in xs), sum(x[1] for x in xs)


def scale(k: int, x: Interval) -> Interval:
    return (k * x[0], k * x[1]) if k >= 0 else (k * x[1], k * x[0])


def multiply(x: Interval, y: Interval) -> Interval:
    values = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(values), max(values)


centers = tuple(
    Fraction(x)
    for x in (
        "0.02309570896612101",
        "0.04615431729580455",
        "-0.00011115823145213533",
        "-0.00007362722126180721",
    )
)
radius = Fraction(1, 10**12)
l0, l1, l2, l3 = ((x - radius, x + radius) for x in centers)

A0 = l0
A1 = add(scale(2, l0), scale(-1, l1))
A2 = add(l2, scale(-3, l1), scale(6, l0))
A3 = add(scale(-1, l3), scale(4, l2), scale(-10, l1), scale(20, l0))

lower = add(multiply(A1, A3), scale(-1, multiply(A2, A2)))
upper00 = add(scale(4, A0), scale(-1, A1))
upper01 = add(scale(4, A1), scale(-1, A2))
upper11 = add(scale(4, A2), scale(-1, A3))
upper = add(multiply(upper00, upper11), scale(-1, multiply(upper01, upper01)))

assert lower[0] > 0
assert upper[0] > 0

result = {
    "input": "independent exact rational boxes l_i=center_i +/- 1e-12",
    "lower_determinant_interval": [float(lower[0]), float(lower[1])],
    "upper_determinant_interval": [float(upper[0]), float(upper[1])],
    "conditional_sign_certificate": True,
    "analytic_input_boxes_certified": False,
    "zero_locations_used": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "quarter-point-localizer-interval-robustness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
