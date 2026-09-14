#!/usr/bin/env python3
"""Exact lattice selected by the b-reflection orbit of the physical vertex."""
import json
from pathlib import Path
import sympy as sp

R=Path(__file__).resolve().parents[3]
rb=json.loads((R/"research/voevodsky/results/b_reflection_fixed_pencil_transport.json").read_text())
M=sp.Matrix(rb["alpha_frame_action"])
d1=sp.Matrix([1,1,1]);d2=M*d1
ainv=(d1+d2)/2
borbit=(d1-d2)/2
bperp=sp.Matrix([0,1,-1])
G=-2*sp.eye(3)
A=sp.Matrix.hstack(ainv,borbit,bperp)
checks={
 "reflected_vertex_d2":d2==sp.Matrix([1,-1,-1]),
 "orbit_sum_alpha12":ainv==sp.Matrix([1,0,0]),
 "orbit_difference":borbit==sp.Matrix([0,1,1]),
 "orbit_directions_orthogonal":(ainv.T*G*borbit)[0]==0,
 "squares":((ainv.T*G*ainv)[0],(borbit.T*G*borbit)[0],(bperp.T*G*bperp)[0])==(-2,-4,-4),
 "transverse_not_in_orbit_plane":sp.Matrix.hstack(ainv,borbit,bperp).rank()==3,
 "three_direction_index_two":abs(int(A.det()))==2,
 "both_nonfixed_directions_odd":M*borbit==-borbit and M*bperp==-bperp,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.reflected-physical-vertex-orbit.v1",
 "passed":True,
 "physical_vertex":[1,1,1],
 "reflected_vertex":[int(q) for q in d2],
 "orbit_invariant":[int(q) for q in ainv],
 "orbit_odd":[int(q) for q in borbit],
 "transverse_odd":[int(q) for q in bperp],
 "orbit_plane_rank":2,
 "full_three_direction_index":2,
 "next_test":"compute the (e6,v_alg) period column of the reflected physical vertex d2",
 "decision_rule":"nonzero v_alg places the physical response on the orbit plane; zero requires a transverse source",
 "checks":checks,
}
p=R/"research/voevodsky/results/reflected_physical_vertex_orbit.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"orbit_plane_rank":2,"next_test":out["next_test"]}))
