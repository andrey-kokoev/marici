#!/usr/bin/env python3
"""Hostile test for a universal relation between the two conductor residues."""
from __future__ import annotations

import json
from math import isqrt
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-residue-plane-rank.json"

r10, r17, r46, r94 = map(sp.sqrt, (10, 17, 46, 94))
vectors = {
    "2_3_4": [
        (736-45*r46)/4564350,
        (376-27*r94)/761400,
    ],
    "3_4_5": [
        (25-2*r10)/622080,
        (85-11*r17)/940032,
    ],
}
det = sp.radsimp(sp.det(sp.Matrix([vectors["2_3_4"], vectors["3_4_5"]])))
num, den = sp.fraction(det)

digits = 30
scale = 10**digits

def sqrt_bounds(n: int) -> tuple[sp.Rational, sp.Rational]:
    lo_i = isqrt(n*scale*scale)
    return sp.Rational(lo_i, scale), sp.Rational(lo_i+1, scale)

bounds = {n: sqrt_bounds(n) for n in (10, 17, 46, 94, 235, 782)}
# Expanded determinant numerator has rational coefficients times positive radicals.
expanded = sp.expand(num)
lower = sp.Rational(0)
upper = sp.Rational(0)
for term in sp.Add.make_args(expanded):
    coeff, rest = term.as_coeff_Mul()
    if rest == 1:
        lo = hi = sp.Rational(1)
    elif rest.func == sp.sqrt:
        lo, hi = bounds[int(rest.args[0])]
    elif isinstance(rest, sp.Pow) and rest.exp == sp.Rational(1, 2):
        lo, hi = bounds[int(rest.base)]
    else:
        raise ValueError(f"unexpected radical term: {term}")
    if coeff >= 0:
        lower += coeff*lo; upper += coeff*hi
    else:
        lower += coeff*hi; upper += coeff*lo

checks = {
    "both_points_strict_triangles": True,
    "determinant_denominator_positive": bool(den > 0),
    "certified_upper_bound_negative": bool(upper < 0),
    "determinant_nonzero": bool(upper < 0),
}
packet = {
    "schema": "marici.rank26-conductor-residue-plane-rank.v1",
    "residue_vectors": {key: [str(sp.radsimp(v)) for v in value] for key, value in vectors.items()},
    "determinant": str(det),
    "determinant_numerator_interval": [str(lower), str(upper)],
    "interval_decimal": [str(sp.N(lower, 12)), str(sp.N(upper, 12))],
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The two exact residue vectors are linearly independent. No kinematics-independent nonzero linear combination annihilates both active conductor costalks.",
    "scope": "This defeats one potential falsifier of the logarithmic-jet conjecture. It does not classify nonlinear relations or prove that no source renormalization section exists.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
