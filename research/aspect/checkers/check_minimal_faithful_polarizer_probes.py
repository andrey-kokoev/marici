#!/usr/bin/env python3
"""Exact finite search for minimal faithful polarizer probe families."""

import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

STATES = (0, 45, 90, 135)
PROBES = (0, 45, 90, 135)
MALUS = {0: Q(1), 45: Q(1, 2), 90: Q(0), 135: Q(1, 2)}


def record(theta, phi):
    return MALUS[(theta - phi) % 180]


def coordinate(family, phi):
    return tuple(record(theta, phi) for theta in family)


def fibers(family):
    result = {}
    for phi in STATES:
        result.setdefault(coordinate(family, phi), []).append(phi)
    return result


def faithful(family):
    return len(fibers(family)) == len(STATES)


families = {}
for size in range(1, len(PROBES) + 1):
    for family in combinations(PROBES, size):
        families[str(family)] = {
            "size": size,
            "faithful": faithful(family),
            "fibers": {str(tuple(str(x) for x in key)): value for key, value in fibers(family).items()},
        }

faithful_families = [family for size in range(1, 5) for family in combinations(PROBES, size) if faithful(family)]
minimal_size = min(len(family) for family in faithful_families)
minimal_families = [family for family in faithful_families if len(family) == minimal_size]
singletons = list(combinations(PROBES, 1))
opposite_pairs = {(0, 90), (45, 135)}
nonopposite_pairs = set(combinations(PROBES, 2)) - opposite_pairs

checks = {
    "every_single_probe_is_nonfaithful": all(not faithful(family) for family in singletons),
    "every_single_probe_has_multiplicity_two_fiber": all(max(map(len, fibers(family).values())) == 2 for family in singletons),
    "minimal_faithful_depth_is_two": minimal_size == 2,
    "adjacent_example_is_faithful": faithful((0, 45)),
    "opposite_pairs_are_nonfaithful": all(not faithful(family) for family in opposite_pairs),
    "all_nonopposite_pairs_are_faithful": all(faithful(family) for family in nonopposite_pairs),
    "removing_probe_from_minimal_family_restores_ambiguity": all(
        not faithful((theta,)) for family in minimal_families for theta in family
    ),
    "finite_quotient_already_mods_out_180_degree_equivalence": all(phi < 180 for phi in STATES),
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.minimal-faithful-polarizer-probes.v1",
    "status": "passed",
    "checks": checks,
    "states": STATES,
    "candidate_probes": PROBES,
    "minimal_depth": minimal_size,
    "minimal_families": minimal_families,
    "opposite_nonfaithful_pairs": sorted(opposite_pairs),
    "families": families,
    "claim_boundary": "Finite four-state ideal-polarization quotient only."
}
output = Path(__file__).parents[1] / "results" / "minimal_faithful_polarizer_probes.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "minimal_depth": minimal_size, "minimal_family_count": len(minimal_families), "checks": checks}, sort_keys=True))
