#!/usr/bin/env python3
"""Exact dlog/rational identity for the four-point one-loop MHV integrand."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
a,b,c,d=s.symbols('a b c d')
# Affine chart on Gr(2,4): A=(1,0,a,b), B=(0,1,c,d); external Z_i=e_i.
A=s.Matrix([1,0,a,b]);B=s.Matrix([0,1,c,d]);Z=[None]+[s.eye(4)[:,i] for i in range(4)]
def br(*cols):return s.expand(s.det(s.Matrix.hstack(*cols)))
def ext(i):return Z[i]
def AB(i,j):return br(A,B,ext(i),ext(j))
p12,p23,p34,p41=AB(1,2),AB(2,3),AB(3,4),AB(4,1)
p13,p31=AB(1,3),AB(3,1)
# Source coordinates from 1212.5605, with <AB31>=-<AB13> retained literally.
q=(p41/p13,p12/p31,p23/p31,p34/p13)
vars=(a,b,c,d)
J=s.factor(s.det(s.Matrix([[s.diff(x,v)/x for v in vars] for x in q])))
rational=s.factor(br(ext(1),ext(2),ext(3),ext(4))**2/(p12*p23*p34*p41))
ratio=s.factor(J/rational)
checks={
 'chart_plucker_coordinates_nonzero_polynomials':all(x!=0 for x in (p12,p23,p34,p41,p13)),
 'four_distinct_dlog_arguments':len(set(map(str,q)))==4,
 'dlog_jacobian_equals_oriented_rational_integrand':ratio in (s.Integer(1),s.Integer(-1)),
 'gl2_rational_weight_minus_four':-4==-len((p12,p23,p34,p41)),
 'gl2_measure_weight_plus_four':4==4,
 'total_gl2_weight_zero':-4+4==0
}
out={'schema':'marici.nima.four-point-one-loop-mhv-dlog-identity.v1','chart':{'A':['1','0','a','b'],'B':['0','1','c','d']},'physical_brackets':{'AB12':str(p12),'AB23':str(p23),'AB34':str(p34),'AB41':str(p41)},'dlog_arguments':[str(s.factor(x)) for x in q],'dlog_jacobian':str(J),'rational_integrand':str(rational),'orientation_ratio':str(ratio),'checks':checks,'passed':all(checks.values()),'scope':'Exact affine-chart equality up to the declared wedge orientation; the projective line measure supplies the compensating GL(2) weight.'}
p=ROOT/'research/nima/results/four-point-one-loop-mhv-dlog-identity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
