"""Exact completeness audit before executing the WP428 response rank."""

import json
from pathlib import Path


root = Path(__file__).parents[1]
wp428 = json.loads((root / "results" / "wp428_threshold_experiment_preregistration.json").read_text(encoding="utf-8"))
wp130 = json.loads((root / "results" / "wp130_detector_smeared_threshold_rank.json").read_text(encoding="utf-8"))

required_spectral_fields = {
    "pole_locations",
    "pole_widths",
    "pole_residues",
    "contact_spectral_density",
    "control_to_signal_normalization",
}
available_top_level = set(wp428)
missing_spectral_fields = sorted(required_spectral_fields - available_top_level)

wp130_fields = set(wp130)
wp130_missing_frequency_model = sorted(required_spectral_fields - wp130_fields)

outcome_fields = {
    "response_matrix",
    "rank",
    "determinant",
    "singular_values",
    "smallest_singular_value",
}

checks = {
    "wp428_preregistration_itself_passed": wp428["passed"],
    "wp428_froze_three_rivals_and_four_readouts": len(wp428["rivals"]) == 3 and len(wp428["readouts"]) == 4,
    "all_required_spectral_fields_are_missing_from_wp428": set(missing_spectral_fields) == required_spectral_fields,
    "wp130_lacks_the_same_frequency_resolved_fields": set(wp130_missing_frequency_model) == required_spectral_fields,
    "wp130_is_a_three_bin_not_four_port_packet": len(wp130["rivals"]) == 3 and "frequency_offsets_in_Gamma_c" not in wp130,
    "no_rank_outcome_was_manufactured_in_wp428": outcome_fields.isdisjoint(available_top_level),
    "response_rank_is_undefined_until_source_spectra_are_frozen": len(missing_spectral_fields) > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP429",
    "title": "Threshold preregistration completeness audit",
    "classification": "WP428 detector ports are frozen but the rival-to-frequency-spectrum arrow is undefined, so response rank cannot yet be computed",
    "required_spectral_fields": sorted(required_spectral_fields),
    "missing_from_wp428": missing_spectral_fields,
    "missing_from_wp130": wp130_missing_frequency_model,
    "first_missing_arrow": "frozen rival constructor -> frequency-resolved source spectrum",
    "rank_status": "undefined, not rank-deficient",
    "smallest_exact_falsifier": "a frozen dependency locator supplying every required spectral field and its map to all four WP428 readouts",
    "repair_contract": "freeze independently sourced pole locations, widths, residues, contact spectral density, normalization, units, common frame, and uncertainties before convolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp429_threshold_preregistration_completeness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
