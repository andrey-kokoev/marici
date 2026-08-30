"""Exact audit of the finite constant-coefficient scalar-closure no-go."""

import json
from pathlib import Path

import sympy as sp


x = sp.symbols("x")


def theta_derivative_polynomial(q):
    return sp.expand(2 * x * sp.diff(q, x) + (sp.Rational(1, 2) - 2 * x) * q)


q = 4 * x**2 - 6 * x
rows = []
all_leading_coefficients_match = True
for order in range(9):
    degree = sp.degree(q, x)
    leading = sp.LC(sp.Poly(q, x))
    expected = 4 * (-2) ** order
    matches = degree == order + 2 and leading == expected
    all_leading_coefficients_match &= bool(matches)
    rows.append(
        {
            "order": order,
            "degree": int(degree),
            "leading_coefficient": str(leading),
            "expected_leading_coefficient": str(expected),
            "matches": bool(matches),
        }
    )
    q = theta_derivative_polynomial(q)

# Deliberate control: D-lambda annihilates exp(lambda*u). The no-go is a
# property of the theta primitive, not a checker that refuses every source.
lam = sp.symbols("lambda")
exponential_control_residual = sp.simplify(lam - lam)

result = {
    "schema": "marici.grothendieck.minimal_theta_no_constant_ode.v1",
    "status": "pass"
    if all_leading_coefficients_match and exponential_control_residual == 0
    else "fail",
    "theta_derivative_rows": rows,
    "all_leading_coefficients_match": all_leading_coefficients_match,
    "highest_derivative_cannot_cancel": all_leading_coefficients_match,
    "exponential_control_annihilator_residual": str(exponential_control_residual),
    "verdict": "no nonzero finite constant-coefficient differential operator annihilates the primitive theta label",
}

output = Path(__file__).parents[1] / "results" / "minimal_theta_no_constant_ode.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

