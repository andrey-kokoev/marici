#!/usr/bin/env python3
"""Verify the odd-doubled Grushin border as a genuine two-term Hodge complex."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

p, w = s.symbols("p w", real=True)
G = s.Matrix([[p, -w], [-w, 0]])
Z = s.zeros(2)
Q = Z.row_join(G.T).col_join(G.row_join(Z))
Gamma = s.eye(2).row_join(Z).col_join(Z.row_join(-s.eye(2)))
delta = Z.row_join(Z).col_join(G.row_join(Z))

checks = {
    "nilpotent_differential": delta**2 == s.zeros(4),
    "hodge_totalization": delta + delta.T == Q,
    "self_adjoint": Q.T == Q,
    "odd_grading": s.simplify(Gamma * Q + Q * Gamma) == s.zeros(4),
    "square_is_laplacian_blocks": s.simplify(Q**2 - (G.T * G).row_join(Z).col_join(Z.row_join(G * G.T))) == s.zeros(4),
    "determinant_is_squared_grushin_determinant": s.factor(Q.det() - G.det()**2) == 0,
    "characteristic_polynomial_is_even": Q.charpoly().all_coeffs()[1::2] == [0, 0],
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-odd-doubled-grushin-complex.v1",
    "grushin_border": [["p", "-w"], ["-w", "0"]],
    "differential": "delta=[[0,0],[G,0]]",
    "hodge_totalization": "Q=delta+delta*= [[0,G*],[G,0]]",
    "grading": "Gamma=diag(I,-I)",
    "checks": checks,
    "passed": True,
    "conclusion": "Odd doubling converts the Grushin border into a genuine two-term complex with symmetric Hodge spectrum while retaining the full bordered operator as its differential.",
    "qualification": "This types the characteristic complex but does not identify it with the Green Clark observation cone; a chain map preserving Clark ports is still required."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-odd-doubled-grushin-complex.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
