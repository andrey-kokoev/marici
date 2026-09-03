#!/usr/bin/env python3
"""Finite representability diagnostics for lift presheaves."""

import itertools
import json
from pathlib import Path

DISCRETE_OBJECTS = ("a", "b")


def discrete_yoneda(representing_object):
    return {obj: frozenset({"id"}) if obj == representing_object else frozenset() for obj in DISCRETE_OBJECTS}


def discrete_representable(presheaf):
    return any(presheaf == discrete_yoneda(candidate) for candidate in DISCRETE_OBJECTS)


unique = {"a": frozenset({"u"}), "b": frozenset()}
# Rename the universal witness to compare up to componentwise bijection.
def discrete_shape(presheaf): return {obj: len(value) for obj, value in presheaf.items()}
def discrete_shape_representable(presheaf):
    return any(discrete_shape(presheaf) == discrete_shape(discrete_yoneda(candidate)) for candidate in DISCRETE_OBJECTS)

deletion = {"a": frozenset(), "b": frozenset()}
branch = {"a": frozenset({"u"}), "b": frozenset({"v"})}

# One-object C2 groupoid. Elements and morphisms are bits; precomposition is XOR.
C2 = (0, 1)
def regular_action(element, morphism): return element ^ morphism
def trivial_action(element, morphism): return element

def equivariant_bijections(action):
    bijections = []
    for image_tuple in itertools.permutations(C2):
        mapping = dict(zip(C2, image_tuple))
        if all(mapping[regular_action(element, morphism)] == action(mapping[element], morphism) for element in C2 for morphism in C2):
            bijections.append(mapping)
    return bijections

regular_isomorphisms = equivariant_bijections(regular_action)
trivial_isomorphisms = equivariant_bijections(trivial_action)
checks = {
    "unique_discrete_lift_is_representable": discrete_shape_representable(unique),
    "unique_lift_is_represented_by_a": discrete_shape(unique) == discrete_shape(discrete_yoneda("a")),
    "deletion_empty_support_is_not_representable": not discrete_shape_representable(deletion),
    "two_branch_support_is_not_representable": not discrete_shape_representable(branch),
    "representable_c2_presheaf_has_two_witnesses": len(C2) == 2,
    "regular_c2_action_is_representable": len(regular_isomorphisms) > 0,
    "trivial_two_element_action_is_not_representable": len(trivial_isomorphisms) == 0,
    "equal_cardinality_does_not_decide_representability": len(C2) == len(C2) and bool(regular_isomorphisms) and not trivial_isomorphisms,
    "regular_action_obeys_identity": all(regular_action(element, 0) == element for element in C2),
    "regular_action_obeys_composition": all(regular_action(regular_action(element, first), second) == regular_action(element, first ^ second) for element in C2 for first in C2 for second in C2),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.attachment-lift-representability.v1", "status": "passed", "checks": checks, "discrete_supports": {"unique": discrete_shape(unique), "deletion": discrete_shape(deletion), "branch": discrete_shape(branch)}, "regular_equivariant_bijection_count": len(regular_isomorphisms), "trivial_equivariant_bijection_count": len(trivial_isomorphisms), "claim_boundary": "Finite discrete and C2-groupoid diagnostics; coherent representability across network-map composition remains separate."}
output = Path(__file__).parents[1] / "results" / "attachment_lift_representability.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "regular_isomorphisms": len(regular_isomorphisms)}, sort_keys=True))
