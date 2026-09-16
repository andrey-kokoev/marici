#!/usr/bin/env python3
"""Finite hostile check for the four-phase presentation indexing category.

This checks combinatorial generation of all parallel-path equalities.  It does
not instantiate analytic presentation maps or prove their homotopies.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MAX_STAGE = 6

Vertex = tuple[int, int]
PathT = tuple[Vertex, ...]


def edges(v: Vertex) -> list[Vertex]:
    k, i = v
    out = [(k, j) for j in range(i + 1, 5)]
    if i == 4 and k < MAX_STAGE:
        out.append((k + 1, 1))
    return out


@lru_cache(None)
def paths(a: Vertex, b: Vertex) -> tuple[PathT, ...]:
    if a == b:
        return ((a,),)
    ans: list[PathT] = []
    for c in edges(a):
        if c[0] > b[0] or (c[0] == b[0] and c[1] > b[1]):
            continue
        for tail in paths(c, b):
            ans.append((a,) + tail)
    return tuple(ans)


def reduce_once(p: PathT) -> PathT:
    # Triangle/2-Segal move inside one tetrahedron: i->j->l becomes i->l.
    for n in range(len(p) - 2):
        a, b, c = p[n : n + 3]
        if a[0] == b[0] == c[0] and a[1] < b[1] < c[1]:
            return p[: n + 1] + p[n + 2 :]
    return p


def normal_form(p: PathT) -> PathT:
    while True:
        q = reduce_once(p)
        if q == p:
            return p
        p = q


pairs = 0
path_count = 0
max_parallel = 0
failures = []
for ka in range(MAX_STAGE + 1):
    for ia in range(1, 5):
        for kb in range(ka, MAX_STAGE + 1):
            for ib in range(1, 5):
                a, b = (ka, ia), (kb, ib)
                ps = paths(a, b)
                if not ps:
                    continue
                pairs += 1
                path_count += len(ps)
                max_parallel = max(max_parallel, len(ps))
                nfs = {normal_form(p) for p in ps}
                if len(nfs) != 1:
                    failures.append({"source": a, "target": b, "normal_forms": list(nfs)})

# Hostile: delete direct edge 1->4 at stage 0 from the reduction law by refusing
# the triangle contraction through endpoint 4. Two paths then retain distinct forms.
def hostile_nf(p: PathT) -> PathT:
    while True:
        q = p
        for n in range(len(p) - 2):
            a, b, c = p[n : n + 3]
            if a[0] == b[0] == c[0] and a[1] < b[1] < c[1] and not (a == (0, 1) and c == (0, 4)):
                q = p[: n + 1] + p[n + 2 :]
                break
        if q == p:
            return p
        p = q

hostile_paths = paths((0, 1), (1, 1))
hostile_forms = {hostile_nf(p) for p in hostile_paths}

out = {
    "schema": "marici.voevodsky.four-periodic-twisted-successor-path-coherence.v1",
    "status": "passed" if not failures and len(hostile_forms) > 1 else "failed",
    "stage_range": [0, MAX_STAGE],
    "parallel_endpoint_pairs": pairs,
    "enumerated_paths": path_count,
    "maximum_parallel_paths": max_parallel,
    "unique_normal_form_for_every_parallel_family": not failures,
    "hostile_missing_14_face_detected": len(hostile_forms) > 1,
    "hostile_normal_form_count": len(hostile_forms),
    "interpretation": "Triangle contractions plus the 4-to-1 seam generate all strict path equalities in the finite periodic indexing model.",
    "claim_boundary": "Finite combinatorial indexing theorem only; no analytic C_ij map, seam equivalence, homotopy, Rzk Segal type, or unbounded coherence theorem is constructed.",
}
result = ROOT / "research/voevodsky/results/four_periodic_twisted_successor_path_coherence.json"
result.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(out["status"] != "passed")
