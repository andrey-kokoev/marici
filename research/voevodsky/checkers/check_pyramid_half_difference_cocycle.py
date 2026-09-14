#!/usr/bin/env python3
"""Exact oriented edge cocycle and index for the four-vertex pyramid."""
import json
from itertools import permutations
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
prior = json.loads((R / "research/voevodsky/results/split_fiber_primitive_closure.json").read_text())
d = [sp.Matrix(v) for v in prior["difference_coordinates_in_primitive_frame"]]
def beta(i,j): return (d[j]-d[i])/2
B = sp.Matrix.hstack(beta(0,1), beta(0,2), beta(0,3))
alpha12 = (d[0]+d[1])/2
B_anchor = sp.Matrix.hstack(beta(0,1), beta(0,2), alpha12)
checks = {
    "all_oriented_edges_integral": all(q.q == 1 for i,j in permutations(range(4),2) for q in beta(i,j)),
    "antisymmetry": all(beta(i,j) == -beta(j,i) for i,j in permutations(range(4),2)),
    "triangle_cocycle": all(beta(i,j)+beta(j,k) == beta(i,k) for i,j,k in permutations(range(4),3)),
    "based_edge_lattice_index_two": abs(int(B.det())) == 2,
    "one_half_sum_anchor_completes_lattice": abs(int(B_anchor.det())) == 1,
    "mod_two_vertices_indistinguishable": len({tuple(int(q)%2 for q in v) for v in d}) == 1,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.pyramid-half-difference-cocycle.v1",
    "passed": True,
    "edge_definition": "beta_ij=(d_j-d_i)/2",
    "based_edges": [[int(q) for q in beta(0,j)] for j in (1,2,3)],
    "edge_flow_lattice_index": 2,
    "anchor": {"class": "alpha12=(d1+d2)/2", "completes_to_index": 1},
    "face_law": "beta_ij+beta_jk+beta_ki=0",
    "interpretation": "relative coherent flow plus one primitive absolute anchor reconstructs A1^3",
    "remaining": "attach the physical e6 corner to an explicit anchor and evaluate v_alg on a transported edge",
    "checks": checks,
}
p = R / "research/voevodsky/results/pyramid_half_difference_cocycle.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "relative_index": 2, "anchored_index": 1}))
