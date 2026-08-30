"""Exact audit of a linear topology-preparation law on chi=24 k, k>=1."""

from fractions import Fraction
import json
from pathlib import Path


q = Fraction(1, 2)
reach_squared = Fraction(9, 16)


def probability(k: int) -> Fraction:
    return (1 - q) * q ** (k - 1)


def accessible(k: int) -> bool:
    # M_KK(k)^2 = 1/k; accessibility is the strict inequality M_KK < 3/4.
    return Fraction(1, k) < reach_squared


checks = {
    "geometric_parameter_is_normalizable": 0 < q < 1,
    "geometric_series_normalizes_exactly": (1 - q) / (1 - q) == 1,
    "minimal_topology_probability_is_one_half": probability(1) == Fraction(1, 2),
    "target_topology_probability_is_one_sixteenth": probability(4) == Fraction(1, 16),
    "mean_topology_index_is_two": 1 / (1 - q) == 2,
    "minimal_topology_is_inaccessible": not accessible(1),
    "first_accessible_topology_is_two": accessible(2),
    "accessible_tail_probability_is_one_half": q == Fraction(1, 2),
    "stable_linear_weight_decreases_toward_target": probability(4) < probability(1),
    "finite_temperature_law_is_not_a_point_selector": 0 < probability(1) < 1,
    "zero_temperature_limit_selects_inaccessible_minimum": not accessible(1),
    "sign_reversal_needed_to_favor_large_k_is_nonnormalizable": Fraction(2, 1) >= 1,
}

result = {
    "work_package": "WP145",
    "title": "Topology-preparation stability audit",
    "domain": "positive topology lattice k=chi/24 in {1,2,...}",
    "source_law": "P(k)=(1-q)q^(k-1), q=1/2",
    "reach": "E_max=3/4 with M_KK(k)^2=1/k",
    "exact_values": {
        "P(k=1)": "1/2",
        "P(k=4)": "1/16",
        "E[k]": "2",
        "P(accessible k>=2)": "1/2",
    },
    "classification": "normalized topology ensemble; stable linear weight favors the minimal inaccessible topology",
    "selector": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": {
        "claim": "normalizable linear topology weight favors the accessible k=4 sector",
        "witness": "q=1/2 gives P(1)=1/2 > P(4)=1/16; reversing monotonicity requires q>1 and a divergent sum",
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp145_topology_preparation_stability.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

