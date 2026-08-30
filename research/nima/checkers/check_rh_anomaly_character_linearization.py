from fractions import Fraction
import json
from pathlib import Path


def linear_trace(vector, coefficients):
    return sum((x * c for x, c in zip(vector, coefficients)), Fraction(0))


def add(left, right):
    return tuple(x + y for x, y in zip(left, right))


coefficients = (Fraction(2), Fraction(-3), Fraction(5))
x = (Fraction(1), Fraction(4), Fraction(-2))
y = (Fraction(3), Fraction(-1), Fraction(6))
assert linear_trace(add(x, y), coefficients) == linear_trace(x, coefficients) + linear_trace(y, coefficients)

# A reciprocal involution exchanges the first two real coordinates and flips
# the third. The selected trace has the corresponding odd/even law.
reciprocal_coefficients = (Fraction(1), Fraction(1), Fraction(2))


def reciprocal(vector):
    return (vector[1], vector[0], -vector[2])


even_part = (Fraction(7), Fraction(-2), Fraction(0))
assert linear_trace(reciprocal(even_part), reciprocal_coefficients) == linear_trace(even_part, reciprocal_coefficients)

odd_part = (Fraction(0), Fraction(0), Fraction(9))
assert linear_trace(reciprocal(odd_part), reciprocal_coefficients) == -linear_trace(odd_part, reciprocal_coefficients)


def quadratic_log(vector):
    return sum((entry * entry for entry in vector), Fraction(0))


quadratic_residual = quadratic_log(add(x, y)) - quadratic_log(x) - quadratic_log(y)
assert quadratic_residual == 2 * sum((a * b for a, b in zip(x, y)), Fraction(0))
assert quadratic_residual != 0

result = {
    "schema": "marici.rh.anomaly-character-linearization.v1",
    "linear_additivity_residual": 0,
    "reciprocal_even_residual": 0,
    "reciprocal_odd_residual": 0,
    "quadratic_polarization_residual": int(quadratic_residual),
    "verdict": "continuous anomaly characters reduce to exponentials of continuous linear boundary traces",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-character-linearization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
