"""Exact WP578 two-setting conditioning and noise-amplification gate."""

import json
from pathlib import Path

import sympy as sp


epsilon = sp.Rational(1, 10)
delta = sp.Rational(1, 100)
w = sp.Matrix([1, -1, 0])

x_fragile = sp.Matrix([[1, 1], [0, epsilon]])
error = sp.Matrix.hstack(sp.zeros(3, 1), delta * w)
reconstruction_error = sp.simplify(error * x_fragile.inv())

x_orthogonal = sp.eye(2)
orthogonal_reconstruction_error = sp.simplify(error * x_orthogonal.inv())

fragile_error_squared = sp.simplify(sum(value**2 for value in reconstruction_error))
input_error_squared = sp.simplify(sum(value**2 for value in error))
orthogonal_error_squared = sp.simplify(sum(value**2 for value in orthogonal_reconstruction_error))

gram_fragile = sp.simplify(x_fragile.T * x_fragile)
gram_orthogonal = x_orthogonal.T * x_orthogonal

checks = {
    "fragile_design_is_invertible": x_fragile.det() == epsilon,
    "calibration_error_preserves_completed_normalization": sp.ones(1, 3) * error == sp.zeros(1, 2),
    "fragile_reconstruction_has_expected_form": reconstruction_error == sp.Matrix.hstack(
        sp.zeros(3, 1), delta * w / epsilon
    ),
    "fragile_squared_error_amplification_is_one_over_epsilon_squared": sp.simplify(
        fragile_error_squared / input_error_squared
    ) == 1 / epsilon**2,
    "numerical_hostile_amplifies_norm_by_ten": fragile_error_squared == 100 * input_error_squared,
    "orthogonal_design_has_unit_gram": gram_orthogonal == sp.eye(2),
    "orthogonal_design_does_not_amplify_this_error": orthogonal_error_squared == input_error_squared,
    "fragile_design_is_not_orthogonal": gram_fragile != sp.eye(2),
    "orthogonal_design_uses_energy_two": sp.trace(gram_orthogonal) == 2,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP578",
    "classification": "exact identifiability requires nonzero design determinant, while robust calibration requires a positive smallest-singular-value margin",
    "fragile_design": encode_matrix(x_fragile),
    "fragile_design_determinant": str(x_fragile.det()),
    "calibration_error": encode_matrix(error),
    "reconstructed_transport_error": encode_matrix(reconstruction_error),
    "squared_error_amplification": str(sp.simplify(fragile_error_squared / input_error_squared)),
    "orthogonal_design": encode_matrix(x_orthogonal),
    "orthogonal_gram": encode_matrix(gram_orthogonal),
    "smallest_exact_falsifier": "epsilon=1/10 and delta=1/100 give an invertible design but amplify transport-error norm by ten",
    "optimality_contract": "under tr(X^T X)=2 in a frozen Euclidean invariant-source metric, sigma_min(X)<=1 with equality for orthogonal equal-norm settings",
    "remaining_gate": "publish the portal setting metric, feasible design, uncertainty on X and Y, and an uncertainty-stable composed detector singular value",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp578_two_setting_conditioning_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
