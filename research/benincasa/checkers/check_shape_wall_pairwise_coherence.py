#!/usr/bin/env python3
"""Exact pairwise coherence audit for the physical shape-wall lowering maps."""

import json
from itertools import combinations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-wall-pairwise-coherence.json"

a, b, c, t = sp.symbols("a b c t")
variables = (a, b, c)
walls = {
    "g1": b + c + 1,
    "g2": c + a + 1,
    "g3": a + b + 1,
    "B12": c + 3,
    "B23": a + 3,
    "B31": b + 3,
    "s12": a + b + 2,
    "s23": b + c + 2,
    "s31": c + a + 2,
}

P1, P2, P3 = 1 + t, 1 - t, sp.Integer(1)
cm = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, P2**2, P1**2],
    [1, a**2, P2**2, 0, P3**2],
    [1, b**2, P1**2, P3**2, 0],
])
K0 = sp.factor((-cm.det() / 2).subs(t, 0))


def gradient(f):
    return sp.Matrix([[sp.diff(f, x) for x in variables]])


def directional(vector, f):
    return sp.expand(sum(vector[i] * sp.diff(f, variables[i]) for i in range(3)))


def dual_normals(first, second):
    matrix = sp.Matrix.vstack(gradient(first), gradient(second))
    _, pivots = matrix.rref()
    chosen = list(pivots[:2])
    block = matrix[:, chosen]
    inverse = block.inv()
    vectors = []
    for target in range(2):
        vector = sp.zeros(3, 1)
        solution = inverse[:, target]
        for row, coordinate in enumerate(chosen):
            vector[coordinate] = solution[row]
        vectors.append(vector)
    return matrix, vectors


records = {}
checks = {}
for left, right in combinations(walls, 2):
    first, second = walls[left], walls[right]
    key = f"{left}__{right}"
    matrix = sp.Matrix.vstack(gradient(first), gradient(second))
    if matrix.rank() == 1:
        solution = sp.linsolve((first, second), variables)
        disjoint = solution is sp.EmptySet
        records[key] = {"kind": "parallel", "intersection_empty": bool(disjoint)}
        checks[f"{key}_parallel_is_disjoint"] = bool(disjoint)
        continue

    matrix, (v_left, v_right) = dual_normals(first, second)
    identities = [
        directional(v_left, first) == 1,
        directional(v_left, second) == 0,
        directional(v_right, first) == 0,
        directional(v_right, second) == 1,
    ]
    # The Kummer twist connection is exact: A_v=-V(K0)/(2K0).
    A_left = -directional(v_left, K0) / (2 * K0)
    A_right = -directional(v_right, K0) / (2 * K0)
    curvature = sp.factor(directional(v_left, A_right) - directional(v_right, A_left))
    remainder = sp.groebner([first, second], *variables).reduce(K0)[1]
    records[key] = {
        "kind": "transverse",
        "left_normal": [sp.sstr(x) for x in v_left],
        "right_normal": [sp.sstr(x) for x in v_right],
        "dual_normal_identities": all(identities),
        "twisted_commutator_curvature": sp.sstr(curvature),
        "K0_not_identically_zero_on_intersection": remainder != 0,
    }
    checks[f"{key}_dual_normals"] = all(identities)
    checks[f"{key}_twisted_derivatives_commute"] = curvature == 0
    checks[f"{key}_proper_intersection_not_in_K0"] = remainder != 0

assert all(checks.values()), {k: v for k, v in checks.items() if not v}
packet = {
    "schema": "marici.shape-wall-pairwise-coherence.v1",
    "wall_count": len(walls),
    "pair_count": len(records),
    "transverse_pair_count": sum(r["kind"] == "transverse" for r in records.values()),
    "parallel_disjoint_pair_count": sum(r["kind"] == "parallel" for r in records.values()),
    "records": records,
    "all_checks_pass": True,
    "check_count": len(checks),
    "triple_associator_constructed": False,
    "full_filtered_homotopy_constructed": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(f"transverse={packet['transverse_pair_count']} parallel_disjoint={packet['parallel_disjoint_pair_count']}")
print(OUT)
