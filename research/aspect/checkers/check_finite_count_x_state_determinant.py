from __future__ import annotations

import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def exp_series_lower(x: F, degree: int) -> F:
    return sum((x**k / factorial(k) for k in range(degree + 1)), F(0))


def lower_square(estimate: F, radius: F) -> F:
    return max(abs(estimate) - radius, F(0)) ** 2


def main() -> None:
    # Statistical and systematic allocations are kept distinct.
    correlation_statistical = F(17, 2000)
    correlation_systematic = F(17, 2000)
    population_statistical = F(1, 400)
    population_systematic = F(1, 400)
    correlation_total = correlation_statistical + correlation_systematic
    population_total = population_statistical + population_systematic

    correlation_trials_each = 276817
    population_trials = 800000

    # Outcomes for correlations lie in [-1,1]. Population indicators lie in
    # [0,1]. Each frozen sample size makes its Hoeffding exponent at least 10.
    correlation_exponent = (
        F(correlation_trials_each) * correlation_statistical**2 / 2
    )
    population_exponent = (
        2 * F(population_trials) * population_statistical**2
    )
    assert correlation_exponent >= 10
    assert population_exponent == 10

    # Four correlations plus two population indicators: six two-sided tails.
    # Their union is at most 12 exp(-10). Certify that bound rationally.
    exp_lower = exp_series_lower(F(10), 6)
    family_tail_upper = F(12) / exp_lower
    confidence_lower = F(1) - family_tail_upper
    assert exp_lower > 1200
    assert family_tail_upper < F(1, 100)
    assert confidence_lower > F(99, 100)

    quadrature_total = correlation_total / 2
    assert correlation_total == F(17, 1000)
    assert population_total == F(1, 200)
    assert quadrature_total == F(17, 2000)

    b, c = F(1, 100), F(9, 100)
    x, y = F(3, 100), F(4, 100)
    certificate_lower = (
        lower_square(x, quadrature_total)
        + lower_square(y, quadrature_total)
        - (b + population_total) * (c + population_total)
    )
    assert certificate_lower == F(59, 2000000)
    assert certificate_lower > 0

    total_trials = 4 * correlation_trials_each + population_trials
    assert total_trials == 1907268

    result = {
        "schema": "marici.aspect.finite-count-x-state-determinant.v1",
        "status": "pass",
        "correlation_settings": ["XX", "YY", "XY", "YX"],
        "correlation_trials_each": correlation_trials_each,
        "joint_population_trials": population_trials,
        "total_trials": total_trials,
        "correlation_statistical_radius": str(correlation_statistical),
        "correlation_systematic_radius": str(correlation_systematic),
        "correlation_total_radius": str(correlation_total),
        "population_statistical_radius": str(population_statistical),
        "population_systematic_radius": str(population_systematic),
        "population_total_radius": str(population_total),
        "derived_quadrature_total_radius": str(quadrature_total),
        "correlation_hoeffding_exponent": str(correlation_exponent),
        "population_hoeffding_exponent": str(population_exponent),
        "family_tail_probability_strict_upper": str(family_tail_upper),
        "confidence_strict_lower": str(confidence_lower),
        "confidence_exceeds": "99/100",
        "hostile_certificate_lower": str(certificate_lower),
        "verdict": "A separately derived five-setting finite-count contract certifies the asymmetric determinant hostile with greater than 99 percent confidence.",
        "claim_boundary": "iid bounded outcomes within each setting and frozen systematic radii; no predicted source trajectory, loss repair, or phase-drift model",
    }
    output = Path(__file__).parents[1] / "results" / "finite_count_x_state_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
