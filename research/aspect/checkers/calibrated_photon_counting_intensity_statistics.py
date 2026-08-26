"""Exact finite photon-counting and intensity-statistics checks."""

from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


def binomial_counts(n, eta):
    return [F(comb(n, k)) * eta ** k * (1 - eta) ** (n - k)
            for k in range(n + 1)]


def convolve(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def moments(probabilities):
    mean = sum(F(k) * p for k, p in enumerate(probabilities))
    second = sum(F(k * k) * p for k, p in enumerate(probabilities))
    return mean, second - mean * mean


def main():
    eta = F(9, 25)
    detected = binomial_counts(2, eta)
    dark = [F(9, 10), F(1, 10)]
    observed = convolve(detected, dark)
    detected_mean, detected_variance = moments(detected)
    observed_mean, observed_variance = moments(observed)

    certain_one = [F(0), F(1), F(0)]
    zero_two_mixture = [F(1, 2), F(0), F(1, 2)]
    mean_one, variance_one = moments(certain_one)
    mean_mix, variance_mix = moments(zero_two_mixture)
    factorial_one = sum(F(k * (k - 1)) * p for k, p in enumerate(certain_one))
    factorial_mix = sum(F(k * (k - 1)) * p for k, p in enumerate(zero_two_mixture))

    field = (F(3, 5), F(4, 5))
    rotated = (-field[1], field[0])
    intensity = field[0] ** 2 + field[1] ** 2
    rotated_intensity = rotated[0] ** 2 + rotated[1] ** 2

    time_record_a = [F(1), F(0)]
    time_record_b = [F(0), F(1)]

    # Threshold response on exact Fock inputs n=1 and n=2.
    threshold_one = (F(0), F(1))
    threshold_two = (F(0), F(1))

    # Effects 0,1,2 plus overflow form a complete partition on labels 0..4.
    finite_labels = list(range(5))
    categorized = ["0" if n == 0 else "1" if n == 1 else "2" if n == 2 else "overflow"
                   for n in finite_labels]

    checks = {
        "two_photon_efficiency_distribution_is_exact": detected == [F(256, 625), F(288, 625), F(81, 625)],
        "lossy_count_probabilities_normalize": sum(detected) == 1,
        "detected_mean_and_variance_match_binomial": detected_mean == F(18, 25) and detected_variance == F(288, 625),
        "independent_dark_count_convolution_normalizes": sum(observed) == 1,
        "dark_counts_add_exact_mean_and_variance": observed_mean == F(41, 50) and observed_variance == F(1377, 2500),
        "threshold_detector_is_not_number_resolving": threshold_one == threshold_two,
        "equal_mean_intensity_does_not_fix_statistics": mean_one == mean_mix == 1 and variance_one == 0 and variance_mix == 1,
        "factorial_correlation_separates_equal_means": factorial_one == 0 and factorial_mix == 1,
        "intensity_is_global_phase_blind": intensity == rotated_intensity == 1 and field != rotated,
        "integrated_counts_erase_arrival_order": sum(time_record_a) == sum(time_record_b) == 1 and time_record_a != time_record_b,
        "overflow_effect_completes_truncated_counter": categorized == ["0", "1", "2", "overflow", "overflow"],
    }
    result = {
        "schema": "marici.aspect.calibrated_photon_counting_intensity.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "calibration": {
            "input_photon_number": 2,
            "intensity_efficiency": str(eta),
            "dark_probability": "1/10",
            "temporal_bins": 2,
        },
        "probabilities": {
            "detected_without_dark": [str(p) for p in detected],
            "observed_with_dark": [str(p) for p in observed],
        },
        "moments": {
            "detected_mean": str(detected_mean),
            "detected_variance": str(detected_variance),
            "observed_mean": str(observed_mean),
            "observed_variance": str(observed_variance),
            "equal_mean_state_variances": [str(variance_one), str(variance_mix)],
            "equal_mean_factorial_second": [str(factorial_one), str(factorial_mix)],
        },
        "faithfulness_boundary": {
            "faithful_on": "diagonal photon-number distributions within declared resolved cutoff",
            "invisible": ["number coherences", "phase without coherent reference", "arrival order after integration", "distribution inside overflow", "lost environment identity"],
        },
        "completion_missing": ["detector instrument", "dead-time state", "afterpulse law", "time-tag response", "spectral mode response", "dark point process", "finite-bin point-process convergence"],
    }
    out = Path(__file__).parents[1] / "results" / "calibrated_photon_counting_intensity_statistics.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
