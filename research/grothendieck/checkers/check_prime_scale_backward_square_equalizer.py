"""Dependency-free exact verification of the backward equalizer."""

from fractions import Fraction
import json


# A polynomial in q whose coefficients are linear forms in (F, B1, B2).
ZERO_FORM = (Fraction(0), Fraction(0), Fraction(0))


def form_add(left, right):
    return tuple(left[i] + right[i] for i in range(3))


def form_scale(value, form):
    return tuple(value * entry for entry in form)


def poly_add(left, right):
    size = max(len(left), len(right))
    return [
        form_add(left[i] if i < len(left) else ZERO_FORM, right[i] if i < len(right) else ZERO_FORM)
        for i in range(size)
    ]


def poly_scale(value, polynomial):
    return [form_scale(value, coefficient) for coefficient in polynomial]


def poly_shift(polynomial, amount=1):
    return [ZERO_FORM] * amount + polynomial


F = (Fraction(1), Fraction(0), Fraction(0))
B1 = (Fraction(0), Fraction(1), Fraction(0))
B2 = (Fraction(0), Fraction(0), Fraction(1))

# R=(1-q)F+qB1 and A1=(1+q)B1-qB2.
R = [F, form_add(form_scale(-1, F), B1)]
A1 = [B1, form_add(B1, form_scale(-1, B2))]

one_plus_q_R = poly_add(R, poly_shift(R))
q_A1 = poly_shift(A1)
q2_B2 = poly_shift([B2], 2)
one_minus_q2_F = [F, ZERO_FORM, form_scale(-1, F)]

residual = poly_add(
    poly_add(one_plus_q_R, poly_scale(-1, q_A1)),
    poly_add(poly_scale(-1, q2_B2), poly_scale(-1, one_minus_q2_F)),
)

checks = {
    "primitive_recursion_has_expected_form": R == [F, form_add(form_scale(-1, F), B1)],
    "seam_recursion_has_expected_form": A1 == [B1, form_add(B1, form_scale(-1, B2))],
    "all_parameter_equalizer_identity": all(coefficient == ZERO_FORM for coefficient in residual),
    "zero_state_equalizer_identity": all(
        coefficient[1:] == ZERO_FORM[1:] for coefficient in residual
    ),
    "square_coefficient_is_q_squared": q2_B2 == [ZERO_FORM, ZERO_FORM, B2],
}

result = {
    "schema": "marici.grothendieck.prime-scale-backward-square-equalizer.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "identity": "(1+q)R-qA1-q^2B2=(1-q^2)F",
}

print(json.dumps(result, indent=2, sort_keys=True))
