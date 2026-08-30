"""Exact four-phase reconstruction of a cross-angle Breit-Wheeler kernel."""

import hashlib
import json
from pathlib import Path

import sympy as sp


# Scalar components suffice; the construction applies entrywise to a helicity
# matrix after fixing the incoming Stokes preparation and outgoing spin channel.
x, y, u, v = sp.symbols("x y u v", real=True)
A = x + sp.I * y
B = u + sp.I * v
K = sp.expand(A * sp.conjugate(B))

def intensity(zeta):
    return sp.expand((A + zeta * B) * sp.conjugate(A + zeta * B))

P0 = intensity(1)
Ppi = intensity(-1)
Ppi2 = intensity(sp.I)
P3pi2 = intensity(-sp.I)

reconstructed_re = sp.simplify((P0 - Ppi) / 4)
reconstructed_im = sp.simplify((Ppi2 - P3pi2) / 4)

assert sp.simplify(reconstructed_re - sp.re(K)) == 0
assert sp.simplify(reconstructed_im - sp.im(K)) == 0
assert sp.simplify(reconstructed_re + sp.I * reconstructed_im - K) == 0

payload = {
    "schema": "marici.breit-wheeler-cross-angle-interferometer.v1",
    "settings": ["0", "pi", "pi/2", "3pi/2"],
    "reconstruction": {
        "ReK": "(P_0-P_pi)/4",
        "ImK": "(P_pi/2-P_3pi/2)/4",
        "K": "ReK+i ImK",
    },
    "kernel": str(K),
    "required_resource": "Coherent unitary recombination of two distinct outgoing e+e- momentum modes before detection, with a controlled relative phase.",
    "typing": "This measures a cross-angle amplitude kernel; independent angular rate bins do not.",
    "scope": "Algebraic sufficiency only. It does not establish that a practical MeV charged-particle interferometer can preserve the required coherence.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "breit-wheeler-cross-angle-interferometer.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"four_phase_reconstruction": "passed", "sha256": payload["content_sha256"]}))
