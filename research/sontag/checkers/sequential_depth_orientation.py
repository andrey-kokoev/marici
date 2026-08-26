#!/usr/bin/env python3
"""Exact depth test for orientation under cyclic trace readout."""

import json
from itertools import product
from pathlib import Path


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(a):
    return a[0][0] + a[1][1]


def word_value(word):
    value = [[1, 0], [0, 1]]
    for letter in word:
        value = mul(value, letter)
    return tr(value)


I = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Y = [[0, -1j], [1j, 0]]
Z = [[1, 0], [0, -1]]
generators = [I, X, Y, Z]

depth_one_equal = all(word_value((a,)) == word_value((a,)) for a in generators)
depth_two_equal = all(
    word_value((a, b)) == word_value((b, a))
    for a, b in product(generators, repeat=2)
)
xyz = word_value((X, Y, Z))
zyx = word_value((Z, Y, X))

checks = {
    "depth_one_cannot_orient": depth_one_equal,
    "depth_two_trace_cannot_orient": depth_two_equal,
    "depth_three_trace_separates": xyz != zyx,
    "depth_three_values_are_nonzero": xyz != 0 and zyx != 0,
    "depth_three_reversal_flips_sign": xyz == -zyx,
    "ordinary_xyz_value": xyz == 2j,
    "opposite_xyz_value": zyx == -2j,
}

result = {
    "schema": "marici.sontag.sequential_depth_orientation.v1",
    "claim_strength": "finite exact hostile fixture",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "trace_xyz": str(xyz),
    "trace_zyx": str(zyx),
    "interpretation": (
        "Cyclic trace readout erases orientation through word depth two on the "
        "Pauli basis, while a depth-three word separates ordinary and opposite products."
    ),
}

out = Path(__file__).parents[1] / "results" / "sequential_depth_orientation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
