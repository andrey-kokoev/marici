#!/usr/bin/env python3
"""Exact minimality test for path and Stokes probes on a finite optical quotient."""

import itertools
import json
from pathlib import Path

PATHS = (0, 1)
POLARIZATIONS = ("H", "V", "D", "A", "R", "L")
STOKES = {
    "H": (1, 0, 0),
    "V": (-1, 0, 0),
    "D": (0, 1, 0),
    "A": (0, -1, 0),
    "R": (0, 0, 1),
    "L": (0, 0, -1),
}
STATES = tuple(itertools.product(PATHS, POLARIZATIONS))
PROBES = ("P", "S1", "S2", "S3")


def probe(name, state):
    path, polarization = state
    if name == "P":
        return path
    return STOKES[polarization][int(name[1]) - 1]


def coordinate(probe_names, state):
    return tuple(probe(name, state) for name in probe_names)


def fibers(probe_names):
    result = {}
    for state in STATES:
        result.setdefault(coordinate(probe_names, state), []).append(state)
    return result


def is_injective(probe_names):
    return all(len(fiber) == 1 for fiber in fibers(probe_names).values())


subset_results = {}
for size in range(len(PROBES) + 1):
    for subset in itertools.combinations(PROBES, size):
        subset_results[subset] = is_injective(subset)

deletion_witnesses = {}
for omitted in PROBES:
    retained = tuple(name for name in PROBES if name != omitted)
    ambiguous = next(fiber for fiber in fibers(retained).values() if len(fiber) > 1)
    deletion_witnesses[omitted] = ambiguous[:2]

expected_witness_types = {
    "P": lambda left, right: left[0] != right[0] and left[1] == right[1],
    "S1": lambda left, right: left[0] == right[0] and {left[1], right[1]} == {"H", "V"},
    "S2": lambda left, right: left[0] == right[0] and {left[1], right[1]} == {"D", "A"},
    "S3": lambda left, right: left[0] == right[0] and {left[1], right[1]} == {"R", "L"},
}
checks = {
    "quotient_has_twelve_states": len(STATES) == 12,
    "stokes_coordinates_are_distinct_on_six_eigenstates": len(set(STOKES.values())) == 6,
    "full_probe_family_is_jointly_monic": is_injective(PROBES),
    "full_coordinate_has_twelve_singleton_fibers": len(fibers(PROBES)) == 12 and all(len(value) == 1 for value in fibers(PROBES).values()),
    "no_proper_candidate_subset_is_injective": all(not injective for subset, injective in subset_results.items() if len(subset) < len(PROBES)),
    "only_full_candidate_family_is_injective": [subset for subset, injective in subset_results.items() if injective] == [PROBES],
    "every_probe_has_deletion_witness": set(deletion_witnesses) == set(PROBES),
    "deletion_witnesses_have_predicted_types": all(expected_witness_types[name](*witness) for name, witness in deletion_witnesses.items()),
    "path_probe_separates_path_lifts": probe("P", (0, "H")) != probe("P", (1, "H")),
    "polarization_probes_ignore_path": all(probe(name, (0, polarization)) == probe(name, (1, polarization)) for name in ("S1", "S2", "S3") for polarization in POLARIZATIONS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.minimal-optical-probe-family.v1", "status": "passed", "checks": checks, "states": STATES, "probes": PROBES, "deletion_witnesses": deletion_witnesses, "injective_subsets": [subset for subset, injective in subset_results.items() if injective], "claim_boundary": "Minimal only among four declared probes on the twelve-state path/polarization quotient."}
output = Path(__file__).parents[1] / "results" / "minimal_optical_probe_family.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "state_count": len(STATES), "minimal_probe_count": len(PROBES)}, sort_keys=True))
