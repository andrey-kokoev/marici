"""Verify the finite signed-measure form of the double-Weil wedge identity."""

import json
from pathlib import Path

import sympy as sp

w = sp.symbols("w0:3", real=True)
x = sp.symbols("x0:3", real=True)
y = sp.symbols("y0:3", real=True)

M = sp.zeros(2)
for j in range(3):
    vector = sp.Matrix([x[j], y[j]])
    M += w[j] * vector * vector.T
G = 2 * M

double_sum = 0
for i in range(3):
    for j in range(3):
        wedge = x[i] * y[j] - x[j] * y[i]
        double_sum += w[i] * w[j] * wedge**2

identity = sp.expand(G.det() - 2 * double_sum) == 0

# Verify the trigonometric conversion of completed kernel entries to parity moments.
A, B, u = sp.symbols("A B u", real=True)
S, D = (A + B) / 2, (B - A) / 2
trig_checks = [
    sp.trigsimp(1 + sp.cos((A + B) * u) - 2 * sp.cos(S * u) ** 2) == 0,
    sp.trigsimp(1 + sp.cos((B - A) * u) - 2 * sp.cos(D * u) ** 2) == 0,
    sp.trigsimp(sp.cos(A * u) + sp.cos(B * u) - 2 * sp.cos(S * u) * sp.cos(D * u)) == 0,
    sp.trigsimp(1 - sp.cos((A + B) * u) - 2 * sp.sin(S * u) ** 2) == 0,
    sp.trigsimp(1 - sp.cos((B - A) * u) - 2 * sp.sin(D * u) ** 2) == 0,
    sp.trigsimp(sp.cos(A * u) - sp.cos(B * u) - 2 * sp.sin(S * u) * sp.sin(D * u)) == 0,
]

result = {
    "schema": "marici.grothendieck.double-weil-wedge-identity.v1",
    "three_atom_signed_measure_identity": identity,
    "parity_trigonometric_identities": trig_checks,
    "all_verified": identity and all(trig_checks),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "double-weil-wedge-identity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
