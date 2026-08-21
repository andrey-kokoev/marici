"""Exact fixed-t crossing and moment adapter for the D10 Bell coefficients."""

import hashlib
import json
from pathlib import Path

import sympy as sp


nu, nup, t, m = sp.symbols("nu nup t m", nonzero=True)
f2, f3, h3 = sp.symbols("f2 f3 h3")
s = nu - t / 2
u = -nu - t / 2

phi2 = sp.expand(f2 * (s**2 + t**2 + u**2) + f3 * s * t * u)
phi5 = sp.expand(h3 * s * t * u)
expected_phi2 = sp.Rational(3, 2) * f2 * t**2 + sp.Rational(1, 4) * f3 * t**3 + nu**2 * (2 * f2 - f3 * t)
expected_phi5 = sp.Rational(1, 4) * h3 * t**3 - nu**2 * h3 * t
assert sp.simplify(phi2 - expected_phi2) == 0
assert sp.simplify(phi5 - expected_phi5) == 0

# Crossing-even fixed-t kernel. Its nu^2 coefficient is the inverse-cubic
# absorptive moment, up to the conventional factor 2/pi.
kernel_even = 2 * nup / (nup**2 - nu**2)
series_even = sp.series(kernel_even, nu, 0, 6).removeO()
assert sp.expand(series_even).coeff(nu, 0) == 2 / nup
assert sp.expand(series_even).coeff(nu, 2) == 2 / nup**3
assert sp.expand(series_even).coeff(nu, 4) == 2 / nup**5

# Two fixed spacelike transfers give an invertible frame for (f2,f3).
t1 = -m**2
t2 = -2 * m**2
M = sp.Matrix([[2, -t1], [2, -t2]])
assert sp.factor(M.det()) == 2 * m**2
C1, C2, H1 = sp.symbols("C1 C2 H1")
rec_f2, rec_f3 = [sp.factor(q) for q in M.inv() * sp.Matrix([C1, C2])]
rec_h3 = sp.factor(-H1 / t1)
assert sp.simplify(rec_f2.subs({C1: 2*f2-f3*t1, C2: 2*f2-f3*t2}) - f2) == 0
assert sp.simplify(rec_f3.subs({C1: 2*f2-f3*t1, C2: 2*f2-f3*t2}) - f3) == 0
assert sp.simplify(rec_h3.subs({H1: -h3*t1}) - h3) == 0

payload = {
    "schema": "marici.fixed-t-dispersive-moment-adapter.v1",
    "crossing_coordinate": "nu=s+t/2; s<->u sends nu->-nu",
    "fixed_t_expansion": {"Phi2": str(expected_phi2), "Phi5": str(expected_phi5)},
    "even_kernel_series": str(series_even),
    "nu2_moment": "C2(t)=(2/pi) integral_{nu0(t)}^infinity Im F_+(nu',t)/nu'^3 dnu'",
    "sample_transfers": ["-m^2", "-2m^2"],
    "coefficient_matrix_determinant": "2*m^2",
    "reconstruction": {"f2": str(rec_f2), "f3": str(rec_f3), "h3": str(rec_h3)},
    "subtraction_gate": "Valid only if the chosen crossing-even amplitude has no independent nu^2 subtraction polynomial. This must be established from QED asymptotics/Ward identities before treating the moment as a theorem.",
    "conclusion": "Conditional on the subtraction gate, two fixed-t inverse-cubic absorptive moments recover f2,f3 and one recovers h3.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "fixed-t-dispersive-moment-adapter.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"conditional_adapter": "passed", "sha256": payload["content_sha256"]}))
