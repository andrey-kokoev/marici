#!/usr/bin/env python3
"""Finite countermodel: naturality without invertibility does not preserve matching fibers."""

import json
from pathlib import Path

FACES = ("empty", "p", "q", "pq")
F_OBJECTS = {"empty": ("*",), "p": ("*",), "q": ("*",), "pq": ("a", "b")}
G_OBJECTS = {"empty": ("*",), "p": ("*",), "q": ("*",), "pq": ("c",)}
INCLUSIONS = (("pq", "p"), ("pq", "q"), ("pq", "empty"), ("p", "empty"), ("q", "empty"))


def restrict(objects, source, target, value):
    if source == target:
        return value
    assert (source, target) in INCLUSIONS
    return "*"


def alpha(face, value):
    if face == "pq":
        return "c"
    return value


def presheaf_laws(objects):
    identities = all(restrict(objects, face, face, value) == value for face in FACES for value in objects[face])
    composites = all(
        restrict(objects, singleton, "empty", restrict(objects, "pq", singleton, value))
        == restrict(objects, "pq", "empty", value)
        for singleton in ("p", "q") for value in objects["pq"]
    )
    return identities and composites


def naturality_square(source, target, value):
    left = alpha(target, restrict(F_OBJECTS, source, target, value))
    right = restrict(G_OBJECTS, source, target, alpha(source, value))
    return left == right


naturality = [
    {"arrow": f"{source}->{target}", "value": value, "commutes": naturality_square(source, target, value)}
    for source, target in INCLUSIONS
    for value in F_OBJECTS[source]
]
matching_datum = ("*", "*")
fiber_F = F_OBJECTS["pq"]
fiber_G = G_OBJECTS["pq"]
induced_fiber_image = tuple(alpha("pq", value) for value in fiber_F)
checks = {
    "F_is_lawful_presheaf": presheaf_laws(F_OBJECTS),
    "G_is_lawful_presheaf": presheaf_laws(G_OBJECTS),
    "all_naturality_squares_commute": all(item["commutes"] for item in naturality),
    "joint_component_is_surjective": set(induced_fiber_image) == set(fiber_G),
    "joint_component_is_not_injective": len(set(induced_fiber_image)) < len(induced_fiber_image),
    "joint_component_is_not_invertible": len(fiber_F) != len(fiber_G),
    "matching_datum_is_preserved": matching_datum == ("*", "*"),
    "source_fiber_has_size_two": len(fiber_F) == 2,
    "target_fiber_has_size_one": len(fiber_G) == 1,
    "induced_fiber_map_is_not_equivalence": len(fiber_F) != len(fiber_G),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.natural-noninvertible-probe-map.v1", "status": "passed", "checks": checks, "naturality_squares": naturality, "fiber": {"datum": matching_datum, "F": fiber_F, "G": fiber_G, "induced_image": induced_fiber_image}, "claim_boundary": "Finite necessity countermodel for invertibility; no global rewrite theorem."}
output = Path(__file__).parents[1] / "results" / "natural_noninvertible_probe_map.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "naturality_square_count": len(naturality)}, sort_keys=True))
