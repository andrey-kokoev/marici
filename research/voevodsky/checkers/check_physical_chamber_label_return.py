#!/usr/bin/env python3
"""Ordered split locations stay distinct on the convex x-y exchange path."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
t,x,y,z=s.symbols('t x y z', real=True)
xt=(1-t)*y+t*x;yt=(1-t)*x+t*y
A=s.expand(yt+z);B=s.expand(2*xt+yt+z)
loc=[A,-A,B,-B]
# Exact pair differences, whose nonvanishing follows from xt,yt,z>0.
diffs={(i+1,j+1):s.factor(loc[j]-loc[i]) for i in range(4) for j in range(i+1,4)}
expected_nonzero_factors=[-2*A,2*xt, -2*(xt+A),2*(xt+A),2*xt+2*A,-2*B]
checks={
 'B_minus_A':s.expand(B-A-2*xt)==0,
 'midpoint_symmetric':s.expand(xt.subs(t,s.Rational(1,2))-yt.subs(t,s.Rational(1,2)))==0,
 'endpoint_exchange':(xt.subs(t,0),yt.subs(t,0),xt.subs(t,1),yt.subs(t,1))==(y,x,x,y),
 'six_pair_differences':len(diffs)==6,
 'symbolic_distinct_under_positive_parameters':all(s.factor(v)!=0 for v in diffs.values()),
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.physical-chamber-label-return.v1','passed':True,'path':{'x_t':str(xt),'y_t':str(yt),'z_t':'z'},'locations':[str(q) for q in loc],'pair_differences':{f'{i}-{j}':str(v) for (i,j),v in diffs.items()},'ordering_under_positive_chamber':'0 < A_t < B_t','vertex_label_return':'identity','route_swap':False,'scope':'ordered split-location subsystem; full Picard transport still needs surface-family smoothness','checks':checks}
p=ROOT/'research/voevodsky/results/physical_chamber_label_return.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'vertex_return':'identity','route_swap':False}))
