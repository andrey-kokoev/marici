#!/usr/bin/env python3
"""Exact stabilizer of the labelled integral magnetic constructor packet."""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

labels = {name: source[name] for name in ("C", "X", "Z", "Yneg")}


def coefficient_row(matrix, i, j):
    row = [Fraction(0) for _ in range(16)]
    for k in range(4):
        row[4 * i + k] += matrix[k][j]
        row[4 * k + j] -= matrix[i][k]
    return row


def nullspace(matrix):
    a = [row[:] for row in matrix if any(row)]
    pivots = []
    column = 0
    for target_row in range(len(a)):
        while column < 16:
            pivot = next((r for r in range(target_row, len(a)) if a[r][column]), None)
            if pivot is not None:
                break
            column += 1
        if column == 16:
            break
        a[target_row], a[pivot] = a[pivot], a[target_row]
        scale = a[target_row][column]
        a[target_row] = [x / scale for x in a[target_row]]
        for r in range(len(a)):
            if r != target_row and a[r][column]:
                scale = a[r][column]
                a[r] = [x - scale * y for x, y in zip(a[r], a[target_row])]
        pivots.append(column)
        column += 1
    free = [c for c in range(16) if c not in pivots]
    answer = []
    for c in free:
        vector = [Fraction(0) for _ in range(16)]
        vector[c] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = -a[r][c]
        answer.append(vector)
    return answer


equations = [
    coefficient_row(matrix, i, j)
    for matrix in labels.values()
    for i in range(4)
    for j in range(4)
]
basis_vectors = nullspace(equations)
basis = [
    [vector[4 * i:4 * i + 4] for i in range(4)]
    for vector in basis_vectors
]
identity = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


identity_index = next((i for i, matrix in enumerate(basis) if matrix == identity), None)
other_index = next(i for i in range(len(basis)) if i != identity_index)
K = basis[other_index]
N = subtract(K, identity)
zero = [[Fraction(0) for _ in range(4)] for _ in range(4)]
gauge_vector = [Fraction(1) for _ in range(4)]
relational_projection = [
    [Fraction(int(i == j) - int(j == 3)) for j in range(4)]
    for i in range(3)
]
projection_times_N = [
    [sum(relational_projection[i][k] * N[k][j] for k in range(4)) for j in range(4)]
    for i in range(3)
]
sample_unimodular = True
for a in range(-5, 6):
    U = [[identity[i][j] + a * N[i][j] for j in range(4)] for i in range(4)]
    Ui = [[identity[i][j] - a * N[i][j] for j in range(4)] for i in range(4)]
    sample_unimodular &= multiply(U, Ui) == identity

gates = {
    "labelled_packet_rational_centralizer_has_dimension_two": len(basis) == 2,
    "extra_generator_is_square_zero_gauge_shear": multiply(N, N) == zero,
    "gauge_shear_image_is_common_gauge_line": all(row == N[0] for row in N),
    "gauge_shear_kills_common_gauge_vector": all(
        sum(N[i][j] * gauge_vector[j] for j in range(4)) == 0
        for i in range(4)
    ),
    "relational_projection_kills_gauge_shear": all(
        x == 0 for row in projection_times_N for x in row
    ),
    "sampled_integral_shears_are_unimodular": sample_unimodular,
}

payload = {
    "schema": "marici.strominger.labelled_constructor_stabilizer_checks.v2",
    "status": "passed" if all(gates.values()) else "failed",
    "labels": list(labels),
    "rational_centralizer_dimension": len(basis),
    "rational_centralizer_basis": [
        [[str(x) for x in row] for row in matrix]
        for matrix in basis
    ],
    "square_zero_generator_N": [[str(x) for x in row] for row in N],
    "integral_stabilizer_family": "epsilon I_4 + a N, epsilon in {+1,-1}, a in Z",
    "relational_projection_times_N": [
        [str(x) for x in row] for row in projection_times_N
    ],
    "interpretation": (
        "The complete labelled packet retains one non-scalar natural automorphism: "
        "a square-zero shear into the common gauge line. Its entire integral "
        "one-parameter family is unimodular and the relational quotient kills it."
    ),
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
