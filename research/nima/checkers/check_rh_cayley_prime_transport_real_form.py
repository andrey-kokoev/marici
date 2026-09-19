#!/usr/bin/env python3
"""Check the fixed Cayley transform of determinant-one prime transport."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as s

x, y = s.symbols("x y", real=True)
w = x + s.I * y

C = s.Matrix([[1, 1], [-s.I, s.I]]) / s.sqrt(2)
J0 = s.I * s.Matrix([[0, 1], [-1, 0]])
J = s.diag(1, -1)
T = s.diag(s.exp(w), s.exp(-w))
R = s.simplify(C * T * C.inv())
expected = s.Matrix(
    [
        [s.cosh(w), s.I * s.sinh(w)],
        [-s.I * s.sinh(w), s.cosh(w)],
    ]
)
R_on_seam = s.simplify(R.subs(x, 0).rewrite(s.sin))
expected_on_seam = s.Matrix(
    [[s.cos(y), -s.sin(y)], [s.sin(y), s.cos(y)]]
)

# The two independent imaginary parts in the first row are
# sinh(x) sin(y) and sinh(x) cos(y). Their squared sum is sinh(x)^2.
imaginary_obstruction = s.simplify(
    s.im(R[0, 0]) ** 2 + s.im(R[0, 1]) ** 2
)

checks = {
    "cayley_identifies_forms": s.simplify(C.conjugate().T * J0 * C - J) == s.zeros(2),
    "transport_formula": s.simplify(R - expected) == s.zeros(2),
    "seam_transport_is_real_rotation": s.simplify(R_on_seam - expected_on_seam) == s.zeros(2),
    "realness_obstruction_is_sinh_x_squared": s.simplify(imaginary_obstruction - s.sinh(x) ** 2) == 0,
    "determinant_one": s.simplify(R.det()) == 1,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-cayley-prime-real-form.v1",
    "spectral_coordinate": "w=(log(p)/2)z=x+i*y",
    "cayley_matrix": [["1/sqrt(2)", "1/sqrt(2)"], ["-i/sqrt(2)", "i/sqrt(2)"]],
    "real_frame_transport": [
        ["cosh(w)", "i*sinh(w)"],
        ["-i*sinh(w)", "cosh(w)"],
    ],
    "on_seam": [["cos(y)", "-sin(y)"], ["sin(y)", "cos(y)"]],
    "imaginary_obstruction": "sinh(x)^2",
    "checks": checks,
    "passed": True,
    "conclusion": "In the fixed Cayley frame, prime transport is real exactly when Re(z)=0.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-cayley-prime-real-form.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
