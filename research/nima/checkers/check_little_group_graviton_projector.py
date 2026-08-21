#!/usr/bin/env python3
"""Derive the four-dimensional graviton projector from total helicity."""

import json
import sympy as sp
from pathlib import Path


h = sp.diag(1, -1)
I = sp.eye(2)
P = sp.Matrix([[0, 1], [1, 0]])
Htot = sp.kronecker_product(h, I) + sp.kronecker_product(I, h)
Pi = sp.simplify(Htot**2 / 4)
P2 = sp.kronecker_product(P, P)

assert Pi == sp.diag(1, 0, 0, 1)
assert Pi**2 == Pi
assert Pi.rank() == 2
assert P2 * Htot * P2 == -Htot
assert P2 * Pi * P2 == Pi

result = {
    "status": "PASS",
    "basis": ["++", "+-", "-+", "--"],
    "total_helicity": [int(Htot[i, i]) for i in range(4)],
    "projector": [[int(Pi[i, j]) for j in range(4)] for i in range(4)],
    "idempotent": True,
    "rank": int(Pi.rank()),
    "parity_natural": True,
    "interpretation": "Pi_grav=(h1+h2)^2/4 is the canonical nonzero-total-helicity projector in the two-copy state space",
}

out = Path(__file__).resolve().parents[1] / "results" / "little_group_graviton_projector.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
