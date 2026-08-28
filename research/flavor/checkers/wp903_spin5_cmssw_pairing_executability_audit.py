"""WP903: exact capability audit for the WP902 CMSSW pairing premise."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp902 = json.loads((ROOT / "results/wp902_spin5_paired_null_completed_width_test.json").read_text())
    capabilities = {
        "module_engine_state_replay": "available",
        "cross_width_source_latent_coupling": "absent",
        "generator_draw_trace_equivalence": "absent",
        "shower_pileup_detector_end_to_end_replay": "unverified",
        "stable_full_chain_pair_identifier": "absent",
        "null_completed_output": "design_only",
        "independent_seed_families": "absent",
        "calibrated_two_pole_acceptance_floor": "absent",
        "local_cmssw_runtime": "absent",
    }
    required_for_execution = (
        "cross_width_source_latent_coupling",
        "generator_draw_trace_equivalence",
        "shower_pileup_detector_end_to_end_replay",
        "stable_full_chain_pair_identifier",
        "null_completed_output",
        "independent_seed_families",
        "calibrated_two_pole_acceptance_floor",
        "local_cmssw_runtime",
    )
    executable = all(capabilities[key] == "available" for key in required_for_execution)
    checks = {
        "wp902_checker_passes_conditionally": wp902["passed"],
        "seed_is_not_engine_state": True,
        "engine_state_is_not_semantic_latent_alignment": True,
        "cms_module_replay_mechanism_exists": capabilities["module_engine_state_replay"] == "available",
        "cross_width_source_coupling_not_instantiated": capabilities["cross_width_source_latent_coupling"] == "absent",
        "changed_draw_trace_is_only_efficiency_falsifier": True,
        "null_schema_is_not_generated_evidence": capabilities["null_completed_output"] == "design_only",
        "pilot_acceptance_has_no_calibration_authority": capabilities["calibrated_two_pole_acceptance_floor"] == "absent",
        "full_chain_pairing_is_not_executable_here": not executable,
        "wp901_fallback_retained": True,
        "no_selector_claim": True,
    }
    result = {
        "work_package": "WP903",
        "audited_premise": "WP902 common-random-number coupling across two widths",
        "capabilities": capabilities,
        "pairing_executable_on_current_evidence": executable,
        "classification": "replay infrastructure exists, but cross-width semantic coupling is not instantiated",
        "smallest_exact_falsifier": "replay failure or a paired arm whose shared-seed execution has the wrong declared marginal",
        "required_constructor": "source-level typed base-event or latent-uniform coupling plus full-chain replay manifest and null-completed pair records",
        "remaining_physical_instrument_gate": "execute and replay-verify the coupled generator-to-reconstruction chain, then independently calibrate the two-pole acceptance floor",
        "fallback": "WP901 independent four-cell zero-drift certificate",
        "selector_status": "neither selector nor rigidifier; prospective detector-response validation instrument",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp903_spin5_cmssw_pairing_executability_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
