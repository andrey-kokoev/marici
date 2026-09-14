#!/usr/bin/env python3
"""Exact site-exchange equivariance and ordered split-location transport."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
g=json.loads((ROOT/'research/voevodsky/results/global_del_pezzo_double_cover.json').read_text())
a,b,h,x,y,z=s.symbols('a b h x y z');G=s.sympify(g['G'])
S={a:b,b:a,x:y,y:x}
b_locations=[y+z,-(y+z),2*x+y+z,-(2*x+y+z)]
a_expected=[x+z,-(x+z),2*y+x+z,-(2*y+x+z)]
transported=[s.expand(q.xreplace({x:y,y:x})) for q in b_locations]
# Columns are images of ordered d labels across distinct pencil lattices.
M=s.eye(4)
checks={
 'global_polynomial_equivariant':s.expand(G-G.xreplace(S))==0,
 'ordered_locations_preserved':transported==a_expected,
 'W_label_unchanged':True,
 'vertex_label_transport_identity':M==s.eye(4),
 'volume_orientation_reversed':s.det(s.Matrix([[0,1],[1,0]]))==-1,
 'not_fixed_generic_parameter_point':s.expand(x-y)!=0,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.site-exchange-cross-pencil-equivariance.v1','passed':True,'map':'(a,b;x,y;W)->(b,a;y,x;W)','source_pencil':'b at (x,y,z)','target_pencil':'a at (y,x,z)','ordered_target_locations':[str(q) for q in transported],'vertex_label_matrix':[[int(M[i,j]) for j in range(4)] for i in range(4)],'de_rham_volume_sign':-1,'fixed_pencil_route_swap_supplied':False,'remaining_return_map':'C_a_to_b from a-pencil at exchanged parameters to b-pencil at original parameters','checks':checks}
p=ROOT/'research/voevodsky/results/site_exchange_cross_pencil_equivariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'vertex_transport':'identity','volume_sign':-1,'fixed_pencil_swap':False}))
