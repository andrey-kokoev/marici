#!/usr/bin/env python3
"""Finite hostile: a generic Grushin border is not a plain Hodge differential d+d*."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

p, w = s.symbols("p w", real=True)
G = s.Matrix([[p, -w], [-w, 0]])
d = s.symbols("d", real=True)
Hodge = s.Matrix([[0, d], [d, 0]])

checks = {
    "grushin_trace_is_p": s.trace(G) == p,
    "plain_hodge_trace_is_zero": s.trace(Hodge) == 0,
    "grushin_characteristic_polynomial": G.charpoly().all_coeffs() == [1, -p, -w**2],
    "plain_hodge_characteristic_polynomial_is_even": Hodge.charpoly().all_coeffs() == [1, 0, -d**2],
    "generic_similarity_obstructed_by_trace": s.simplify(s.trace(G) - s.trace(Hodge)) == p,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-grushin-plain-hodge-obstruction.v1",
    "scalar_grushin": [["p", "-w"], ["-w", "0"]],
    "plain_hodge": [["0", "d"], ["d", "0"]],
    "checks": checks,
    "passed": True,
    "conclusion": "For generic nonzero characteristic pencil p, the Grushin border cannot be similar to an unstabilized Hodge operator d+d*: trace and spectral symmetry disagree.",
    "allowed_repairs": [
        "descriptor or curved complex retaining P as a degree-zero potential",
        "odd doubling [[0,G],[G*,0]]",
        "source-derived internal grading in which P itself is odd"
    ]
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-grushin-plain-hodge-obstruction.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
