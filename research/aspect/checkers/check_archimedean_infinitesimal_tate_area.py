import json

import sympy as sp


s, t, h = sp.symbols("s t h", positive=True)
z0 = sp.pi ** (-s / 2) * sp.gamma(s / 2)
z_t = sp.exp(s * t) * z0
centered = sp.simplify((z_t.subs(t, h) - z_t.subs(t, -h)) / (2 * h))
target = sp.simplify(s * z0)
normalized_error = sp.simplify((centered - target) / target)

checks = {
    "dilation_covariance": sp.simplify(sp.diff(z_t, t).subs(t, 0) - target)
    == 0,
    "evaluation_derivative_is_zero": sp.diff(sp.Integer(1), t) == 0,
    "centered_estimator_formula": centered
    == z0 * sp.sinh(h * s) / h,
    "centered_estimator_limit": sp.simplify(sp.limit(centered, h, 0) - target)
    == 0,
    "quadratic_leading_error": sp.limit(normalized_error / h**2, h, 0)
    == s**2 / 6,
}

result = {
    "schema": "marici.aspect.archimedean-infinitesimal-tate-area.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "predicted_area": str(target),
    "centered_estimator": str(centered),
    "relative_error_leading_coefficient": "s**2/6",
    "interpretation": (
        "After full Tate normalization makes finite minors unit, the real "
        "infinitesimal dilation orbit carries the nontrivial local area."
    ),
}

print(json.dumps(result, indent=2))
