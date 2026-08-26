"""WP331: exact common-frame instrument contract for the CP-domain source."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta, epsilon, c0, gap, gain = sp.symbols(
        "beta epsilon c0 gap gain", real=True, positive=True
    )
    thermal_ratio = sp.exp(-beta * gap)
    cp_amplitude = gain * c0
    log_odds = 2 * beta * epsilon * c0
    source_parameters = (beta, epsilon, c0)
    readouts = (thermal_ratio, cp_amplitude, log_odds)
    calibrated_response = sp.Matrix([
        [sp.diff(readout, parameter) for parameter in source_parameters]
        for readout in readouts
    ])
    determinant = sp.factor(calibrated_response.det())
    beta_inverse = -sp.log(thermal_ratio) / gap
    c0_inverse = cp_amplitude / gain
    epsilon_inverse = sp.simplify(log_odds / (2 * beta_inverse * c0_inverse))
    extended_parameters = (beta, epsilon, c0, gap, gain)
    uncalibrated_response = sp.Matrix([
        [sp.diff(readout, parameter) for parameter in extended_parameters]
        for readout in readouts
    ])
    gap_kernel = sp.Matrix([beta, -epsilon, 0, -gap, 0])
    gain_kernel = sp.Matrix([0, epsilon, -c0, 0, gain])
    checks = {
        "calibrated_three_channel_response_has_rank_three": calibrated_response.rank() == 3,
        "calibrated_determinant_is_nonzero_on_positive_domain": determinant == 2 * beta * c0 * gap * gain * sp.exp(-beta * gap),
        "inverse_temperature_is_reconstructed": sp.simplify(beta_inverse - beta) == 0,
        "cp_scale_is_reconstructed": sp.simplify(c0_inverse - c0) == 0,
        "bias_is_reconstructed": sp.simplify(epsilon_inverse - epsilon) == 0,
        "floating_calibrations_leave_two_dimensional_kernel": len(uncalibrated_response.nullspace()) == 2,
        "gap_rescaling_is_exact_kernel_direction": sp.simplify(uncalibrated_response * gap_kernel) == sp.zeros(3, 1),
        "gain_rescaling_is_exact_kernel_direction": sp.simplify(uncalibrated_response * gain_kernel) == sp.zeros(3, 1),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP331",
        "admitted_state_domain": "one freeze-out cell carrying a two-level thermometer, a CP-amplitude transducer, and repeated CP-domain outcomes",
        "faithful_quotient_coordinate": "the source triple (beta,epsilon,c0) relative to frozen thermometer gap and amplitude gain",
        "candidate_physical_instrument": {
            "thermal_channel": "population ratio A=exp(-beta*gap)",
            "cp_scale_channel": "co-located amplitude C=gain*c0",
            "domain_channel": "calibrated branch log-odds L=2*beta*epsilon*c0",
        },
        "common_frame_constructor": "all three channels must sample the same freeze-out cell, time window, support, and normalization record",
        "calibrated_response_jacobian": [[str(value) for value in row] for row in calibrated_response.tolist()],
        "calibrated_determinant": str(determinant),
        "inverse_map": {
            "beta": "-log(A)/gap",
            "c0": "C/gain",
            "epsilon": "L*gap*gain/(-2*C*log(A))",
        },
        "uncalibrated_response_rank": uncalibrated_response.rank(),
        "uncalibrated_parameter_count": len(extended_parameters),
        "contextual_partition": "frozen gap and gain yield singleton source fibers; floating calibrations restore a two-dimensional rescaling fiber",
        "classification": "an executable algebraic instrument contract with full calibrated rank; it identifies a prepared source packet but does not select its numerical values",
        "smallest_exact_falsifier": "allowing either thermometer gap or amplitude gain to float introduces an exact rescaling direction; allowing both gives a two-dimensional kernel",
        "remaining_physical_instrument_gate": "supply an actual co-located thermometer transition and CP transducer, independent gap and gain calibrations with uncertainties, freeze-out simultaneity, repeated domain statistics, and nonzero detector contrast",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp331_common_frame_cp_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
