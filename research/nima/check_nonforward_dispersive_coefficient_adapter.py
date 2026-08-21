"""Exact fixed-energy angular adapter for the D10 photon Bell coefficients."""

import hashlib
import json
from pathlib import Path

import sympy as sp


s = sp.symbols("s", nonzero=True)
f2, f3, h3 = sp.symbols("f2 f3 h3")
x = sp.symbols("x")  # x=t/s, with u/s=-1-x

F = sp.expand(1 + x**2 + (1 + x) ** 2)
T = sp.expand(-x * (1 + x))
phi2 = sp.expand(s**2 * F * f2 + s**3 * T * f3)
phi5 = sp.expand(s**3 * T * h3)

# Use two generic nonforward angles. Neither selection is derived from the Bell
# condition; they are simply a minimal interpolation frame.
x1 = sp.Rational(-1, 2)
x2 = sp.Rational(-1, 3)
M = sp.Matrix(
    [
        [s**2 * F.subs(x, x1), s**3 * T.subs(x, x1)],
        [s**2 * F.subs(x, x2), s**3 * T.subs(x, x2)],
    ]
)
det_M = sp.factor(M.det())
assert det_M == -s**5 / 18

Y1, Y2, Z1 = sp.symbols("Y1 Y2 Z1")
recovered_f2, recovered_f3 = [sp.factor(q) for q in M.inv() * sp.Matrix([Y1, Y2])]
recovered_h3 = sp.factor(Z1 / (s**3 * T.subs(x, x1)))

assert sp.simplify(recovered_f2.subs({Y1: phi2.subs(x, x1), Y2: phi2.subs(x, x2)}) - f2) == 0
assert sp.simplify(recovered_f3.subs({Y1: phi2.subs(x, x1), Y2: phi2.subs(x, x2)}) - f3) == 0
assert sp.simplify(recovered_h3.subs({Z1: phi5.subs(x, x1)}) - h3) == 0

payload = {
    "schema": "marici.nonforward-fixed-energy-coefficient-adapter.v2",
    "angular_coordinate": "x=t/s, u/s=-1-x",
    "samples": [str(x1), str(x2)],
    "phi2_design_matrix": [[str(q) for q in row] for row in M.tolist()],
    "determinant": str(det_M),
    "reconstruction": {
        "f2": str(recovered_f2),
        "f3": str(recovered_f3),
        "h3": str(recovered_h3),
    },
    "conclusion": "At one fixed nonzero energy, two Phi2 angles and one Phi5 angle recover the D10 transverse coefficient directions from amplitude-level data with coherent phase transport.",
    "boundary": "This is fixed-energy angular interpolation, not a fixed-t dispersion relation. The latter must use nu=s+t/2 and hold t fixed while nu varies.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "nonforward-dispersive-coefficient-adapter.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"determinant": str(det_M), "sha256": payload["content_sha256"]}))
