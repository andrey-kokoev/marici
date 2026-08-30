"""Exact counterexample: local polarized rates do not fix a nonforward cut kernel."""

import hashlib
import json
from pathlib import Path

import sympy as sp


# Two initial-helicity components at two distinct pair-production angles.
A = sp.Matrix([1, 2])
B = sp.Matrix([3, 5])

# An angle-dependent final-state phase is invisible to every same-angle Gram
# matrix but changes the cross-angle kernel needed by nonforward unitarity.
phase = sp.I
A_prime = A
B_prime = phase * B

G_A = A * A.conjugate().T
G_B = B * B.conjugate().T
G_A_prime = A_prime * A_prime.conjugate().T
G_B_prime = B_prime * B_prime.conjugate().T

K_AB = A * B.conjugate().T
K_AB_prime = A_prime * B_prime.conjugate().T

assert G_A == G_A_prime
assert G_B == G_B_prime
assert K_AB_prime == -sp.I * K_AB
assert K_AB_prime != K_AB

payload = {
    "schema": "marici.breit-wheeler-local-tomography-obstruction.v1",
    "same_angle_gram_A": [[str(x) for x in row] for row in G_A.tolist()],
    "same_angle_gram_B": [[str(x) for x in row] for row in G_B.tolist()],
    "cross_angle_kernel": [[str(x) for x in row] for row in K_AB.tolist()],
    "transformed_cross_angle_kernel": [[str(x) for x in row] for row in K_AB_prime.tolist()],
    "invisible_gauge": "A(theta) -> exp(i phi(theta)) A(theta)",
    "conclusion": "Arbitrary initial-polarization tomography at each angle fixes diagonal Gram data but not the cross-angle kernel required by a nonforward unitarity relation.",
    "surviving_route": "Add a source-derived cross-angle phase reference, amplitude-level theory input, or a genuinely interferometric final-state measurement; differential rates alone are insufficient.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "breit-wheeler-local-tomography-obstruction.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"cross_kernel_changed": True, "sha256": payload["content_sha256"]}))
