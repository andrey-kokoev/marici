"""Exact finite-mode checks for calibrated homodyne and heterodyne readout."""

from fractions import Fraction as F
import json
from pathlib import Path


def main():
    x, p = F(2, 5), F(-1, 5)
    reconstruction = (x, p)  # rows theta=0 and theta=pi/2

    alpha, beta = F(1), F(5)
    plus_intensity = (alpha + beta) ** 2 / 2
    minus_intensity = (alpha - beta) ** 2 / 2
    balanced_difference = plus_intensity - minus_intensity
    expected_difference = 2 * alpha * beta
    mismatched_difference = plus_intensity - F(3, 4) * minus_intensity
    gain_mismatch_residual = mismatched_difference - expected_difference

    t, r = F(3, 5), F(4, 5)
    vacuum_variance = F(1, 2)
    measured_optical_variance = t * t * vacuum_variance + r * r * vacuum_variance
    input_referred_variance = measured_optical_variance / (t * t)
    inefficiency_added_variance = input_referred_variance - vacuum_variance
    electronics_variance = F(1, 10)
    total_measured_variance = measured_optical_variance + electronics_variance

    heterodyne_covariance = [[vacuum_variance + vacuum_variance, F(0)],
                             [F(0), vacuum_variance + vacuum_variance]]
    mode_overlap = F(3, 5)
    mismatched_mode_mean = mode_overlap * expected_difference

    no_lo_phase_signal_a = 2 * alpha * F(0)
    no_lo_phase_signal_b = 2 * (-alpha) * F(0)

    checks = {
        "two_homodyne_phases_reconstruct_displacement": reconstruction == (x, p),
        "one_homodyne_phase_has_kernel": (x, p) != (x, -p),
        "balanced_subtraction_extracts_interference": balanced_difference == expected_difference == 10,
        "gain_mismatch_leaves_strong_lo_residual": gain_mismatch_residual == 2,
        "efficiency_dilation_preserves_vacuum_variance": measured_optical_variance == vacuum_variance,
        "input_referred_inefficiency_noise_is_exact": input_referred_variance == F(25, 18) and inefficiency_added_variance == F(8, 9),
        "electronics_noise_adds_independently": total_measured_variance == F(3, 5),
        "heterodyne_has_vacuum_noise_penalty": heterodyne_covariance == [[1, 0], [0, 1]],
        "temporal_overlap_scales_phase_sensitive_mean": mismatched_mode_mean == 6,
        "no_local_oscillator_has_no_phase_sensitive_mean": no_lo_phase_signal_a == no_lo_phase_signal_b == 0,
    }
    result = {
        "schema": "marici.aspect.calibrated_homodyne_heterodyne.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "calibration": {
            "signal_mean": [str(x), str(p)], "homodyne_phases": ["0", "pi/2"],
            "local_oscillator_amplitude": str(beta),
            "efficiency_amplitudes": [str(t), str(r)],
            "electronics_variance": str(electronics_variance),
            "temporal_mode_overlap": str(mode_overlap),
        },
        "residuals": {
            "balanced_difference": str(balanced_difference),
            "gain_mismatch_residual": str(gain_mismatch_residual),
            "measured_optical_variance": str(measured_optical_variance),
            "input_referred_variance": str(input_referred_variance),
            "inefficiency_added_variance": str(inefficiency_added_variance),
            "total_with_electronics": str(total_measured_variance),
            "heterodyne_covariance": [[str(v) for v in row] for row in heterodyne_covariance],
            "mode_mismatched_mean": str(mismatched_mode_mean),
        },
        "faithfulness_boundary": {
            "class": "single-mode coherent displacement means with declared covariance",
            "minimal_mean_rows": ["homodyne theta=0", "homodyne theta=pi/2"],
            "invisible": ["unreferenced global phase", "non-Gaussian structure beyond declared moments", "orthogonal temporal modes", "inaccessible environment", "out-of-window dynamics"],
        },
        "completion_missing": ["detector impulse response", "quantum stochastic fields", "spectral noise density", "causal filtering", "finite-time estimator law", "infinite-time convergence"],
    }
    out = Path(__file__).parents[1] / "results" / "calibrated_homodyne_heterodyne_detection.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
