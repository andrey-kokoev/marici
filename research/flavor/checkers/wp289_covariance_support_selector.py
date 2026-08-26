"""WP289: exact same-moment calibration packets with different selector support."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def moments(packet):
    mean = sum(probability * value for value, probability in packet)
    second = sum(probability * value**2 for value, probability in packet)
    variance = sp.simplify(second - mean**2)
    return sp.simplify(mean), variance


def failure_probability(packet):
    return sp.simplify(sum(probability for value, probability in packet if value <= 0))


def main():
    safe_packet = [(sp.Rational(1), sp.Rational(1, 2)), (sp.Rational(3), sp.Rational(1, 2))]
    unsafe_packet = [
        (sp.Rational(-1), sp.Rational(1, 12)),
        (sp.Rational(2), sp.Rational(2, 3)),
        (sp.Rational(3), sp.Rational(1, 4)),
    ]
    safe_mean, safe_variance = moments(safe_packet)
    unsafe_mean, unsafe_variance = moments(unsafe_packet)
    safe_failure = failure_probability(safe_packet)
    unsafe_failure = failure_probability(unsafe_packet)

    checks = {
        "safe_probabilities_normalize": sum(probability for _, probability in safe_packet) == 1,
        "unsafe_probabilities_normalize": sum(probability for _, probability in unsafe_packet) == 1,
        "means_are_exactly_equal": safe_mean == unsafe_mean == 2,
        "variances_are_exactly_equal": safe_variance == unsafe_variance == 1,
        "safe_support_is_strictly_positive": min(value for value, _ in safe_packet) > 0,
        "unsafe_support_crosses_selector_boundary": min(value for value, _ in unsafe_packet) < 0,
        "safe_selector_failure_probability_is_zero": safe_failure == 0,
        "unsafe_selector_failure_probability_is_one_twelfth": unsafe_failure == sp.Rational(1, 12),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP289",
        "theorem_domain": "discrete calibrated laws for one exact local selector margin m_i=h_i-sum_j J_ij",
        "safe_packet": {
            "law": [[str(value), str(probability)] for value, probability in safe_packet],
            "mean": str(safe_mean),
            "variance": str(safe_variance),
            "failure_probability": str(safe_failure),
        },
        "unsafe_packet": {
            "law": [[str(value), str(probability)] for value, probability in unsafe_packet],
            "mean": str(unsafe_mean),
            "variance": str(unsafe_variance),
            "failure_probability": str(unsafe_failure),
        },
        "contextual_partition": "mean and covariance place the two packets in one equivalence class, but support-sensitive selector readout separates them",
        "classification": "covariance is not a robust selector certificate; exact support or an independently justified tail-risk tolerance is required",
        "smallest_exact_falsifier": "both margin laws have mean 2 and variance 1, but one has zero failure probability and the other fails with probability 1/12",
        "remaining_physical_instrument_gate": "calibrate distributional support or certified tail bounds in the source frame and declare the tolerated selector failure probability before observing flavor readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp289_covariance_support_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
