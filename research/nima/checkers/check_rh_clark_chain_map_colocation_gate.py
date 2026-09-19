#!/usr/bin/env python3
"""Finite chain-map test from the Grushin complex to the Clark observation cone."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

p, w, o = s.symbols("p w o")
# Scalar model of G_Cl: bulk pencil p, port column w, transpose row w.
G = s.Matrix([[p, -w], [-w, 0]])
# beta_-1 forgets the auxiliary Clark input; beta_0 reads the bordered output.
beta_minus = s.Matrix([[1, 0]])
beta_zero = s.Matrix([[0, 1]])
O = s.Matrix([[o]])
left = O * beta_minus
right = beta_zero * G
defect = s.simplify(left - right)

checks = {
    "chain_defect_formula": defect == s.Matrix([[o + w, 0]]),
    "commutes_under_colocation": s.simplify(defect.subs(o, -w)) == s.zeros(1, 2),
    "bulk_pencil_drops_out": p not in defect.free_symbols,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-clark-chain-map-colocation-gate.v1",
    "beta_minus_one": "projection (x,a) -> x",
    "beta_zero": "projection (y,b) -> b",
    "chain_condition": "O_Cl beta_-1 = beta_0 G_Cl",
    "chain_defect": "[O_Cl + W_Cl^times, 0]",
    "required_colocation": "O_Cl = -W_Cl^times",
    "checks": checks,
    "passed": True,
    "conclusion": "The canonical projection pair defines the characteristic-to-Green chain map exactly when the Green Clark observation is the oriented rigged transpose of the characteristic Clark port column. The bulk pencil contributes no further obstruction to this square."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-clark-chain-map-colocation-gate.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
