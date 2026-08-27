from fractions import Fraction
import json
from pathlib import Path


def log_one_plus_coeff(power):
    return Fraction((-1) ** (power + 1), power)


regularized_coefficients = {}
for power in range(1, 9):
    coefficient = log_one_plus_coeff(power)
    if power == 1:
        coefficient -= 1
    if power == 2:
        coefficient += Fraction(1, 2)
    regularized_coefficients[power] = coefficient

assert regularized_coefficients[1] == 0
assert regularized_coefficients[2] == 0
for power in range(3, 9):
    assert regularized_coefficients[power] == Fraction((-1) ** (power + 1), power)


def determinant_diagonal_i_plus(values):
    result = Fraction(1)
    for value in values:
        result *= 1 + value
    return result


zero_samples = [
    [Fraction(-1), Fraction(2), Fraction(3)],
    [Fraction(4), Fraction(-1), Fraction(-2)],
]
nonzero_samples = [
    [Fraction(1), Fraction(2), Fraction(3)],
    [Fraction(-1, 2), Fraction(4), Fraction(-2)],
]

for values in zero_samples:
    assert determinant_diagonal_i_plus(values) == 0

for values in nonzero_samples:
    assert determinant_diagonal_i_plus(values) != 0

result = {
    "regularization_order": 3,
    "formal_coefficients_1_through_8": {
        str(power): str(value)
        for power, value in regularized_coefficients.items()
    },
    "linear_coefficient_cancelled": True,
    "quadratic_coefficient_cancelled": True,
    "connected_tail_begins_at_order": 3,
    "zero_samples": len(zero_samples),
    "nonzero_samples": len(nonzero_samples),
    "regularizing_exponential_is_invertible": True,
    "zero_divisor_preserved": True,
    "orientation_supplied": False,
    "verdict": "det_3 is the correct singular determinant vessel, while its nonvanishing remains the unresolved operator-orientation problem",
}

out = Path(__file__).parents[1] / "results" / "rh-third-order-determinant-vessel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
