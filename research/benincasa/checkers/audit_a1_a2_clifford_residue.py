#!/usr/bin/env python3
"""Derive the A1 plus A2 Clifford metric and cyclic bivector orbit."""

import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def quadratic(vector, gram):
    return sum(vector[i] * gram[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector)))


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


C = [[2, -1], [-1, 2]]
R = [[0, -1], [1, -1]]
identity2 = [[1, 0], [0, 1]]

Q = [[2, 0, 0], [0, 2, -1], [0, -1, 2]]
T = [[1, 0, 0], [0, 0, -1], [0, 1, -1]]
identity3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Source-labelled root alpha_32 in the basis (alpha_12,alpha_23).
root0 = [0, -1]
root1 = matvec(R, root0)
root2 = matvec(R, root1)
root3 = matvec(R, root2)

# A row cross term c between the fixed A1 line and A2 must obey cR=c.
cross_invariance_matrix = [
    [R[0][0] - 1, R[0][1]],
    [R[1][0], R[1][1] - 1],
]

# Invariance equations for S=[[a,b],[b,d]] under R^T S R=S.
symmetric_basis = [
    [[1, 0], [0, 0]],
    [[0, 1], [1, 0]],
    [[0, 0], [0, 1]],
]
invariance_columns = []
for basis in symmetric_basis:
    defect = matmul(matmul(transpose(R), basis), R)
    defect = [[defect[i][j] - basis[i][j] for j in range(2)] for i in range(2)]
    invariance_columns.append([defect[0][0], defect[0][1], defect[1][1]])
invariance_system = [list(row) for row in zip(*invariance_columns)]

hostile_cross = [1, 0]
hostile_cross_defect = [
    sum(hostile_cross[k] * R[k][j] for k in range(2)) - hostile_cross[j]
    for j in range(2)
]

checks = {
    "cyclic_order_three": matmul(matmul(R, R), R) == identity2,
    "a2_cartan_form_is_preserved": matmul(matmul(transpose(R), C), R) == C,
    "global_metric_is_preserved": matmul(matmul(transpose(T), Q), T) == Q,
    "global_transport_has_order_three": matmul(matmul(T, T), T) == identity3,
    "cross_metric_is_forced_zero": rank(cross_invariance_matrix) == 2,
    "a2_invariant_symmetric_forms_are_one_dimensional": rank(invariance_system) == 2,
    "root_orbit_closes": root3 == root0,
    "root_orbit_sums_to_zero": [root0[i] + root1[i] + root2[i] for i in range(2)] == [0, 0],
    "all_roots_have_norm_two": [quadratic(root, C) for root in [root0, root1, root2]] == [2, 2, 2],
    "all_relational_bivectors_square_to_minus_four": [-2 * quadratic(root, C) for root in [root0, root1, root2]] == [-4, -4, -4],
    "hostile_nonzero_cross_term_fails_invariance": hostile_cross_defect != [0, 0],
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.a1_a2_clifford_residue.v1",
    "space": "V=A1_Leray direct_sum A2_soft",
    "gram_matrix": Q,
    "cyclic_transport": T,
    "a2_cartan": C,
    "a2_cyclic_action": R,
    "root_orbit": [root0, root1, root2],
    "bivector_orbit": ["f*alpha_32", "f*sigma(alpha_32)", "f*sigma^2(alpha_32)"],
    "bivector_squares": [-4, -4, -4],
    "hostile_cross_term": hostile_cross,
    "hostile_cross_invariance_defect": hostile_cross_defect,
    "checks": checks,
    "verdict": (
        "The source root lattices and cyclic action force the orthogonal "
        "A1 plus A2 metric up to the already fixed primitive root norms. The "
        "three Leray-soft relational residues form a cyclic A2 bivector orbit "
        "in the resulting rank-three Clifford algebra; they do not collapse "
        "to a cyclic-trivial scalar line."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "a1_a2_clifford_residue.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
