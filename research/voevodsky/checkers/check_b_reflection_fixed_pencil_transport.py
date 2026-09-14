#!/usr/bin/env python3
"""Exact action of global b-reflection on four split-fiber vertices."""
import json
from pathlib import Path
import sympy as sp

R=Path(__file__).resolve().parents[3]
global_surface=json.loads((R/"research/voevodsky/results/global_del_pezzo_double_cover.json").read_text())
lat=json.loads((R/"research/voevodsky/results/split_fiber_primitive_closure.json").read_text())
d=[sp.Matrix(v) for v in lat["difference_coordinates_in_primitive_frame"]]
# Vertex permutation (12)(34), represented on alpha coordinates by solving images.
P=[d[1],d[0],d[3],d[2]]
A=sp.Matrix.hstack((d[0]+d[1])/2,(d[0]+d[2])/2,(d[0]+d[3])/2)
images=sp.Matrix.hstack((P[0]+P[1])/2,(P[0]+P[2])/2,(P[0]+P[3])/2)
M=A.inv()*images
G=-2*sp.eye(3)
checks={
 "global_b_reflection_constructed":global_surface["checks"]["b_reflection_global"],
 "vertex_relation_preserved":sum(P,sp.zeros(3,1))==sp.zeros(3,1),
 "alpha_action_diag_plus_minus_minus":M==sp.diag(1,-1,-1),
 "integral_isometry":M.T*G*M==G,
 "involution":M*M==sp.eye(3),
 "fixed_rank_one":(M-sp.eye(3)).nullspace()==[sp.Matrix([1,0,0])],
 "odd_rank_two":len((M+sp.eye(3)).nullspace())==2,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.b-reflection-fixed-pencil-transport.v1",
 "passed":True,
 "global_map":"[a:b:h:W] -> [a:-b:h:W]",
 "pencil_base_action":"q=b/h -> -q",
 "vertex_permutation":"(d1 d2)(d3 d4)",
 "alpha_frame_action":[[int(M[i,j]) for j in range(3)] for i in range(3)],
 "character_split":{"fixed":["alpha12"],"odd":["alpha13","alpha14"]},
 "remaining":"identify e6 and v_alg within the +1 and rank-two -1 character sectors using source period columns",
 "checks":checks,
}
p=R/"research/voevodsky/results/b_reflection_fixed_pencil_transport.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"vertex_permutation":"(12)(34)","characters":[1,-1,-1]}))
