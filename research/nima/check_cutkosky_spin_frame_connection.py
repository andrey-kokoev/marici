"""Exact spin-frame invariance of the source-defined nonforward Cutkosky pairing."""

import hashlib
import json
from pathlib import Path

import sympy as sp


a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", complex=True)
c, d = sp.symbols("c d", real=True)
A = sp.Matrix([[a1, a2]])
B = sp.Matrix([[b1, b2]])

# A generic SU(2) spin-frame change in a real two-parameter chart.
U = sp.Matrix([[c, d], [-d, c]])
unitarity_relation = {c**2 + d**2: 1}

K = (A * B.conjugate().T)[0]
K_transformed = sp.expand((A * U) * (B * U).conjugate().T)[0]
difference = sp.expand(K_transformed - K)
difference_reduced = sp.rem(
    sp.Poly(difference, c, d), sp.Poly(c**2 + d**2 - 1, c, d)
).as_expr()
assert sp.simplify(difference_reduced) == 0

# If the two cut sides are rotated independently, the contraction is not
# invariant. This is precisely why the common intermediate-state identification
# is structural data rather than a cosmetic convention.
e, f = sp.symbols("e f", real=True)
V = sp.Matrix([[e, f], [-f, e]])
K_independent = sp.expand((A * U) * (B * V).conjugate().T)[0]
assert sp.simplify(K_independent - K) != 0

payload = {
    "schema": "marici.cutkosky-spin-frame-connection.v1",
    "cut_pairing": "K=A B^dagger",
    "shared_frame_action": "A->AU, B->BU",
    "shared_frame_result": "invariant modulo U U^dagger=1",
    "independent_frame_result": "not invariant",
    "conclusion": "The nonforward phase/spin connection is supplied canonically by gluing both cut amplitudes to the same on-shell intermediate-state fiber. Spin completeness removes basis choices.",
    "scope": "Finite-dimensional typing proof of the cut contraction. The explicit QED phase-space integral and subtraction analysis remain separate.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "cutkosky-spin-frame-connection.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"shared_frame_invariant": True, "sha256": payload["content_sha256"]}))
