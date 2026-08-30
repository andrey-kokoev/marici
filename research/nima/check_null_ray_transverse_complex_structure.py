"""Exact frame audit for the complex structure on a null transverse quotient."""

import hashlib
import json
from pathlib import Path

import sympy as sp

c, s = sp.symbols("c s", real=True)
J = sp.Matrix([[0, -1], [1, 0]])
R = sp.Matrix([[c, -s], [s, c]])
F = sp.diag(1, -1)
I = sp.eye(2)

rotation_residual = sp.simplify(R * J - J * R)
reflection_residual = sp.simplify(F * J * F.inv() + J)
Pplus = (I - sp.I * J) / 2
Pminus = (I + sp.I * J) / 2
reflection_helicity_swap = sp.simplify(F * Pplus * F.inv() - Pminus)

payload = {
    "schema": "marici.null-ray-transverse-complex-structure.v1",
    "strength": "exact oriented-frame theorem",
    "J_squared_plus_identity": [str(x) for x in sp.simplify(J*J+I)],
    "orientation_preserving_frame_residual": [str(x) for x in rotation_residual],
    "orientation_reversal_anticommutator_residual": [str(x) for x in reflection_residual],
    "reflection_helicity_swap_residual": [str(x) for x in reflection_helicity_swap],
    "typing": (
        "A spacetime orientation, time orientation, and future null ray orient the "
        "Euclidean Ward quotient; its metric and orientation determine J."
    ),
    "boundary": "Entry 126's time-root line is not by itself the spacetime orientation datum.",
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"null-ray-transverse-complex-structure.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert J*J == -I
assert rotation_residual == sp.zeros(2)
assert reflection_residual == sp.zeros(2)
assert reflection_helicity_swap == sp.zeros(2)
print(json.dumps({"SO2_invariant":True,"reflection_swaps_helicity":True,"sha256":payload["content_sha256"]}))
