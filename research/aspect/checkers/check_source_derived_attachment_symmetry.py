#!/usr/bin/env python3
"""Finite source-versus-downstream attachment symmetry diagnostic."""

import itertools
import json
from pathlib import Path

VERTICES = (0, 1)
PERMUTATIONS = tuple(itertools.permutations(VERTICES))
EDGE = frozenset({0, 1})
STATES = tuple(itertools.product((0, 1), repeat=2))
MATCHING = tuple(state for state in STATES if state[0] == state[1])


def apply_permutation(permutation, vertex):
    return permutation[vertex]


def compose(first, second):
    return tuple(apply_permutation(first, apply_permutation(second, vertex)) for vertex in VERTICES)


def permute_state(permutation, state):
    result = [None, None]
    for source_vertex in VERTICES:
        result[apply_permutation(permutation, source_vertex)] = state[source_vertex]
    return tuple(result)


def source_automorphisms(labels):
    admitted = []
    for permutation in PERMUTATIONS:
        labels_preserved = all(labels[vertex] == labels[apply_permutation(permutation, vertex)] for vertex in VERTICES)
        edge_preserved = frozenset(apply_permutation(permutation, vertex) for vertex in EDGE) == EDGE
        if labels_preserved and edge_preserved:
            admitted.append(permutation)
    return tuple(admitted)


def constraint_automorphisms():
    return tuple(permutation for permutation in PERMUTATIONS if {permute_state(permutation, state) for state in MATCHING} == set(MATCHING))


IDENTITY = (0, 1)
SWAP = (1, 0)
symmetric_source = source_automorphisms(("detector", "detector"))
asymmetric_source = source_automorphisms(("source", "detector"))
downstream = constraint_automorphisms()
checks = {
    "two_permutations_enumerated": len(PERMUTATIONS) == 2,
    "symmetric_source_admits_identity_and_swap": set(symmetric_source) == {IDENTITY, SWAP},
    "swap_squares_to_identity": compose(SWAP, SWAP) == IDENTITY,
    "swap_preserves_matching_object": {permute_state(SWAP, state) for state in MATCHING} == set(MATCHING),
    "swap_is_bijective_on_matching_object": len({permute_state(SWAP, state) for state in MATCHING}) == len(MATCHING),
    "asymmetric_source_admits_only_identity": asymmetric_source == (IDENTITY,),
    "downstream_constraint_still_admits_swap": SWAP in downstream,
    "downstream_symmetry_exceeds_asymmetric_source_symmetry": set(downstream) - set(asymmetric_source) == {SWAP},
    "algebraic_swap_is_rejected_without_source_preimage": SWAP not in asymmetric_source and SWAP in downstream,
    "source_authorized_actions_preserve_constraints": all(permutation in downstream for permutation in symmetric_source),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.source-derived-attachment-symmetry.v1", "status": "passed", "checks": checks, "symmetric_source_automorphisms": symmetric_source, "asymmetric_source_automorphisms": asymmetric_source, "constraint_automorphisms": downstream, "matching_states": MATCHING, "claim_boundary": "Finite labelled-source witness; downstream permutation invariance alone is not symmetry authority."}
output = Path(__file__).parents[1] / "results" / "source_derived_attachment_symmetry.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "symmetric_source_group_size": len(symmetric_source), "asymmetric_source_group_size": len(asymmetric_source), "downstream_group_size": len(downstream)}, sort_keys=True))
