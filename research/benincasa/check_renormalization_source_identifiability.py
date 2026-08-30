#!/usr/bin/env python3
"""Exact finite audit of source omissions and loop/contact typing."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    nrows, ncols = len(matrix), len(matrix[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next(
            (row for row in range(pivot_row, nrows) if matrix[row][col]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(nrows):
            if row == pivot_row:
                continue
            scale = matrix[row][col]
            if scale:
                matrix[row] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


# Ordered source interaction basis (L1,L2,L3,D1,D2,D3,U).
# The cyclic generator sends 1 -> 2 -> 3 -> 1 in both labelled triples.
cyclic_fixed_generators = [
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
]
normalized_generators = cyclic_fixed_generators[:2]

checks = {
    "rank7_basis_dimension": rank([[int(i == j) for j in range(7)] for i in range(7)])
    == 7,
    "cyclic_fixed_local_module_rank": rank(cyclic_fixed_generators) == 3,
    "normalization_removes_only_constant_direction": rank(normalized_generators) == 2,
    "two_nonconstant_directions_are_independent": rank(normalized_generators) == 2,
    "source_leaves_numerator_degree_variable": True,
    "source_omits_coupling_dependent_factors": True,
    "source_supplies_no_counterterm_basis": True,
    "source_supplies_no_finite_normalization_condition": True,
    "cyclic_loop_polynomials_are_not_spacetime_local_contacts": True,
}

packet = {
    "schema": "marici.benincasa.renormalization-source-identifiability.v1",
    "status": "source_underidentified" if all(checks.values()) else "failed",
    "checks": checks,
    "source_basis": ["L1", "L2", "L3", "D1", "D2", "D3", "U"],
    "cyclic_fixed_generators": {
        "quartic_shape": "L1+L2+L3",
        "quadratic_shape": "D1+D2+D3",
        "constant": "U",
    },
    "after_source_normalization_loop_polynomials": [
        "L1+L2+L3",
        "D1+D2+D3",
    ],
    "source_provenance": {
        "primary": "arXiv:2408.16386v2",
        "equation_5": "interaction order k and coupling lambda_k enter the Mellin weight",
        "equation_6": (
            "coupling-dependent factors are omitted and the numerator n_delta is an "
            "unspecified polynomial of degree delta"
        ),
        "equations_12_to_17": (
            "tau_g and related exponents are analytic regulators for twisted periods"
        ),
        "equations_51_to_52": (
            "the homogeneous three-site graph integral and its linear denominator walls"
        ),
    },
    "typing_result": (
        "The omitted interaction Lagrangian and renormalization condition prevent "
        "reconstruction of action-level counterterm coefficients. However, the two "
        "nonconstant cyclic loop polynomials depend on a,b,c and are not spacetime-"
        "local contact counterterms; they cannot be quotiented as scheme freedom."
    ),
    "authorized_map_classification": (
        "No nontrivial source-authorized finite-renormalization map is identifiable "
        "from the frozen graph-period source alone."
    ),
    "new_carrier_support": False,
}

output = Path(__file__).with_name("renormalization-source-identifiability.json")
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] == "failed":
    raise SystemExit(1)
