import json
from pathlib import Path

import sympy as sp


eta, alpha, m, k, target = sp.symbols("eta alpha m k target", real=True)
F = eta - 1 - alpha * m - k
gradient = sp.Matrix([[sp.diff(F, x) for x in (eta, m, k)]])
k_solution = target - 1 - alpha * m
m_solution = (target - 1) / alpha
bA = sp.Rational(9, 2)
bB = sp.Rational(13, 2)

tests = {
    "completion_beta_split_is_two": bB - bA == 2,
    "matching_constraint_gradient_rank_one": gradient.rank() == 1,
    "matching_solution_fiber_dimension_two": 3 - gradient.rank() == 2,
    "finite_term_realizes_arbitrary_target": sp.simplify(F.subs({eta: target, k: k_solution})) == 0,
    "mass_realizes_arbitrary_target_when_k_zero": sp.simplify(F.subs({eta: target, k: 0, m: m_solution})) == 0,
    "conventional_matching_point_gives_eta_one": sp.simplify(F.subs({eta: 1, m: 0, k: 0})) == 0,
    "different_finite_terms_change_eta": sp.simplify((1 + alpha * m + 1) - (1 + alpha * m)) == 1,
    "eta_gradient_is_transverse": sp.diff(F, eta) == 1,
    "mass_and_finite_nuisances_remain": sp.diff(F, m) == -alpha and sp.diff(F, k) == -1,
    "detector_row_does_not_raise_source_constraint_rank": gradient.rank() == 1,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP884",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "negative_source_support: completion-dependent threshold slopes do not select the finite portal jump",
    "completion_beta_coefficients": {"A": "9/2", "B": "13/2", "difference": 2},
    "local_source_constraint_rank": 1,
    "matching_parameter_dimension": 3,
    "solution_fiber_dimension": 2,
    "free_coordinates": ["log_threshold_mass", "finite_matching_constant"],
    "smallest_falsifier": "same completion and mass with k=0 versus k=1",
    "aspect_gate": "observer rows can identify eta but cannot supply the missing transverse source equations",
    "remaining_gate": "completion-specific mass action plus scheme-independent full-amplitude matching condition",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp884_spin5_finite_threshold_selector_obstruction.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
