"""Exact-rational derivative-sign and remainder bounds for Euler eta tails."""
import json
import math
from fractions import Fraction
from pathlib import Path

N, transforms, max_order = 10_000, 60, 4

def normalized_rising_coefficients(m):
    q = [Fraction(1)]
    for k in range(1, m + 1):
        new = q + [Fraction(0)]
        for r, value in enumerate(q):
            new[r + 1] += value / k
        q = new
    return q

def derivative_polynomial(m, j, y):
    q = normalized_rising_coefficients(m)
    return sum(
        Fraction(math.comb(j, r)) * y ** (j-r) * (-1) ** r
        * math.factorial(r) * q[r]
        for r in range(j + 1)
    )

sign_table = {}
for m in (transforms, transforms + 1):
    sign_table[str(m)] = [derivative_polynomial(m, j, Fraction(9)) for j in range(5)]
assert all(value > 0 for row in sign_table.values() for value in row)

# On 9 <= log(x) <= 10, positivity of the lower-j polynomials makes each
# P_{m,j} increasing.  The m-th derivative magnitude is therefore at most
# m! P_{m,j}(10) / N^(m+1).  Euler transformation contributes 2^-m.
bounds = []
for j in range(max_order + 1):
    bound = (Fraction(math.factorial(transforms))
             * derivative_polynomial(transforms, j, Fraction(10))
             / (Fraction(2) ** transforms * Fraction(N) ** (transforms + 1)))
    bounds.append(bound)
assert max(bounds) < Fraction(1, 10**100)

result = {
    "tail_start": N,
    "euler_transforms": transforms,
    "maximum_eta_derivative_order": max_order,
    "derivative_signs_exactly_positive_at_log_x_9": True,
    "remainder_upper_bounds_scientific": [f"{float(x):.6e}" for x in bounds],
    "all_remainders_below_1e-100": True,
    "transcendental_prefix_interval_still_required": True,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-euler-tail-bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
