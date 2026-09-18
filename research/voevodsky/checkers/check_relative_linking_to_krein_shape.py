#!/usr/bin/env python3
"""Exact rational/complex-pair check of relative-linking quotient shape."""
import json
from fractions import Fraction as Q
from pathlib import Path

def mm(A,B):
 return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((A[i][j]*v[j] for j in range(len(v))),Q(0)) for i in range(len(A))]
def tr(A): return list(map(list,zip(*A)))

O=[[Q(0),Q(1),Q(-1)],[Q(-1),Q(0),Q(1)],[Q(1),Q(-1),Q(0)]]
# Exact generic nonzero rational fixture for derivative loadings and source scalar.
A,B,w=Q(-3,5),Q(7,11),Q(13,17)
P=[[A,0,0],[0,B,0],[0,0,1]]
Op=[[w*x for x in row] for row in mm(mm(P,O),P)]
r=[1/A,1/B,Q(1)]
Q2=[[Op[i][j] for j in range(2)] for i in range(2)]
expected=[[0,w*A*B],[-w*A*B,0]]
# Complex matrices represented as (real,imag). H=iQ2 and S=diag(1,-i).
def cmul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cconj(x):return (x[0],-x[1])
def cmm(X,Y):
 return [[tuple(map(sum,zip(*(cmul(X[i][k],Y[k][j]) for k in range(len(Y)))))) for j in range(len(Y[0]))] for i in range(len(X))]
H=[[(0,x) for x in row] for row in Q2]
S=[[(1,0),(0,0)],[(0,0),(0,-1)]]
Sstar=[[cconj(S[j][i]) for j in range(2)] for i in range(2)]
congr=cmm(cmm(Sstar,H),S)
c=w*A*B
J=[[ (0,0),(c,0)],[(c,0),(0,0)]]
checks={'base_radical':mv(O,[Q(1)]*3)==[0,0,0],'loaded_radical':mv(Op,r)==[0,0,0],'quotient_skew_matrix':Q2==expected,'phase_congruence_to_exchange_metric':congr==J,'coefficient_nonzero':c!=0}
out={'schema':'marici.voevodsky.relative-linking-to-krein-shape.v1','fixture':{'A':str(A),'B':str(B),'omega':str(w)},'loaded_radical':[str(x) for x in r],'quotient_coefficient':str(c),'checks':checks,'passed':all(checks.values()),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'relative_linking_to_krein_shape.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
