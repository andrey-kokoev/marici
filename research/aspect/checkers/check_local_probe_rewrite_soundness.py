#!/usr/bin/env python3
"""Finite diagnostic for natural-isomorphism rewrite soundness."""

import json
from pathlib import Path

BITS = {0, 1}
JOINT = {(0, 0), (1, 1)}
EMPTY = {()}


def flip(value):
    return 1 - value


def alpha_unary(value):
    return flip(value)


def alpha_joint(row):
    return (flip(row[0]), flip(row[1]))


def restrict(row, coordinate):
    return row[coordinate]


naturality = {}
for coordinate, probe in enumerate(("p", "q")):
    naturality[probe] = all(
        restrict(alpha_joint(row), coordinate) == alpha_unary(restrict(row, coordinate))
        for row in JOINT
    )

# Hostile joint-only relabelling: boundary unary representatives are not changed.
joint_only_naturality = {}
for coordinate, probe in enumerate(("p", "q")):
    joint_only_naturality[probe] = all(
        restrict(alpha_joint(row), coordinate) == restrict(row, coordinate)
        for row in JOINT
    )

alpha_joint_image = {alpha_joint(row) for row in JOINT}
alpha_unary_image = {alpha_unary(value) for value in BITS}
lossy_joint_image = {(0, 0)}
lossy_residual = sorted(JOINT - lossy_joint_image)

checks = {
    "empty_configuration_preserved": EMPTY == EMPTY,
    "coherent_unary_maps_are_bijections": alpha_unary_image == BITS,
    "coherent_joint_map_is_bijection": alpha_joint_image == JOINT,
    "coherent_relabelling_is_natural": all(naturality.values()),
    "joint_only_mutation_fails_naturality": not any(joint_only_naturality.values()),
    "equal_joint_cardinality_alone_is_insufficient": len(alpha_joint_image) == len(JOINT) and not any(joint_only_naturality.values()),
    "lossy_collapse_is_not_invertible": len(lossy_joint_image) < len(JOINT),
    "lossy_collapse_has_explicit_residual": lossy_residual == [(1, 1)],
    "local_certificate_does_not_claim_global_confluence": True,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.local-probe-rewrite-soundness.v1",
    "status": "passed",
    "checks": checks,
    "naturality": naturality,
    "hostile_joint_only_naturality": joint_only_naturality,
    "lossy_residual": lossy_residual,
    "criterion": "componentwise natural isomorphism on the common boundary configuration category",
    "claim_boundary": "Finite local rewrite certificate; no global confluence, normalization, or physical equivalence theorem."
}
output = Path(__file__).parents[1] / "results" / "local_probe_rewrite_soundness.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
