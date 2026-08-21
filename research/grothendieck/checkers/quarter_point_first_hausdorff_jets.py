"""Dependency-free numerical regression of the first completed quarter-point jets."""

import json
import math
from pathlib import Path


gamma0 = 0.5772156649015328606
gamma1 = -0.0728158454836767249
gamma2 = -0.00969036319287231848
zeta3 = 1.2020569031595942854

l0 = 1 + gamma0 / 2 - math.log(2 * math.sqrt(math.pi))
l1 = -1 - 2 * gamma1 - gamma0**2 + math.pi**2 / 8
l2 = 1 + gamma0**3 + 3 * gamma0 * gamma1 + 1.5 * gamma2 - 7 * zeta3 / 8

A0 = l0
A1 = 2 * l0 - l1
A2 = l2 - 3 * l1 + 6 * l0
ordinary_determinant = A0 * A2 - A1**2
upper_diagonal = 4 * A0 - A1

assert A0 > 0
assert A1 > 0
assert A2 > 0
assert ordinary_determinant > 0
assert upper_diagonal > 0

result = {
    "l0": l0,
    "l1": l1,
    "l2": l2,
    "A0": A0,
    "A1": A1,
    "A2": A2,
    "ordinary_order_one_determinant": ordinary_determinant,
    "upper_support_diagonal": upper_diagonal,
    "first_three_moments_positive": True,
    "first_coupled_determinant_positive": True,
    "interval_certified": False,
    "zero_locations_used": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "quarter-point-first-hausdorff-jets.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
