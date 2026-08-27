#!/usr/bin/env python3
"""Automorphism census for raw channels and the typed associativity pentagon."""

import itertools
import json
from pathlib import Path


vertices = tuple(range(5))
pentagon_edges = {frozenset((index, (index + 1) % 5)) for index in vertices}


def is_pentagon_automorphism(permutation):
    image_edges = {
        frozenset((permutation[a], permutation[b]))
        for a, b in (tuple(edge) for edge in pentagon_edges)
    }
    return image_edges == pentagon_edges


automorphisms = [
    permutation
    for permutation in itertools.permutations(vertices)
    if is_pentagon_automorphism(permutation)
]
assert len(automorphisms) == 10


def permutation_order(permutation):
    current = tuple(vertices)
    order = 0
    while True:
        current = tuple(permutation[current[index]] for index in vertices)
        order += 1
        if current == vertices:
            return order


orders = sorted(permutation_order(permutation) for permutation in automorphisms)
assert orders == [1, 2, 2, 2, 2, 2, 5, 5, 5, 5]

# Four state channels and one arrow-level coherence channel form a nontrivial
# typed partition. No transitive five-cycle preserves it.
raw_types = ("state", "state", "state", "state", "coherence")
type_preserving_raw = [
    permutation
    for permutation in automorphisms
    if all(raw_types[index] == raw_types[permutation[index]] for index in vertices)
]
assert all(permutation_order(permutation) != 5 for permutation in type_preserving_raw)

# The five parenthesizations of four ordered adapters have distinct internal
# interval signatures. A strict automorphism preserving those signatures is
# therefore the identity.
parenthesization_signatures = (
    ((0, 1), (0, 2), (0, 3)),
    ((0, 1), (2, 3), (0, 3)),
    ((1, 2), (1, 3), (0, 3)),
    ((1, 2), (0, 2), (0, 3)),
    ((2, 3), (1, 3), (0, 3)),
)
assert len(set(parenthesization_signatures)) == 5
strictly_typed = [
    permutation
    for permutation in automorphisms
    if all(
        parenthesization_signatures[index]
        == parenthesization_signatures[permutation[index]]
        for index in vertices
    )
]
assert strictly_typed == [vertices]

# A separately declared reversal duality can admit one reflection, but it does
# not generate an order-five rotation.
reflection = tuple((-index) % 5 for index in vertices)
assert reflection in automorphisms
assert permutation_order(reflection) == 2

result = {
    "untyped_pentagon_automorphism_count": len(automorphisms),
    "untyped_automorphism_orders": orders,
    "untyped_group": "D5",
    "raw_channel_types": list(raw_types),
    "raw_type_preserving_order_five_exists": False,
    "strict_parenthesization_type_preserving_count": len(strictly_typed),
    "reciprocal_reversal_order": permutation_order(reflection),
    "typed_order_five_constructor_constructed": False,
    "verdict": (
        "D5 is currently an automorphism of the untyped pentagon only; raw channel "
        "typing and ordered adapter signatures admit no order-five rotation"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-d5-typed-rotation-gate.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
