#!/usr/bin/env python3
"""Exact finite comparison of internal groupoid limits and external actions."""

import json
from itertools import product
from pathlib import Path

X = (0, 1)
DISCRETE_MATCHING = tuple(product(X, repeat=2))


def flip(value):
    return 1 - value


def external_swap(pair):
    return pair[1], pair[0]


external_fixed = tuple(pair for pair in DISCRETE_MATCHING if external_swap(pair) == pair)
external_orbits = {frozenset((pair, external_swap(pair))) for pair in DISCRETE_MATCHING}
walking_iso_flip_limit = tuple(pair for pair in DISCRETE_MATCHING if pair[1] == flip(pair[0]))
walking_iso_identity_limit = tuple(pair for pair in DISCRETE_MATCHING if pair[1] == pair[0])
bs2_flip_limit = tuple(value for value in X if flip(value) == value)
bs2_trivial_limit = X

checks = {
    "discrete_two_occurrence_limit_has_four_points": len(DISCRETE_MATCHING) == 4,
    "external_swap_fixed_subset_is_diagonal": set(external_fixed) == {(0, 0), (1, 1)},
    "external_orbit_quotient_has_three_points": len(external_orbits) == 3,
    "internal_flip_isomorphism_limit_is_antidiagonal": set(walking_iso_flip_limit) == {(0, 1), (1, 0)},
    "internal_identity_isomorphism_limit_is_diagonal": set(walking_iso_identity_limit) == {(0, 0), (1, 1)},
    "equal_cardinality_does_not_identify_internal_and_external_objects": len(walking_iso_flip_limit) == len(external_fixed) == 2 and set(walking_iso_flip_limit) != set(external_fixed),
    "hostile_equal_cardinality_objects_are_disjoint": set(walking_iso_flip_limit).isdisjoint(external_fixed),
    "internal_BS2_flip_limit_is_empty": bs2_flip_limit == (),
    "internal_BS2_trivial_limit_is_all_X": bs2_trivial_limit == X,
    "four_constructors_have_distinct_outputs": len(DISCRETE_MATCHING) != len(external_orbits) and set(walking_iso_flip_limit) != set(external_fixed) and len(bs2_flip_limit) == 0,
}
assert all(checks.values()), checks
result = {
    "schema": "marici.aspect.internal-boundary-groupoid-matching.v1",
    "status": "passed",
    "checks": checks,
    "objects": {
        "discrete_matching": DISCRETE_MATCHING,
        "external_fixed": external_fixed,
        "external_orbit_count": len(external_orbits),
        "walking_iso_flip_limit": walking_iso_flip_limit,
        "walking_iso_identity_limit": walking_iso_identity_limit,
        "BS2_flip_limit": bs2_flip_limit,
        "BS2_trivial_limit": bs2_trivial_limit,
    },
    "claim_boundary": "Ordinary finite Set-valued limits only; no homotopy or physical quotient claim."
}
output = Path(__file__).parents[1] / "results" / "internal_boundary_groupoid_matching.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "discrete": len(DISCRETE_MATCHING), "orbit": len(external_orbits), "internal_flip": len(walking_iso_flip_limit), "BS2_flip": len(bs2_flip_limit)}, sort_keys=True))
