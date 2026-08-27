#!/usr/bin/env python3
"""Construct the primitive bidegree-(1,1) Leray-soft relational cell."""

import json
import math
from pathlib import Path


# Ordered bases: fiber endpoints (p_minus,p_plus), base soft faces (s3,s2).
fiber_difference = (-1, 1)
base_difference = (1, -1)

residue = [
    [fiber_difference[i] * base_difference[j] for j in range(2)]
    for i in range(2)
]

row_sums = [sum(row) for row in residue]
column_sums = [sum(residue[i][j] for i in range(2)) for j in range(2)]
entries = [entry for row in residue for entry in row]
primitive_gcd = math.gcd(*[abs(entry) for entry in entries])
determinant = residue[0][0] * residue[1][1] - residue[0][1] * residue[1][0]
nonzero = any(entry != 0 for entry in entries)
rank = 1 if determinant == 0 and nonzero else 2 if determinant != 0 else 0

reversed_fiber = tuple(-value for value in fiber_difference)
reversed_base = tuple(-value for value in base_difference)
fiber_reversal = [
    [reversed_fiber[i] * base_difference[j] for j in range(2)]
    for i in range(2)
]
base_reversal = [
    [fiber_difference[i] * reversed_base[j] for j in range(2)]
    for i in range(2)
]
simultaneous_reversal = [
    [reversed_fiber[i] * reversed_base[j] for j in range(2)]
    for i in range(2)
]

checks = {
    "row_sums_vanish": row_sums == [0, 0],
    "column_sums_vanish": column_sums == [0, 0],
    "primitive_integral_cell": primitive_gcd == 1,
    "rank_one": rank == 1,
    "single_orientation_reversal_is_odd": fiber_reversal
    == [[-entry for entry in row] for row in residue]
    and base_reversal == [[-entry for entry in row] for row in residue],
    "simultaneous_reversal_is_even": simultaneous_reversal == residue,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.bigraded_leray_soft_residue.v1",
    "fiber_basis": ["p_minus", "p_plus"],
    "base_basis": ["s3", "s2"],
    "fiber_difference": list(fiber_difference),
    "base_difference": list(base_difference),
    "bidegree_11_cell": residue,
    "rank": rank,
    "primitive_gcd": primitive_gcd,
    "row_sums": row_sums,
    "column_sums": column_sums,
    "checks": checks,
    "verdict": (
        "The external product of the vertical Leray boundary and horizontal "
        "soft-divisor difference is a canonical primitive rank-one relational "
        "cell. It is a candidate fifth-tower residue, not a scalar readout and "
        "not yet an identified q0-by-e6 extension class."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "bigraded_leray_soft_residue.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
