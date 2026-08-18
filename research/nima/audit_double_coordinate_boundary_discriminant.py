#!/usr/bin/env python3
"""Verify that the double-boundary energy cover is branched only on Lambda."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
source = json.loads((ROOT / "research/nima/finite-sextic-higher-critical-locus.json").read_text(encoding="utf-8"))


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(coefficient, poly):
    return {m: coefficient * c for m, c in poly.items() if coefficient * c}


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


one = {(0, 0, 0): 1}
p1 = {(1, 0, 0): 1}
p2 = {(0, 1, 0): 1}
p3 = {(0, 0, 1): 1}
p1sq, p2sq, p3sq = mul(p1, p1), mul(p2, p2), mul(p3, p3)
h = add(p1sq, p2sq, scale(-1, p3sq))
quadratic_discriminant = add(mul(h, h), scale(-4, mul(p1sq, p2sq)))
triangle = one
for factor in (
    add(p1, scale(-1, p2), scale(-1, p3)),
    add(p1, scale(-1, p2), p3),
    add(p1, p2, scale(-1, p3)),
    add(p1, p2, p3),
):
    triangle = mul(triangle, factor)
assert quadratic_discriminant == triangle
assert source["double_coordinate_boundary"]["critical_value"] == (
    "P3**2*(E**4 - E**2*P1**2 - E**2*P2**2 + E**2*P3**2 + P1**2*P2**2)"
)

print(json.dumps({
    "energy_variable": "z=E^2",
    "quadratic": "z^2-(P1^2+P2^2-P3^2)z+P1^2*P2^2",
    "discriminant": "Lambda(P1,P2,P3)",
    "roots": ["(H+sqrt(Lambda))/2", "(H-sqrt(Lambda))/2"],
    "independent_branch_divisor": False,
}, indent=2))
