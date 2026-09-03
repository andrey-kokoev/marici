"""Verify the sum/difference-coordinate factorization of parity wedges."""

import json
from pathlib import Path

import sympy as sp

A, B, u, v = sp.symbols("A B u v", real=True)
S, D = (A + B) / 2, (B - A) / 2
Wp = sp.cos(S * u) * sp.cos(D * v) - sp.cos(S * v) * sp.cos(D * u)
Wm = sp.sin(S * u) * sp.sin(D * v) - sp.sin(S * v) * sp.sin(D * u)
P = sp.sin(A * (u + v) / 2) * sp.sin(B * (u - v) / 2)
R = sp.sin(B * (u + v) / 2) * sp.sin(A * (u - v) / 2)

checks = {
    "plus_wedge_factorization": sp.trigsimp(sp.expand_trig(Wp + P + R)) == 0,
    "minus_wedge_factorization": sp.trigsimp(sp.expand_trig(Wm + P - R)) == 0,
    "square_sum_identity": sp.expand((P + R) ** 2 + (P - R) ** 2 - 2 * (P**2 + R**2)) == 0,
    "square_difference_identity": sp.expand((P + R) ** 2 - (P - R) ** 2 - 4 * P * R) == 0,
}
result = {
    "schema": "marici.grothendieck.two-prime-wedge-coordinate-factorization.v1",
    **checks,
    "all_verified": all(checks.values()),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "two-prime-wedge-coordinate-factorization.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
