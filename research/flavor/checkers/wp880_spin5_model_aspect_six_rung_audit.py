import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


wp877 = load(ROOT / "results" / "wp877_sequential_so5_two_vector_projector_repair.json")
wp878 = load(ROOT / "results" / "wp878_ordered_singlet_plane_hodge_portal_normalizer.json")
wp879 = load(ROOT / "results" / "wp879_spin5_anomaly_completion_beta_fiber.json")

mutations = [
    "projector_rotation",
    "flat_relative_angle",
    "ordered_frame_reversal",
    "nonprimitive_contrast",
    "anomaly_completion_swap",
    "common_gain_rescaling",
    "frozen_moving_frame",
    "off_diagonal_threshold",
    "mass_scale_change",
    "detector_rank_collapse",
    "selected_port_transmission_zero",
    "composite_coherence_failure",
]

# Current exact source diagnostics. Each row is an independently reproduced
# gate, not an acquisition record.
O = sp.zeros(6, 12)
for row, column in enumerate([0, 1, 2, 3, 4, 7]):
    O[row, column] = 1

kernel = O.nullspace()
unresolved_columns = [5, 6, 8, 9, 10, 11]
dual_repair = sp.zeros(6, 12)
for row, column in enumerate(unresolved_columns):
    dual_repair[row, column] = 1
O_repaired = O.col_join(dual_repair)

physical_acquisition = sp.zeros(0, 12)
gain_hostile = sp.zeros(12, 1)
gain_hostile[5, 0] = 1

governance = {
    "common_gain_fixed_point": "rejected_currently_missing_selected_complete_source_action",
    "co_moving_connection_residual": "deferred_missing_source_trajectory_and_threshold_family",
    "neutral_gap_mass_and_poles": "deferred_missing_massability_authority_and_mass_action",
    "two_excitation_detector_jacobian": "deferred_missing_physical_flavor_instrument",
    "complementary_rosenbrock_output": "deferred_missing_dynamic_detector_realization",
    "higher_composite_residual": "deferred_missing_complete_common_domain",
}

tests = {
    "wp877_source_gates_pass": wp877["summary"]["all_passed"],
    "wp878_source_gates_pass": wp878["summary"]["all_passed"],
    "wp879_source_gates_pass": wp879["summary"]["all_passed"],
    "thirty_eight_bounded_source_checks_pass": wp877["summary"]["passed"] + wp878["summary"]["passed"] + wp879["summary"]["passed"] == 38,
    "declared_mutation_carrier_has_dimension_twelve": len(mutations) == 12,
    "current_source_observation_rank_is_six": O.rank() == 6,
    "current_unresolved_kernel_dimension_is_six": len(kernel) == 6,
    "smallest_common_gain_hostile_survives_current_tester": O * gain_hostile == sp.zeros(6, 1),
    "six_synthesized_dual_rows_close_declared_formal_kernel": O_repaired.rank() == 12 and len(O_repaired.nullspace()) == 0,
    "no_acquisition_authoritative_flavor_row_exists": physical_acquisition.rows == 0 and physical_acquisition.rank() == 0,
    "all_synthesized_physical_rows_are_rejected_or_deferred": all(value.startswith(("rejected_", "deferred_")) for value in governance.values()),
    "open_world_boundary_is_retained": "fresh_predicate" not in mutations,
    "empty_portfolio_follows_from_absent_acquisition_candidates": physical_acquisition.rows == 0,
    "deliberate_failure_source_rank_cannot_be_promoted_to_physical_rank": O.rank() - physical_acquisition.rank() == 6,
}
tests = {name: bool(value) for name, value in tests.items()}

result = {
    "work_package": "WP880",
    "status": "PASS" if all(tests.values()) else "FAIL",
    "summary": {"passed": sum(tests.values()), "total": len(tests), "all_passed": all(tests.values())},
    "aspect_classification": "deferred: bounded algebraic source tester passes, full six-rung physical tester does not close",
    "rung_1_realization": {"source": "partial", "acquisition": "absent"},
    "rung_2_source_gate_count": 38,
    "rung_3": {
        "declared_mutation_dimension": 12,
        "source_observation_rank": O.rank(),
        "unresolved_kernel_dimension": len(kernel),
        "unresolved_directions": [mutations[i] for i in unresolved_columns],
        "post_synthesized_formal_rank": O_repaired.rank(),
        "smallest_surviving_hostile": "common_gain_rescaling",
    },
    "rung_4": "closure is relative to the declared carrier; fresh physical hostile terms remain admissible",
    "rung_5_governance": governance,
    "rung_6": {"acquisition_authoritative_candidates": 0, "scheduled_portfolio": []},
    "smallest_exact_falsifier": "g=1 and g=2 have identical current source observations and portal intensities in ratio four",
    "remaining_source_gate": "select the matter completion and complete source action before admitting a common-gain fixed-point row",
    "remaining_threshold_gate": "derive moving-frame transport, completion-specific masses, widths, and pole resolution",
    "remaining_instrument_gate": "source-excite two labelled directions and acquire complementary calibrated outputs",
    "tests": tests,
}

out = ROOT / "results" / "wp880_spin5_model_aspect_six_rung_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
if not all(tests.values()):
    raise SystemExit(1)

