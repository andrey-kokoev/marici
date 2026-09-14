#!/usr/bin/env python3
"""Unimodularly anchor the primitive pyramid at the physical e6 vertex."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
lat = json.loads((R / "research/voevodsky/results/split_fiber_primitive_closure.json").read_text())
c3 = json.loads((R / "research/voevodsky/results/C3_local_global_e6_comparison.json").read_text())
mark = json.loads((R / "research/voevodsky/results/infinity_component_picard_marking.json").read_text())
d1,d2,d3,d4 = [sp.Matrix(v) for v in lat["difference_coordinates_in_primitive_frame"]]
b12=(d2-d1)/2
b13=(d3-d1)/2
A=sp.Matrix.hstack(d1,b12,b13)
reconstructed=[d1,d1+2*b12,d1+2*b13,-d1-(d1+2*b12)-(d1+2*b13)]
checks={
    "physical_corner_global_comparison_passed": c3["passed"],
    "infinity_marking_passed": mark["passed"],
    "physical_class_is_primitive": mark["checks"]["difference_primitive"],
    "anchor_edge_matrix_unimodular": abs(int(A.det()))==1,
    "all_vertices_reconstructed": reconstructed==[d1,d2,d3,d4],
    "vertex_relation": sum(reconstructed,sp.zeros(3,1))==sp.zeros(3,1),
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.physical-e6-vertex-anchor.v1",
 "passed":True,
 "anchor":"d1=d_infinity, detected primitively by the physical e6 corner",
 "unimodular_basis":{"d1":[int(q) for q in d1],"beta12":[int(q) for q in b12],"beta13":[int(q) for q in b13],"determinant":int(A.det())},
 "reconstruction":{"d2":"d1+2 beta12","d3":"d1+2 beta13","d4":"-d1-d2-d3"},
 "consequence":"the physical vertex plus two relative edge flows reconstruct the full primitive A1^3 lattice with no index defect",
 "remaining":"construct the rank-two comparison from beta12,beta13 to the de Rham complement of e6 and identify v_alg",
 "checks":checks,
}
p=R/"research/voevodsky/results/physical_e6_vertex_anchor.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"basis_determinant":int(A.det()),"full_lattice_reconstructed":True}))
