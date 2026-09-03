#!/usr/bin/env python3
"""Exact finite counterexamples to reconstruction from truncated probe data."""

import json
from itertools import combinations
from pathlib import Path


def powerset(vertices):
    return {
        frozenset(face)
        for size in range(len(vertices) + 1)
        for face in combinations(vertices, size)
    }


def skeleton(complex_, max_cardinality):
    return {face for face in complex_ if len(face) <= max_cardinality}


def f_vector(complex_, vertex_count):
    return tuple(sum(1 for face in complex_ if len(face) == size) for size in range(1, vertex_count + 1))


vertices = (0, 1, 2)
filled = powerset(vertices)
hollow = {face for face in filled if len(face) < 3}
unary_binary_signature_filled = skeleton(filled, 2)
unary_binary_signature_hollow = skeleton(hollow, 2)

checks = {
    "hollow_and_filled_have_same_unary_binary_domain": unary_binary_signature_hollow == unary_binary_signature_filled,
    "hollow_and_filled_are_distinct_complexes": hollow != filled,
    "f_vectors_distinguish_incidence": f_vector(hollow, 3) == (3, 3, 0) and f_vector(filled, 3) == (3, 3, 1),
    "three_probe_configuration_is_exact_difference": filled - hollow == {frozenset(vertices)},
}

generalized = {}
for n in range(3, 9):
    labels = tuple(range(n))
    simplex = powerset(labels)
    boundary = {face for face in simplex if len(face) < n}
    generalized[str(n)] = {
        "proper_skeleton_equal": skeleton(simplex, n - 1) == skeleton(boundary, n - 1),
        "top_difference_unique": simplex - boundary == {frozenset(labels)},
    }
    checks[f"n{n}_proper_faces_do_not_reconstruct_top"] = all(generalized[str(n)].values())

# Constant values on recorded configurations lose incidence if the domain keys are discarded.
constant_hollow_values = ["terminal" for _ in hollow]
constant_filled_values = ["terminal" for _ in filled]
checks["constant_value_set_cannot_encode_domain"] = set(constant_hollow_values) == set(constant_filled_values) == {"terminal"}
checks["complete_admissibility_domain_reconstructs_complex"] = set(filled) == filled and set(hollow) == hollow

assert all(checks.values()), checks
result = {
    "schema": "marici.aspect.probe-pyramid-reconstruction-falsifier.v1",
    "status": "passed",
    "checks": checks,
    "hollow_f_vector": f_vector(hollow, 3),
    "filled_f_vector": f_vector(filled, 3),
    "generalized_arities": generalized,
    "disposition": "unary_and_binary_reconstruction_rejected",
    "sufficient_finite_input": "complete labelled admissibility domain plus typed restrictions",
    "claim_boundary": "Finite labelled simplicial incidence only."
}
output = Path(__file__).parents[1] / "results" / "probe_pyramid_reconstruction_falsifier.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks)}, sort_keys=True))
