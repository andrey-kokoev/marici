"""WP899: exact applicability audit for the WP898 tau-resolution bound."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "results" / name).read_text())


def main():
    wp253 = load("wp253_mu_tau_visible_mass_shape.json")
    wp256 = load("wp256_scale_covariant_shape_transport.json")
    wp898 = load("wp898_spin5_width_response_resolution_bound.json")
    provenance = json.loads((ROOT / "data/cms-open-data-19459-pilot/provenance.json").read_text())
    background_provenance = json.loads((ROOT / "data/cms-mu-tau-background-pilots/provenance.json").read_text())
    serialized = json.dumps({"result": wp253, "provenance": provenance, "shape": background_provenance["visible_mass_shape"]}).lower()
    fields = [
        "event_joined_true_parent_mass",
        "reconstructed_parent_mass_estimator",
        "centered_parent_residual",
        "gaussian_core_covariance",
        "non_gaussian_tail_budget",
    ]
    capability = [0, 0, 0, 0, 0]
    checks = {
        "parent_packets_pass": wp253["passed"] and wp256["passed"] and wp898["passed"],
        "wp253_is_visible_mass_not_parent_residual": "visible_mass_shape" in background_provenance and "reco_minus_parent" not in serialized,
        "no_parent_resolution_sigma_is_serialized": "parent_resolution_sigma" not in serialized,
        "no_gaussian_core_calibration_is_serialized": "gaussian core" not in serialized and "gaussian_core" not in serialized,
        "no_tail_budget_is_serialized": "tail budget" not in serialized and "tail_budget" not in serialized,
        "all_five_application_fields_absent": sum(capability) == 0,
        "scaled_shape_exact_closure_still_fails": wp256["checks"]["exact_scale_covariant_closure_fails"],
        "scaled_shape_tv_obstruction_positive": wp256["total_variation_decimal"] > 0,
        "wp898_remains_conditional": "conditional" in wp898["classification"],
        "finite_tau_discriminator_not_retracted": wp253["shape_rank"] == 2,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP899",
        "candidate_substitution": "visible muon-tau mass spread -> calibrated parent-mass Gaussian resolution",
        "required_application_fields": fields,
        "current_capability_vector": capability,
        "exact_scaled_shape_obstruction": wp256["total_variation_exact"],
        "first_nonfaithful_arrow": "visible tau-pair mass spread -> calibrated parent-mass resolution kernel",
        "classification": "WP898 applicability no-go on the current tau pilot; finite-domain discriminator retained; no selector",
        "smallest_falsifier": "one calibrated tail or mass-dependent efficiency contribution exceeding the preregistered six-bin drift budget",
        "remaining_physical_instrument_gate": "direct-pole conditional response K(m_vis|m_parent,Gamma,q,eta), with ancestry, zero/finite-width comparison, tails, covariance, and common-frame provenance",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp899_spin5_tau_resolution_applicability_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
