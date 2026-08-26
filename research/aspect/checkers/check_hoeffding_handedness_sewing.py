from __future__ import annotations

import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def exponential_series_lower(x: F, degree: int) -> F:
    return sum((x**power / factorial(power) for power in range(degree + 1)), F(0))


def main() -> None:
    settings = 3
    trials_per_setting = 2000
    statistical_correlation_radius = F(1, 10)
    systematic_correlation_radius = F(1, 100)

    # Two-sided Hoeffding for a mean of N variables in [-1,1]:
    # P(|c_hat-c| >= t) <= 2 exp(-N t^2 / 2).
    exponent = F(trials_per_setting) * statistical_correlation_radius**2 / 2
    assert exponent == 10

    # Prove the exponential comparison using rational arithmetic only.
    # exp(10) exceeds every finite positive Taylor partial sum.
    exp_lower = exponential_series_lower(exponent, 4)
    assert exp_lower == F(1933, 3)
    assert exp_lower > 600

    # Union over three settings gives 6 exp(-10). Replacing exp(10) by
    # its strict lower bound yields a fully rational strict upper bound.
    family_tail_rational_upper = F(6) / exp_lower
    confidence_rational_lower = F(1) - family_tail_rational_upper
    assert family_tail_rational_upper == F(18, 1933)
    assert family_tail_rational_upper < F(1, 100)
    assert confidence_rational_lower == F(1915, 1933)
    assert confidence_rational_lower > F(99, 100)

    combined_correlation_radius = (
        statistical_correlation_radius + systematic_correlation_radius
    )
    witness_radius = F(3, 4) * combined_correlation_radius
    benchmark_witness = F(-19147, 40000)
    certificate_upper = benchmark_witness + witness_radius
    assert witness_radius == F(33, 400)
    assert certificate_upper == F(-15847, 40000)
    assert certificate_upper < 0

    result = {
        "schema": "marici.aspect.hoeffding-handedness-sewing.v1",
        "status": "pass",
        "settings": ["XX", "YY", "ZZ"],
        "trials_per_setting": trials_per_setting,
        "total_trials": settings * trials_per_setting,
        "statistical_correlation_radius": str(statistical_correlation_radius),
        "hoeffding_exponent": str(exponent),
        "exp_taylor_degree": 4,
        "exp_taylor_rational_lower": str(exp_lower),
        "family_tail_probability_strict_upper": str(family_tail_rational_upper),
        "confidence_strict_lower": str(confidence_rational_lower),
        "confidence_exceeds": "99/100",
        "systematic_correlation_radius": str(systematic_correlation_radius),
        "witness_radius": str(witness_radius),
        "benchmark_certificate_upper": str(certificate_upper),
        "event_reduction_from_chebyshev_contract": "15-fold",
        "verdict": "A rationally certified Hoeffding contract reduces the prospective acquisition from 90000 to 6000 coincidence events while retaining the same error radius and greater than 99 percent confidence.",
        "claim_boundary": "independent stationary trials within each setting; calibrated systematic bound; theorem arithmetic checked but theorem assumptions remain experimental obligations",
    }
    output = Path(__file__).parents[1] / "results" / "hoeffding_handedness_sewing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
