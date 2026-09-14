#!/usr/bin/env python3
"""Identify the normalized collision-jet sign pattern as the alpha12 covector."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
lat=json.loads((ROOT/'research/voevodsky/results/split_fiber_primitive_closure.json').read_text())
jet=json.loads((ROOT/'research/voevodsky/results/split_fiber_first_normal_jet.json').read_text())
d=[s.Matrix(v) for v in lat['difference_coordinates_in_primitive_frame']]
# Order d1,d2,d3,d4; normalize the square-root jets by 2xy.
values=s.Matrix([-1,-1,1,1])
D=s.Matrix.hstack(*d).T
sol=s.linsolve((D,values));q=next(iter(sol));qv=s.Matrix(q)
checks={
 'prior_lattice':lat['passed'],
 'prior_jet':jet['passed'],
 'covector_unique':len(q)==3 and not any(v.free_symbols for v in q),
 'covector_alpha12':qv==s.Matrix([-1,0,0]),
 'all_vertex_values':D*qv==values,
 'primitive':s.gcd_list(list(qv))==1,
 'kernel_rank_two':len((qv.T).nullspace())==2,
 'kernel_alpha13_alpha14':(qv.T).nullspace()==[s.Matrix([0,1,0]),s.Matrix([0,0,1])],
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.normal-jet-e6-covector.v1','passed':True,'normalized_vertex_values':list(map(int,values)),'covector_alpha_frame':list(map(int,qv)),'identified_response':'e6, by the universal primitive two-wall filtered residue theorem','kernel':['alpha13','alpha14'],'remaining':'one primitive v_alg covector on the rank-two kernel','checks':checks}
p=ROOT/'research/voevodsky/results/normal_jet_e6_covector.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'e6_covector':out['covector_alpha_frame'],'kernel':out['kernel']}))
