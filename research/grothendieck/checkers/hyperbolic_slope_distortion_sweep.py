"""Random hostile test of the proposed abstract hyperbolic distortion theorem."""

from __future__ import annotations

import json
import math
import random


def main() -> None:
    generator = random.Random(20260820)
    trials = 2_000_000
    minimum = (1.0, None)
    failures = 0
    for _ in range(trials):
        length = 10.0 ** generator.uniform(-3.0, 1.5)
        left_slope = generator.random()
        left_rapidity = math.atanh(left_slope)
        minimum_right = math.tanh(max(0.0, left_rapidity - length))
        right_slope = minimum_right + generator.random() * (left_slope - minimum_right)
        descent_time = left_rapidity - math.atanh(right_slope)
        descent_integral = math.log(
            math.cosh(left_rapidity) / math.cosh(left_rapidity - descent_time)
        )
        secant_minimum = (
            descent_integral + right_slope * (length - descent_time)
        ) / length
        secant_maximum = (
            left_slope * (length - descent_time) + descent_integral
        ) / length
        secant = secant_minimum + generator.random() * (secant_maximum - secant_minimum)
        image_length = secant * length

        tx = math.tanh(length / 2.0)
        th = math.tanh(image_length / 2.0)
        correlation = math.cosh(image_length / 2.0) / math.cosh(length / 2.0)
        margin = (tx - left_slope * th) * (tx - right_slope * th) - (
            1.0 - correlation * correlation
        ) * (
            1.0 / math.cosh(length / 2.0) ** 2
            - left_slope * right_slope / math.cosh(image_length / 2.0) ** 2
        )
        if margin < minimum[0]:
            minimum = (
                margin,
                {
                    "length": length,
                    "image_length": image_length,
                    "left_slope": left_slope,
                    "right_slope": right_slope,
                    "secant": secant,
                },
            )
        if margin < -1e-12:
            failures += 1
            break
    print(
        json.dumps(
            {
                "seed": 20260820,
                "trials": trials,
                "failures_below_1e-12": failures,
                "minimum_margin": minimum[0],
                "minimum_package": minimum[1],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
