"""Generic chiral lift of the six-scalar alternating-fusion conductor."""

import itertools
import json
from pathlib import Path
import sympy as sp


words = list(itertools.product((0, 1), repeat=6))  # 0=angle, 1=square
generic = [w for w in words if all(w[i] != w[(i + 1) % 6] for i in range(6))]
assert generic == [(0, 1, 0, 1, 0, 1), (1, 0, 1, 0, 1, 0)]

rotate = lambda w: w[1:] + w[:1]
parity = lambda w: tuple(1-v for v in w)
assert all(rotate(w) == parity(w) for w in generic)

# Explicit nonempty momentum-conserving point for the first word.  Adjacent
# pairs alternately share a left and a right spinor.
A, C, E = (sp.Matrix(v) for v in ([1, 0], [0, 1], [1, 1]))
B, D, F = (sp.Matrix(v) for v in ([1, 0], [0, 1], [1, 1]))
coeff = [1, -2, -1, 1, -2, 1]
outer = lambda l, r: l*r.T
p = [
    coeff[0]*outer(A, F), coeff[1]*outer(A, B),
    coeff[2]*outer(C, B), coeff[3]*outer(C, D),
    coeff[4]*outer(E, D), coeff[5]*outer(E, F),
]
assert sum(p, sp.zeros(2)) == sp.zeros(2)
assert all(M.det() == 0 for M in p)
adjacent = [sp.expand((p[i] + p[(i+1) % 6]).det()) for i in range(6)]
next_nearest = [sp.expand((p[i] + p[(i+2) % 6]).det()) for i in range(6)]
assert adjacent == [0]*6
assert all(v != 0 for v in next_nearest)

result = {
    "status": "PASS",
    "generic_spin_words": [list(w) for w in generic],
    "count": len(generic),
    "rotation_equals_parity_on_generic_lift": True,
    "explicit_coefficients": coeff,
    "adjacent_pair_invariants": [int(v) for v in adjacent],
    "next_nearest_invariants": [int(v) for v in next_nearest],
    "conclusion": (
        "The generic chiral normalization of the six-scalar conductor has two "
        "components. One-step scaffold rotation and physical parity exchange "
        "them identically, so the product character is invariant under the "
        "source-defined diagonal action."
    ),
}
out = Path(__file__).parents[1] / "results" / "generic_conductor_spin_lift.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
