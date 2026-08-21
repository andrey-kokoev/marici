"""Dependency-free numerical regression of the first full Hausdorff localizers."""

import json
import math
from pathlib import Path


gamma0 = 0.5772156649015328606
gamma1 = -0.0728158454836767249
gamma2 = -0.00969036319287231848
gamma3 = 0.0020538344203033459
zeta3 = 1.2020569031595942854

l0 = 1 + gamma0 / 2 - math.log(2 * math.sqrt(math.pi))
l1 = -1 - 2 * gamma1 - gamma0**2 + math.pi**2 / 8
l2 = 1 + gamma0**3 + 3 * gamma0 * gamma1 + 1.5 * gamma2 - 7 * zeta3 / 8
l3 = (
    -1
    - 2 * gamma3 / 3
    - 2 * gamma0 * gamma2
    - 2 * gamma1**2
    - 4 * gamma0**2 * gamma1
    - gamma0**4
    + math.pi**4 / 96
)

A0 = l0
A1 = 2 * l0 - l1
A2 = l2 - 3 * l1 + 6 * l0
A3 = -l3 + 4 * l2 - 10 * l1 + 20 * l0

lower_determinant = A1 * A3 - A2**2
lower_positive_term = A1 * A3
lower_negative_term = A2**2
lower_cancellation_condition = (lower_positive_term + lower_negative_term) / lower_determinant
upper00 = 4 * A0 - A1
upper01 = 4 * A1 - A2
upper11 = 4 * A2 - A3
upper_determinant = upper00 * upper11 - upper01**2

assert A3 > 0
assert lower_determinant > 0
assert upper00 > 0 and upper11 > 0
assert upper_determinant > 0

result = {
    "l3": l3,
    "A3": A3,
    "lower_order_one_determinant": lower_determinant,
    "lower_positive_term": lower_positive_term,
    "lower_negative_term": lower_negative_term,
    "lower_subtraction_condition": lower_cancellation_condition,
    "upper_localizer_00": upper00,
    "upper_localizer_01": upper01,
    "upper_localizer_11": upper11,
    "upper_order_one_determinant": upper_determinant,
    "numerical_regression_passed": True,
    "interval_certified": False,
    "zero_locations_used": False,
    "warning": "Binary-float signs, especially the lower determinant, are not proofs.",
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "quarter-point-first-localizer-determinants.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
