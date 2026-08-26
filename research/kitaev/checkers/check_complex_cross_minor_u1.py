import hashlib
import json
from pathlib import Path

import sympy as sp


I = sp.I
M0 = sp.Matrix([[2, sp.Rational(1, 2)], [sp.Rational(1, 2), 1]])
M1 = sp.Matrix([[2, -I / 2], [I / 2, 1]])


def invariants(matrix):
    a, z, d = matrix[0, 0], matrix[0, 1], matrix[1, 1]
    t = sp.simplify(a + d)
    determinant = sp.simplify(matrix.det())
    q = sp.simplify(a - d)
    cross = sp.simplify(z * sp.conjugate(z))
    radius = sp.simplify(t**2 - 4 * determinant)
    return t, determinant, q, cross, radius


inv0 = invariants(M0)
inv1 = invariants(M1)
assert inv0 == inv1 == (3, sp.Rational(7, 4), 1, sp.Rational(1, 4), 2)
assert all(minor > 0 for minor in (M0[0, 0], M0.det(), M1[0, 0], M1.det()))
assert sp.simplify(inv0[3] - (inv0[4] - inv0[2] ** 2) / 4) == 0
assert M0[0, 1] != M1[0, 1]

payload = {
    "status": "pass",
    "theorem": "complex_cross_minor_needs_u1_frame",
    "shared_invariants": {
        "trace": "3",
        "determinant": "7/4",
        "longitudinal_q": "1",
        "cross_minor_abs_z_squared": "1/4",
        "bloch_radius_squared": "2",
    },
    "off_diagonal_witnesses": ["1/2", "-I/2"],
    "residual_frame": "U(1)",
    "real_restriction": "C2",
    "theta_application_frozen": True,
}
encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(encoded.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "complex-cross-minor-u1.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
