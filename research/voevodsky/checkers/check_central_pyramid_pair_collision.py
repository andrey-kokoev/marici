#!/usr/bin/env python3
"""Exact first-order collision of the four split-fiber locations at E=0."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
x,y,z,E=s.symbols('x y z E')
qs=[y+z,-(y+z),2*x+y+z,-(2*x+y+z)]
lift=[s.expand(q.subs(z,-x-y+E)) for q in qs]
central=[s.expand(q.subs(E,0)) for q in lift]
velocities=[s.diff(q,E) for q in lift]
checks={
 "lifted_locations":lift==[-x+E,x-E,x+E,-x-E],
 "central_pair_collision":central==[-x,x,x,-x],
 "q1_equals_q4_centrally":central[0]==central[3],
 "q2_equals_q3_centrally":central[1]==central[2],
 "opposite_velocities_at_plus_x":velocities[1:3]==[-1,1],
 "opposite_velocities_at_minus_x":[velocities[0],velocities[3]]==[1,-1],
 "separation_plus_x":s.expand(lift[2]-lift[1])==2*E,
 "separation_minus_x":s.expand(lift[0]-lift[3])==2*E,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.central-pyramid-pair-collision.v1",
 "passed":True,
 "generic_locations":["y+z","-(y+z)","2x+y+z","-(2x+y+z)"],
 "E_normal_lift":[str(q) for q in lift],
 "central_locations":[str(q) for q in central],
 "collision_pairs":[[1,4],[2,3]],
 "first_velocities":[int(v) for v in velocities],
 "consequence":"E=0 boundary residues cannot distinguish all four Picard vertices",
 "required":"first normal E-jet of the marked v_alg form and antisymmetric collision residues",
 "checks":checks,
}
p=ROOT/"research/voevodsky/results/central_pyramid_pair_collision.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"central_locations":[str(q) for q in central],"velocities":[int(v) for v in velocities]}))
