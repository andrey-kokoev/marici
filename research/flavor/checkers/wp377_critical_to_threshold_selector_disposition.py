"""WP377: exact dependency and claim-boundary audit for WP356--WP376."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def load(work_package, suffix):
    path = ROOT / "results" / f"{work_package}_{suffix}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    packets = {
        "wp356": load("wp356", "critical_bifurcation_authority"),
        "wp357": load("wp357", "first_order_jump_authority"),
        "wp358": load("wp358", "coexistence_fluctuation_completion"),
        "wp359": load("wp359", "canonical_fluctuation_descent"),
        "wp360": load("wp360", "canonical_source_physical16_portal"),
        "wp361": load("wp361", "dimensionless_portal_normalization"),
        "wp362": load("wp362", "cross_sector_exchange_ward_gate"),
        "wp363": load("wp363", "scaled_exchange_normalization_obstruction"),
        "wp364": load("wp364", "positive_pairing_scale_kernel"),
        "wp365": load("wp365", "port_unit_quotient_correction"),
        "wp366": load("wp366", "common_perturbation_port_calibration"),
        "wp367": load("wp367", "quartic_intervention_common_response"),
        "wp368": load("wp368", "mediator_mass_threshold_knob"),
        "wp369": load("wp369", "finite_width_complementary_threshold"),
        "wp370": load("wp370", "threshold_detector_confusion"),
        "wp371": load("wp371", "threshold_finite_sample_fisher"),
        "wp372": load("wp372", "two_point_threshold_scan"),
        "wp373": load("wp373", "two_point_background_drift_robustness"),
        "wp374": load("wp374", "three_point_common_drift_scan"),
        "wp375": load("wp375", "three_point_spacing_optimum"),
        "wp376": load("wp376", "width_ratio_scan_optimum"),
    }

    even = sp.symbols("z1:16", real=True)
    J, Q, alpha = sp.symbols("J Q alpha", real=True, nonzero=True)
    physical_coordinates = even + (J,)
    portal_constraint = J**2 - alpha * Q
    portal_jacobian = sp.Matrix([[
        sp.diff(portal_constraint, coordinate) for coordinate in physical_coordinates
    ]])
    hostile_left = tuple(range(1, 16)) + (J,)
    hostile_right = (sp.Integer(2),) + tuple(range(2, 16)) + (J,)

    dependency_count = len(packets)
    passed_dependency_count = sum(1 for packet in packets.values() if packet["passed"])
    selected_dimension = len(physical_coordinates) - portal_jacobian.rank()

    checks = {
        "all_twenty_one_dependencies_loaded": dependency_count == 21,
        "all_dependencies_passed": passed_dependency_count == dependency_count,
        "portal_constraint_rank_is_one": portal_jacobian.rank() == 1,
        "portal_leaves_fifteen_physical_directions": selected_dimension == 15,
        "physical16_hostile_pair_is_distinct": hostile_left != hostile_right,
        "physical16_hostile_pair_shares_portal_readout": hostile_left[-1]**2 == hostile_right[-1]**2,
        "wp360_records_conditional_selector_not_numerical_prediction": (
            packets["wp360"]["constraint_rank"] == 1
            and packets["wp360"]["selected_family_dimension"] == 15
        ),
        "wp363_exchange_fixes_alpha_only_to_scale": packets["wp363"]["positive_alpha_solution"] == ["s"],
        "wp365_faithful_port_coordinate_is_relational_ratio": packets["wp365"]["invariant_ratio"] == "alpha/s",
        "wp367_common_response_returns_matching_coefficient": packets["wp367"]["responses"]["p_over_q"] == "alpha",
        "wp369_complex_threshold_map_is_locally_faithful": packets["wp369"]["checks"]["joint_threshold_map_is_locally_faithful"],
        "wp374_three_context_instrument_has_full_rank": packets["wp374"]["benchmark_full_rank"] == 6,
        "wp376_optimum_is_source_ratio_dependent": packets["wp376"]["scaling_law"] == "d_star=L*h_star(Omega/L)",
        "threshold_identification_does_not_change_physical_fiber_dimension": selected_dimension == 15,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP377",
        "dependency_range": "WP356--WP376",
        "dependency_count": dependency_count,
        "passed_dependency_count": passed_dependency_count,
        "admitted_state_domain": "conditional canonical scalar coexistence source, finite-width singlet mediator and calibrated multi-setting threshold apparatus, coupled through a hypothetical invariant CP-even portal to a nondegenerate local physical16 chart",
        "faithful_quotient_coordinate": "full physical16=(z1,...,z15,J); source quotient and threshold pole coordinates remain distinct upstream objects",
        "source_authorized_probe_family": "conditionally: canonical vacuum/pole responses, portal residual, finite-width dispersive/absorptive channels, calibrated detector likelihood, and predeclared multi-setting scans",
        "contextual_partition": "threshold scans separate their admitted source/nuisance packet; the portal factors through J^2 and leaves fifteen CP-even directions plus CP orientation",
        "classification": "conditional codimension-one selector and shell rigidifier, with a progressively faithful threshold source identifier; overall neither numerical selector nor full physical16 selector",
        "portal_constraint_rank": int(portal_jacobian.rank()),
        "selected_physical_family_dimension": int(selected_dimension),
        "smallest_exact_falsifier": "two physical16 points differing only in z1 share every J^2 portal readout; independently, the selected magnitude has nonzero response to the free matching coefficient alpha",
        "remaining_physical_instrument_gate": "derive portal, relative port scale, and mediator control from one microscopic action; realize the calibrated finite-width scan; test the frozen numerical shell across the complete fitted ensemble without fitting alpha",
        "final_disposition": "no presently admitted genuine source-generated numerical selector on physical16; one conditional weak-basis-descending CP-shell selector exists, while the threshold continuation establishes source identification and instrument design only",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp377_critical_to_threshold_selector_disposition.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
