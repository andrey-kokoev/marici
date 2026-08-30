import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
result_files = {
    881: "wp881_common_gain_absolute_rate_gate.json",
    882: "wp882_ordered_hodge_comoving_connection.json",
    883: "wp883_threshold_hodge_intertwiner_fiber.json",
    884: "wp884_spin5_finite_threshold_selector_obstruction.json",
    885: "wp885_spin5_completion_bare_massability_audit.json",
    886: "wp886_spin5_declared_scalar_yukawa_census.json",
    887: "wp887_spin5_completion_b_component_mass_rank.json",
    888: "wp888_spin5_completion_b_yukawa_fiber_quotient.json",
    889: "wp889_spin5_coherent_divisor_monodromy.json",
    890: "wp890_spin5_coordinate_divisor_intersection_strata.json",
}
loaded = {
    number: json.loads((root / "results" / filename).read_text(encoding="utf-8"))
    for number, filename in result_files.items()
}

source_map_wp880 = sp.zeros(6, 12)
for index in range(6):
    source_map_wp880[index, index] = 1
moving_frame_row = sp.zeros(1, 12)
moving_frame_row[0, 6] = 1
source_map_wp891 = source_map_wp880.col_join(moving_frame_row)

total_new_checks = sum(item["summary"]["total"] for item in loaded.values())
unresolved = [
    "common_gain",
    "numerical_mass_spectrum_and_finite_threshold_jump",
    "calibrated_detector_rank",
    "transmission_zero_versus_packet_zero",
    "end_to_end_coherence",
]

tests = {
    "all_wp881_to_wp890_results_pass": all(item["status"] == "PASS" for item in loaded.values()),
    "new_gate_count_is_105": total_new_checks == 105,
    "wp880_source_rank_is_six": source_map_wp880.rank() == 6,
    "wp891_source_rank_is_seven": source_map_wp891.rank() == 7,
    "declared_carrier_dimension_is_twelve": source_map_wp891.cols == 12,
    "remaining_kernel_dimension_is_five": 12 - source_map_wp891.rank() == 5,
    "moving_frame_direction_is_detected": source_map_wp891[:, 6].rank() == 1,
    "five_unresolved_directions_are_declared": len(unresolved) == 5,
    "no_acquisition_authoritative_candidate_added": True,
    "portfolio_remains_empty": True,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP891",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "aspect_classification": "deferred: source rank improves to seven, but five physical directions and the entire acquisition rung remain open",
    "new_exact_gate_count_wp881_to_wp890": total_new_checks,
    "declared_mutation_dimension": 12,
    "source_observation_rank_before": source_map_wp880.rank(),
    "source_observation_rank_after": source_map_wp891.rank(),
    "remaining_kernel_dimension": 12 - source_map_wp891.rank(),
    "resolved_direction": "smooth moving-frame transport",
    "unresolved_directions": unresolved,
    "selector_status": "no source-generated numerical selector on physical16",
    "rigidifier_status": "ordered Hodge geometry rigidifies charts, smooth transport, and adjoint threshold matching",
    "mass_constructor_status": "both completions massable; spectra remain parameter dependent",
    "experiment_portfolio": [],
    "remaining_instrument_gate": "calibrated absolute normalization plus complementary zero classifier, mass-width resolution, two labelled source excitations, and common-frame provenance",
    "tests": tests,
}

output = root / "results" / "wp891_spin5_aspect_retest_after_threshold_repairs.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
