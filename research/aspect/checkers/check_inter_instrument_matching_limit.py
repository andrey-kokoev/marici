#!/usr/bin/env python3
"""Finite matching-limit diagnostic for inter-instrument coherence."""

import itertools
import json
from pathlib import Path

OCCURRENCES = ("A", "B", "C")
EDGES = (("A", "B"), ("B", "C"), ("C", "A"))
LOCAL_FAMILIES = tuple(itertools.product((0, 1), repeat=len(OCCURRENCES)))


def assignment(family):
    return dict(zip(OCCURRENCES, family))


def matches(family, edges=EDGES):
    values = assignment(family)
    return all(values[left] == values[right] for left, right in edges)


def rotate(family):
    values = assignment(family)
    return values["C"], values["A"], values["B"]


MATCHING = tuple(family for family in LOCAL_FAMILIES if matches(family))
TRUNCATED = tuple(family for family in LOCAL_FAMILIES if matches(family, (("A", "B"),)))
HOSTILE = (0, 0, 1)
rotated_matching = tuple(rotate(family) for family in MATCHING)
checks = {
    "occurrences_are_distinct": len(set(OCCURRENCES)) == 3,
    "local_product_has_eight_points": len(LOCAL_FAMILIES) == 8,
    "full_matching_limit_has_two_points": len(MATCHING) == 2,
    "matching_points_are_constant_families": set(MATCHING) == {(0, 0, 0), (1, 1, 1)},
    "local_admissibility_does_not_imply_coherence": HOSTILE in LOCAL_FAMILIES and HOSTILE not in MATCHING,
    "truncated_incidence_accepts_hostile_family": HOSTILE in TRUNCATED,
    "full_incidence_rejects_hostile_family": not matches(HOSTILE),
    "cyclic_rewrite_preserves_matching_set": set(rotated_matching) == set(MATCHING),
    "cyclic_rewrite_is_bijective_on_matching_set": len(set(rotated_matching)) == len(MATCHING),
    "every_declared_edge_is_tested": len(EDGES) == 3 and all(any(left in edge and right in edge for edge in EDGES) for left, right in EDGES),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.inter-instrument-matching-limit.v1", "status": "passed", "checks": checks, "occurrences": OCCURRENCES, "edges": EDGES, "matching_points": MATCHING, "hostile_family": HOSTILE, "truncated_matching_size": len(TRUNCATED), "claim_boundary": "Finite equality-constraint limit; no physical simultaneity, interaction, or realizability theorem."}
output = Path(__file__).parents[1] / "results" / "inter_instrument_matching_limit.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "local_size": len(LOCAL_FAMILIES), "matching_size": len(MATCHING)}, sort_keys=True))
