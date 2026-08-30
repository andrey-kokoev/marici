"""Hostile two-atom test for compact Schwarzian-numerator monotonicity.

This tests whether positivity of an even source alone forces N'(H)<0 for
H=(x-1/4)(log C)' and C=sum_j weight_j cosh(sqrt(x) u_j).
"""

import json
import math
from pathlib import Path


def cosh_x_jets(x, u, max_order=5):
    jets = [0.0] * (max_order + 1)
    term = 1.0
    for k in range(240):
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


def evaluate(x, atom, weight):
    zero = cosh_x_jets(x, 0.0)
    nonzero = cosh_x_jets(x, atom)
    transform = [
        zero[order] + weight * nonzero[order] for order in range(6)
    ]
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
        "atom": atom,
        "weight": weight,
        "H_jets": [h1, h2, h3, h4],
        "schwarzian_numerator": numerator,
        "schwarzian_numerator_prime": numerator_prime,
        "violates_theta_monotonicity_sign": numerator_prime >= 0.0,
    }


x_values = [0.251, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
atom_values = [0.1, 0.25, 0.5, 1.0, 2.0, 4.0]
weight_values = [10.0**power for power in range(-4, 5)]
rows = [
    evaluate(x, atom, weight)
    for x in x_values
    for atom in atom_values
    for weight in weight_values
]
violations = [row for row in rows if row["violates_theta_monotonicity_sign"]]

result = {
    "target": "generic positive even source implies N'(H)<0",
    "source_family": "delta_0 + weight*(delta_atom+delta_-atom)/2",
    "sample_count": len(rows),
    "violation_count": len(violations),
    "first_violation": violations[0] if violations else None,
    "largest_numerator_prime": max(
        rows, key=lambda row: row["schwarzian_numerator_prime"]
    ),
    "generic_positive_source_theorem_survives_scan": not violations,
    "theta_specific_structure_required_if_falsified": bool(violations),
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-compact-monotonicity-two-atom-falsifier.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
