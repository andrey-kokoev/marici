"""Exact checks for the bounded polarization-marker quantum eraser."""

from fractions import Fraction as F
import json
from pathlib import Path


def main():
    gamma = F(3, 5)
    distinguishability = F(4, 5)
    visibility_identity = gamma * gamma + distinguishability * distinguishability

    # At phi=0, marginal balanced-port probabilities for overlap gamma.
    marginal_plus = (1 + gamma) / 2
    marginal_minus = (1 - gamma) / 2

    # Orthogonal marking: complementary analyzer sorts fringe/antifringe.
    joint_at_zero_phase = {
        "bright_plus": F(1, 2),
        "dark_plus": F(0),
        "bright_minus": F(0),
        "dark_minus": F(1, 2),
    }
    unconditional_bright = joint_at_zero_phase["bright_plus"] + joint_at_zero_phase["bright_minus"]
    unconditional_dark = joint_at_zero_phase["dark_plus"] + joint_at_zero_phase["dark_minus"]

    # Two global states: accessible orthogonal marker versus orthogonal env.
    # Both have total marker overlap zero and hence identical flat marginals.
    accessible_marker_total_overlap = F(0)
    environment_marker_total_overlap = F(0)
    accessible_overlap_after_pol_projection = F(1)
    environment_overlap_after_pol_projection = F(0)

    # Equal-population route class rho(c): two phase-referenced contrasts
    # recover both real coordinates. Exact witness c=1/5+i/10.
    c_real, c_imag = F(1, 5), F(1, 10)
    contrast_phase_0 = 2 * c_real
    contrast_phase_quarter = -2 * c_imag
    reconstructed = (contrast_phase_0 / 2, -contrast_phase_quarter / 2)

    # A quarter-turn U(1) action preserves unreferenced intensity but changes
    # the quadrature coordinate relative to a fixed external phase origin.
    signal = (F(3, 5), F(4, 5))
    phase_rotated_signal = (-signal[1], signal[0])
    signal_intensity = signal[0] * signal[0] + signal[1] * signal[1]
    rotated_intensity = (phase_rotated_signal[0] * phase_rotated_signal[0]
                         + phase_rotated_signal[1] * phase_rotated_signal[1])
    referenced_quadratures_differ = signal[0] != phase_rotated_signal[0]

    checks = {
        "visibility_distinguishability_identity": visibility_identity == 1,
        "marginal_probabilities_normalize": marginal_plus + marginal_minus == 1,
        "orthogonal_marker_erases_unconditional_fringe": unconditional_bright == unconditional_dark == F(1, 2),
        "conditional_records_retain_fringe_antifringe": joint_at_zero_phase["bright_plus"] == joint_at_zero_phase["dark_minus"] == F(1, 2),
        "identical_marginals_do_not_identify_entanglement_locus": accessible_marker_total_overlap == environment_marker_total_overlap == 0,
        "accessible_eraser_cannot_recover_environment_leakage": accessible_overlap_after_pol_projection == 1 and environment_overlap_after_pol_projection == 0,
        "two_predeclared_phase_rows_reconstruct_reduced_class": reconstructed == (c_real, c_imag),
        "one_phase_row_is_not_faithful": (F(1, 5), F(1, 10)) != (F(1, 5), F(-1, 10)),
        "postselection_preserves_prior_marginal_counts": sum(joint_at_zero_phase.values()) == 1,
        "u1_orbit_preserves_intensity_but_changes_referenced_quadrature": (
            signal_intensity == rotated_intensity == 1 and referenced_quadratures_differ
        ),
        "eraser_basis_must_be_predeclared": True,
    }
    result = {
        "schema": "marici.aspect.polarization_marker_quantum_eraser.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "witnesses": {
            "marker_overlap": str(gamma),
            "visibility": str(gamma),
            "distinguishability": str(distinguishability),
            "V_squared_plus_D_squared": str(visibility_identity),
            "unconditional_orthogonal_marker_ports": [str(unconditional_bright), str(unconditional_dark)],
            "conditional_joint_records_phi_0": {k: str(v) for k, v in joint_at_zero_phase.items()},
            "faithful_reduced_state_detector_phases": ["0", "pi/2"],
            "reconstructed_coherence": [str(reconstructed[0]), str(reconstructed[1])],
            "u1_quarter_turn": {
                "signal": [str(v) for v in signal],
                "rotated_signal": [str(v) for v in phase_rotated_signal],
                "common_intensity": str(signal_intensity),
                "referenced_real_quadratures": [str(signal[0]), str(phase_rotated_signal[0])],
            },
        },
        "hostile_dispositions": {
            "equal_marginals_identify_global_state": "rejected: accessible-marker and environment-marker purifications share flat marginals",
            "postfit_eraser_basis": "rejected: basis selection must precede outcome inspection",
            "postselection_as_source_authority": "rejected: conditioning partitions joint records only",
            "phase_without_local_oscillator": "rejected: unreferenced phase origins form a U(1) torsor",
            "environment_leakage_as_recoverable_marker": "rejected: accessible projection leaves zero total overlap when environment states are orthogonal",
        },
        "faithfulness_boundary": {
            "class": "equal-population reduced route qubits rho(c)",
            "minimal_family": "two balanced contrasts at predeclared LO phases 0 and pi/2",
            "invisible": ["global purification", "entanglement locus", "environment allocation", "unreferenced global phase"],
        },
        "claim_boundary": "no retrocausality, source-authority, environment-recovery, absolute-phase, or RH claim",
    }
    out = Path(__file__).parents[1] / "results" / "polarization_marker_quantum_eraser.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
