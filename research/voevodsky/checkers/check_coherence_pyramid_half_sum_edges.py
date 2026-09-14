#!/usr/bin/env python3
"""Exact primitive edge structure of the four split-fiber pyramid."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
prior = json.loads((R / "research/voevodsky/results/split_fiber_primitive_closure.json").read_text())
# Coordinates in the established alpha12,alpha13,alpha14 frame.
d = [sp.Matrix(v) for v in prior["difference_coordinates_in_primitive_frame"]]
a12 = (d[0] + d[1]) / 2
a13 = (d[0] + d[2]) / 2
a14 = (d[0] + d[3]) / 2
a23 = (d[1] + d[2]) / 2
a24 = (d[1] + d[3]) / 2
a34 = (d[2] + d[3]) / 2
G = -2 * sp.eye(3)
A = sp.Matrix.hstack(a12, a13, a14)
checks = {
    "vertex_sum_zero": sum(d, sp.zeros(3, 1)) == sp.zeros(3, 1),
    "all_half_sums_integral": all(v.q == 1 for a in (a12,a13,a14,a23,a24,a34) for v in a),
    "opposite_edges_are_negatives": a12 == -a34 and a13 == -a24 and a14 == -a23,
    "adjacent_edges_form_basis": abs(int(A.det())) == 1,
    "edge_gram_A1_cubed": A.T * G * A == -2 * sp.eye(3),
    "repeated_middle_pair_is_one_primitive_edge": a23 == -a14,
    "prior_index_four": prior["index_of_difference_lattice"] == 4,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.coherence-pyramid-half-sum-edges.v1",
    "passed": True,
    "vertices": [list(map(int, v)) for v in d],
    "primitive_edges": {
        "alpha12": [int(v) for v in a12],
        "alpha13": [int(v) for v in a13],
        "alpha14": [int(v) for v in a14],
        "alpha23": [int(v) for v in a23],
    },
    "opposite_edge_relations": ["alpha12=-alpha34", "alpha13=-alpha24", "alpha14=-alpha23"],
    "primitive_lattice": "A1^3",
    "information_flow": "two labelled vertex differences -> integral half-sum edge -> primitive lattice coordinate -> readout",
    "remaining": "label energy punctures by oriented d_i and compare two independent primitive edges with e6 and v_alg",
    "checks": checks,
}
p = R / "research/voevodsky/results/coherence_pyramid_half_sum_edges.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "carrier": "A1^3", "middle_pair_edge": out["primitive_edges"]["alpha23"]}))
