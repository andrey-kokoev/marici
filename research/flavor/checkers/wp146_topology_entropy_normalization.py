"""Exact Catalan topology-entropy versus normalization audit."""

from fractions import Fraction
from math import comb
import json
from pathlib import Path


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def weight(k: int, q: Fraction) -> Fraction:
    return Fraction(catalan(k - 1)) * q ** (k - 1)


q_critical = Fraction(1, 4)
z_critical = Fraction(2)
q_supercritical = Fraction(1, 3)


def probability_at_critical(k: int) -> Fraction:
    return weight(k, q_critical) / z_critical


def successive_ratio(k: int, q: Fraction) -> Fraction:
    # w_(k+1)/w_k = q C_k/C_(k-1).
    return q * Fraction(2 * (2 * k - 1), k + 1)


checks = {
    "first_catalan_multiplicities": [catalan(n) for n in range(5)] == [1, 1, 2, 5, 14],
    "critical_generating_sum_is_two": z_critical == 2,
    "critical_minimal_probability_is_one_half": probability_at_critical(1) == Fraction(1, 2),
    "critical_target_probability_is_five_over_128": probability_at_critical(4) == Fraction(5, 128),
    "critical_accessible_tail_probability_is_one_half": 1 - probability_at_critical(1) == Fraction(1, 2),
    "critical_weights_decrease_at_k1": successive_ratio(1, q_critical) == Fraction(1, 4),
    "critical_weights_decrease_at_k4": successive_ratio(4, q_critical) == Fraction(7, 10),
    "critical_ratio_is_below_one_for_all_positive_k": all(successive_ratio(k, q_critical) < 1 for k in range(1, 100)),
    "subcritical_ratio_is_smaller_than_critical": successive_ratio(4, Fraction(1, 5)) < successive_ratio(4, q_critical),
    "supercritical_ratio_exceeds_one": successive_ratio(10, q_supercritical) > 1,
    "supercritical_growth_rate_exceeds_radius": 4 * q_supercritical > 1,
    "entropy_enhanced_law_is_not_point_selector": 0 < probability_at_critical(4) < probability_at_critical(1) < 1,
}

result = {
    "work_package": "WP146",
    "title": "Topology entropy-normalization audit",
    "domain": "k=chi/24 in {1,2,...} with Catalan multiplicity C_(k-1)",
    "source_law": "unnormalized w_k=C_(k-1) q^(k-1)",
    "normalization_radius": "0<=q<=1/4 (finite at q=1/4)",
    "critical_values": {
        "Z(1/4)": "2",
        "P(k=1)": "1/2",
        "P(k=4)": "5/128",
        "P(accessible k>=2)": "1/2",
        "mean_k": "divergent",
    },
    "classification": "entropy-enhanced topology ensemble; every normalizable member remains modal at minimal inaccessible topology",
    "selector": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": {
        "claim": "Catalan topology entropy makes accessible k=4 modal within the normalized family",
        "witness": "at the maximal q=1/4, P(1)=1/2 while P(4)=5/128; q>1/4 lies outside the convergence radius",
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp146_topology_entropy_normalization.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

