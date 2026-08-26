import json
from fractions import Fraction as F


def floor_fraction(t):
    return t.numerator // t.denominator


nonintegral = [F(1, 7), F(9, 5), F(103, 11), F(1000001, 13)]
integer = [F(0), F(1), F(17), F(1000000)]

raw_sums = [floor_fraction(t) + floor_fraction(-t) for t in nonintegral]
centered_sums = [
    (F(floor_fraction(t)) + F(1, 2))
    + (F(floor_fraction(-t)) + F(1, 2))
    for t in nonintegral
]
integer_sums = [floor_fraction(t) + floor_fraction(-t) for t in integer]

result = {
    "schema": "marici.grothendieck.reciprocal_maslov_half_boundary.v1",
    "checks": {
        "reciprocal_raw_grade_sum_is_minus_one_off_crossings": all(v == -1 for v in raw_sums),
        "half_boundary_centered_grade_is_reciprocally_odd": all(v == 0 for v in centered_sums),
        "exact_crossings_have_zero_raw_sum": all(v == 0 for v in integer_sums),
        "cancellation_is_uniform_at_arbitrarily_large_area": raw_sums[-1] == -1,
    },
    "raw_sums": raw_sums,
    "centered_sums": [str(v) for v in centered_sums],
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
