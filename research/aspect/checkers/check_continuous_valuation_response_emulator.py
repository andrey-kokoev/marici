import json

import sympy as sp


ell, z = sp.symbols("ell z")
rho = -sp.sinh(ell * z) / sp.sinh(ell / 2)
rho_half = -sp.sinh(ell * z / 2) / sp.sinh(ell / 4)
richardson = sp.simplify((4 * rho_half - rho) / 3)

series = sp.series(rho, ell, 0, 5).removeO().expand()
richardson_series = sp.series(richardson, ell, 0, 6).removeO().expand()
quadratic_coefficient = sp.simplify(series.coeff(ell, 2))

checks = {
    "reciprocal_oddness": sp.simplify(rho.subs(z, -z) + rho) == 0,
    "positive_endpoint_normalization": sp.simplify(
        rho.subs(z, sp.Rational(1, 2)) + 1
    )
    == 0,
    "negative_endpoint_normalization": sp.simplify(
        rho.subs(z, -sp.Rational(1, 2)) - 1
    )
    == 0,
    "archimedean_limit": sp.limit(rho, ell, 0) == -2 * z,
    "no_linear_error": series.coeff(ell, 1) == 0,
    "quadratic_error_formula": sp.simplify(
        quadratic_coefficient + z * (4 * z**2 - 1) / 12
    )
    == 0,
    "richardson_cancels_quadratic_error": richardson_series.coeff(ell, 2)
    == 0,
    "richardson_retains_limit": sp.limit(richardson, ell, 0) == -2 * z,
}

result = {
    "schema": "marici.aspect.continuous-valuation-response-emulator.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "response": str(rho),
    "series_through_order_four": str(series),
    "richardson_series_through_order_four": str(richardson_series),
    "interpretation": (
        "Finite valuation responses and the archimedean odd response are "
        "samples and the differential limit of one normalized optical family."
    ),
}

print(json.dumps(result, indent=2))
