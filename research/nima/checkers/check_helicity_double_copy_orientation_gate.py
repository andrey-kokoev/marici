#!/usr/bin/env python3
"""Exact parity characters of the two-helicity double-copy state space."""

import json
import sympy as sp
from pathlib import Path


# Basis H=(+, -); parity swaps helicities.
P = sp.Matrix([[0, 1], [1, 0]])
P_tensor = sp.kronecker_product(P, P)  # (++,+-,-+,--)

# Restricted matrices in the ordered graviton (++ , --) and mixed (+-,-+) sectors.
P_graviton = sp.Matrix([[0, 1], [1, 0]])
P_mixed = sp.Matrix([[0, 1], [1, 0]])

assert P.det() == -1
assert P_tensor.det() == 1
assert P_graviton.det() == -1
assert P_mixed.det() == -1

result = {
    "status": "PASS",
    "ym_helicity_doublet_parity_determinant": int(P.det()),
    "unprojected_tensor_square_parity_determinant": int(P_tensor.det()),
    "graviton_diagonal_subspace_parity_determinant": int(P_graviton.det()),
    "mixed_dilaton_b_subspace_parity_determinant": int(P_mixed.det()),
    "conclusion": "the full double copy is parity-even; the graviton orientation line appears only after a typed state-sector projection",
    "remaining_gate": "derive the graviton projector/state pairing and relate its determinant line to the Carrier conductor",
}

out = Path(__file__).resolve().parents[1] / "results" / "helicity_double_copy_orientation_gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
