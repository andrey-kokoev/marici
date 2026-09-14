#!/usr/bin/env python3
"""Identify the unique site-exchange odd line in the primitive A1^3 lattice."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
prior = json.loads((R / "research/voevodsky/results/split_fiber_primitive_closure.json").read_text())
d1, d2, d3, d4 = [sp.Matrix(v) for v in prior["difference_coordinates_in_primitive_frame"]]
a12, a13, a14 = (d1+d2)/2, (d1+d3)/2, (d1+d4)/2
beta = (d2-d3)/2
S = sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
G = -2*sp.eye(3)
x, y = sp.symbols("x y")
# Coefficients of e7,e8,e9 after omitting the common x^2 y^2 factor.
v = sp.Matrix([x**2-y**2, 2, -2])
# Site exchange: x<->y and e8<->e9.
v_swapped = sp.Matrix([y**2-x**2, -2, 2])
checks = {
    "exchange_swaps_middle_vertices": S*d2 == d3 and S*d3 == d2,
    "exchange_fixes_endpoint_vertices": S*d1 == d1 and S*d4 == d4,
    "edge_action": S*a12 == a13 and S*a13 == a12 and S*a14 == a14,
    "beta_is_middle_half_difference": beta == a12-a13,
    "beta_integral_primitive": all(q.q == 1 for q in beta) and sp.gcd(*map(abs,beta)) == 1,
    "beta_exchange_odd": S*beta == -beta,
    "beta_square_minus_four": (beta.T*G*beta)[0] == -4,
    "odd_eigenspace_rank_one": (S+sp.eye(3)).rank() == 2,
    "v_alg_exchange_odd": v_swapped == -v,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.site-exchange-v-alg-primitive-line.v1",
    "passed": True,
    "site_exchange_matrix_alpha_frame": [[0,1,0],[1,0,0],[0,0,1]],
    "primitive_odd_generator": [int(q) for q in beta],
    "vertex_formula": "(d2-d3)/2",
    "square": -4,
    "v_alg_character": -1,
    "consequence": "every nonzero equivariant comparison maps the unique primitive odd line to the v_alg line up to one scalar and orientation",
    "remaining": "compute the nonzero integral Betti-de Rham normalization scalar",
    "checks": checks,
}
p = R / "research/voevodsky/results/site_exchange_v_alg_primitive_line.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "primitive_odd_generator": out["primitive_odd_generator"], "v_alg_character": -1}))
