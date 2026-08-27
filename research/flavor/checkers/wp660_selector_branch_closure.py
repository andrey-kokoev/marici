"""Exact WP660 closure audit for the source-generated selector branch."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
work = {}
for number, stem in [
    (647, "linear_word_source_authority"),
    (648, "triplet_quintet_stabilizer_obstruction"),
    (649, "two_triplet_faithful_frame"),
    (650, "frame_coefficient_nonselection"),
    (651, "frame_messenger_factorization_kernel"),
    (652, "two_width_threshold_instrument"),
    (653, "two_width_confusion_robustness"),
    (654, "finite_width_template_overlap"),
    (655, "gaussian_convolution_pullback"),
    (656, "sideband_background_calibration"),
    (657, "efficiency_control_calibration"),
    (658, "composed_detector_calibration"),
    (659, "cms_two_port_support_audit"),
]:
    work[number] = json.loads((ROOT / "results" / f"wp{number}_{stem}.json").read_text())

checks = {
    "all_dependency_checkers_pass": all(item["status"] == "PASS" for item in work.values()),
    "original_source_has_no_linear_selector": work[647]["source_authorized_linear_coefficient_dimension"] == 0,
    "one_triplet_quintet_frame_is_not_faithful": "not a faithful oriented frame" in work[648]["classification"],
    "two_triplet_source_constructs_trivial_stabilizer": work[649]["stabilizer"] == "trivial in SO(3)",
    "faithful_frame_response_rank_is_eight": work[649]["exact_hostile_witness_response_rank"] == 8,
    "scalar_control_partition_has_four_dimensional_kernel": "four-dimensional" in work[650]["contextual_partition"],
    "messenger_matching_has_six_complex_kernel": "kernel dimension six complex" in work[651]["contextual_partition"],
    "ideal_two_width_instrument_has_rank_two": work[652]["response_rank"] == 2,
    "ideal_composed_detector_has_four_nonzero_gates": len(work[658]["smallest_exact_falsifiers"]) == 4,
    "no_published_candidate_realizes_instrument": all(work[659]["missing_gates"].values()),
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP660", "status": "PASS", "checks": checks,
    "admitted_state_domain": "local exact nondegenerate CP witness in the quark physical quotient; no ensemble-wide selector claim",
    "faithful_quotient_coordinate": "physical16 as a faithful sixteen-entry embedding of the ten-dimensional quark quotient",
    "source_authorized_probe_family": "two-triplet faithful frame with complex {I,J_n,J_m} coefficients in each quark sector",
    "contextual_partition": "twelve real scalar controls have rank-eight physical tangent image and four-dimensional local kernel",
    "operation_classification": {
        "two_triplet_action": "source-generated faithful presentation rigidifier",
        "word_family": "constrained carrier",
        "messenger_matching": "executable transport with constructor kernel",
        "ideal_detector": "conditional source identifier on two magnitude directions",
        "selector": "absent",
    },
    "selector_verdict": "no existing source-derived operation selects coefficient values or a proper numerical physical16 family",
    "smallest_exact_falsifier": "an equation derived from the admitted source action that fixes a scalar sector coefficient without an added source object",
    "remaining_physical_instrument_gate": "a published common-frame likelihood freeing both widths with two efficiency controls, background sideband, joint covariance, and stable finite-width response",
    "ensemble_gate": "any future coefficient law must survive all 1210 fitted sheets before numerical authority",
}
(ROOT / "results" / "wp660_selector_branch_closure.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
