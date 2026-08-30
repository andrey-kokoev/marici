"""Hostile strongly-log-concave test for N'(H) <= 0.

The even densities exp(-V(u)) use
V(u)=u^2/2+epsilon*(1-cos(frequency*u)); convexity is guaranteed by
epsilon*frequency^2 < 1.
"""

import json
import math
from pathlib import Path


def cosh_x_jets(x, u, max_order=5):
    jets = [0.0] * (max_order + 1)
    term = 1.0
    for k in range(220):
        if k:
            term *= x * u * u / ((2 * k - 1) * (2 * k))
        falling = 1.0
        for order in range(max_order + 1):
            if order <= k:
                if order:
                    falling *= k - order + 1
                jets[order] += term * falling / (x**order if order else 1.0)
        if k > max_order + 12 and abs(term) < 1e-16 * max(abs(jets[0]), 1.0):
            break
    return jets


def logarithmic_jets(values):
    normalized = [value / values[0] for value in values]
    logarithmic = [0.0]
    for order in range(1, len(values)):
        correction = math.fsum(
            math.comb(order - 1, index - 1)
            * logarithmic[index]
            * normalized[order - index]
            for index in range(1, order)
        )
        logarithmic.append(normalized[order] - correction)
    return logarithmic[1:]


def evaluate(x, frequency, convexity_fraction, steps=2400):
    epsilon = convexity_fraction / frequency**2
    cutoff = math.sqrt(x) + 10.0
    width = cutoff / steps
    accumulators = [[] for _ in range(6)]
    for index in range(steps + 1):
        u = index * width
        potential = 0.5 * u * u + epsilon * (1.0 - math.cos(frequency * u))
        density = math.exp(-potential)
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        for order, jet in enumerate(cosh_x_jets(x, u)):
            accumulators[order].append(coefficient * density * jet)
    transform = [math.fsum(values) * width / 3.0 for values in accumulators]
    l1, l2, l3, l4, l5 = logarithmic_jets(transform)
    displacement = x - 0.25
    h1 = l1 + displacement * l2
    h2 = 2.0 * l2 + displacement * l3
    h3 = 3.0 * l3 + displacement * l4
    h4 = 4.0 * l4 + displacement * l5
    numerator = 2.0 * h1 * h3 - 3.0 * h2 * h2
    numerator_prime = 2.0 * h1 * h4 - 4.0 * h2 * h3
    return {
        "x": x,
        "frequency": frequency,
        "convexity_fraction": convexity_fraction,
        "minimum_potential_curvature": 1.0 - convexity_fraction,
        "schwarzian_numerator": numerator,
        "schwarzian_numerator_prime": numerator_prime,
        "violates_weak_monotonicity": numerator_prime > 1.0e-12,
    }


def evaluate_increasing_curvature(x, quartic, sextic, steps=2400):
    cutoff = math.sqrt(x) + 10.0
    width = cutoff / steps
    accumulators = [[] for _ in range(6)]
    for index in range(steps + 1):
        u = index * width
        potential = 0.5 * u * u + quartic * u**4 + sextic * u**6
        density = math.exp(-potential)
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        for order, jet in enumerate(cosh_x_jets(x, u)):
            accumulators[order].append(coefficient * density * jet)
    transform = [math.fsum(values) * width / 3.0 for values in accumulators]
    l1, l2, l3, l4, l5 = logarithmic_jets(transform)
    displacement = x - 0.25
    h1 = l1 + displacement * l2
    h2 = 2.0 * l2 + displacement * l3
    h3 = 3.0 * l3 + displacement * l4
    h4 = 4.0 * l4 + displacement * l5
    numerator = 2.0 * h1 * h3 - 3.0 * h2 * h2
    numerator_prime = 2.0 * h1 * h4 - 4.0 * h2 * h3
    return {
        "x": x,
        "quartic": quartic,
        "sextic": sextic,
        "potential_curvature_increases_outward": quartic > 0.0 or sextic > 0.0,
        "schwarzian_numerator": numerator,
        "schwarzian_numerator_prime": numerator_prime,
        "violates_weak_monotonicity": numerator_prime > 1.0e-12,
    }


x_values = [0.251, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
frequency_values = [1.0, 2.0, 4.0, 8.0]
convexity_fractions = [0.25, 0.5, 0.9, 0.99]
rows = [
    evaluate(x, frequency, fraction)
    for x in x_values
    for frequency in frequency_values
    for fraction in convexity_fractions
]
violations = [row for row in rows if row["violates_weak_monotonicity"]]
increasing_curvature_rows = [
    evaluate_increasing_curvature(x, quartic, sextic)
    for x in x_values
    for quartic in [0.0, 0.001, 0.01, 0.1, 1.0]
    for sextic in [0.0, 0.0001, 0.01]
    if quartic > 0.0 or sextic > 0.0
]
increasing_curvature_violations = [
    row for row in increasing_curvature_rows if row["violates_weak_monotonicity"]
]
positive_rank_two_increasing_curvature_violations = [
    row
    for row in increasing_curvature_violations
    if row["schwarzian_numerator"] > 0.0
]
result = {
    "target": "strong even log-concavity implies N'(H)<=0",
    "family": "exp(-u^2/2-epsilon*(1-cos(bu))), epsilon*b^2<1",
    "sample_count": len(rows),
    "violation_count": len(violations),
    "first_violation": violations[0] if violations else None,
    "largest_numerator_prime": max(
        rows, key=lambda row: row["schwarzian_numerator_prime"]
    ),
    "generic_strong_log_concavity_survives_scan": not violations,
    "increasing_curvature_family": "exp(-u^2/2-quartic*u^4-sextic*u^6)",
    "increasing_curvature_sample_count": len(increasing_curvature_rows),
    "increasing_curvature_violation_count": len(increasing_curvature_violations),
    "first_increasing_curvature_violation": (
        increasing_curvature_violations[0]
        if increasing_curvature_violations
        else None
    ),
    "first_positive_rank_two_increasing_curvature_violation": (
        positive_rank_two_increasing_curvature_violations[0]
        if positive_rank_two_increasing_curvature_violations
        else None
    ),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-compact-monotonicity-strong-log-concavity-falsifier.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
