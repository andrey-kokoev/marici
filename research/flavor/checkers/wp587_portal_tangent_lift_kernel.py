"""Exact WP587 lift kernel from portal couplings to a full generator packet."""

import json
from pathlib import Path

import sympy as sp

a, b = sp.symbols("a b", real=True)

# Columns are exact r and q source settings. Rows are kappa_t^2, kappa_4,
# and one representative omitted generator/width coordinate.
projected_tangent = sp.diag(-1, 1)
lift = sp.Matrix([[-1, 0], [0, 1], [a, b]])
projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
detector_row = sp.Matrix([[0, 1, 1]])
detector_response = sp.simplify(detector_row * lift)

zero_completion = lift.subs({a: 0, b: 0})
cancelling_completion = lift.subs({a: 0, b: -1})

checks = {
    "projected_tangent_has_rank_two": projected_tangent.rank() == 2,
    "every_lift_projects_to_known_tangent": projection * lift == projected_tangent,
    "lift_family_has_two_free_coefficients": {a, b}.issubset(lift.free_symbols),
    "detector_q_response_depends_on_completion": detector_response[0, 1] == 1 + b,
    "zero_completion_has_q_response_one": (detector_row * zero_completion)[0, 1] == 1,
    "cancelling_completion_has_q_response_zero": (
        detector_row * cancelling_completion
    )[0, 1]
    == 0,
    "hostile_completions_have_same_projection": projection * zero_completion
    == projection * cancelling_completion,
}

if not all(checks.values()):
    raise SystemExit(f"WP587 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP587",
    "status": "PASS",
    "checks": checks,
    "known_physical_coupling_projection": "(r,q) -> (kappa_t^2,kappa_4) with tangent diag(-1,1)",
    "lift_family": "[[-1,0],[0,1],[a,b]] for one representative omitted coordinate",
    "contextual_equivalence": "lifts are equivalent under projection to (kappa_t^2,kappa_4) iff they differ only in omitted-coordinate rows",
    "classification": "rank-two source-derived coupling projection with a nonunique full-generator lift; neither selector nor instrument",
    "smallest_exact_falsifier": "for detector row (0,1,1), b=0 gives q response 1 while b=-1 gives q response 0, although both lifts project identically",
    "remaining_gate": "derive every detector-sensitive omitted row or prove the publication-bound detector annihilates the lift kernel",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp587_portal_tangent_lift_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
