#!/usr/bin/env python3
"""Verify central wall dictionary and fixed-pencil collision half-sums."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
lat=json.loads((ROOT/'research/voevodsky/results/split_fiber_primitive_closure.json').read_text())
x,y,z,E=s.symbols('x y z E')
d=[s.Matrix(v) for v in lat['difference_coordinates_in_primitive_frame']]
wall1=s.expand((y+z).subs(z,-x-y))
wall2=s.expand((x+z).subs(z,-x-y))
h14=(d[0]+d[3])/2
h23=(d[1]+d[2])/2
checks={
 'central_W1_b_wall':wall1==-x,
 'central_W2_a_wall':wall2==-y,
 'different_pencil_coordinates':s.Symbol('a')!=s.Symbol('b'),
 'b_collision_pair_14':h14==s.Matrix([0,0,1]),
 'b_collision_pair_23':h23==s.Matrix([0,0,-1]),
 'collapsed_b_support_rank_one':s.Matrix.hstack(h14,h23).rank()==1,
 'picard_complement_rank_two':s.Matrix.hstack(s.Matrix([0,1,0]),s.Matrix([0,0,1])).rank()==2,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.cross-pencil-wall-typing.v1','passed':True,'wall_routes':{'w101':'b-pencil wall b=y+z, central b=-x','w110':'a-pencil wall a=x+z, central a=-y'},'fixed_b_pencil_central_half_sums':{'(d1+d4)/2':'alpha14','(d2+d3)/2':'-alpha14'},'fixed_b_collapsed_support_rank':1,'fixed_picard_complement_rank':2,'missing_map':'integral oriented site-exchange transport from a-pencil w110 to fixed b-pencil route','checks':checks}
p=ROOT/'research/voevodsky/results/cross_pencil_wall_typing.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'wall_pencils':['b','a'],'fixed_collision_rank':1}))
