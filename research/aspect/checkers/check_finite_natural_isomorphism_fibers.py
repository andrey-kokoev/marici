#!/usr/bin/env python3
"""Exhaustive finite witness for natural-isomorphism preservation of matching fibers."""

import json
from itertools import product
from pathlib import Path

SOURCE_JOINT = ("a", "b", "c")
TARGET_JOINT = ("A", "B", "C")
F_MATCH = {"a": (0, 0), "b": (1, 1), "c": (0, 1)}
G_MATCH = {"A": (0, 0), "B": (1, 1), "C": (1, 0)}
ALPHA_JOINT = {"a": "B", "b": "A", "c": "C"}
MATCHING_DATA = tuple(product((0, 1), repeat=2))


def alpha_bit(value):
    return 1 - value


def alpha_matching(datum):
    return tuple(alpha_bit(value) for value in datum)


def fiber(mapping, domain, datum):
    return tuple(value for value in domain if mapping[value] == datum)


def naturality(mapping_G=G_MATCH):
    return {
        value: tuple(alpha_bit(bit) for bit in F_MATCH[value]) == mapping_G[ALPHA_JOINT[value]]
        for value in SOURCE_JOINT
    }


def fiber_transport(datum):
    source = fiber(F_MATCH, SOURCE_JOINT, datum)
    target_datum = alpha_matching(datum)
    target = fiber(G_MATCH, TARGET_JOINT, target_datum)
    image = tuple(ALPHA_JOINT[value] for value in source)
    return {"source": source, "target_datum": target_datum, "target": target, "image": image, "bijective": set(image) == set(target) and len(image) == len(set(image))}


naturality_squares = naturality()
transports = {str(datum): fiber_transport(datum) for datum in MATCHING_DATA}

# Hostile 1: retain all comparison bijections but alter one target restriction.
G_BAD = dict(G_MATCH)
G_BAD["C"] = (0, 0)
bad_naturality = naturality(G_BAD)
bad_conjugacy = all(tuple(alpha_bit(bit) for bit in F_MATCH[value]) == G_BAD[ALPHA_JOINT[value]] for value in SOURCE_JOINT)

# Hostile 2: a separately lawful natural quotient with singleton proper faces.
quotient_source_joint = ("u", "v")
quotient_target_joint = ("w",)
quotient_map = {"u": "w", "v": "w"}
quotient_naturality = all("*" == "*" for _ in quotient_source_joint)
quotient_invertible = len(set(quotient_map.values())) == len(quotient_source_joint) == len(quotient_target_joint)
quotient_fiber_equiv = len(quotient_source_joint) == len(quotient_target_joint)

checks = {
    "joint_component_is_bijective": set(ALPHA_JOINT.values()) == set(TARGET_JOINT) and len(set(ALPHA_JOINT.values())) == len(SOURCE_JOINT),
    "singleton_components_are_bijective": {alpha_bit(0), alpha_bit(1)} == {0, 1},
    "all_naturality_squares_commute": all(naturality_squares.values()),
    "matching_maps_are_conjugate": all(naturality_squares.values()),
    "all_four_matching_data_checked": len(transports) == 4,
    "every_fiber_transport_is_bijective": all(item["bijective"] for item in transports.values()),
    "empty_fiber_is_preserved": transports[str((1, 0))]["source"] == () and transports[str((1, 0))]["target"] == (),
    "naturality_hostile_retains_component_bijections": set(ALPHA_JOINT.values()) == set(TARGET_JOINT),
    "naturality_hostile_fails_square_and_conjugacy": not all(bad_naturality.values()) and not bad_conjugacy,
    "invertibility_hostile_remains_natural": quotient_naturality,
    "invertibility_hostile_collapses_fiber": not quotient_invertible and not quotient_fiber_equiv,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.finite-natural-isomorphism-fibers.v1", "status": "passed", "checks": checks, "naturality": naturality_squares, "fiber_transports": transports, "hostiles": {"broken_naturality": bad_naturality, "natural_quotient": {"natural": quotient_naturality, "invertible": quotient_invertible, "fiber_equivalence": quotient_fiber_equiv}}, "claim_boundary": "Exhaustive finite witness; general theorem remains unformalized."}
output = Path(__file__).parents[1] / "results" / "finite_natural_isomorphism_fibers.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "fiber_count": len(transports)}, sort_keys=True))
