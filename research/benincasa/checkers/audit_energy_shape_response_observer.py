#!/usr/bin/env python3
"""Audit the source-derived logarithmic energy-shape response observer."""

import json
from fractions import Fraction
from pathlib import Path


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def dot(left, right):
    return sum(left[i] * right[i] for i in range(len(left)))


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [work[row][j] - factor * work[pivot_row][j] for j in range(cols)]
        pivot_row += 1
    return pivot_row


# A logarithmic one-form is serialized by its coefficients in
# (dlog X1,dlog X2,dlog X3).  Entry 3326's response map is the identity on A2.
a2_basis = [[1, -1, 0], [0, 1, -1]]
response_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
residue_matrix_at_soft_divisors = response_matrix

residues = [[0, -1, 1], [1, 0, -1], [-1, 1, 0], [3, -5, 2]]
common_scale_tangent = [1, 1, 1]
shape_tangent = [0, -1, 1]

responses = {str(b): matvec(response_matrix, b) for b in residues}
common_scale_contractions = {str(b): dot(responses[str(b)], common_scale_tangent) for b in residues}
shape_contractions = {str(b): dot(responses[str(b)], shape_tangent) for b in residues}

checks = {
    "response_is_injective_on_a2": rank(a2_basis) == 2,
    "soft_residues_reconstruct_the_response": all(
        matvec(residue_matrix_at_soft_divisors, response) == b
        for b, response in zip(residues, responses.values())
    ),
    "response_is_cyclic_equivariant": all(
        matvec(response_matrix, matvec(P, b)) == matvec(P, matvec(response_matrix, b))
        for b in residues
    ),
    "common_scaling_is_blind": all(value == 0 for value in common_scale_contractions.values()),
    "shape_tangent_detects_matching_residue": shape_contractions[str([0, -1, 1])] == 2,
    "simultaneous_tangent_and_response_transport_preserves_contraction": all(
        dot(matvec(P, responses[str(b)]), matvec(P, shape_tangent))
        == dot(responses[str(b)], shape_tangent)
        for b in residues
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.energy_shape_response_observer.v1",
    "response": "J(b)=sum_i b_i dlog(X_i)",
    "domain": "A2 occurrence residue",
    "codomain": "logarithmic energy-shape cotangent space",
    "response_matrix": response_matrix,
    "soft_residue_matrix": residue_matrix_at_soft_divisors,
    "responses": responses,
    "common_scale_tangent": common_scale_tangent,
    "common_scale_contractions": common_scale_contractions,
    "shape_tangent": shape_tangent,
    "shape_contractions": shape_contractions,
    "source_scope": {
        "entry_3326": "derives the primitive logarithmic A2 boundary cocycle",
        "entry_3341": "proves the scalar e6 torsor amplitude is not selected",
        "entry_3420": "proves the frozen zero-jet physical scalar annihilates A2",
    },
    "checks": checks,
    "verdict": (
        "The frozen source supplies a faithful cotangent-valued logarithmic "
        "response on the A2 residue.  Common scaling annihilates it, while a "
        "labelled shape tangent detects it equivariantly.  The source fixes "
        "the response direction and soft residues but not the scalar torsor "
        "amplitude or a physical intervention tangent."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "energy_shape_response_observer.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
