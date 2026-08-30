"""Exact WP588 detector factorization criterion over the portal lift kernel."""

import json
from pathlib import Path

import sympy as sp

u, v, w, a, b = sp.symbols("u v w a b", real=True)

projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
known_tangent = sp.diag(-1, 1)
lift = sp.Matrix([[-1, 0], [0, 1], [a, b]])
detector = sp.Matrix([[u, v, w]])
kernel_generator = sp.Matrix([0, 0, 1])
factor = sp.Matrix([[u, v]])

response = sp.simplify(detector * lift)
factorized_detector = factor * projection

inclusive = sp.Matrix([[1, 0, 0]])
quartic = sp.Matrix([[0, 1, 0]])
combined = inclusive.col_join(quartic)
hostile = sp.Matrix([[0, 1, 1]])

checks = {
    "detector_on_lift_kernel_is_w": (detector * kernel_generator)[0] == w,
    "factorization_defect_is_only_w": detector - factorized_detector
    == sp.Matrix([[0, 0, w]]),
    "lift_response_depends_on_completion_only_through_w": response
    == sp.Matrix([[-u + a * w, v + b * w]]),
    "inclusive_detector_annihilates_kernel": inclusive * kernel_generator
    == sp.zeros(1, 1),
    "inclusive_source_response_has_rank_one": (inclusive * lift).rank() == 1,
    "quartic_detector_annihilates_kernel": quartic * kernel_generator
    == sp.zeros(1, 1),
    "combined_factorized_response_has_rank_two": (combined * lift).rank() == 2,
    "combined_response_equals_known_tangent": combined * lift == known_tangent,
    "hostile_detector_does_not_annihilate_kernel": hostile * kernel_generator
    == sp.ones(1, 1),
}

if not all(checks.values()):
    raise SystemExit(f"WP588 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP588",
    "status": "PASS",
    "checks": checks,
    "exact_criterion": "detector response is independent of all portal-tangent lifts iff D annihilates ker(P), equivalently D=K*P",
    "projection": "P selects (kappa_t^2,kappa_4) from the full generator packet",
    "inclusive_higgs": "factors through P and has source rank one",
    "minimal_rank_two_completion": "stack calibrated rows (1,0,0) and (0,1,0), giving source response diag(-1,1)",
    "hostile_detector": "row (0,1,1) is sensitive to the omitted coordinate and therefore does not descend through P",
    "classification": "conditional detector-descent and rank acceptance theorem; neither selector nor rigidifier",
    "remaining_gate": "publication-bound evidence that a quartic-sensitive completed record either factors through P or includes a source-derived lift of every nonannihilated coordinate",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp588_detector_lift_kernel_annihilation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
