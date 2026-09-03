#!/usr/bin/env python3
"""Finite countermodel: objectwise bijections without naturality do not preserve matching fibers."""

import json
from itertools import permutations, product
from pathlib import Path

FACES = ("empty", "p", "q", "pq")
OBJECTS = {"empty": ("*",), "p": (0, 1), "q": (0, 1), "pq": ("a", "b")}


def identity(x):
    return x


def constant_empty(_x):
    return "*"


F = {
    ("pq", "p"): {"a": 0, "b": 1},
    ("pq", "q"): {"a": 0, "b": 1},
}
G = {
    ("pq", "p"): {"a": 0, "b": 0},
    ("pq", "q"): {"a": 0, "b": 0},
}


def restrict(presheaf, source, target, value):
    if source == target:
        return identity(value)
    if target == "empty":
        return constant_empty(value)
    return presheaf[(source, target)][value]


def matching_map(presheaf, joint):
    return (restrict(presheaf, "pq", "p", joint), restrict(presheaf, "pq", "q", joint))


def fiber(presheaf, datum):
    return tuple(joint for joint in OBJECTS["pq"] if matching_map(presheaf, joint) == datum)


def presheaf_laws(presheaf):
    identities = all(restrict(presheaf, face, face, value) == value for face in FACES for value in OBJECTS[face])
    composites = all(
        restrict(presheaf, singleton, "empty", restrict(presheaf, "pq", singleton, value))
        == restrict(presheaf, "pq", "empty", value)
        for singleton in ("p", "q") for value in OBJECTS["pq"]
    )
    return identities and composites


objectwise_identity_is_bijective = all(len(set(OBJECTS[face])) == len(OBJECTS[face]) for face in FACES)
naturality_failures = []
for target in ("p", "q"):
    for value in OBJECTS["pq"]:
        left = restrict(F, "pq", target, value)
        right = restrict(G, "pq", target, value)
        if left != right:
            naturality_failures.append({"arrow": f"pq->{target}", "value": value, "F": left, "G": right})

# Exhaust every objectwise bijection family. The empty component is forced;
# p, q, and pq each have two permutations, hence eight candidates.
def bijections(values):
    return [{source: target for source, target in zip(values, image)} for image in permutations(values)]


def is_natural_family(alpha_p, alpha_q, alpha_pq):
    for value in OBJECTS["pq"]:
        mapped = alpha_pq[value]
        if alpha_p[restrict(F, "pq", "p", value)] != restrict(G, "pq", "p", mapped):
            return False
        if alpha_q[restrict(F, "pq", "q", value)] != restrict(G, "pq", "q", mapped):
            return False
    return True

candidate_families = list(product(bijections(OBJECTS["p"]), bijections(OBJECTS["q"]), bijections(OBJECTS["pq"])))
natural_isomorphism_count = sum(is_natural_family(*family) for family in candidate_families)

datum = (1, 1)
fiber_F = fiber(F, datum)
fiber_G = fiber(G, datum)
checks = {
    "F_is_lawful_presheaf": presheaf_laws(F),
    "G_is_lawful_presheaf": presheaf_laws(G),
    "identity_maps_are_objectwise_bijections": objectwise_identity_is_bijective,
    "identity_family_is_not_natural": bool(naturality_failures),
    "matching_maps_are_not_conjugate_by_identities": any(matching_map(F, value) != matching_map(G, value) for value in OBJECTS["pq"]),
    "F_fiber_over_11_has_one_element": fiber_F == ("b",),
    "G_fiber_over_11_is_empty": fiber_G == (),
    "fiber_cardinality_is_not_preserved": len(fiber_F) != len(fiber_G),
    "all_eight_objectwise_bijection_families_exhausted": len(candidate_families) == 8,
    "no_objectwise_bijection_family_is_natural": natural_isomorphism_count == 0,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.nonnatural-probe-rewrite-countermodel.v1", "status": "passed", "checks": checks, "objectwise_bijection_family_count": len(candidate_families), "natural_isomorphism_count": natural_isomorphism_count, "naturality_failures": naturality_failures, "matching_maps": {"F": {x: matching_map(F, x) for x in OBJECTS["pq"]}, "G": {x: matching_map(G, x) for x in OBJECTS["pq"]}}, "fiber_over_11": {"F": fiber_F, "G": fiber_G}, "claim_boundary": "Finite necessity countermodel; no global rewrite theorem."}
output = Path(__file__).parents[1] / "results" / "nonnatural_probe_rewrite_countermodel.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "naturality_failure_count": len(naturality_failures)}, sort_keys=True))
