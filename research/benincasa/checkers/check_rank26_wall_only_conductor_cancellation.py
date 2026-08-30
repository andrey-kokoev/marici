#!/usr/bin/env python3
"""Falsify wall-only cancellation of the two active conductor logarithms."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-wall-only-conductor-cancellation.json"
t = sp.symbols("t")

# Entry 3832's source-oriented positive-sheet coefficients at (2,3,4).
c1 = sp.Rational(16, 99225) - sp.sqrt(46) / 101430
c2 = sp.Rational(1, 2025) - sp.sqrt(94) / 28200
direct = sp.simplify(c1 + c2)
opposite = sp.simplify(c1 - c2)
min_direct = sp.factor(sp.minpoly(direct, t))
min_opposite = sp.factor(sp.minpoly(opposite, t))

checks = {
    "g1_nonzero": c1 != 0,
    "g2_nonzero": c2 != 0,
    "same_orientation_sum_nonzero": direct != 0,
    "opposite_orientation_sum_nonzero": opposite != 0,
    "same_orientation_minpoly_nonzero_constant": sp.Poly(min_direct, t).TC() != 0,
    "opposite_orientation_minpoly_nonzero_constant": sp.Poly(min_opposite, t).TC() != 0,
}

packet = {
    "schema": "marici.rank26-wall-only-conductor-cancellation.v1",
    "sample": {"x": 2, "y": 3, "z": 4},
    "coefficients": {"g1": str(c1), "g2": str(c2)},
    "orientation_tests": {
        "c1_plus_c2": str(direct),
        "c1_minus_c2": str(opposite),
        "minpoly_c1_plus_c2": str(min_direct),
        "minpoly_c1_minus_c2": str(min_opposite),
    },
    "checks": {k: bool(v) for k, v in checks.items()},
    "passed": all(bool(v) for v in checks.values()),
    "conclusion": "Neither relative orientation makes the two active wall logarithms cancel. A universal wall-to-wall cancellation is falsified by this exact source point.",
    "scope": "This rejects a wall-only two-term mechanism. It does not imply divergence of the full source period; bulk, endpoint, or relative-current terms remain available only if source-derived.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
