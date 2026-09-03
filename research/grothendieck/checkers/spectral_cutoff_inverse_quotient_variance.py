"""Exact finite witness that positive spectral cutoffs shrink radicals."""

import json
from pathlib import Path

import sympy as sp

F1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
F2 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
G1 = F1.T * F1
G2 = G1 + F2.T * F2
witness = sp.Matrix([0, 0, 1, 0])

rad1 = G1.nullspace()
rad2 = G2.nullspace()
checks = {
    "first_cutoff_rank": G1.rank() == 2,
    "second_cutoff_rank": G2.rank() == 4,
    "first_radical_dimension": len(rad1) == 2,
    "second_radical_dimension": len(rad2) == 0,
    "witness_zero_at_first_cutoff": G1 * witness == sp.zeros(4, 1),
    "witness_detected_at_second_cutoff": G2 * witness != sp.zeros(4, 1),
}
result = {
    "schema": "marici.grothendieck.spectral-cutoff-inverse-quotient-variance.v1",
    **checks,
    "all_verified": all(checks.values()),
    "conclusion": "Identity cannot induce V/rad(G1) -> V/rad(G2); it canonically induces the reverse projection.",
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "spectral-cutoff-inverse-quotient-variance.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
