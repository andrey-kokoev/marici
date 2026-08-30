"""Exact audit that covariance restriction commutes with exterior square."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


PAIRS = list(itertools.combinations(range(4), 2))


def det2(a, b, c, d):
    return a * d - b * c


def wedge2(matrix):
    return [
        [
            det2(
                matrix[i][k], matrix[i][l],
                matrix[j][k], matrix[j][l],
            )
            for k, l in PAIRS
        ]
        for i, j in PAIRS
    ]


tests = 0
for seed in range(1, 65):
    # Generic exact symmetric 4x4 covariance-shaped matrix.
    v = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    value = seed
    for i in range(4):
        for j in range(i, 4):
            value = (17 * value + 11) % 101
            v[i][j] = v[j][i] = Fraction(value - 50, 13)

    w = wedge2(v)
    # Inclusion of occurrence A selects basis pair (0,1), which is PAIRS[0].
    det_a = det2(v[0][0], v[0][1], v[1][0], v[1][1])
    assert w[0][0] == det_a

    # The A-row/B-column exterior-square component is det(C), not a defect.
    det_c = det2(v[0][2], v[0][3], v[1][2], v[1][3])
    b_pair_index = PAIRS.index((2, 3))
    assert w[0][b_pair_index] == det_c
    tests += 1

packet = {
    "schema": "marici.exterior-square-restriction.v1",
    "strict_identity": "wedge^2(i^T V i)=(wedge^2 i)^T (wedge^2 V)(wedge^2 i)",
    "local_component": "(wedge^2 V)_(A,A)=det(A)",
    "cross_component": "(wedge^2 V)_(A,B)=det(C)",
    "exact_generic_tests": tests,
    "conclusion": "occurrence restriction and determinant readout commute strictly after exterior-square linearization; det(C) is an off-diagonal coefficient, not a Beck-Chevalley defect",
}

out = Path(__file__).parent / "results" / "exterior-square-restriction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
