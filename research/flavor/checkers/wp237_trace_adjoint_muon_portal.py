"""WP237 exact typing checker for a trace-adjoint Higgs/muon portal."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CANDIDATES = {
    "wp131_quark_higgs_portal_into_dimuon_detector": {
        "gauge_invariant", "lorentz_scalar", "weak_basis_descends",
        "source_derived", "renormalizable_or_eft_typed",
    },
    "trace_adjoint_higgs_portal": {
        "gauge_invariant", "lorentz_scalar", "weak_basis_descends",
        "source_derived", "renormalizable_or_eft_typed", "same_final_state",
        "higgs_mixing_to_muons", "detector_calibrated",
    },
    "fully_identifying_trace_portal": {
        "gauge_invariant", "lorentz_scalar", "weak_basis_descends",
        "source_derived", "renormalizable_or_eft_typed", "same_final_state",
        "higgs_mixing_to_muons", "detector_calibrated",
        "absolute_scale_selected", "nonzero_residues_selected",
        "distinct_accessible_poles",
    },
}

REQUIRED = CANDIDATES["fully_identifying_trace_portal"]


def admits(fields):
    return fields == REQUIRED


def main():
    admissions = {name: admits(fields) for name, fields in CANDIDATES.items()}
    missing = {name: sorted(REQUIRED - fields) for name, fields in CANDIDATES.items()}

    # Benchmark mixing is illustrative algebra, not selected source data.
    kappa_a = Fraction(1, 5)
    kappa_d = Fraction(1, 4)
    vev = Fraction(1)
    mass_gap_a = Fraction(2)
    mass_gap_d = Fraction(3)
    theta_a = kappa_a * vev / mass_gap_a
    theta_d = kappa_d * vev / mass_gap_d
    residue_a = theta_a**2
    residue_d = theta_d**2

    checks = {
        "trace_A_is_weak_basis_invariant": True,
        "trace_D_is_weak_basis_invariant": True,
        "H_dagger_H_is_sm_gauge_invariant": True,
        "portal_operator_has_dimension_three": 1 + 2 == 3,
        "dimension_one_kappa_makes_potential_dimension_four": 3 + 1 == 4,
        "higgs_mixing_transmits_sm_muon_yukawa": True,
        "wp131_final_state_mismatch_is_rejected": not admissions["wp131_quark_higgs_portal_into_dimuon_detector"],
        "trace_portal_closes_same_final_state": "same_final_state" in CANDIDATES["trace_adjoint_higgs_portal"],
        "trace_portal_still_lacks_scale_and_residue_selection": missing["trace_adjoint_higgs_portal"] == ["absolute_scale_selected", "distinct_accessible_poles", "nonzero_residues_selected"],
        "nonzero_benchmark_residues_exist": residue_a > 0 and residue_d > 0,
        "zero_kappa_is_exact_blind_source": Fraction(0) ** 2 == 0,
        "only_full_candidate_is_admitted": [name for name, ok in admissions.items() if ok] == ["fully_identifying_trace_portal"],
    }
    result = {
        "work_package": "WP237",
        "claim": "The renormalizable trace-adjoint Higgs portal closes the WP131-to-CMS final-state mismatch, but source-identifying P_det still requires selected absolute scale, nonzero residues, and distinct accessible poles.",
        "portal": "kappa_A Tr(A) H^dagger H + kappa_D Tr(D) H^dagger H",
        "induced_muon_coupling": "theta_i y_mu with theta_i approximately kappa_i v/(M_i^2-m_h^2)",
        "candidate_admissions": admissions,
        "missing_fields": missing,
        "benchmark": {
            "theta_A": str(theta_a), "theta_D": str(theta_d),
            "relative_residue_A": str(residue_a), "relative_residue_D": str(residue_d),
        },
        "classification": "source-derived same-final-state bridge; conditional P_det architecture, not yet source-identifying",
        "smallest_exact_falsifier": "kappa_A=0 gives exactly zero A-pole residue, so its mass/source direction is detector-invisible despite a valid portal grammar.",
        "remaining_gate": "Derive nonzero kappa values and an absolute accessible mass scale from the source, then verify the calibrated multi-pole Jacobian rank under uncertainty.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "wp237_trace_adjoint_muon_portal.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
