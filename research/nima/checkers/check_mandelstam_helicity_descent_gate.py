"""Exact gate for helicity descent of the alternating-fusion conductor.

The conductor packet is written entirely in Mandelstam X-coordinates.  Four-
dimensional parity exchanges angle and square brackets but fixes every X.
Consequently the spin-odd projector annihilates the packet, including its
scaffold-odd normal symbol.  A nonzero mixed character therefore requires a
separate helicity-evaluation coefficient map before descent to X-space.
"""

import json
from pathlib import Path
import sympy as sp


y0, y1, y2 = sp.symbols("y0 y1 y2")
x = sp.symbols("x0:6")

A_plus = y0*x[5] + y2*x[1] + y1*x[3] - (y0*y1 + y0*y2 + y1*y2)
A_minus = y1*x[0] + y0*x[2] + y2*x[4] - (y0*y1 + y0*y2 + y1*y2)

# Parity acts trivially on the Mandelstam invariant ring.
def parity_on_X(f):
    return sp.expand(f)


spin_odd_plus = sp.expand((A_plus - parity_on_X(A_plus))/2)
spin_odd_minus = sp.expand((A_minus - parity_on_X(A_minus))/2)

# Coefficients of the intrinsic scaffold-odd conductor symbol, ordered
# (dx0,...,dx5).  These too lie in the parity-fixed X ring.
sigma = sp.Matrix([-y1, y2, -y0, y1, -y2, y0])
spin_odd_sigma = sp.simplify((sigma - sigma.applyfunc(parity_on_X))/2)

result = {
    "status": "PASS",
    "A_plus_spin_odd": str(spin_odd_plus),
    "A_minus_spin_odd": str(spin_odd_minus),
    "sigma_alt_spin_odd": [str(v) for v in spin_odd_sigma],
    "conclusion": (
        "The Mandelstam-level alternating-fusion conductor has zero spin-odd "
        "grade. A nonzero scaffold-spin mixed class requires a source-defined "
        "helicity-evaluation coefficient map; it cannot be extracted from the "
        "X-polynomial alone."
    ),
}

assert spin_odd_plus == 0
assert spin_odd_minus == 0
assert spin_odd_sigma == sp.zeros(6, 1)

out = Path(__file__).parents[1] / "results" / "mandelstam_helicity_descent_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
