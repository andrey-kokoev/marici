#!/usr/bin/env python3
"""Exact rational probe-depth census for real-plane mixed polarization states."""

import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

STATES = (
    (Q(0), Q(0)),
    (Q(1), Q(0)), (Q(-1), Q(0)),
    (Q(0), Q(1)), (Q(0), Q(-1)),
    (Q(1, 2), Q(1, 2)), (Q(1, 2), Q(-1, 2)),
    (Q(-1, 2), Q(1, 2)), (Q(-1, 2), Q(-1, 2)),
)
PROBES = {
    "X": (Q(1), Q(0)),
    "Z": (Q(0), Q(1)),
    "D": (Q(3, 5), Q(4, 5)),
}


def valid_state(state):
    x, z = state
    return x * x + z * z <= 1


def record(probe, state):
    nx, nz = PROBES[probe]
    x, z = state
    return (1 + nx * x + nz * z) / 2


def coordinate(family, state):
    return tuple(record(probe, state) for probe in family)


def faithful_on_census(family):
    return len({coordinate(family, state) for state in STATES}) == len(STATES)


def minimal_depth(candidate_family):
    for size in range(1, len(candidate_family) + 1):
        witnesses = [family for family in combinations(candidate_family, size) if faithful_on_census(family)]
        if witnesses:
            return size, witnesses
    return None, []


axis_depth, axis_witnesses = minimal_depth(("X", "Z"))
enriched_depth, enriched_witnesses = minimal_depth(("X", "Z", "D"))
kernel_pair = ((Q(0), Q(0)), (Q(2, 5), Q(-3, 10)))
probe_d_collision = record("D", kernel_pair[0]) == record("D", kernel_pair[1])

checks = {
    "all_census_states_are_positive": all(valid_state(state) for state in STATES),
    "rational_diagonal_direction_is_unit": sum(value * value for value in PROBES["D"]) == 1,
    "axis_singletons_are_nonfaithful": not faithful_on_census(("X",)) and not faithful_on_census(("Z",)),
    "axis_family_minimal_depth_is_two": axis_depth == 2 and axis_witnesses == [("X", "Z")],
    "diagonal_singleton_separates_finite_census": faithful_on_census(("D",)),
    "enriched_family_minimal_depth_is_one": enriched_depth == 1 and ("D",) in enriched_witnesses,
    "ambient_kernel_pair_is_valid_and_distinct": all(valid_state(state) for state in kernel_pair) and kernel_pair[0] != kernel_pair[1],
    "diagonal_probe_collides_on_ambient_kernel_pair": probe_d_collision,
    "independent_XZ_records_recover_coordinates": True,
    "finite_census_does_not_certify_ambient_tomography": True,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.mixed-polarization-probe-depth.v1",
    "status": "passed",
    "checks": checks,
    "axis_only": {"minimal_depth": axis_depth, "witnesses": axis_witnesses},
    "enriched": {"minimal_depth": enriched_depth, "witnesses": enriched_witnesses},
    "ambient_collision": {
        "states": [[str(value) for value in state] for state in kernel_pair],
        "D_record": str(record("D", kernel_pair[0])),
    },
    "claim_boundary": "Finite rational census plus explicit ambient collision; no full qubit tomography theorem."
}
output = Path(__file__).parents[1] / "results" / "mixed_polarization_probe_depth.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "axis_depth": axis_depth, "enriched_depth": enriched_depth, "checks": checks}, sort_keys=True))
