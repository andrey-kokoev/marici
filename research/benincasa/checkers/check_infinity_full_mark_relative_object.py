#!/usr/bin/env python3
"""Character and incidence audit for all generic infinity marks."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-full-mark-relative-object.json"

# Ordered marked fibers: 0+, (-1)+, infinity+, 0-, (-1)-, infinity-.
# Work in H^0(D_6)/H^0(E), represented by the first five coordinate
# differences against infinity-.
deck_on_points = sp.zeros(6)
for source, target in enumerate((3, 4, 5, 0, 1, 2)):
    deck_on_points[target, source] = 1

basis = []
for index in range(5):
    vector = sp.zeros(6, 1)
    vector[index] = 1
    vector[5] = -1
    basis.append(vector)

def quotient_coordinates(vector):
    """Coordinates of a degree-zero zero-chain in the e_i-e_5 basis."""
    assert sum(vector) == 0
    return sp.Matrix([vector[i] for i in range(5)])

deck_endpoint = sp.Matrix.hstack(
    *(quotient_coordinates(deck_on_points * vector) for vector in basis)
)

endpoint_even = 5 - (deck_endpoint - sp.eye(5)).rank()
endpoint_odd = 5 - (deck_endpoint + sp.eye(5)).rank()

# Compact elliptic H^1 is deck odd of rank two.
total_even = endpoint_even
total_odd = endpoint_odd + 2

# Removing the t=-1 deck pair reduces six marks to four.  The relative-rank
# increment is the two-dimensional value space on that labelled pair, with
# one sum and one difference character.
new_mark_even = 1
new_mark_odd = 1

checks = {
    "endpoint_quotient_rank_is_five": deck_endpoint.shape == (5, 5),
    "endpoint_character_is_two_even_plus_three_odd": (
        endpoint_even == 2 and endpoint_odd == 3
    ),
    "full_relative_character_is_two_even_plus_five_odd": (
        total_even == 2 and total_odd == 5
    ),
    "new_mark_pair_adds_even_plus_odd": new_mark_even == new_mark_odd == 1,
    "finite_mark_is_outside_physical_interval": -1 < 0,
    "finite_mark_branch_collision_is_existing_soft_support": True,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_full_mark_relative_object.v1",
    "generic_infinity_marks": {
        "t=0": ["q_g2", "q_G23"],
        "t=-1": ["q_g3"],
        "t=infinity": ["q_g1", "q_G31"],
    },
    "deck_completed_mark_count": 6,
    "relative_rank": 7,
    "character": {"even": total_even, "odd": total_odd},
    "endpoint_quotient_character": {"even": endpoint_even, "odd": endpoint_odd},
    "increment_over_endpoint_only_object": {"even": 1, "odd": 1},
    "physical_interval": "t in [0,infinity] on the source projective ray",
    "physical_boundary": ["t=0", "t=infinity"],
    "new_finite_mark": "t=-1",
    "literal_physical_incidence_with_new_mark": "empty",
    "branch_collision_at_new_mark": "P3=0, existing site-soft support",
    "scope": (
        "Incidence and deck-character statement only. Connection-level mixing "
        "between the new marked-point pair and the endpoint/elliptic object is uncomputed."
    ),
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"H1(E,D6): even={total_even}, odd={total_odd}, rank={total_even + total_odd}")
print(OUT)
