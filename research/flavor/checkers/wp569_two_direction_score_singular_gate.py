"""Exact WP569 two-direction robust smallest-singular-value gate."""

import json
from pathlib import Path

import sympy as sp


d = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
w = sp.eye(3)
gram = sp.simplify(d.T * w * d)
gram_eigenvalues = sorted(gram.eigenvals().keys(), key=lambda value: float(value))
sigma_min_squared = gram_eigenvalues[0]
sigma_min = sp.sqrt(sigma_min_squared)

weak_left = sp.Matrix([1, 0, -1]) / sp.sqrt(2)
weak_right = sp.Matrix([1, 1]) / sp.sqrt(2)
unit_rank_one = sp.simplify(weak_left * weak_right.T)


def operator_norm(matrix):
    eigenvalues = matrix.T.multiply(matrix).eigenvals().keys()
    return sp.sqrt(max(eigenvalues, key=lambda value: float(value)))


def audit_completion(radius):
    perturbation = sp.simplify(-radius * unit_rank_one)
    completed = sp.simplify(d + perturbation)
    completed_gram = sp.simplify(completed.T * w * completed)
    eigenvalues = sorted(completed_gram.eigenvals().keys(), key=lambda value: float(value))
    lower_bound = sp.simplify(sp.Max(sigma_min - radius, 0) ** 2)
    return {
        "radius": radius,
        "perturbation": perturbation,
        "perturbation_operator_norm": sp.simplify(operator_norm(perturbation)),
        "completed": completed,
        "completed_gram": completed_gram,
        "completed_gram_eigenvalues": eigenvalues,
        "smallest_completed_gram_eigenvalue": eigenvalues[0],
        "lower_bound": lower_bound,
        "rank": completed.rank(),
        "column_norms_squared": [
            sp.simplify((completed[:, index].T * completed[:, index])[0])
            for index in range(completed.cols)
        ],
    }


resolved = audit_completion(sp.Rational(1, 2))
critical = audit_completion(sp.Integer(1))

checks = {
    "source_response_columns_preserve_probability": all(sum(d[:, index]) == 0 for index in range(d.cols)),
    "nominal_response_has_rank_two": d.rank() == 2,
    "nominal_gram_eigenvalues_are_one_and_three": gram_eigenvalues == [1, 3],
    "nominal_smallest_singular_value_is_one": sigma_min == 1,
    "weak_rank_one_direction_has_unit_operator_norm": operator_norm(unit_rank_one) == 1,
    "resolved_perturbation_preserves_probability": all(sum(resolved["perturbation"][:, index]) == 0 for index in range(d.cols)),
    "resolved_bound_is_sharp_and_positive": resolved["smallest_completed_gram_eigenvalue"] == resolved["lower_bound"] == sp.Rational(1, 4),
    "resolved_completion_retains_rank_two": resolved["rank"] == 2,
    "critical_perturbation_has_unit_radius": critical["perturbation_operator_norm"] == 1,
    "critical_completion_preserves_probability": all(sum(critical["completed"][:, index]) == 0 for index in range(d.cols)),
    "critical_completion_keeps_each_column_visible": all(value > 0 for value in critical["column_norms_squared"]),
    "critical_completion_erases_joint_rank": critical["rank"] == 1,
    "critical_smallest_gram_eigenvalue_is_zero": critical["smallest_completed_gram_eigenvalue"] == critical["lower_bound"] == 0,
    "critical_gram_determinant_vanishes": sp.det(critical["completed_gram"]) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


def encode_case(case):
    return {
        "radius": str(case["radius"]),
        "perturbation": encode_matrix(case["perturbation"]),
        "perturbation_operator_norm": str(case["perturbation_operator_norm"]),
        "completed_response": encode_matrix(case["completed"]),
        "completed_gram": encode_matrix(case["completed_gram"]),
        "completed_gram_eigenvalues": [str(value) for value in case["completed_gram_eigenvalues"]],
        "smallest_completed_gram_eigenvalue": str(case["smallest_completed_gram_eigenvalue"]),
        "certified_lower_bound": str(case["lower_bound"]),
        "rank": case["rank"],
        "column_norms_squared": [str(value) for value in case["column_norms_squared"]],
    }


result = {
    "work_package": "WP569",
    "classification": "robust rank-two separator gate from the smallest singular value, prospective or surrogate-only until physically instantiated",
    "nominal_response": encode_matrix(d),
    "detector_metric": encode_matrix(w),
    "nominal_gram": encode_matrix(gram),
    "nominal_gram_eigenvalues": [str(value) for value in gram_eigenvalues],
    "nominal_smallest_singular_value": str(sigma_min),
    "robust_lower_bound": "max(sigma_min(W^(1/2) D) - rho, 0)^2",
    "resolved_case": encode_case(resolved),
    "critical_falsifier": encode_case(critical),
    "contextual_partition": "joint separation survives only if the entire admitted response uncertainty set avoids rank loss",
    "weak_basis_descent": "passes for invariant physical16 source paths and probability-conserving detector tangents",
    "remaining_gate": "an executed publication-bound two-error portal experiment with calibrated D, independently fixed W, covariance, nuisances, and resolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp569_two_direction_score_singular_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
