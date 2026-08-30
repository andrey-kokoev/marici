"""Exact 2x2-bispinor model of one scalar-scaffold fusion node."""

import json
from pathlib import Path
import sympy as sp


def outer(a, b):
    return sp.Matrix(a) * sp.Matrix(b).T


t = sp.symbols("t", nonzero=True)
l0, l1, a0, a1, b0, b1 = sp.symbols("l0 l1 a0 a1 b0 b1")
lam = sp.Matrix([l0, l1])
ta = sp.Matrix([a0, a1])
tb = sp.Matrix([b0, b1])

# Angle branch: lambda_b=t lambda_a.
p_a = outer(lam, ta)
p_b = outer(t*lam, tb)
q_angle = sp.expand(p_a + p_b)
eps_angle = sp.expand(p_b - p_a)

# Square branch is the transpose/parity image with independent left spinors.
q_square = q_angle.T
eps_square = eps_angle.T

def rank_one(M):
    return sp.expand(M.det()) == 0


assert rank_one(q_angle) and rank_one(eps_angle)
assert rank_one(q_square) and rank_one(eps_square)
assert q_square == q_angle.T and eps_square == eps_angle.T

# Exchanging the two scalar labels fixes q and negates epsilon.  It does not
# transpose the bispinor and hence does not exchange the spin branches.
q_swapped = sp.expand(p_b + p_a)
eps_swapped = sp.expand(p_a - p_b)
assert q_swapped == q_angle
assert eps_swapped == -eps_angle

result = {
    "status": "PASS",
    "angle_branch": {
        "q_rank_one": rank_one(q_angle),
        "epsilon_rank_one": rank_one(eps_angle),
        "shared_spinor_side": "left",
    },
    "square_branch": {
        "q_rank_one": rank_one(q_square),
        "epsilon_rank_one": rank_one(eps_square),
        "shared_spinor_side": "right",
    },
    "parity_action": "matrix transpose exchanges the two branches",
    "scalar_label_swap": "q fixed, epsilon negated, branch not exchanged",
    "conclusion": "spin parity and scaffold-label exchange are independent source involutions",
}

out = Path(__file__).parents[1] / "results" / "spinor_scaffold_source_normalization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
