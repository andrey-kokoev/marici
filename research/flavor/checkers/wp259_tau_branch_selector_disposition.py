"""WP259: exact disposition of the WP252--WP258 muon-tau branch."""

import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "results" / name).read_text())


def main():
    p252 = load("wp252_mu_tau_background_pilots.json")
    p253 = load("wp253_mu_tau_visible_mass_shape.json")
    p254 = load("wp254_mu_tau_signal_grid_shape.json")
    p255 = load("wp255_signal_shape_transport_closure.json")
    p256 = load("wp256_scale_covariant_shape_transport.json")
    p257 = load("wp257_source_mass_reference_descent.json")
    p258 = load("wp258_actual_pole_reference_interface.json")

    # Columns: detector-executable pilot, separates admitted finite columns,
    # descends to physical16, selects a proper physical16 subfamily,
    # complete physical instrument.
    capability = Matrix([
        [1, 1, 0, 0, 0],  # fixed-GeV visible-mass family
        [1, 1, 0, 0, 0],  # source-relative visible-mass family
        [1, 1, 0, 0, 0],  # actual-pole dimuon reference candidate
    ])
    selector_columns = capability[:, 2:5]
    checks = {
        "all_parent_checkers_pass": all(packet.get("passed", False) for packet in (p252, p253, p254, p255, p256, p257, p258)),
        "rate_only_identification_falsified": "falsify" in p252["classification"],
        "finite_shape_separates_signal_background": p253["shape_rank"] == 2,
        "finite_grid_separates_labelled_columns": p254["signal_grid_rank"] == 3,
        "fixed_bin_transport_fails": p255["checks"]["exact_linear_closure_fails"],
        "scaled_transport_still_fails": p256["checks"]["exact_scale_covariant_closure_fails"],
        "scaled_operation_does_not_descend": p257["checks"]["therefore_no_descent_to_physical16"],
        "actual_pole_interface_incomplete": p258["checks"]["interface_is_incomplete"],
        "no_candidate_has_selector_capability": selector_columns == Matrix.zeros(3, 3),
        "deliberate_selector_claim_fails": sum(selector_columns) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP259",
        "admitted_state_domain": "the frozen 2015 CMS muon-tau signal/background pilot family at labelled 130, 140, and 160 GeV, with the 2016 actual-pole dimuon records kept as a separate source domain",
        "faithful_quotient_coordinate": "physical16 = six ordered quark masses, nine CKM moduli, and signed J modulo the full weak-basis group",
        "source_authorized_probe_family": "WP251 same-path muon-tau trigger/offline-object selection followed by WP253 visible-mass bins on the declared CMS source-labelled pilot domain",
        "contextual_partition": "the finite visible-mass probe separates the admitted labelled signal columns and simulated background; rate collapses them, interpolation to actual poles is unauthorized, and physical16 fibers are not refined without an extra source label",
        "capability_columns": ["detector_executable_pilot", "finite_domain_separator", "descends_to_physical16", "proper_physical16_selector", "complete_physical_instrument"],
        "capability_rows": {
            "fixed_GeV_visible_mass": [int(value) for value in capability.row(0)],
            "source_relative_visible_mass": [int(value) for value in capability.row(1)],
            "actual_pole_dimuon_reference": [int(value) for value in capability.row(2)],
        },
        "classification": "finite-domain source-labelled discriminator/readout; neither selector nor texture-presentation rigidifier, and not a complete physical instrument on physical16",
        "first_nonfaithful_arrows": [
            "visible-mass shape -> rate projection",
            "finite labelled mass grid -> actual-pole transport",
            "source-relative normalization -> physical16 after forgetting the mass-reference port",
            "actual-pole dimuon record -> 2015 muon-tau response",
        ],
        "smallest_exact_falsifier": "WP257's fixed physical16 and 65 GeV visible record yields 1/2 or 13/32 solely from the external 130 or 160 GeV label",
        "remaining_physical_instrument_gate": "same-frame actual-pole tau samples or an independently derived reweighting with common topology, era, selection, physical branching normalization, QCD control, weighted completion, and uncertainties",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp259_tau_branch_selector_disposition.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
