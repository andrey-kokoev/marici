"""Exact algebra audit of the denominator-free four-transform Pick identity."""
import json
from fractions import Fraction as Q
from pathlib import Path


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def inverse(value):
    denominator = value[0] ** 2 + value[1] ** 2
    return value[0] / denominator, -value[1] / denominator


def divide(left, right):
    return multiply(left, inverse(right))


# Hostile rational placeholders for the four real integral transforms. The
# identity is algebraic and therefore independent of how they are evaluated.
a, b = Q(7, 5), Q(3, 8)
P, Q_imag, R, T = Q(11, 7), Q(-2, 9), Q(5, 6), Q(13, 10)
radius_squared = a * a + b * b
alpha = 2 * a - a / (2 * radius_squared)
beta = 2 * b + b / (2 * radius_squared)

B = (P, Q_imag)
B_prime = (R, T)
prefactor = (alpha, beta)
F = multiply(prefactor, divide(B_prime, B))
norm_B_squared = P * P + Q_imag * Q_imag

cleared_direct = norm_B_squared * F[1]
cleared_four_transform = beta * (R * P + T * Q_imag) + alpha * (T * P - R * Q_imag)

assert cleared_direct == cleared_four_transform
assert alpha == 2 * a - a / (2 * radius_squared)
assert beta == 2 * b + b / (2 * radius_squared)
assert norm_B_squared > 0

result = {
    "rational_test_point_z": [str(a), str(b)],
    "four_real_transform_placeholders_P_Q_R_T": [str(value) for value in (P, Q_imag, R, T)],
    "prefactor_real_imag_alpha_beta": [str(alpha), str(beta)],
    "B_norm_squared": str(norm_B_squared),
    "cleared_direct_imaginary_part": str(cleared_direct),
    "four_transform_quadratic": str(cleared_four_transform),
    "exact_identity_verified": cleared_direct == cleared_four_transform,
    "zero_locations_used": False,
    "inequality_for_actual_riemann_theta_source_proved": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-four-transform-pick-reduction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
