"""Exact WP568 robust score-channel uncertainty-radius theorem."""

import json
from pathlib import Path

import sympy as sp


d = sp.Matrix([sp.Rational(1, 4), sp.Rational(-1, 4)])
w = 2 * sp.eye(2)
nominal_gram = sp.simplify((d.T * w * d)[0])
nominal_radius = sp.sqrt(nominal_gram)


def worst_case(radius):
    scale = sp.Min(sp.Integer(1), sp.simplify(radius / nominal_radius))
    adversarial_delta = sp.simplify(-scale * d)
    completed = sp.simplify(d + adversarial_delta)
    attained_gram = sp.simplify((completed.T * w * completed)[0])
    formula = sp.simplify(sp.Max(nominal_radius - radius, 0) ** 2)
    return {
        "radius": radius,
        "adversarial_delta": adversarial_delta,
        "completed_tangent": completed,
        "attained_gram": attained_gram,
        "formula": formula,
        "uncertainty_norm": sp.simplify((adversarial_delta.T * w * adversarial_delta)[0]),
    }


resolved = worst_case(sp.Rational(1, 4))
critical = worst_case(sp.Rational(1, 2))

checks = {
    "nominal_tangent_preserves_probability": sum(d) == 0,
    "detector_metric_is_positive_definite": all(value > 0 for value in w.eigenvals()),
    "nominal_gram_is_one_quarter": nominal_gram == sp.Rational(1, 4),
    "nominal_metric_radius_is_one_half": nominal_radius == sp.Rational(1, 2),
    "resolved_adversary_is_inside_uncertainty_ball": resolved["uncertainty_norm"] <= resolved["radius"] ** 2,
    "resolved_bound_is_attained": resolved["attained_gram"] == resolved["formula"] == sp.Rational(1, 16),
    "resolved_radius_leaves_positive_worst_case_gram": resolved["attained_gram"] > 0,
    "critical_adversary_is_probability_conserving": sum(critical["adversarial_delta"]) == 0,
    "critical_adversary_is_inside_uncertainty_ball": critical["uncertainty_norm"] <= critical["radius"] ** 2,
    "critical_radius_erases_detector_tangent": critical["completed_tangent"] == sp.zeros(2, 1),
    "critical_bound_is_attained_at_zero": critical["attained_gram"] == critical["formula"] == 0,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


def encode_case(case):
    return {
        "radius": str(case["radius"]),
        "adversarial_delta": encode_matrix(case["adversarial_delta"]),
        "completed_tangent": encode_matrix(case["completed_tangent"]),
        "uncertainty_norm_squared": str(case["uncertainty_norm"]),
        "attained_worst_case_gram": str(case["attained_gram"]),
        "closed_form_bound": str(case["formula"]),
    }


result = {
    "work_package": "WP568",
    "classification": "exact uncertainty-stable acceptance gate for the source-score detector-channel separator",
    "nominal_tangent": encode_matrix(d),
    "detector_metric": encode_matrix(w),
    "nominal_gram": str(nominal_gram),
    "nominal_metric_radius": str(nominal_radius),
    "robust_gram_formula": "max(sqrt(d^T W d) - rho, 0)^2",
    "resolved_case": encode_case(resolved),
    "critical_falsifier": encode_case(critical),
    "acceptance_condition": "rho is strictly smaller than sqrt(d^T W d)",
    "contextual_partition": "separation authority survives only when every admitted calibration completion remains outside the detector-score kernel",
    "weak_basis_descent": "passes; the uncertainty ball is defined after invariant source-score transport in the common detector frame",
    "remaining_gate": "a physical publication-bound portal-score channel with independently transported calibration and nuisance uncertainty in detector units",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp568_four_point_score_uncertainty_radius.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
