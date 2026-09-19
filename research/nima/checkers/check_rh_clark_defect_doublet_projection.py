#!/usr/bin/env python3
"""Project reciprocal parity embeddings through the fixed Clark codiagonal."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

d1, d2 = s.symbols("d1 d2")
I = s.I
S = I*s.Rational(1, 2)*s.Matrix([[-1, 1, 1, 1], [-1, 1, -1, -1]])

kernel_basis = [s.Matrix([1, 1, 0, 0]), s.Matrix([0, 0, 1, -1])]
odd_odd = s.Matrix([d1, -d1, d2, -d2])
even_odd = s.Matrix([d1, d1, d2, -d2])

checks = {
    "rank_two": S.rank() == 2,
    "kernel_dimension_two": len(S.nullspace()) == 2,
    "declared_kernel_basis": all(S*v == s.zeros(2, 1) for v in kernel_basis),
    "even_odd_packet_is_hidden": s.simplify(S*even_odd) == s.zeros(2, 1),
    "odd_odd_output_is_common_d1": s.simplify(S*odd_odd) == s.Matrix([-I*d1, -I*d1]),
    "d2_odd_channel_is_hidden": d2 not in (S*odd_odd).free_symbols,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-clark-defect-doublet-projection.v1",
    "input_order": ["channel1_plus", "channel1_minus", "channel2_plus", "channel2_minus"],
    "kernel": "{(a,a,b,-b)}",
    "defect_parity": "D1 and D2 are both reflection-odd",
    "odd_odd_embedding": ["D1", "-D1", "D2", "-D2"],
    "odd_odd_output": ["-i D1", "-i D1"],
    "checks": checks,
    "passed": True,
    "conclusion": "Under the declared phase-pair ordering, Clark projection kills the second odd defect D2 but retains D1 as a common two-output obstruction. The whole doublet lies in the Clark kernel only if the first defect occupies an even-character slot or D1 vanishes."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-clark-defect-doublet-projection.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
