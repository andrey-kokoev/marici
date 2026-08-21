"""Exact counterexample: time orientation does not determine helicity orientation."""

import hashlib
import json
from pathlib import Path

import sympy as sp

eta = sp.diag(1, -1, -1, -1)
k = sp.Matrix([1, 0, 0, 1])
t = sp.Matrix([1, 0, 0, 0])

# Reflection of one transverse spatial axis: parity-odd but time preserving.
P = sp.diag(1, -1, 1, 1)
J = sp.Matrix([[0, -1], [1, 0]])
Pperp = sp.diag(-1, 1)

payload = {
    "schema": "marici.time-root-vs-helicity-orientation.v1",
    "strength": "exact Lorentz-frame counterexample",
    "lorentz_residual": [str(x) for x in sp.simplify(P.T*eta*P-eta)],
    "future_time_residual": [str(x) for x in P*t-t],
    "null_ray_residual": [str(x) for x in P*k-k],
    "spacetime_determinant": str(P.det()),
    "transverse_determinant": str(Pperp.det()),
    "helicity_flip_residual": [str(x) for x in sp.simplify(Pperp*J*Pperp.inv()+J)],
    "conclusion": (
        "A Lorentz transformation can preserve the time orientation and future null "
        "ray while reversing the transverse orientation and swapping helicities."
    ),
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"time-root-vs-helicity-orientation.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert P.T*eta*P == eta
assert P*t == t and P*k == k
assert P.det() == -1 and Pperp.det() == -1
assert sp.simplify(Pperp*J*Pperp.inv()+J) == sp.zeros(2)
print(json.dumps({"time_preserved":True,"helicity_orientation_flipped":True,"sha256":payload["content_sha256"]}))
