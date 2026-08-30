"""WP307: exact uncertainty margins for source and detector Jacobians."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def singular_values(matrix):
    return sorted((sp.sqrt(value) for value in (matrix.T * matrix).eigenvals()), key=sp.default_sort_key)


def main():
    nominal_source = sp.zeros(2, 2)
    source_completion = sp.diag(sp.Rational(1, 100), 0)
    nominal_detector = sp.diag(2, 1)
    safe_detector_completion = sp.diag(-sp.Rational(1, 2), -sp.Rational(1, 2))
    boundary_detector_completion = sp.diag(0, -1)
    safe_detector = nominal_detector + safe_detector_completion
    boundary_detector = nominal_detector + boundary_detector_completion

    nominal_detector_singular = singular_values(nominal_detector)
    safe_detector_singular = singular_values(safe_detector)
    boundary_detector_singular = singular_values(boundary_detector)
    uncertainty_radius = sp.Rational(1, 2)
    weyl_lower_bound = nominal_detector_singular[0] - uncertainty_radius

    checks = {
        "nominal_source_rank_is_zero": nominal_source.rank() == 0,
        "arbitrarily_small_admitted_source_completion_breaks_exact_prediction": source_completion.rank() == 1,
        "source_completion_operator_norm_is_one_hundredth": max(singular_values(source_completion)) == sp.Rational(1, 100),
        "nominal_detector_smallest_singular_value_is_one": nominal_detector_singular[0] == 1,
        "half_radius_weyl_margin_is_positive": weyl_lower_bound == sp.Rational(1, 2),
        "explicit_safe_completion_remains_full_rank": safe_detector.rank() == 2 and safe_detector_singular[0] == sp.Rational(1, 2),
        "boundary_completion_at_unit_radius_is_singular": boundary_detector.rank() == 1 and boundary_detector_singular[0] == 0,
        "positive_gram_margin_matches_full_rank": (safe_detector.T * safe_detector).det() > 0 and (boundary_detector.T * boundary_detector).det() == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP307",
        "theorem_domain": "two-coordinate Euclidean source and detector Jacobians with spectral-norm-bounded additive uncertainty",
        "source_gate": {
            "nominal_rank": nominal_source.rank(),
            "hostile_completion_norm": "1/100",
            "hostile_completion_rank": source_completion.rank(),
            "exact_rule": "rank-zero predictivity must hold for every admitted completion; a merely small response authorizes only approximate sensitivity bounds",
        },
        "detector_gate": {
            "nominal_singular_values": [str(value) for value in nominal_detector_singular],
            "uncertainty_radius": str(uncertainty_radius),
            "weyl_lower_bound": str(weyl_lower_bound),
            "boundary_singular_values": [str(value) for value in boundary_detector_singular],
            "robust_rule": "sigma_min(J_det_nominal)>epsilon guarantees full rank for every spectral-norm perturbation of size at most epsilon",
        },
        "classification": "exact source predictivity needs a structural zero over the entire support, while detector faithfulness admits a quantitative positive singular-value margin",
        "smallest_exact_falsifier": "a source response diag(1/100,0) is small but rank one; a detector perturbation diag(0,-1) at the nominal unit margin kills rank",
        "remaining_physical_instrument_gate": "derive an exact symmetry or source theorem forcing J_src=0 on all admitted completions and calibrate a detector sigma_min margin that survives uncertainty and support completion",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp307_robust_dual_jacobian_margins.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
