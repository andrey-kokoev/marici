#!/usr/bin/env python3
"""Construct the finite A3 associahedral cellular resolution exactly."""
from itertools import combinations
from math import gcd
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/a3-coherent-resolution.json"
N = 6
boundary = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
diagonals = [tuple(sorted((i, j))) for i in range(N) for j in range(i + 1, N)
             if tuple(sorted((i, j))) not in boundary]

def crosses(a, b):
    x, y = a; u, v = b
    return (x < u < y < v) or (u < x < v < y)

vertices = sorted(tuple(sorted(ds)) for ds in combinations(diagonals, 3)
                  if all(not crosses(a, b) for a, b in combinations(ds, 2)))
vpos = {v: i for i, v in enumerate(vertices)}
edges = sorted((i, j) for i, a in enumerate(vertices) for j, b in enumerate(vertices)
               if i < j and len(set(a) ^ set(b)) == 2)
epos = {e: i for i, e in enumerate(edges)}
faces = []
for d in diagonals:
    vs = sorted(i for i, tri in enumerate(vertices) if d in tri)
    adj = {i: sorted(j for e in edges for j in (() if i not in e else (e[1] if e[0] == i else e[0],)) if j in vs) for i in vs}
    start = min(vs); prev = None; cur = start; cycle = [start]
    nxt = min(adj[start])
    while nxt != start:
        cycle.append(nxt); prev, cur = cur, nxt
        opts = [x for x in adj[cur] if x != prev]
        nxt = opts[0]
    faces.append({"diagonal": d, "cycle": cycle})
faces.sort(key=lambda f: f["diagonal"])

D1 = sp.zeros(len(vertices), len(edges))
for k, (a, b) in enumerate(edges): D1[a, k] = -1; D1[b, k] = 1
D2 = sp.zeros(len(edges), len(faces))
for k, f in enumerate(faces):
    cyc = f["cycle"]
    for a, b in zip(cyc, cyc[1:] + cyc[:1]):
        e = tuple(sorted((a, b))); D2[epos[e], k] = 1 if e == (a, b) else -1
ns = D2.nullspace()
assert len(ns) == 1
vec = ns[0]; den = sp.ilcm(*[x.q for x in vec]); ints = [int(x * den) for x in vec]
g = 0
for x in ints: g = gcd(g, abs(x))
ints = [x // g for x in ints]
if next(x for x in ints if x) < 0: ints = [-x for x in ints]
D3 = sp.Matrix(ints)
AUG = sp.ones(1, len(vertices))
checks = {
    "fourteen_clusters": len(vertices) == 14,
    "twenty_one_mutations": len(edges) == 21,
    "three_squares_six_pentagons": sorted(len(f["cycle"]) for f in faces) == [4]*3 + [5]*6,
    "d1_d2_zero": D1 * D2 == sp.zeros(len(vertices), len(faces)),
    "d2_d3_zero": D2 * D3 == sp.zeros(len(edges), 1),
    "augmentation_d1_zero": AUG * D1 == sp.zeros(1, len(edges)),
    "ranks_13_8_1": [D1.rank(), D2.rank(), D3.rank()] == [13, 8, 1],
    "exact_augmented_homology": [len(vertices)-D1.rank()-1, len(edges)-D1.rank()-D2.rank(), len(faces)-D2.rank()-D3.rank(), 1-D3.rank()] == [0,0,0,0],
    "integral_top_orientation": all(abs(x) == 1 for x in ints),
}
out = {
    "schema": "marici.nima.a3-coherent-resolution.v1",
    "object": "augmented cellular chain complex of the A3 associahedron",
    "complex": "0 -> Z -> Z^9 -> Z^21 -> Z^14 -> Z -> 0",
    "basis": {"C0_clusters": len(vertices), "C1_mutations": len(edges), "C2_faces": len(faces), "C3_polytope": 1},
    "face_lengths": [len(f["cycle"]) for f in faces],
    "top_boundary_signs": ints,
    "ranks": {"d1": D1.rank(), "d2": D2.rank(), "d3": D3.rank()},
    "checks": checks,
    "passed": all(checks.values()),
    "claim_boundary": "A finite exact resolution of the A3 cluster-label carrier. It does not yet resolve positroid canonical forms, physical weights, arbitrary n, or any radiative target.",
    "reopening_data": "A physical extension requires a generator map from labelled history/positroid cells to this basis, coefficient transport on every mutation edge, and compatibility with these differentials."
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
