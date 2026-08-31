"""No canonical torsion bridge from the all-soft Z/3 character to the mu2-odd nearby line.

The only admissible bridge at this gate is a source-derived homomorphism of the
recorded torsion/descent data.  The current source records an order-three flat
relative character and a sheet-odd mu2 descent demand.  Any group homomorphism
Z/3 -> Z/2 is zero because the image of a generator must have order dividing
both 3 and 2.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_z3_to_mu2_bridge_no_go.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def hom_count(cyclic_source_order: int, cyclic_target_order: int) -> int:
    # Hom(Z/n, Z/m) has gcd(n,m) elements.
    return gcd(cyclic_source_order, cyclic_target_order)


def main() -> None:
    separation = load("cosmology_triple_incidence_all_soft_separation.json")
    character = load("all-soft-relative-differential-character.json")
    activation = load("cosmology_triple_incidence_activation_obstruction.json")

    source_order = character["order"]
    target_order = 2
    assert source_order == 3
    assert separation["order_and_descent"]["nearby_line_descent_type"] == "mu2_sheet_odd"
    assert activation["deck_descent_gate"]["coefficient_deck_character"] == "odd"

    all_homs = hom_count(source_order, target_order)
    nonzero_homs = all_homs - 1
    assert all_homs == 1
    assert nonzero_homs == 0

    packet = {
        "schema": "marici.cosmology-z3-to-mu2-bridge-no-go.v1",
        "source_object": "all-soft flat relative differential character",
        "source_torsion_order": source_order,
        "target_object": "triple-incidence sheet-odd nearby coefficient",
        "target_descent_order": target_order,
        "hom_group_cardinality": all_homs,
        "nonzero_homomorphisms": nonzero_homs,
        "canonical_torsion_bridge_exists": False,
        "source_map_from_all_soft_to_mu2_odd_nearby_coefficient": False,
        "physical_twisted_pairing_constructed": False,
        "conclusion": (
            "any torsion-respecting source map from the all-soft Z/3 character "
            "to the mu2-odd nearby coefficient is zero; the existing all-soft "
            "character cannot activate the triple-incidence physical period"
        ),
        "remaining_escape_hatches": [
            "non-torsion analytic-continuation contour with independent source authority",
            "new coefficient object not factoring through the recorded Z/3 character",
            "all-soft physical chain coupling constructed outside the mu2-odd nearby line",
        ],
        "next_gate": (
            "stop using the all-soft Z/3 character as a bridge to the mu2-odd "
            "nearby line; pursue only independently sourced analytic continuation "
            "or a new coefficient object"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
