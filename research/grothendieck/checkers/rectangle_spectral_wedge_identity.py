"""Symbolically verify the parity rank-one and two-frequency wedge identities."""

import json
from pathlib import Path

import sympy as sp

A, B, g1, g2, w1, w2 = sp.symbols("A B g1 g2 w1 w2", real=True)


def vectors(g):
    return (
        sp.Matrix([sp.cos(g * (A + B) / 2), sp.cos(g * (B - A) / 2)]),
        sp.Matrix([sp.sin(g * (A + B) / 2), sp.sin(g * (B - A) / 2)]),
    )


def parity_blocks(g):
    r, s = sp.cos(g * A), sp.cos(g * B)
    c, d = sp.cos(g * (A + B)), sp.cos(g * (B - A))
    return sp.Matrix([[1 + c, r + s], [r + s, 1 + d]]), sp.Matrix(
        [[1 - c, r - s], [r - s, 1 - d]]
    )

X1, U1 = vectors(g1)
X2, U2 = vectors(g2)
P1, M1 = parity_blocks(g1)
rank_one_plus = sp.simplify(sp.expand_trig(P1 - 2 * X1 * X1.T)) == sp.zeros(2)
rank_one_minus = sp.simplify(sp.expand_trig(M1 - 2 * U1 * U1.T)) == sp.zeros(2)

Z = w1 + w2
Pmix = 2 * (w1 * X1 * X1.T + w2 * X2 * X2.T) / Z
Mmix = 2 * (w1 * U1 * U1.T + w2 * U2 * U2.T) / Z
wedge_plus = 4 * w1 * w2 * (X1[0] * X2[1] - X2[0] * X1[1]) ** 2 / Z**2
wedge_minus = 4 * w1 * w2 * (U1[0] * U2[1] - U2[0] * U1[1]) ** 2 / Z**2
mixture_plus = sp.simplify(Pmix.det() - wedge_plus) == 0
mixture_minus = sp.simplify(Mmix.det() - wedge_minus) == 0

result = {
    "schema": "marici.grothendieck.rectangle-spectral-wedge-identity.v1",
    "rank_one_plus_verified": rank_one_plus,
    "rank_one_minus_verified": rank_one_minus,
    "two_frequency_wedge_plus_verified": mixture_plus,
    "two_frequency_wedge_minus_verified": mixture_minus,
    "all_verified": all((rank_one_plus, rank_one_minus, mixture_plus, mixture_minus)),
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "rectangle-spectral-wedge-identity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
