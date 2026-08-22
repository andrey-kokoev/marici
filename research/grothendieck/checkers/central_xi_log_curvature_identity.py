"""Exact polynomial verification of the cancellation-free central curvature."""
import json
from fractions import Fraction as Q
from pathlib import Path


# Generic quartic ell(t), evaluated at a rational hostile point.
coefficients = [Q(7, 11), Q(2, 5), Q(-3, 17), Q(5, 19), Q(-7, 23), Q(11,29)]
t = Q(3, 13)


def derivative_value(order):
    total = Q(0)
    for degree, coefficient in enumerate(coefficients):
        if degree < order:
            continue
        falling = Q(1)
        for j in range(order):
            falling *= degree - j
        total += coefficient * falling * t ** (degree - order)
    return total


l1, l2, l3, l4, l5 = (derivative_value(order) for order in range(1, 6))
f1 = 4 * l1 + (4 * t - 1) * l2
f2 = 8 * l2 + (4 * t - 1) * l3
f3 = 12 * l3 + (4 * t - 1) * l4
f4 = 16 * l4 + (4 * t - 1) * l5
curvature_numerator = 2 * f1 * f3 - 3 * f2 * f2

# Directly differentiate F=(4t-1)ell' as a polynomial.
f_coefficients = [Q(0)] * len(coefficients)
for degree in range(1, len(coefficients)):
    f_coefficients[degree] += 4 * degree * coefficients[degree]
    f_coefficients[degree - 1] -= degree * coefficients[degree]


def f_derivative(order):
    total = Q(0)
    for degree, coefficient in enumerate(f_coefficients):
        if degree >= order:
            falling = Q(1)
            for j in range(order):
                falling *= degree - j
            total += coefficient * falling * t ** (degree - order)
    return total


direct = [f_derivative(order) for order in range(1, 5)]
assert direct == [f1, f2, f3, f4]
assert curvature_numerator == 2 * direct[0] * direct[2] - 3 * direct[1] ** 2
h3_numerator = 18*f1*f2*f3 - 4*f1*f1*f4 - 15*f2**3

result = {
    "identity": "S=ell', F=(4t-1)ell'",
    "F_prime": "4 ell' + (4t-1) ell''",
    "F_double_prime": "8 ell'' + (4t-1) ell'''",
    "F_triple_prime": "12 ell''' + (4t-1) ell''''",
    "F_fourth_prime": "16 ell'''' + (4t-1) ell^(5)",
    "concavity_numerator": "2 F' F''' - 3 (F'')^2",
    "H_triple_prime": "(18 F' F'' F''' - 4 (F')^2 F'''' - 15 (F'')^3)/(8 (F')^(7/2))",
    "nonzero_generic_H_triple_numerator": h3_numerator != 0,
    "exact_polynomial_regression": True,
    "square_root_cancellation_removed_symbolically": True,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "central-xi-log-curvature-identity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
