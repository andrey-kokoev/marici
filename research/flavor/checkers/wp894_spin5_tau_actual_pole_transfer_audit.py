"""WP894: exact Spin(5)-to-tau actual-pole transfer audit."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "results" / name).read_text())


def main():
    wp256 = load("wp256_scale_covariant_shape_transport.json")
    wp258 = load("wp258_actual_pole_reference_interface.json")
    wp893 = load("wp893_spin5_radial_dimuon_instrument_adapter.json")

    residual = Fraction(wp256["total_variation_exact"])
    first_bin = Fraction(wp256["residual_exact"][0])
    fields = [
        "spin5_pole_reference",
        "physical_branching_semantics",
        "actual_pole_tau_topology",
        "common_detector_era_reconstruction",
        "common_selection_at_poles",
        "qcd_control",
        "weighted_completion",
        "correlated_uncertainty_transport",
    ]
    capability = [1, 1, 0, 0, 0, 0, 0, 0]
    checks = {
        "parent_packets_pass": wp256["passed"] and wp258["passed"] and wp893["summary"]["all_passed"],
        "spin5_dimuon_adapter_is_conditional": "conditional" in wp893["classification"],
        "scale_covariant_tau_closure_fails": residual > 0,
        "smallest_recorded_bin_falsifier_nonzero": first_bin != 0,
        "spin5_repairs_pole_reference": capability[0] == 1,
        "spin5_repairs_branching_semantics": capability[1] == 1,
        "six_detector_transfer_fields_remain_missing": capability[2:].count(0) == 6,
        "actual_pole_tau_adapter_incomplete": sum(capability) < len(capability),
        "no_interpolation_authority_from_rank_preservation": wp256["checks"]["interpolation_authority_withheld"],
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP894",
        "admitted_state_domain": "WP893 frozen two-pole Spin(5) radial source slice plus the separate WP251-WP256 2015 tau pilot grid",
        "candidate_operation": "source-relative transport of the finite tau visible-mass response to the two Spin(5) radial poles",
        "interface_fields": fields,
        "capability_vector": capability,
        "repaired_source_fields": fields[:2],
        "missing_detector_fields": fields[2:],
        "exact_total_variation_obstruction": str(residual),
        "smallest_exact_falsifier": f"first source-relative 140 GeV leave-one-out bin residual {first_bin}",
        "classification": "conditional dimuon identifier plus finite-grid tau discriminator; no admitted Spin(5) actual-pole tau transfer and no selector",
        "remaining_physical_instrument_gate": "same-frame actual-pole tau samples, or a preregistered source-derived detector kernel surviving held-out closure, QCD, weighted completion, and correlated uncertainty",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp894_spin5_tau_actual_pole_transfer_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
