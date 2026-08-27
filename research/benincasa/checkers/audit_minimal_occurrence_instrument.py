#!/usr/bin/env python3
"""Audit the minimal occurrence-sensitive instrument on the Clifford A2 residue."""

import itertools
import json
from pathlib import Path


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]


def matvec(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def rowvec(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(len(vector))) for j in range(len(vector))]


def dot(left, right):
    return sum(left[i] * right[i] for i in range(len(left)))


def support_size(vector):
    return sum(value != 0 for value in vector)


# Entry 3375's source-labelled relational residue.  The instrument uses the
# same ordered occurrence pair: it compares occurrence 3 against occurrence 2.
b0 = [0, -1, 1]
d0 = [0, -1, 1]

bivectors = [b0]
detectors = [d0]
P_inverse = matmul(P, P)
for _ in range(2):
    bivectors.append(matvec(P, bivectors[-1]))
    # Instruments are dual rows: d maps to d P^{-1}.  In this orthogonal
    # permutation representation the metric-dual column happens to transform
    # by P, which is why the variance distinction was previously hidden.
    detectors.append(rowvec(detectors[-1], P_inverse))

pairing_matrix = [[dot(detector, bivector) for bivector in bivectors] for detector in detectors]
transported_values = [pairing_matrix[i][i] for i in range(3)]
fixed_instrument_values = [dot(d0, bivector) for bivector in bivectors]

# Exhaust the smallest integral search box.  A nonzero A2 covector must have
# at least two nonzero entries; the source-labelled detector attains that bound.
primitive_candidates = [
    list(candidate)
    for candidate in itertools.product([-1, 0, 1], repeat=3)
    if candidate != (0, 0, 0) and sum(candidate) == 0
]
minimum_support = min(support_size(candidate) for candidate in primitive_candidates)
minimum_candidates = [
    candidate for candidate in primitive_candidates if support_size(candidate) == minimum_support
]

invariant_detector = [1, 1, 1]

checks = {
    "instrument_is_a_primitive_occurrence_difference": sum(d0) == 0 and support_size(d0) == 2,
    "two_ports_are_minimal_in_the_integral_a2_dual": minimum_support == 2,
    "source_detector_occurs_in_minimal_orbit": d0 in minimum_candidates,
    "transported_pairing_is_nonzero": all(value != 0 for value in transported_values),
    "transported_pairing_is_chart_independent": transported_values == [2, 2, 2],
    "instrument_transforms_contravariantly": all(
        detectors[(i + 1) % 3] == rowvec(detectors[i], P_inverse)
        for i in range(3)
    ),
    "residue_transforms_covariantly": all(
        bivectors[(i + 1) % 3] == matvec(P, bivectors[i])
        for i in range(3)
    ),
    "balanced_pairing_is_invariant": all(
        dot(rowvec(detectors[i], P_inverse), matvec(P, bivectors[i])) == transported_values[i]
        for i in range(3)
    ),
    "fixed_instrument_is_intentionally_occurrence_sensitive": fixed_instrument_values == [2, -1, -1],
    "cyclic_invariant_detector_remains_blind": [dot(invariant_detector, b) for b in bivectors] == [0, 0, 0],
    "pairing_matrix_is_triangle_cartan_laplacian": pairing_matrix
    == [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]],
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.minimal_occurrence_instrument.v1",
    "source_residue_orbit": bivectors,
    "instrument_orbit": detectors,
    "instrument_variance": "contravariant row: d maps to d P^{-1}",
    "residue_variance": "covariant column: b maps to P b",
    "instrument_semantics": "ordered comparison of two labelled occurrence ports",
    "pairing_matrix": pairing_matrix,
    "transported_scalar_values": transported_values,
    "fixed_instrument_values": fixed_instrument_values,
    "minimal_integral_support": minimum_support,
    "minimal_integral_instruments": minimum_candidates,
    "checks": checks,
    "verdict": (
        "The smallest nonblind algebraic instrument is a primitive two-port "
        "occurrence difference.  Its pairing with the matching Clifford A2 "
        "residue is nonzero and invariant under simultaneous cyclic transport. "
        "A frozen instrument remains occurrence-sensitive, while the cyclic "
        "invariant detector annihilates the relational grade."
    ),
    "scope": (
        "This derives the minimal instrument-residue pairing from the labelled "
        "occurrence lattice.  It does not establish that a physical preparation "
        "or detector realizes this instrument."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "minimal_occurrence_instrument.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
