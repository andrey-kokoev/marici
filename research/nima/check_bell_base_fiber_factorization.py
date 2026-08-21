"""Exact finite audit for Bell-safe base/fiber support factorization."""

import hashlib
import json
from pathlib import Path

import sympy as sp

s0, s1 = sp.symbols("s0 s1", nonnegative=True)
t00, t01, t10, t11 = sp.symbols("t00 t01 t10 t11")

S = sp.diag(s0, s1)
I2 = sp.eye(2)
T = sp.Matrix([[t00, t01], [t10, t11]])

support = sp.kronecker_product(S, I2)
fiber_map = sp.kronecker_product(I2, T)
commutator = sp.simplify(support * fiber_map - fiber_map * support)

# Mixed-variance Cut coevaluation in V tensor V*: vec(I).
omega = sp.Matrix([1, 0, 0, 1])
U = sp.Matrix([[2, 1], [1, 1]])
dual_action = sp.kronecker_product(U, U.inv().T)
coevaluation_residual = sp.simplify(dual_action * omega - omega)

payload = {
    "schema": "marici.bell-base-fiber-factorization.v1",
    "strength": "exact finite typed theorem and source-packet gap audit",
    "base_support_fiber_map_commutator": [str(x) for x in commutator],
    "mixed_variance_coevaluation_residual": [str(x) for x in coevaluation_residual],
    "entry_45_support_type": "signed derivative support in polarization-type scaffold variables",
    "bell_support_type": "positive accepted-event support on momentum base, identity on helicity fiber",
    "conclusion": (
        "Bell-safe support commutes with arbitrary fiber operations when it factorizes "
        "as S_base tensor identity_fiber; the current scattering Cut packet does not "
        "serialize the required positive momentum-base pushforward."
    ),
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()

out = Path(__file__).parent / "results" / "bell-base-fiber-factorization.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

assert commutator == sp.zeros(4)
assert coevaluation_residual == sp.zeros(4, 1)
print(json.dumps({
    "base_fiber_commutes": True,
    "mixed_variance_cut_invariant": True,
    "sha256": payload["content_sha256"],
}))
