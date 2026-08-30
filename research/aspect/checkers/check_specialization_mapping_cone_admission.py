#!/usr/bin/env python3
"""Independently admit the exported rank-26 specialization mapping cone."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research" / "aspect" / "results" / "specialization_mapping_cone_admission.json"


def dense(columns, rows, prime):
    return [[int(column.get(str(i), 0)) % prime for column in columns] for i in range(rows)]


def rank(matrix, prime):
    a = [row[:] for row in matrix]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, prime)
        a[r] = [(x * inv) % prime for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x - q * y) % prime for x, y in zip(a[i], a[r])]
        r += 1
    return r


def multiply(left, right, prime):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) % prime
             for j in range(len(right[0]))] for i in range(len(left))]


reports = []
for suffix in ("", "-p31957"):
    path = ROOT / "research" / "benincasa" / "results" / f"rank26-conductor-specialization-cone-homology{suffix}.json"
    packet = json.loads(path.read_text(encoding="utf-8"))
    p = packet["prime"]
    cone = packet["mapping_cone"]
    d2 = dense(cone["d_minus_two_columns"], 29, p)
    d1 = dense(cone["d_minus_one_columns"], 4, p)
    r2, r1 = rank(d2, p), rank(d1, p)
    product = multiply(d1, d2, p)
    homology = [2-r2, 29-r1-r2, 4-r1]
    primitive = [1] + [0] * 28
    boundary = [sum(d1[i][j] * primitive[j] for j in range(29)) % p for i in range(4)]
    target = [int(packet["weighted_sheet_boundary"].get(str(i), 0)) % p for i in range(4)]
    reports.append({
        "prime": p,
        "dimensions": [2, 29, 4],
        "ranks": [r2, r1],
        "square_zero": all(x == 0 for row in product for x in row),
        "homology": homology,
        "primitive_boundary_matches": boundary == target,
        "cyclic_units": packet["defect_primitive"]["cyclic_edge_units"],
    })

checks = {
    "two_independent_prime_packets": [r["prime"] for r in reports] == [32009, 31957],
    "full_block_dimensions_agree": all(r["dimensions"] == [2, 29, 4] for r in reports),
    "differentials_have_ranks_2_and_4": all(r["ranks"] == [2, 4] for r in reports),
    "composition_is_zero": all(r["square_zero"] for r in reports),
    "graded_homology_is_0_23_0": all(r["homology"] == [0, 23, 0] for r in reports),
    "explicit_B_primitive_has_claimed_boundary": all(r["primitive_boundary_matches"] for r in reports),
    "cyclic_transport_is_literal_identity": all(r["cyclic_units"] == [1, 1, 1] for r in reports),
}
out = {
    "schema": "marici.aspect.specialization-mapping-cone-admission.v1",
    "reports": reports,
    "checks": checks,
    "passed": all(checks.values()),
    "admitted_scope": "finite-field full block mapping cone at primes 32009 and 31957",
    "next_gate": "Gauss-Manin horizontality of the rank-one boundary subbundle",
}
RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
