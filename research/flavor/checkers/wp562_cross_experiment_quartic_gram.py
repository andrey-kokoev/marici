"""Exact WP562 cross-experiment quartic Gram audit."""

import json
from pathlib import Path

import sympy as sp


lambda_s, z, lambda_h = sp.symbols("lambda_s z lambda_H", positive=True, real=True)
sigma_r, sigma_q = sp.symbols("sigma_r sigma_q", positive=True, real=True)
tau = sp.symbols("tau", nonnegative=True, real=True)
a, b = sp.symbols("a b", real=True)

cms_up = sp.Rational(55, 1000)
cms_down = sp.Rational(53, 1000)
cms_sigma = (cms_up + cms_down) / 2

covariance = sp.Matrix(
    [
        [sigma_r**2 + a**2 * tau**2, a * b * tau**2],
        [a * b * tau**2, sigma_q**2 + b**2 * tau**2],
    ]
)
covariance_determinant = sp.factor(covariance.det())

readouts = sp.Matrix([1 - z, lambda_s * z**2 / lambda_h])
source_coordinates = sp.Matrix([lambda_s, z])
jacobian = readouts.jacobian(source_coordinates)
weighted_gram = sp.simplify(jacobian.T * covariance.inv() * jacobian)
gram_determinant = sp.factor(weighted_gram.det())
expected_covariance_determinant = (
    sigma_r**2 * sigma_q**2
    + tau**2 * (sigma_r**2 * b**2 + sigma_q**2 * a**2)
)

checks = {
    "cms_symmetrized_uncertainty_is_exact": cms_sigma == sp.Rational(27, 500),
    "joint_covariance_is_symmetric": covariance == covariance.T,
    "shared_nuisance_determinant_has_no_negative_term": sp.simplify(
        covariance_determinant - expected_covariance_determinant
    ) == 0,
    "joint_response_has_rank_two": jacobian.rank() == 2,
    "joint_jacobian_determinant_is_exact": jacobian.det() == z**2 / lambda_h,
    "weighted_gram_determinant_is_exact": gram_determinant == z**4 / (lambda_h**2 * covariance_determinant),
    "zero_mixing_collapses_the_gram": gram_determinant.subs(z, 0) == 0,
    "zero_shared_theory_limit_remains_positive_form": covariance_determinant.subs(tau, 0) == sigma_r**2 * sigma_q**2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP562",
    "classification": "detector-independent complementary probe and covariance acceptance theorem; ATLAS portal-complete curvature remains uncalibrated",
    "cms_instrument": {
        "record": "CMS HIG-21-018",
        "integrated_luminosity_fb_inverse": 138,
        "inclusive_signal_yield": "1.014 +0.055 -0.053",
        "symmetrized_sigma": str(cms_sigma),
    },
    "source_coordinates": ["lambda_s", "z = sin(theta)^2"],
    "readouts": [str(x) for x in readouts],
    "joint_covariance": [[str(x) for x in row] for row in covariance.tolist()],
    "covariance_determinant": str(covariance_determinant),
    "joint_jacobian": [[str(x) for x in row] for row in jacobian.tolist()],
    "joint_jacobian_determinant": str(jacobian.det()),
    "weighted_gram_determinant": str(gram_determinant),
    "remaining_gate": "portal-complete ATLAS HHH bin interpolation, calibrated sigma_q and shared-theory loading, then smallest-eigenvalue resolution test",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp562_cross_experiment_quartic_gram.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
