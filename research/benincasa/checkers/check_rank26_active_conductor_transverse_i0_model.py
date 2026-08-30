#!/usr/bin/env python3
"""Exact transverse local models at the two literal rank-26 conductors."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-active-conductor-transverse-i0-model.json"

a, b, x, y, z = sp.symbols("a b x y z")
E = x + y + z
K = (
    x**2 * a**4
    - a**2 * b**2 * (x**2 + y**2 - z**2)
    + y**2 * b**4
    + a**2 * x**2 * (x**2 - y**2 - z**2)
    + E**2 * a**2 * (y**2 - x**2 - z**2)
    + b**2 * y**2 * (y**2 - x**2 - z**2)
    + E**2 * b**2 * (x**2 - y**2 - z**2)
    + z**2 * E**4
    + E**2 * z**2 * (z**2 - x**2 - y**2)
    + z**2 * x**2 * y**2
)
R1 = -a**2*x + x**2*y + x**2*z + x*y**2 + 2*x*y*z + 2*x*z**2 - y**3 - y**2*z + y*z**2 + z**3
R2 = b**2*y + x**3 - x**2*y + x**2*z - x*y**2 - 2*x*y*z - x*z**2 - y**2*z - 2*y*z**2 - z**3

# q1=b-y-z and q2=a-x-z are the source-normal wall coordinates.
S1 = sp.factor(sp.diff(K, b).subs(b, y + z))
S2 = sp.factor(sp.diff(K, a).subs(a, x + z))
rem1 = sp.factor(sp.rem(S1, R1, a))
rem2 = sp.factor(sp.rem(S2, R2, b))
expected1 = 2*(y+z)*(x-y-z)*(x-y+z)*(x+y-z)*E**2/x
expected2 = 2*(x+z)*(x-y-z)*(x-y+z)*(x+y-z)*E**2/y
res1 = sp.factor(sp.resultant(R1, S1, a))
res2 = sp.factor(sp.resultant(R2, S2, b))

sample = {x: 2, y: 3, z: 4}
r1 = 3*sp.sqrt(46)/2
r2 = sp.sqrt(94)
s1_sample = sp.factor(S1.subs(sample).subs(a, r1))
s2_sample = sp.factor(S2.subs(sample).subs(b, r2))

checks = {
    "g1_wall_square": sp.expand(K.subs(b, y+z) - R1**2) == 0,
    "g2_wall_square": sp.expand(K.subs(a, x+z) - R2**2) == 0,
    "g1_conductor_remainder": sp.expand(rem1-expected1) == 0,
    "g2_conductor_remainder": sp.expand(rem2-expected2) == 0,
    "g1_transversality_resultant_nonzero": res1 != 0,
    "g2_transversality_resultant_nonzero": res2 != 0,
    "g1_sample_transverse_negative": s1_sample < 0,
    "g2_sample_transverse_negative": s2_sample < 0,
}

packet = {
    "schema": "marici.rank26-active-conductor-transverse-i0-model.v1",
    "wall_coordinates": {"g1": "q1=b-y-z", "g2": "q2=a-x-z"},
    "local_models": {
        "g1": "K=R1^2+q1*S1+O(q1^2)",
        "g2": "K=R2^2+q2*S2+O(q2^2)",
    },
    "transverse_coefficients": {"S1": str(S1), "S2": str(S2)},
    "conductor_remainders": {"S1_mod_R1": str(rem1), "S2_mod_R2": str(rem2)},
    "transversality_resultants": {"g1": str(res1), "g2": str(res2)},
    "strict_triangle_sign": "Both conductor remainders are negative because x-y-z<0 and every other displayed factor is positive.",
    "source_boundary_value": "For q_i -> q_i-i0, K -> r_i^2-i0*S_i = r_i^2+i0*|S_i| at either selected conductor.",
    "sample_2_3_4": {"S1": str(s1_sample), "S2": str(s2_sample)},
    "checks": {k: bool(v) for k, v in checks.items()},
    "passed": all(bool(v) for v in checks.values()),
    "scope": "This derives the local bypass and transversality. It does not assign a standalone finite-part wall period or split the unsplit physical relative cocycle.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
