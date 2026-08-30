"""Exact connected-grade audit of the positive convolution hostile."""

from fractions import Fraction
import json


def connected_coefficient(k):
    return Fraction((-1) ** (k + 1), k) * (Fraction(2) ** k + Fraction(1, 2) ** k)


coefficients = [connected_coefficient(k) for k in range(1, 7)]

# (1+2u)(1+u/2)=1+(5/2)u+u^2.
checks = {
    "normalized_factorization": (
        Fraction(2) + Fraction(1, 2) == Fraction(5, 2)
        and Fraction(2) * Fraction(1, 2) == 1
    ),
    "primitive_grade_is_positive": coefficients[0] == Fraction(5, 2),
    "square_grade_is_negative": coefficients[1] == Fraction(-17, 8),
    "first_sign_failure_is_grade_two": coefficients[0] > 0 and coefficients[1] < 0,
    "connected_signs_alternate_through_six": all(
        ((-1) ** (k + 1)) * coefficients[k - 1] > 0 for k in range(1, 7)
    ),
    "no_connected_coefficient_vanishes": all(value != 0 for value in coefficients),
}

result = {
    "schema": "marici.grothendieck.prime-square-rejects-convolution-hostile.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "normalized_factor": "(1+2u)(1+u/2)",
        "connected_coefficients_k1_to_k6": [str(x) for x in coefficients],
        "first_forbidden_grade": 2,
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
