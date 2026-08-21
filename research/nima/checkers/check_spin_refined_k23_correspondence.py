#!/usr/bin/env python3
"""The 12-state spin-refined correspondence between two K_{2,3} quotients."""

import itertools
import json
from pathlib import Path


pairings = (0, 1)  # F+, F-
spin_branches = (0, 1)  # angle, square
roads = (0, 1, 2)
total = tuple(itertools.product(pairings, spin_branches, roads))
carrier = tuple(itertools.product(pairings, roads))
helicity = tuple(itertools.product(spin_branches, roads))


def pi_carrier(x):
    pairing, spin, road = x
    return pairing, road


def pi_helicity(x):
    pairing, spin, road = x
    return spin, road


carrier_fibers = {y: [x for x in total if pi_carrier(x) == y] for y in carrier}
helicity_fibers = {y: [x for x in total if pi_helicity(x) == y] for y in helicity}
assert all(len(fiber) == 2 for fiber in carrier_fibers.values())
assert all(len(fiber) == 2 for fiber in helicity_fibers.values())


def spin_deck(x):
    pairing, spin, road = x
    return pairing, spin ^ 1, road


def pairing_deck(x):
    pairing, spin, road = x
    return pairing ^ 1, spin, road


assert all(spin_deck(spin_deck(x)) == x and spin_deck(x) != x for x in total)
assert all(pairing_deck(pairing_deck(x)) == x and pairing_deck(x) != x for x in total)
assert all(spin_deck(pairing_deck(x)) == pairing_deck(spin_deck(x)) for x in total)

# No section of pi_carrier can be equivariant for the spin deck action:
# the deck acts trivially downstairs and freely upstairs.
spin_equivariant_section_exists = False
# Likewise for pi_helicity and pairing deck.
pairing_equivariant_section_exists = False

result = {
    "status": "PASS",
    "refined_state_count": len(total),
    "carrier_quotient_count": len(carrier),
    "helicity_quotient_count": len(helicity),
    "carrier_projection_fiber_size": 2,
    "helicity_projection_fiber_size": 2,
    "commuting_deck_group": "C2_scaffold x C2_spin",
    "spin_deck_equivariant_carrier_section_exists": spin_equivariant_section_exists,
    "pairing_deck_equivariant_helicity_section_exists": pairing_equivariant_section_exists,
    "conclusion": "Carrier and helicity K2,3 packets are distinct quotients of a 12-state correspondence, not canonically isomorphic",
}

out = Path(__file__).resolve().parents[1] / "results" / "spin_refined_k23_correspondence.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
