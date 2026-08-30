"""Exact typing audit: forward photon-fusion data versus the transverse Bell ratio."""

import hashlib
import json
from pathlib import Path

import sympy as sp


s, t = sp.symbols("s t")
u = -s - t
g2, g3, f2, f3, h3 = sp.symbols("g2 g3 f2 f3 h3")

phi1 = g2 * s**2 + g3 * s**3
phi2 = f2 * (s**2 + t**2 + u**2) + f3 * s * t * u
phi5 = h3 * s * t * u

forward = {t: 0}
transverse = {t: -s / 2}

forward_packet = [sp.expand(q.subs(forward)) for q in (phi1, phi2, phi5)]
transverse_packet = [sp.expand(q.subs(transverse)) for q in (phi1, phi2, phi5)]

assert forward_packet == [g2 * s**2 + g3 * s**3, 2 * f2 * s**2, 0]
assert transverse_packet == [g2 * s**2 + g3 * s**3, sp.Rational(3, 2) * f2 * s**2 + sp.Rational(1, 4) * f3 * s**3, sp.Rational(1, 4) * h3 * s**3]

# Jacobian ranks over the coefficient coordinates make the information loss explicit.
coordinates = (g2, g3, f2, f3, h3)
forward_jacobian = sp.Matrix(forward_packet).jacobian(coordinates)
transverse_jacobian = sp.Matrix(transverse_packet).jacobian(coordinates)
assert forward_jacobian.rank() == 2
assert transverse_jacobian.rank() == 3
assert forward_jacobian[:, 3] == sp.zeros(3, 1)
assert forward_jacobian[:, 4] == sp.zeros(3, 1)
assert transverse_jacobian[:, 3] != sp.zeros(3, 1)
assert transverse_jacobian[:, 4] != sp.zeros(3, 1)

payload = {
    "schema": "marici.breit-wheeler-forward-blindness.v1",
    "basis": {
        "Phi1": str(phi1),
        "Phi2": str(phi2),
        "Phi5": str(phi5),
    },
    "forward_restriction": [str(q) for q in forward_packet],
    "transverse_restriction": [str(q) for q in transverse_packet],
    "forward_kernel_directions": ["f3", "h3"],
    "coefficient_jacobian_ranks": {"forward": 2, "transverse": 3},
    "conclusion": "Forward polarized photon-fusion sum rules cannot reconstruct the transverse Bell ratio because they erase the dimension-ten f3 and h3 directions. Angular-resolved fixed-t absorptive amplitude data, including coherence/phase information, is required.",
    "scope": "Exact photon EFT typing statement through dimension ten; it does not deny that a complete nonforward dispersion construction could recover the amplitudes.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "breit-wheeler-forward-blindness.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"forward_kernel": ["f3", "h3"], "sha256": payload["content_sha256"]}))
