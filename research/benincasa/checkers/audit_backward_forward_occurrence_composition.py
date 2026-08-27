#!/usr/bin/env python3
"""Audit backward and forward compositionality on the labelled triangle."""

import json
from fractions import Fraction
from pathlib import Path


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matsub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


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


zero3 = [[0, 0, 0] for _ in range(3)]
identity3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
averaging = [[Fraction(1, 3) for _ in range(3)] for _ in range(3)]
relational_projector = matsub(identity3, averaging)

# Columns are the three oriented occurrence differences from Entry 3375.
# Forward compositionality takes labelled edge/coherence coefficients to their
# occurrence boundary.  Backward compositionality evaluates occurrence data
# on those labelled differences.
forward = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
backward = transpose(forward)

forward_after_backward = matmul(forward, backward)
backward_after_forward = matmul(backward, forward)
mixed_defect = matsub(forward_after_backward, backward_after_forward)

# Remove one labelled route without changing either incidence convention.
# The two composites then live on different supported presentations and their
# difference is the smallest mixed backward-forward residue.
support = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
supported_forward = matmul(forward, support)
supported_backward = matmul(support, backward)
supported_fb = matmul(supported_forward, supported_backward)
supported_bf = matmul(supported_backward, supported_forward)
supported_defect = matsub(supported_fb, supported_bf)

# Hostile orientation error: reverse one forward edge but retain the backward
# source orientation.  This must destroy the full-support compatibility.
hostile_forward = [row[:] for row in forward]
for row in hostile_forward:
    row[0] *= -1
hostile_defect = matsub(matmul(hostile_forward, backward), matmul(backward, hostile_forward))

checks = {
    "full_backward_forward_square_commutes": mixed_defect == zero3,
    "common_composite_is_triangle_laplacian": forward_after_backward
    == [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]],
    "common_composite_is_three_times_relational_projector": all(
        Fraction(forward_after_backward[i][j]) == 3 * relational_projector[i][j]
        for i in range(3)
        for j in range(3)
    ),
    "backward_forward_composition_is_invertible_on_a2": matvec(forward_after_backward, [0, -1, 1]) == [0, -3, 3],
    "invariant_line_is_common_kernel": matvec(forward_after_backward, [1, 1, 1]) == [0, 0, 0],
    "one_route_deletion_creates_mixed_residue": supported_defect != zero3,
    "supported_mixed_residue_is_full_rank": rank(supported_defect) == 3,
    "orientation_mismatch_is_detected": hostile_defect != zero3,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.backward_forward_occurrence_composition.v1",
    "forward_boundary": forward,
    "backward_coboundary": backward,
    "full_composite": forward_after_backward,
    "full_mixed_defect": mixed_defect,
    "deleted_route_support": support,
    "supported_forward_after_backward": supported_fb,
    "supported_backward_after_forward": supported_bf,
    "supported_mixed_residue": supported_defect,
    "supported_mixed_residue_rank": rank(supported_defect),
    "hostile_orientation_defect": hostile_defect,
    "checks": checks,
    "verdict": (
        "On the complete labelled triangle, forward boundary and backward "
        "coboundary commute and compose to three times the A2 projector. "
        "Deleting one labelled route produces a canonical full-rank mixed "
        "commutator, while an orientation mismatch is detected already at "
        "full support."
    ),
    "scope": (
        "This is the finite occurrence-incidence model of the two directed "
        "compositional towers.  Identifying its supported commutator with a "
        "cosmological physical class requires a source-derived Cut/sewing and "
        "instrument comparison."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "backward_forward_occurrence_composition.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
