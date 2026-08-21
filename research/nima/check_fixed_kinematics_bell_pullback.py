"""Exact distinction between fixed-kinematics pullback and base pushforward."""

import hashlib
import json
from pathlib import Path

import sympy as sp

sqrt2 = sp.sqrt(2)

def bell(r, s):
    return sp.simplify(4 * sqrt2 * r * s / (r**2 + s**2))

# Two exact momentum fibers with inequivalent helicity states.
I0 = bell(sp.Integer(1), sp.Integer(1))
I1 = bell(sp.Integer(1), sp.Integer(2))
Imix = sp.simplify((I0 + I1) / 2)

# Evaluation at a base point commutes with a pointwise fiber endomorphism.
a0, a1, t = sp.symbols("a0 a1 t")
section = sp.Matrix([a0, a1])
pointwise = t * sp.eye(2)
eval0_after = (pointwise * section)[0]
after_eval0 = t * section[0]

payload = {
    "schema": "marici.fixed-kinematics-bell-pullback.v1",
    "strength": "exact two-fiber variance audit",
    "fixed_fiber_0_bell": str(I0),
    "fixed_fiber_1_bell": str(I1),
    "equal_weight_pushforward_bell": str(Imix),
    "evaluation_naturality_residual": str(sp.simplify(eval0_after-after_eval0)),
    "source_fact": "Sinha-Zahed define the massless outgoing qubits at fixed momenta.",
    "conclusion": (
        "Their theoretical Bell value is a pullback to one kinematic fiber, not an "
        "accepted-event pushforward. Positive base support is required only when "
        "integrating or postselecting over kinematic bins."
    ),
}
canonical=json.dumps(payload,sort_keys=True,separators=(",",":"))
payload["content_sha256"]=hashlib.sha256(canonical.encode()).hexdigest().upper()
out=Path(__file__).parent/"results"/"fixed-kinematics-bell-pullback.json"
out.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")

assert I0 == 2*sqrt2
assert I1 == 8*sqrt2/5
assert Imix == 9*sqrt2/5
assert sp.simplify(eval0_after-after_eval0) == 0
print(json.dumps({"pullback_natural":True,"pushforward_changes_value":True,"sha256":payload["content_sha256"]}))
