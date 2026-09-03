"""Verify endpoint radicality and determinant mixed-sector polarization."""

import json
from pathlib import Path

import sympy as sp

A, B, t, z = sp.symbols("A B t z", real=True)


def endpoint(a):
    return sp.exp(t / 4) * sp.cosh(a / 2)


def blocks(values):
    k0, ka, kb, kab, kdiff = values
    return (
        sp.Matrix([[k0 + kab, ka + kb], [ka + kb, k0 + kdiff]]),
        sp.Matrix([[k0 - kab, ka - kb], [ka - kb, k0 - kdiff]]),
    )

endpoint_values = [endpoint(a) for a in (0, A, B, A + B, B - A)]
eplus, eminus = blocks(endpoint_values)
endpoint_plus_radical = sp.simplify(sp.expand_trig(eplus.det())) == 0
endpoint_minus_radical = sp.simplify(sp.expand_trig(eminus.det())) == 0

# For symmetric 2x2 matrices, det(X+zY) has a generally nonzero linear
# polarization term; determinant is not additive across source sectors.
x11, x12, x22, y11, y12, y22 = sp.symbols("x11 x12 x22 y11 y12 y22")
X = sp.Matrix([[x11, x12], [x12, x22]])
Y = sp.Matrix([[y11, y12], [y12, y22]])
linear = sp.expand((X + z * Y).det()).coeff(z, 1)
expected = x11 * y22 + x22 * y11 - 2 * x12 * y12
mixed_polarization_verified = sp.expand(linear - expected) == 0
mixed_term_not_identically_zero = expected != 0

result = {
    "schema": "marici.grothendieck.endpoint-rectangle-radical.v1",
    "endpoint_plus_determinant_zero": endpoint_plus_radical,
    "endpoint_minus_determinant_zero": endpoint_minus_radical,
    "determinant_mixed_polarization_verified": mixed_polarization_verified,
    "mixed_term_not_identically_zero": mixed_term_not_identically_zero,
    "all_verified": all(
        (
            endpoint_plus_radical,
            endpoint_minus_radical,
            mixed_polarization_verified,
            mixed_term_not_identically_zero,
        )
    ),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "endpoint-rectangle-radical.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
