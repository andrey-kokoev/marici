"""Exact conditional audit of a topology congruence selector."""

from fractions import Fraction
import json
from pathlib import Path


q = Fraction(1, 2)
m_target = 4
m_hostile = 1
reach_squared = Fraction(9, 16)


def allowed(k: int, modulus: int) -> bool:
    return k >= 1 and k % modulus == 0


def accessible(k: int) -> bool:
    return Fraction(1, k) < reach_squared


def sector_probability(j: int, modulus: int) -> Fraction:
    ratio = q ** modulus
    return (1 - ratio) * ratio ** (j - 1)


target_ratio = q ** m_target
hostile_ratio = q ** m_hostile

checks = {
    "target_projector_is_proper": allowed(4, m_target) and not allowed(1, m_target),
    "target_projector_is_idempotent": all((allowed(k, m_target) and allowed(k, m_target)) == allowed(k, m_target) for k in range(1, 17)),
    "target_minimum_is_four": min(k for k in range(1, 17) if allowed(k, m_target)) == 4,
    "target_minimum_is_accessible": accessible(4),
    "entire_target_domain_is_accessible": all(accessible(4 * j) for j in range(1, 17)),
    "target_ratio_is_one_sixteenth": target_ratio == Fraction(1, 16),
    "target_ground_probability_is_fifteen_sixteenths": sector_probability(1, m_target) == Fraction(15, 16),
    "target_mean_topology_is_sixty_four_fifteenths": Fraction(m_target, 1 - target_ratio) == Fraction(64, 15),
    "finite_temperature_is_not_point_selection": 0 < sector_probability(2, m_target) < sector_probability(1, m_target) < 1,
    "zero_temperature_selects_target_minimum": min(k for k in range(1, 17) if allowed(k, m_target)) == m_target,
    "hostile_modulus_selects_inaccessible_minimum": min(k for k in range(1, 5) if allowed(k, m_hostile)) == 1 and not accessible(1),
    "modulus_changes_physical_accessibility": accessible(m_target) != accessible(m_hostile),
}

result = {
    "work_package": "WP147",
    "title": "Topology congruence-selector audit",
    "domain": "positive topology lattice k=chi/24 with conditional admissibility k=0 mod m",
    "source_operation": "congruence projector Pi_m followed by the inherited linear topology weight q^k",
    "target_packet": {
        "m": 4,
        "allowed_domain": "{4,8,12,...}",
        "conditional_ratio": "1/16",
        "P(k=4)": "15/16",
        "E[k]": "64/15",
        "accessibility": "uniform",
    },
    "classification": "conditional admissibility selector and ensemble producer; not an unconditional numerical selector",
    "selector": "conditional",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": {
        "claim": "congruence form alone derives the accessible k=4 sector",
        "witness": "the equally formed m=1 projector admits k=1 as its zero-temperature minimum, which is inaccessible",
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp147_topology_congruence_selector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

