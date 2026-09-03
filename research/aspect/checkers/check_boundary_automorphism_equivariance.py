#!/usr/bin/env python3
"""Exact finite action, orbit quotient, and matching-equivariance diagnostic."""

import json
from pathlib import Path
from itertools import product

X = (0, 1)
M = tuple(product(X, repeat=2))
GROUP = ("id", "swap")


def act(group_element, datum):
    return datum if group_element == "id" else (datum[1], datum[0])


def orbit(datum):
    return frozenset(act(group_element, datum) for group_element in GROUP)


def compose(left, right):
    return "id" if left == right else "swap"


orbits = {orbit(datum) for datum in M}
fixed = tuple(datum for datum in M if act("swap", datum) == datum)
quotient_record = {datum: tuple(sorted(orbit(datum))) for datum in M}
mixed_record = quotient_record[(0, 1)]
mixed_fiber = tuple(datum for datum in M if quotient_record[datum] == mixed_record)

# The joint set equals M and the matching map is identity.
def matching_map(joint):
    return joint


action_laws = all(
    act(left, act(right, datum)) == act(compose(left, right), datum)
    for left in GROUP for right in GROUP for datum in M
)
matching_equivariance = all(
    matching_map(act(group_element, joint)) == act(group_element, matching_map(joint))
    for group_element in GROUP for joint in M
)
quotient_invariance = all(quotient_record[act("swap", datum)] == quotient_record[datum] for datum in M)
checks = {
    "matching_object_retains_four_occurrence_resolved_points": len(M) == 4,
    "swap_action_satisfies_group_laws": action_laws,
    "matching_map_is_equivariant": matching_equivariance,
    "orbit_quotient_has_three_points": len(orbits) == 3,
    "fixed_point_object_has_two_points": len(fixed) == 2,
    "full_orbit_and_fixed_objects_are_distinct": len({len(M), len(orbits), len(fixed)}) == 3,
    "orbit_projection_is_swap_invariant": quotient_invariance,
    "orbit_projection_is_not_injective": len(set(quotient_record.values())) < len(M),
    "mixed_orbit_has_multiplicity_two": set(mixed_fiber) == {(0, 1), (1, 0)},
    "external_action_does_not_impose_internal_fixed_point_equation": len(M) != len(fixed),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.boundary-automorphism-equivariance.v1", "status": "passed", "checks": checks, "matching_object": M, "orbits": [sorted(value) for value in sorted(orbits, key=lambda item: sorted(item))], "fixed_points": fixed, "mixed_orbit_fiber": mixed_fiber, "claim_boundary": "Finite external S2 action; no source authorization to quotient occurrences."}
output = Path(__file__).parents[1] / "results" / "boundary_automorphism_equivariance.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "matching_size": len(M), "orbit_size": len(orbits), "fixed_size": len(fixed)}, sort_keys=True))
