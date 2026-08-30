#!/usr/bin/env python3
"""Audit cyclic equivariance of the Clifford bivector and e6 difference modules."""

import json
from fractions import Fraction
from pathlib import Path


P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
identity3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def dot(left, right):
    return sum(left[i] * right[i] for i in range(len(left)))


b0 = [0, -1, 1]
b1 = matvec(P, b0)
b2 = matvec(P, b1)
b3 = matvec(P, b2)
bivector_orbit = [b0, b1, b2]

# The coefficient realization is the identity between the source-labelled A2
# bivector differences and the e6 occurrence-difference submodule.
rho = identity3

source_weight = -2
target_weight = -2
cycle_scales = [Fraction(2), Fraction(3), Fraction(1, 6)]
cycle_factor = Fraction(1)
for scale in cycle_scales:
    cycle_factor *= scale**source_weight

invariant_detector = [1, 1, 1]
detector_values = [dot(invariant_detector, vector) for vector in bivector_orbit]

# Deliberate hostile convention: assign the source bivector the inverse weight.
hostile_source_weight = 2
hostile_scale = Fraction(2)
hostile_weight_defect = hostile_scale**hostile_source_weight - hostile_scale**target_weight

checks = {
    "cyclic_action_has_order_three": matmul(matmul(P, P), P) == identity3,
    "bivector_orbit_closes": b3 == b0,
    "bivector_orbit_sum_zero": [sum(vector[i] for vector in bivector_orbit) for i in range(3)] == [0, 0, 0],
    "realization_intertwines_cyclic_transport": matmul(rho, P) == matmul(P, rho),
    "source_and_target_homogeneities_match": source_weight == target_weight,
    "threefold_weighted_transport_is_identity": cycle_factor == 1,
    "cyclic_invariant_detector_annihilates_relational_grade": detector_values == [0, 0, 0],
    "hostile_inverse_weight_has_nonzero_defect": hostile_weight_defect != 0,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.clifford_e6_cyclic_equivariance.v1",
    "cyclic_permutation": P,
    "source_bivector_orbit": bivector_orbit,
    "target": "A2 occurrence-difference submodule of the three e6 chart lines",
    "realization": rho,
    "source_homogeneity": source_weight,
    "target_homogeneity": target_weight,
    "cycle_scales": [str(value) for value in cycle_scales],
    "cycle_factor": str(cycle_factor),
    "invariant_detector": invariant_detector,
    "detector_values": detector_values,
    "hostile_inverse_weight_defect_at_scale_2": str(hostile_weight_defect),
    "checks": checks,
    "verdict": (
        "The source-derived Clifford bivector orbit maps equivariantly to the "
        "A2 occurrence-difference part of the e6 bridge system. Matching weight "
        "minus two and positive cyclic orientations close the three-chart "
        "square. The cyclic-invariant physical detector annihilates this "
        "relational grade, so activation requires an occurrence-sensitive "
        "instrument relation."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "clifford_e6_cyclic_equivariance.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
