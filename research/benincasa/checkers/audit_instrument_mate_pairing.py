#!/usr/bin/env python3
"""Audit the balanced instrument pairing for invertible and support maps."""

import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def rowvec(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(len(vector))) for j in range(len(matrix[0]))]


def dot(left, right):
    return sum(left[i] * right[i] for i in range(len(left)))


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matsub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


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


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
S = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
F = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
D = transpose(F)

basis_states = [[0, -1, 1], [1, 0, -1], [-1, 1, 0], [2, -3, 5]]
basis_instruments = [[0, -1, 1], [1, 1, 1], [2, 0, -1], [-4, 3, 2]]
maps = {"cyclic_automorphism": P, "route_support": S, "forward_incidence": F}

mate_defects = {}
for name, morphism in maps.items():
    defects = []
    for detector in basis_instruments:
        for state in basis_states:
            # Covariant transport is f_* b = f b.  Contravariant transport is
            # precomposition f^* d = d f.  No inverse is required.
            defects.append(dot(rowvec(detector, morphism), state) - dot(detector, matvec(morphism, state)))
    mate_defects[name] = defects

# Functoriality for the composable pair S then P.
composite = matmul(P, S)
state = [2, -3, 5]
detector = [-4, 3, 2]
covariant_one_step = matvec(composite, state)
covariant_two_step = matvec(P, matvec(S, state))
contravariant_one_step = rowvec(detector, composite)
contravariant_two_step = rowvec(rowvec(detector, P), S)

# Entry 3385's support-sensitive comparison remains nonzero even though the
# evaluation mate is exact.  Balanced readout and Beck-Chevalley compatibility
# are therefore different conditions.
supported_forward = matmul(F, S)
supported_backward = matmul(S, D)
supported_commutator = matsub(
    matmul(supported_forward, supported_backward),
    matmul(supported_backward, supported_forward),
)

matched_state = [0, -1, 1]
matched_detector = [0, -1, 1]
supported_readout_left = dot(rowvec(matched_detector, S), matched_state)
supported_readout_right = dot(matched_detector, matvec(S, matched_state))

checks = {
    "mate_identity_holds_for_automorphism": all(value == 0 for value in mate_defects["cyclic_automorphism"]),
    "mate_identity_holds_for_noninvertible_support": all(value == 0 for value in mate_defects["route_support"]),
    "mate_identity_holds_for_incidence_map": all(value == 0 for value in mate_defects["forward_incidence"]),
    "covariant_transport_is_functorial": covariant_one_step == covariant_two_step,
    "contravariant_transport_reverses_composition": contravariant_one_step == contravariant_two_step,
    "route_support_is_genuinely_noninvertible": rank(S) == 2,
    "supported_readout_is_balanced_and_nonzero": supported_readout_left == supported_readout_right == 1,
    "supported_backward_forward_comparison_still_fails": rank(supported_commutator) == 3,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.instrument_mate_pairing.v1",
    "covariant_rule": "f_* b = f b",
    "contravariant_rule": "f^* d = d f",
    "balanced_identity": "(d f)(b) = d(f b)",
    "maps": maps,
    "mate_defects": mate_defects,
    "composite": composite,
    "covariant_one_step": covariant_one_step,
    "covariant_two_step": covariant_two_step,
    "contravariant_one_step": contravariant_one_step,
    "contravariant_two_step": contravariant_two_step,
    "supported_readout": supported_readout_left,
    "supported_backward_forward_commutator": supported_commutator,
    "supported_backward_forward_commutator_rank": rank(supported_commutator),
    "checks": checks,
    "verdict": (
        "Instrument evaluation is the exact mate pairing between contravariant "
        "precomposition and covariant transport, including for a noninvertible "
        "route-support map.  This balanced pairing can remain exact while the "
        "supported backward-forward comparison has a full-rank defect."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "instrument_mate_pairing.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
