"""WP300: exact dependency-checked disposition of the domain selector route."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def load(number, stem):
    path = RESULTS / f"wp{number}_{stem}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    dependencies = {
        284: load(284, "biased_domain_coarsening_threshold"),
        285: load(285, "graph_domain_coarsening_threshold"),
        286: load(286, "heterogeneous_domain_selector"),
        287: load(287, "robust_calibrated_domain_selector"),
        288: load(288, "correlated_calibration_selector"),
        289: load(289, "covariance_support_selector"),
        290: load(290, "moment_tail_selector_bound"),
        291: load(291, "joint_tail_selector_bound"),
        292: load(292, "boolean_coincidence_selector"),
        293: load(293, "unlabelled_coincidence_quotient"),
        294: load(294, "branch_to_physical16_fiber"),
        295: load(295, "signed_j_physical16_kernel"),
        296: load(296, "first_row_signed_j_kernel"),
        297: load(297, "finite_ckm_phase_fiber"),
        298: load(298, "minimal_faithful_ckm_readout"),
        299: load(299, "faithful_readout_not_selector"),
    }

    checks = {
        "all_dependency_checkers_pass": all(packet["passed"] is True for packet in dependencies.values()),
        "finite_ring_selector_is_conditional": dependencies[284]["classification"].startswith("source-biased local domain dynamics is a conditional"),
        "topology_enters_selector_contract": "topology-dependent" in dependencies[285]["classification"],
        "local_calibrated_margins_are_required": dependencies[287]["robust_selector_condition"].startswith("for every vertex"),
        "covariance_does_not_fix_support": dependencies[289]["safe_packet"]["failure_probability"] != dependencies[289]["unsafe_packet"]["failure_probability"],
        "complete_boolean_tower_closes_declared_risk_packet": "complete finite coincidence tower is faithful" in dependencies[292]["classification"],
        "labels_change_groupoid": "stabilizer groupoid" in dependencies[293]["classification"],
        "branch_to_sign_j_has_hostile_physical16_pair": dependencies[294]["checks"]["binary_branch_readout_collapses_hostile_pair"],
        "signed_j_still_has_cp_even_kernel": dependencies[295]["checks"]["signed_j_readouts_are_exactly_equal"] and dependencies[295]["checks"]["physical16_embeddings_are_distinct"],
        "finite_phase_fiber_is_not_singleton": dependencies[297]["durable_rule"] == "finite fiber is not singleton fiber",
        "compact_physical16_readout_is_faithful_on_declared_chart": dependencies[298]["classification"].startswith("faithful physical readout"),
        "faithful_readout_is_not_selector": dependencies[299]["classification"].endswith("before readout"),
        "branch_to_flavor_source_map_remains_a_gate": "derive the CP-domain branch-to-signed-J map" in dependencies[294]["remaining_physical_instrument_gate"],
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP300",
        "dependency_range": "WP284-WP299",
        "admitted_state_domain": "nondegenerate ordered quark-Yukawa quotient on the declared standard CKM chart; domain models are separate finite graph extensions with explicitly bounded dynamics and calibration support",
        "faithful_quotient_coordinate": "physical16 = six ordered masses, nine CKM moduli, and signed J modulo the full weak-basis group",
        "source_authorized_probe_family": "none newly established for physical16 selection; the domain operation is source-conditional, while invariant CKM coordinates are readouts",
        "contextual_partition": {
            "domain_branch": "favored versus unfavored CP-domain branch, conditional on local robust margins and declared groupoid",
            "sign_j": "positive, negative, and zero-J classes with nonsingleton physical16 fibers",
            "signed_j": "nonsingleton CP-even physical16 fibers",
            "compact_ckm_readout": "generic equality of physical16 on the declared nondegenerate standard chart",
        },
        "pipeline_factorization": [
            "declared domain carrier",
            "source-calibrated local dynamics and uncertainty support",
            "conditional branch selector",
            "missing source-derived branch-to-physical16 map",
            "weak-basis-invariant readout family",
            "physical16 reconstruction",
        ],
        "operation_classification": {
            "domain_coarsening": "conditional branch selector inside its added domain experiment",
            "branch_to_sign_j": "unproved source interface; if granted, an orientation selector only",
            "sign_j_and_signed_j": "partial invariant readouts with exact physical16 kernels",
            "compact_wp298_family": "faithful readout/separator on its chart; neither selector nor rigidifier",
            "texture_role": "unchanged presentation rigidifier evidence only",
            "overall": "no genuine source-generated proper physical16 selector established",
        },
        "first_missing_arrow": "conditional CP-domain branch -> source-derived physical16 image",
        "first_nonfaithful_arrow_if_missing_map_is_granted": "physical16 -> sign(J)",
        "smallest_exact_falsifier": dependencies[294]["smallest_exact_falsifier"],
        "remaining_physical_instrument_gate": "derive a common-frame flavor source whose executable dynamics maps the prepared branch to a proper physical16 image, with calibrated CP-even and CP-odd response and uncertainty support; WP298 can then read out but not authorize that image",
        "nima_report": {
            "admitted_state_domain": "nondegenerate ordered standard-chart physical16 plus separately typed finite domain carriers",
            "faithful_quotient_coordinate": "physical16",
            "source_authorized_probe_family": "no new physical16 selector probes; only conditional domain dynamics and invariant readouts",
            "contextual_partition": "branch classes refine to sign-J and signed-J fibers; WP298 separates physical16 generically",
            "classification": "conditional domain selector, physical16 readout, no source-generated physical16 selector",
            "smallest_exact_falsifier": dependencies[294]["smallest_exact_falsifier"],
            "remaining_physical_instrument_gate": "source-derived branch-to-physical16 interface with CP-even response in one calibrated frame",
        },
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = RESULTS / "wp300_domain_physical16_disposition.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
