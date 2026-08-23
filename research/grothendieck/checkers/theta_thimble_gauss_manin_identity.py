"""Exact rational audit of the thimble Gauss--Manin cone derivative."""
import json
from fractions import Fraction as Q
from pathlib import Path


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def multiply(left, right):
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def scale(value, scalar):
    return (scalar * value[0], scalar * value[1])


def conjugate(value):
    return (value[0], -value[1])


i_unit = (Q(0), Q(1))
half_i = scale(i_unit, Q(1, 2))
lambda_value = (Q(7, 3), Q(-5, 4))
lambda_prime = (Q(11, 9), Q(2, 7))
i_j = (Q(2, 5), Q(-3, 8))
j_j = (Q(-4, 9), Q(7, 6))
k_j = (Q(5, 12), Q(8, 13))
i_k = (Q(3, 10), Q(2, 11))
j_k = (Q(-7, 15), Q(1, 4))

# Product-rule derivative using I'=iJ/2 and J'=iK/2.
direct = add(
    multiply(lambda_prime, multiply(j_j, conjugate(i_k))),
    add(
        multiply(lambda_value, multiply(multiply(half_i, k_j), conjugate(i_k))),
        multiply(lambda_value, multiply(j_j, conjugate(multiply(half_i, j_k)))),
    ),
)

# Closed formula lambda' J Ibar + i lambda/2 (K Ibar - J Jbar).
difference = add(multiply(k_j, conjugate(i_k)), scale(multiply(j_j, conjugate(j_k)), Q(-1)))
closed = add(
    multiply(lambda_prime, multiply(j_j, conjugate(i_k))),
    multiply(multiply(half_i, lambda_value), difference),
)
assert direct[0] == closed[0]

result = {
    "direct_real_derivative": str(direct[0]),
    "closed_real_derivative": str(closed[0]),
    "ordered_cone_derivative_identity_exact": True,
    "arithmetic": "fractions.Fraction",
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-thimble-gauss-manin-identity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

