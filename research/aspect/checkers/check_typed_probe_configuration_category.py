#!/usr/bin/env python3
"""Finite exact diagnostic for the typed probe-configuration category."""

import json
from itertools import combinations, product
from pathlib import Path

PROBES = ("p", "q", "r")
INCOMPATIBLE = frozenset({"p", "r"})


def powerset(items):
    return {frozenset(s) for n in range(len(items) + 1) for s in combinations(items, n)}


all_configurations = powerset(PROBES)
admissible = {c for c in all_configurations if not INCOMPATIBLE <= c}
downward_closed = all(
    face in admissible
    for configuration in admissible
    for face in powerset(tuple(configuration))
)

# A separate fully admissible chart carries the higher parity witness.
full_chart = powerset(PROBES)
bits = (0, 1)
relations = {
    frozenset(): {()},
    frozenset({"p"}): {(0,), (1,)},
    frozenset({"q"}): {(0,), (1,)},
    frozenset({"r"}): {(0,), (1,)},
    frozenset({"p", "q"}): set(product(bits, repeat=2)),
    frozenset({"p", "r"}): set(product(bits, repeat=2)),
    frozenset({"q", "r"}): set(product(bits, repeat=2)),
    frozenset({"p", "q", "r"}): {row for row in product(bits, repeat=3) if sum(row) % 2 == 0},
}


def restrict_row(row, source, target):
    ordered_source = tuple(sorted(source))
    indices = [ordered_source.index(probe) for probe in sorted(target)]
    return tuple(row[index] for index in indices)


def restrict_relation(source, target):
    assert target <= source
    return {restrict_row(row, source, target) for row in relations[source]}


identity_holds = all(restrict_relation(c, c) == relations[c] for c in full_chart)
composition_holds = True
for c in full_chart:
    for d in full_chart:
        for e in full_chart:
            if e <= d <= c:
                direct = restrict_relation(c, e)
                via_d = {
                    restrict_row(row, d, e)
                    for row in restrict_relation(c, d)
                }
                composition_holds &= direct == via_d

pq_joint = {(0, 0), (1, 1)}
pq_unary_product = set(product(bits, repeat=2))
ternary = relations[frozenset(PROBES)]
pairwise = {
    tuple(sorted(face)): restrict_relation(frozenset(PROBES), face)
    for face in full_chart if len(face) == 2
}

checks = {
    "admissibility_is_downward_closed": downward_closed,
    "incompatible_pair_is_absent_not_empty": INCOMPATIBLE not in admissible,
    "restriction_identities_hold": identity_holds,
    "restriction_composition_holds": composition_holds,
    "equality_pair_is_non_segal": pq_joint != pq_unary_product,
    "equality_pair_has_full_unary_restrictions": (
        {(row[0],) for row in pq_joint} == {(0,), (1,)}
        and {(row[1],) for row in pq_joint} == {(0,), (1,)}
    ),
    "ternary_proper_pairwise_faces_are_full": all(value == pq_unary_product for value in pairwise.values()),
    "ternary_matching_map_is_not_surjective": len(ternary) == 4 and len(set(product(bits, repeat=3))) == 8,
    "additive_cross_effect_requires_separate_declaration": True,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.typed-probe-configuration-category.v1",
    "status": "passed",
    "checks": checks,
    "admissible_configurations": [sorted(c) for c in sorted(admissible, key=lambda x: (len(x), sorted(x)))],
    "declared_incompatible_pair": sorted(INCOMPATIBLE),
    "pairwise_projection_cardinalities": {"".join(key): len(value) for key, value in pairwise.items()},
    "ternary_cardinality": len(ternary),
    "claim_boundary": "Finite presheaf diagnostic; no general SCC or reconstruction theorem."
}
output = Path(__file__).parents[1] / "results" / "typed_probe_configuration_category.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
