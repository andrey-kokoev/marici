#!/usr/bin/env python3
"""Verify the cyclic assembly of the universal finite-sextic specializations."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


orbits = load("research/nima/generic-finite-collision-cyclic-orbits.json")
constraint = load("research/nima/higher-specialization-cyclic-constraint.json")
inertia = load("research/nima/higher-sextic-kummer-ramification.json")
local = load("research/benincasa/finite-sextic-higher-vanishing-cycles.json")

assert orbits["orbit_count"] == 8
assert all(o["occurrence_orbit_size"] == 3 for o in orbits["orbits"])
assert all(o["transport_closes"] for o in orbits["orbits"])
assert len(constraint["orbits"]) == 8
assert local["E_zero"]["anti_invariant_vanishing_rank"] == 1
assert local["Lambda_zero"]["anti_invariant_vanishing_rank"] == 1
assert local["intersection"]["iterated_vanishing_rank"] == 1
assert local["intersection"]["reduced_excess_tor_rank"] == 0
assert inertia["local_kummer_monodromy"] == {"E=0": 1, "Lambda=0": -1}

orbit_dimension = 3
aggregate_dimension = orbits["orbit_count"] * orbit_dimension
assert aggregate_dimension == 24

result = {
    "orbit_count": orbits["orbit_count"],
    "rank_per_labelled_occurrence": 1,
    "rank_per_free_orbit": orbit_dimension,
    "aggregate_rank_on_E": aggregate_dimension,
    "aggregate_rank_on_Lambda_transverse": aggregate_dimension,
    "aggregate_rank_at_intersection": aggregate_dimension,
    "C3_character_on_each_stratum": [aggregate_dimension, 0, 0],
    "E_inertia": 1,
    "Lambda_inertia": -1,
    "reduced_excess_rank": 0,
}
print(json.dumps(result, indent=2))
