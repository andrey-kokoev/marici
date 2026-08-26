"""WP290: exact Cantelli tail certificate for a probabilistic selector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def moments(packet):
    mean = sp.simplify(sum(value * probability for value, probability in packet))
    variance = sp.simplify(sum((value - mean) ** 2 * probability for value, probability in packet))
    return mean, variance


def main():
    mean, sigma = sp.symbols("mean sigma", positive=True)
    cantelli_bound = sp.simplify(sigma**2 / (sigma**2 + mean**2))
    target = sp.Rational(1, 100)

    sharp_packet = [(sp.Rational(0), sp.Rational(1, 5)), (sp.Rational(5, 2), sp.Rational(4, 5))]
    sharp_mean, sharp_variance = moments(sharp_packet)
    sharp_failure = sum(probability for value, probability in sharp_packet if value <= 0)
    example_bound = cantelli_bound.subs({mean: sharp_mean, sigma: sp.sqrt(sharp_variance)})

    ratio = sp.symbols("ratio", nonnegative=True)
    ratio_solution = sp.solve_univariate_inequality(1 / (1 + ratio**2) <= target, ratio)
    checks = {
        "sharp_packet_normalizes": sum(probability for _, probability in sharp_packet) == 1,
        "sharp_packet_has_mean_two": sharp_mean == 2,
        "sharp_packet_has_variance_one": sharp_variance == 1,
        "cantelli_bound_at_mean_two_variance_one_is_one_fifth": example_bound == sp.Rational(1, 5),
        "sharp_packet_attains_cantelli_bound": sharp_failure == example_bound,
        "one_percent_solver_returns_three_sqrt_eleven": ratio_solution.equals(ratio >= 3 * sp.sqrt(11)),
        "three_sqrt_eleven_equals_sqrt_99": sp.simplify(3 * sp.sqrt(11) - sp.sqrt(99)) == 0,
        "strict_support_is_not_obtained_from_finite_ratio": cantelli_bound > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP290",
        "theorem_domain": "all real selector-margin laws with calibrated positive mean mu and finite nonzero variance sigma^2",
        "cantelli_certificate": "P(m<=0) <= sigma^2/(sigma^2+mu^2)",
        "mean_two_variance_one": {
            "upper_failure_bound": str(example_bound),
            "sharp_law": [[str(value), str(probability)] for value, probability in sharp_packet],
            "sharp_failure_probability": str(sharp_failure),
        },
        "one_percent_gate": {
            "maximum_failure_probability": str(target),
            "required_signal_to_uncertainty_ratio": "mu/sigma >= sqrt(99)",
            "required_squared_ratio": "mu^2/sigma^2 >= 99",
        },
        "classification": "mean and variance authorize only a sharp probabilistic selector certificate; they never certify strict positive support at finite signal-to-uncertainty ratio",
        "smallest_exact_falsifier": "the law P(m=0)=1/5 and P(m=5/2)=4/5 has mean 2 and variance 1 and exactly saturates the 1/5 failure bound",
        "remaining_physical_instrument_gate": "calibrate mean and variance of the actual local margin in one source frame, predeclare tolerated failure, justify finite-moment and sampling assumptions, and validate dynamics plus the physical16 map",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp290_moment_tail_selector_bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
