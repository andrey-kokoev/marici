#!/usr/bin/env python3
"""Audit the full cyclic family of primitive occurrence observers."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
L = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


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


a2_basis = [[1, -1, 0], [0, 1, -1]]
test_residues = [[0, -1, 1], [1, 0, -1], [-1, 1, 0], [3, -5, 2]]

readout_packets = {str(vector): matvec(L, vector) for vector in test_residues}
reconstructions = {
    key: [Fraction(value, 3) for value in packet]
    for key, packet in readout_packets.items()
}

subset_census = []
for size in range(1, 4):
    for subset in itertools.combinations(range(3), size):
        rows = [L[index] for index in subset]
        restricted = [[sum(row[k] * basis[k] for k in range(3)) for basis in a2_basis] for row in rows]
        subset_census.append(
            {
                "rows": list(subset),
                "size": size,
                "rank_on_a2": rank(restricted),
                "faithful_on_a2": rank(restricted) == 2,
            }
        )

one_row_faithful = [item for item in subset_census if item["size"] == 1 and item["faithful_on_a2"]]
two_row_faithful = [item for item in subset_census if item["size"] == 2 and item["faithful_on_a2"]]

checks = {
    "observer_family_is_cyclic_equivariant": matmul(L, P) == matmul(P, L),
    "observer_family_has_rank_two": rank(L) == 2,
    "observer_family_kernel_is_invariant_line": matvec(L, [1, 1, 1]) == [0, 0, 0],
    "observer_family_is_three_times_identity_on_a2": all(
        matvec(L, vector) == [3 * value for value in vector] for vector in test_residues
    ),
    "one_third_reconstructs_every_tested_residue": all(
        reconstructions[str(vector)] == [Fraction(value) for value in vector]
        for vector in test_residues
    ),
    "no_single_observer_is_faithful_on_a2": not one_row_faithful,
    "every_two_observer_subfamily_is_faithful_on_a2": len(two_row_faithful) == 3,
    "full_three_observer_orbit_is_required_for_cyclic_closure": all(
        matvec(P, [1 if i in subset else 0 for i in range(3)])
        != [1 if i in subset else 0 for i in range(3)]
        for size in [1, 2]
        for subset in itertools.combinations(range(3), size)
    ),
    "invariant_scalar_aggregation_annihilates_all_packets": all(
        sum(packet) == 0 for packet in readout_packets.values()
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.cyclic_occurrence_observer_family.v1",
    "observer_matrix": L,
    "cyclic_transport": P,
    "domain": "A2 occurrence-residue module",
    "codomain": "three labelled scalar observer ports with zero total",
    "readout_packets": readout_packets,
    "reconstructions": {key: [str(value) for value in values] for key, values in reconstructions.items()},
    "subset_census": subset_census,
    "checks": checks,
    "verdict": (
        "The full cyclic orbit of primitive two-port observers is a canonical "
        "rank-two vector-valued readout.  It reconstructs every A2 relational "
        "residue by division by three and requires no support projector or "
        "splitting.  Any two ports are algebraically faithful, but all three "
        "are required for cyclic closure; invariant scalar aggregation remains zero."
    ),
    "scope": (
        "This is a source-normalized algebraic observer family, not an "
        "outcome-bearing physical instrument or apparatus cycle."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "cyclic_occurrence_observer_family.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
