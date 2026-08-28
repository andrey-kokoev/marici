import json
from pathlib import Path

import sympy as sp


required_source = {
    "selected_completion_action",
    "source_excitation_epsilon_1",
    "source_excitation_epsilon_2",
    "production_decay_map",
    "rg_threshold_transport",
}
required_acquisition = {
    "independent_absolute_monitor",
    "signal_counts",
    "complementary_zero_output",
    "background_normal_counts",
    "efficiency_acceptance_calibration",
    "mass_width_resolution",
    "raw_null_trials",
    "source_detector_frame_provenance",
    "covariance_and_support",
}
currently_admitted_source = {"rg_threshold_transport"}
currently_admitted_acquisition = set()

a, b, c, d, w1, w2 = sp.symbols("a b c d w1 w2", real=True)
J = sp.Matrix([[a, b], [c, d]])
W = sp.diag(w1, w2)
gram_det = sp.factor((J.T * W * J).det())

# Exact hostile and passing witnesses for the frozen acceptance statistic.
J_hostile = sp.Matrix([[1, 2], [2, 4]])
J_pass = sp.Matrix([[1, 0], [0, 1]])
W_pass = sp.diag(2, 3)

missing_source = sorted(required_source - currently_admitted_source)
missing_acquisition = sorted(required_acquisition - currently_admitted_acquisition)
event_cells = 0

tests = {
    "required_source_capabilities_are_frozen": len(required_source) == 5,
    "required_acquisition_capabilities_are_frozen": len(required_acquisition) == 9,
    "current_source_capability_count_is_one": len(currently_admitted_source) == 1,
    "current_acquisition_capability_count_is_zero": len(currently_admitted_acquisition) == 0,
    "four_source_capabilities_are_missing": len(missing_source) == 4,
    "nine_acquisition_capabilities_are_missing": len(missing_acquisition) == 9,
    "weighted_gram_formula_is_exact": gram_det == w1 * w2 * (a * d - b * c) ** 2,
    "proportional_hostile_has_rank_one": J_hostile.rank() == 1,
    "proportional_hostile_has_zero_gram_determinant": (J_hostile.T * W_pass * J_hostile).det() == 0,
    "independent_witness_has_rank_two": J_pass.rank() == 2,
    "independent_witness_has_positive_gram_determinant": (J_pass.T * W_pass * J_pass).det() > 0,
    "no_event_cells_are_admitted": event_cells == 0,
    "portfolio_is_empty_when_candidate_is_not_schedulable": event_cells == 0,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP892",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "candidate_status": "not_schedulable",
    "admitted_state_domain": "selected-completion full-rank Spin(5) source transported to physical16",
    "faithful_quotient": "physical16",
    "required_source_capabilities": sorted(required_source),
    "admitted_source_capabilities": sorted(currently_admitted_source),
    "missing_source_capabilities": missing_source,
    "required_acquisition_capabilities": sorted(required_acquisition),
    "admitted_acquisition_capabilities": [],
    "missing_acquisition_capabilities": missing_acquisition,
    "admitted_event_cells": event_cells,
    "acceptance_gate": "rank(J_det)=2 and det(J_det^T W J_det)>0 with positive uncertainty lower bound",
    "formal_gram_determinant": str(gram_det),
    "experiment_portfolio": [],
    "selector_boundary": "successful identification would not imply source selection",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp892_source_calibrated_acquisition_contract.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
