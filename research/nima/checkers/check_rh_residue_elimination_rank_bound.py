#!/usr/bin/env python3
"""Exact finite rank test for a one-dimensional residue-state Schur correction."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

r = s.symbols("r", nonzero=True, real=True)
x1, x2, y1, y2 = s.symbols("x1 x2 y1 y2")
# Algebraic left/right incidence is kept independent; Hermitian specialization is y=x*.
x = s.Matrix([x1, x2])
yT = s.Matrix([[y1, y2]])
correction = s.simplify(x * yT / r)

checks = {
    "rank_at_most_one": correction.rank() == 1,
    "determinant_zero": s.factor(correction.det()) == 0,
    "all_two_by_two_minors_zero": s.factor(correction[0, 0] * correction[1, 1] - correction[0, 1] * correction[1, 0]) == 0,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-residue-elimination-rank-bound.v1",
    "residue_dimension": 1,
    "schur_correction": [["x1*y1/r", "x1*y2/r"], ["x2*y1/r", "x2*y2/r"]],
    "checks": checks,
    "passed": True,
    "finite_falsifier": "For a simple residue channel, any nonzero 2x2 elimination anomaly with nonzero determinant cannot arise from residue Schur elimination.",
    "higher_multiplicity": "For residue dimension m, rank(anomaly) must be at most m."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-residue-elimination-rank-bound.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
