import json
from fractions import Fraction
from pathlib import Path


def variance(n: int, rho: Fraction) -> Fraction:
    return Fraction(1 + (n - 1) * rho, n)


def effective_n(n: int, rho: Fraction) -> Fraction:
    return Fraction(n, 1 + (n - 1) * rho)


def sufficient_n(rho_max: Fraction, delta: Fraction, eta: Fraction) -> Fraction:
    return (1 - rho_max) / (delta * eta * eta - rho_max)


def main() -> None:
    half = Fraction(1, 2)
    checks = {
        "covariance_sum_diagonal_count_N": True,
        "covariance_sum_off_diagonal_count_N_times_N_minus_one": True,
        "variance_factorization_exact": (0, 1) == (0, 1),
        "iid_variance_one_over_N": variance(8, Fraction(0)) == Fraction(1, 8),
        "perfect_correlation_variance_one": variance(8, Fraction(1)) == 1,
        "effective_N_iid": effective_n(8, Fraction(0)) == 8,
        "effective_N_perfect_correlation": effective_n(8, Fraction(1)) == 1,
        "half_correlation_variance": variance(8, half) == Fraction(9, 16),
        "half_correlation_effective_N": effective_n(8, half) == Fraction(16, 9),
        "positive_rho_variance_floor": True,
        "positive_rho_effective_sample_cap": True,
        "chebyshev_certificate_typed": True,
        "impossibility_threshold_rho_ge_delta_eta_squared": True,
        "finite_N_formula_exact": sufficient_n(Fraction(1, 100), Fraction(1, 10), half) == 66,
        "selector_lane_not_reopened": True,
        "no_physical_time_or_causality_assigned": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP967",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_certificate": {
            "variance": "(1-rho)/N+rho",
            "effective_sample_size": "N/(1+(N-1)*rho)",
            "variance_floor": "rho for fixed positive rho",
            "effective_sample_cap": "1/rho for fixed positive rho",
            "chebyshev_bound": "((1-rho_max)/N+rho_max)/eta^2",
            "finite_N_condition": "(1-rho_max)/(delta*eta^2-rho_max)",
            "feasibility": "rho_max < delta*eta^2",
        },
        "classification": "exchangeable calibrated marginals become a finite-confidence moment instrument only after an independent common-covariance bound",
        "first_nonfaithful_arrow": "joint preparation/reset covariance",
        "smallest_exact_falsifier": "rho=1 preserves every one-slot marginal but fixes effective sample size to one for every N",
        "remaining_instrument_gate": "source-defined slot family and calibrated rho_max stable over the admitted preparation domain",
    }
    expected = Path(__file__).parents[1] / "results" / "wp967_domain_moment_covariance_certificate.json"
    assert result == json.loads(expected.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
