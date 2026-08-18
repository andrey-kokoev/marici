"""Generic q_G12 restriction census for the five-pole base-change gate."""

import json
from pathlib import Path

import sympy as sp


c, a, b = sp.symbols("c a b")
X1, X2, X3, P1, P2, P3 = sp.symbols("X1 X2 X3 P1 P2 P3")
CM = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, P2**2, P1**2],
    [1, a**2, P2**2, 0, P3**2],
    [1, b**2, P1**2, P3**2, 0],
])
K = sp.expand(-CM.det() / 2)
E = X1 + X2 + X3
K_G = sp.expand(K.subs(c, -E))

# Each line is represented by solving it for a or b, leaving one coordinate.
lines = {
    "L1": (b, X2 + X3, a),
    "L2": (a, X1 + X3, b),
    "L3": (a, -X3 - b, b),
    "L23": (b, X1, a),
}

samples = [
    {X1: 2, X2: 3, X3: 5, P1: 7, P2: 11, P3: 13},
    {X1: 3, X2: 5, X3: 7, P1: 11, P2: 13, P3: 17},
    {X1: 5, X2: 7, X3: 11, P1: 13, P2: 17, P3: 19},
]

censuses = []
for sample in samples:
    line_data = {}
    for name, (solved, value, residual) in lines.items():
        poly = sp.Poly(sp.expand(K_G.subs(solved, value).subs(sample)), residual)
        gcd = sp.gcd(poly, poly.diff())
        squarefree_degree = poly.degree() - gcd.degree()
        assert poly.degree() == 4
        assert squarefree_degree == 4
        line_data[name] = {
            "degree": poly.degree(),
            "squarefree_degree": squarefree_degree,
            "discriminant_nonzero": sp.discriminant(poly.as_expr(), residual) != 0,
        }
    censuses.append({"sample": {str(k): v for k, v in sample.items()}, "lines": line_data})

# Source order L1,L2,L3,L23. L1 and L23 are parallel on q_G12.
new_finite_intersections = {"L1": 0, "L2": 1, "L3": 2, "L23": 2}
increments = {
    name: 4 + new_finite_intersections[name] - 1 for name in lines
}
restricted_rank = 9 + sum(increments.values())
generic_lower_rank = 34
generic_five_pole_rank = generic_lower_rank + restricted_rank

assert increments == {"L1": 3, "L2": 4, "L3": 5, "L23": 5}
assert restricted_rank == 26
assert generic_five_pole_rank == 60

result = {
    "schema": "marici.generic-five-pole-base-change-rank.v1",
    "samples": censuses,
    "new_finite_intersections": new_finite_intersections,
    "rank_increments": increments,
    "absolute_q_G12_residue_rank": 9,
    "generic_restricted_rank": restricted_rank,
    "generic_lower_rank": generic_lower_rank,
    "generic_five_pole_rank": generic_five_pole_rank,
    "homogeneous_five_pole_rank": 35,
    "rank_drop_on_homogeneous_specialization": generic_five_pole_rank - 35,
}

out = Path(__file__).with_name("generic-five-pole-base-change-rank.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
