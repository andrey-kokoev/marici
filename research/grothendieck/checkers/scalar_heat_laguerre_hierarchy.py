"""Exact rational recurrence audit for the heat-prime Laguerre polynomials."""

from fractions import Fraction as F
import json
from pathlib import Path


def derivative(coefficients):
    return [F(index) * value for index, value in enumerate(coefficients)][1:]


def add(left, right):
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else F(0))
        + (right[index] if index < len(right) else F(0))
        for index in range(size)
    ]


def multiply_y(coefficients):
    return [F(0)] + coefficients


def scale(coefficients, scalar):
    return [scalar * value for value in coefficients]


polynomials = [[F(1)]]
for k in range(4):
    current = polynomials[-1]
    next_polynomial = add(
        add(scale(current, F(2 * k + 1, 2)), scale(multiply_y(current), F(-1))),
        multiply_y(derivative(current)),
    )
    while next_polynomial and next_polynomial[-1] == 0:
        next_polynomial.pop()
    polynomials.append(next_polynomial)

expected = [
    [F(1)],
    [F(1, 2), F(-1)],
    [F(3, 4), F(-3), F(1)],
    [F(15, 8), F(-45, 4), F(15, 2), F(-1)],
    [F(105, 16), F(-105, 2), F(105, 2), F(-14), F(1)],
]
assert polynomials == expected

# P1 changes sign at y=1/2, already proving that a prime atom has no fixed
# complete-monotonicity sign across heat scales.
def evaluate(coefficients, y):
    return sum(value * y**index for index, value in enumerate(coefficients))


assert evaluate(polynomials[1], F(1, 4)) > 0
assert evaluate(polynomials[1], F(3, 4)) < 0

result = {
    "orders_checked": list(range(len(polynomials))),
    "P_coefficients_low_to_high": [[str(value) for value in polynomial] for polynomial in polynomials],
    "recurrence_verified": True,
    "Laguerre_identification": "P_k=k!*L_k^(-1/2)",
    "first_derivative_polynomial_changes_sign": True,
    "order_zero_positivity_is_full_Stieltjes_gate": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "scalar-heat-laguerre-hierarchy.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
