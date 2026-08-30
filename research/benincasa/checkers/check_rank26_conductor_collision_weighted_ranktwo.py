#!/usr/bin/env python3
"""Exact weighted limit of the two-sheet conductor matrix at root collision."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-collision-weighted-ranktwo.json"
x, y, z, a, r = sp.symbols("x y z a r", nonzero=True)

spectator = (a-x-z)*(a+y+2*z)*(y+z-x)*(a-y)
h = sp.factor(1/((-2*x)*spectator))
h_plus = sp.factor(h.subs(a, r))
h_minus = sp.factor(h.subs(a, -r))

# Since dR/da=-2*x*a, the raw sheet weight is h(a)/a.
J_sheet = sp.Matrix([
    [h_plus/r, h_plus],
    [-h_minus/r, h_minus],
])

# Source-forced collision lattice: trace row and r-scaled anti-trace row.
L = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
               [r/2, -r/2]])
J_weighted = sp.simplify(L*J_sheet)
J_limit = J_weighted.applyfunc(lambda entry: sp.factor(sp.limit(entry, r, 0)))
h0 = sp.factor(h.subs(a, 0))
h1 = sp.factor(sp.diff(h, a).subs(a, 0))
expected = sp.Matrix([[h1, h0], [h0, 0]])
determinant = sp.factor(J_limit.det())

checks = {
    "raw_sheet_matrix_has_simple_collision_poles": sp.limit(r*J_sheet[0, 0], r, 0) == h0 and sp.limit(r*J_sheet[1, 0], r, 0) == -h0,
    "weighted_limit_exists_entrywise": all(not value.has(sp.oo, -sp.oo, sp.zoo, sp.nan) for value in J_limit),
    "weighted_limit_matches_value_derivative_matrix": sp.simplify(J_limit-expected) == sp.zeros(2),
    "collision_determinant_is_minus_h0_squared": sp.simplify(determinant+h0**2) == 0,
    "generic_collision_rank_is_two": determinant != 0,
}
payload = {
    "schema": "marici.rank26-conductor-collision-weighted-ranktwo.v1",
    "raw_sheet_matrix": str(J_sheet),
    "collision_lattice_transform": str(L),
    "weighted_limit": [[str(J_limit[i, j]) for j in range(2)] for i in range(2)],
    "expected_limit": "[[h'(0),h(0)],[h(0),0]]",
    "h0": str(h0),
    "determinant": str(determinant),
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The singular projector basis has a source-forced weighted limit of rank two. At C1=0 the target becomes the full value/derivative dual of the nonreduced root algebra, not a rank-one determinant or aggregate line.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
