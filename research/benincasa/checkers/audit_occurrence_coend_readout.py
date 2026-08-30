#!/usr/bin/env python3
"""Compute the balanced occurrence coend and its universal scalar readout."""

import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matsub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def flatten(matrix):
    return [entry for row in matrix for entry in row]


def outer(column, row):
    return [[column[i] * row[j] for j in range(len(row))] for i in range(len(column))]


def rank(vectors):
    if not vectors:
        return 0
    work = [[Fraction(value) for value in vector] for vector in vectors]
    rows = len(work)
    cols = len(work[0])
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
        if pivot_row == rows:
            break
    return pivot_row


def matrix_basis():
    basis = []
    for i in range(3):
        for j in range(3):
            matrix = [[0, 0, 0] for _ in range(3)]
            matrix[i][j] = 1
            basis.append(matrix)
    return basis


def commutator_relations(generators):
    return [
        flatten(matsub(matmul(x, generator), matmul(generator, x)))
        for generator in generators
        for x in matrix_basis()
    ]


def algebra_rank(generators):
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    words = [identity] + [generator for generator in generators]
    previous = -1
    while rank([flatten(word) for word in words]) != previous:
        previous = rank([flatten(word) for word in words])
        snapshot = list(words)
        words.extend(matmul(left, right) for left in snapshot for right in generators)
    return rank([flatten(word) for word in words])


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
S = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
F = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

families = {
    "cyclic_only": [P],
    "cyclic_plus_incidence": [P, F],
    "support_only": [S],
    "cyclic_plus_one_support": [P, S],
    "complete_declared_packet": [P, S, F],
}

census = {}
for name, generators in families.items():
    relation_rank = rank(commutator_relations(generators))
    census[name] = {
        "relation_rank": relation_rank,
        "coend_dimension": 9 - relation_rank,
        "generated_algebra_rank": algebra_rank(generators),
    }

trace_covector = [1, 0, 0, 0, 1, 0, 0, 0, 1]
complete_relations = commutator_relations(families["complete_declared_packet"])
trace_defects = [sum(trace_covector[i] * relation[i] for i in range(9)) for relation in complete_relations]

b = [0, -1, 1]
d = [0, -1, 1]
pair_matrix = outer(b, d)
pair_trace = sum(pair_matrix[i][i] for i in range(3))

checks = {
    "cyclic_transport_alone_leaves_three_readout_channels": census["cyclic_only"]["coend_dimension"] == 3,
    "incidence_adds_no_generator_beyond_cyclic_transport": census["cyclic_plus_incidence"]["coend_dimension"] == 3,
    "one_support_map_with_cyclic_transport_generates_full_matrix_algebra": census["cyclic_plus_one_support"]["generated_algebra_rank"] == 9,
    "one_support_map_reduces_balanced_readout_to_one_dimension": census["cyclic_plus_one_support"]["coend_dimension"] == 1,
    "complete_packet_has_one_dimensional_coend": census["complete_declared_packet"]["coend_dimension"] == 1,
    "trace_annihilates_every_balance_relation": all(value == 0 for value in trace_defects),
    "source_pair_maps_to_nonzero_universal_scalar": pair_trace == 2,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.occurrence_coend_readout.v1",
    "balance_relation": "X f is identified with f X, where X=b tensor d",
    "families": families,
    "census": census,
    "universal_quotient_covector": trace_covector,
    "trace_relation_defects": trace_defects,
    "source_pair_matrix": pair_matrix,
    "source_pair_universal_scalar": pair_trace,
    "checks": checks,
    "verdict": (
        "Cyclic transport alone leaves three balanced readout channels. Adding "
        "one independently declared route-support map generates the full 3 by 3 "
        "matrix algebra and reduces the balanced coend to the unique trace line. "
        "The matched source instrument-residue pair maps to scalar 2."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "occurrence_coend_readout.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
