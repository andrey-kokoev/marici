"""Exact rational audit of the oriented two-thimble cone expansion."""
import json
from fractions import Fraction as Q
from pathlib import Path


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def multiply(left, right):
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def conjugate(value):
    return (value[0], -value[1])


def real_cone(lambda_value, moment, denominator):
    return multiply(multiply(lambda_value, moment), conjugate(denominator))[0]


lambda_value = (Q(7, 3), Q(-5, 4))
i1, i2 = (Q(2, 5), Q(-3, 7)), (Q(5, 11), Q(4, 9))
j1, j2 = (Q(-2, 13), Q(7, 8)), (Q(3, 10), Q(-5, 6))

direct = real_cone(lambda_value, add(j1, j2), add(i1, i2))
self_11 = real_cone(lambda_value, j1, i1)
self_22 = real_cone(lambda_value, j2, i2)
cross = real_cone(lambda_value, j1, i2) + real_cone(lambda_value, j2, i1)
assert direct == self_11 + self_22 + cross

result = {
    "direct_paired_numerator": str(direct),
    "self_11": str(self_11),
    "self_22": str(self_22),
    "cross_12": str(cross),
    "expansion_exact": True,
    "arithmetic": "fractions.Fraction",
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-oriented-two-thimble-identity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
