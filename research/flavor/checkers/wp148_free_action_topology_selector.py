"""Exact audit of Euler divisibility from a free finite-group action."""

from fractions import Fraction
import json
from pathlib import Path


quotient_cells = {0: 5, 1: 7, 2: 3}


def euler(cells: dict[int, int]) -> int:
    return sum(((-1) ** degree) * count for degree, count in cells.items())


def free_lift(cells: dict[int, int], group_order: int) -> dict[int, int]:
    return {degree: group_order * count for degree, count in cells.items()}


chi_quotient = euler(quotient_cells)
chi_96 = euler(free_lift(quotient_cells, 96))
chi_24 = euler(free_lift(quotient_cells, 24))
k_96 = Fraction(chi_96, 24)
k_24 = Fraction(chi_24, 24)

# One positive even-dimensional orbit with stabilizer order four has size 24.
# Adding it to an otherwise free order-96 packet preserves k-integrality but
# destroys divisibility by four.
chi_nonfree = chi_96 + 24
k_nonfree = Fraction(chi_nonfree, 24)


checks = {
    "quotient_euler_is_one": chi_quotient == 1,
    "free_order96_multiplies_euler": chi_96 == 96 * chi_quotient,
    "free_order96_derives_k_four": k_96 == 4,
    "free_order96_derives_modulus_four": all(Fraction(96 * j, 24).denominator == 1 and int(Fraction(96 * j, 24)) % 4 == 0 for j in range(1, 17)),
    "derived_minimum_is_accessible": Fraction(1, int(k_96)) < Fraction(9, 16),
    "order24_multiplies_euler": chi_24 == 24 * chi_quotient,
    "order24_derives_hostile_k_one": k_24 == 1,
    "hostile_minimum_is_inaccessible": Fraction(1, int(k_24)) > Fraction(9, 16),
    "nonfree_orbit_has_size_twenty_four": Fraction(96, 4) == 24,
    "nonfree_packet_preserves_k_integrality": k_nonfree.denominator == 1,
    "nonfree_packet_breaks_modulus_four": int(k_nonfree) == 5 and int(k_nonfree) % 4 != 0,
    "group_order_changes_selected_accessibility": (Fraction(1, int(k_96)) < Fraction(9, 16)) != (Fraction(1, int(k_24)) < Fraction(9, 16)),
}

result = {
    "work_package": "WP148",
    "title": "Free-action topology-selector audit",
    "domain": "finite CW-type source geometries with chi/24 positive integral",
    "source_operation": "restrict to geometries carrying a free action of a frozen finite group G",
    "theorem": "free action implies chi(X)=|G| chi(X/G)",
    "target_packet": {
        "group_order": 96,
        "derived_relation": "k=4 chi(X/G)",
        "derived_domain": "k in 4N when chi(X/G)>0",
        "benchmark": "chi(X/G)=1 gives k=4",
    },
    "classification": "conditional source-geometric admissibility selector; group choice and freeness remain authorization gates",
    "selector": "conditional",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifiers": [
        "a free group of order 24 with chi(X/G)=1 gives inaccessible k=1",
        "an order-96 action with one stabilizer-four orbit gives k=5, breaking k=0 mod 4",
    ],
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp148_free_action_topology_selector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

