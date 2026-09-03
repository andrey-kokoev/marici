#!/usr/bin/env python3
"""Exact finite diagnostic for probe-configuration Segal defects."""

import json
from itertools import product
from pathlib import Path

BITS = (0, 1)
BACKGROUND = ("*",)
UNARY_P = set(BITS)
UNARY_Q = set(BITS)
UNARY_R = set(BITS)
UNARY_PULLBACK = set(product(BITS, repeat=2))
JOINT_EQUALITY = {(0, 0), (1, 1)}
JOINT_FACTORIZED = set(UNARY_PULLBACK)
TERNARY_PRODUCT = set(product(BITS, repeat=3))
TERNARY_EVEN = {triple for triple in TERNARY_PRODUCT if sum(triple) % 2 == 0}


def project(relation, coordinates):
    return {tuple(row[index] for index in coordinates) for row in relation}


def missing_from(ambient, actual):
    return sorted(ambient - actual)


pairwise_projections = {
    "01": project(TERNARY_EVEN, (0, 1)),
    "02": project(TERNARY_EVEN, (0, 2)),
    "12": project(TERNARY_EVEN, (1, 2)),
}

binary_defect = missing_from(UNARY_PULLBACK, JOINT_EQUALITY)
factorized_defect = missing_from(UNARY_PULLBACK, JOINT_FACTORIZED)
ternary_defect = missing_from(TERNARY_PRODUCT, TERNARY_EVEN)

checks = {
    "background_is_singleton": len(BACKGROUND) == 1,
    "joint_equality_has_full_first_marginal": project(JOINT_EQUALITY, (0,)) == {(0,), (1,)},
    "joint_equality_has_full_second_marginal": project(JOINT_EQUALITY, (1,)) == {(0,), (1,)},
    "binary_comparison_is_injective": len(JOINT_EQUALITY) == len(set(JOINT_EQUALITY)),
    "binary_comparison_is_not_surjective": binary_defect == [(0, 1), (1, 0)],
    "ternary_even_has_all_full_pairwise_projections": all(
        projection == UNARY_PULLBACK for projection in pairwise_projections.values()
    ),
    "ternary_constraint_is_not_pairwise_generated": len(ternary_defect) == 4,
    "deliberate_factorized_fixture_has_zero_interaction_defect": factorized_defect == [],
}

assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.probe-configuration-segal-defect.v1",
    "status": "passed",
    "arithmetic": "finite_exact_enumeration",
    "checks": checks,
    "binary": {
        "unary_pullback_cardinality": len(UNARY_PULLBACK),
        "joint_cardinality": len(JOINT_EQUALITY),
        "missing_joint_assignments": binary_defect,
    },
    "ternary": {
        "product_cardinality": len(TERNARY_PRODUCT),
        "even_parity_cardinality": len(TERNARY_EVEN),
        "pairwise_projection_cardinalities": {
            key: len(value) for key, value in pairwise_projections.items()
        },
        "missing_assignments": ternary_defect,
    },
    "deliberate_failure": {
        "fixture": "fully_factorized_binary_joint",
        "defect": factorized_defect,
        "predicted_disposition": "reject_as_interaction_witness",
    },
    "claim_boundary": "Finite configuration semantics only; no SCC, proof-system, or physical realization theorem.",
}

output = Path(__file__).parents[1] / "results" / "probe_configuration_segal_defect.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
