#!/usr/bin/env python3
"""Symbolically verify the divided-difference derivatives used in the stationarity note."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages')); import sympy as s
x,y=s.symbols('x y');R=s.Function('R');q=(R(y)-R(x))/(x-y)
dq=s.diff(q,x)
claimed=(-(x-y)*s.diff(R(x),x)-R(y)+R(x))/(x-y)**2
assert s.simplify(dq-claimed)==0
h,R0,R1,R2,R3=s.symbols('h R0 R1 R2 R3')
# Taylor-jet substitution avoids asking SymPy to expand an unspecified function.
jet=R0+R1*h+R2*h**2/2+R3*h**3/6
confluent=s.limit(R1/h-(jet-R0)/h**2,h,0)
assert s.simplify(confluent+R2/2)==0
# Exact nonsingular block determinant/Schur-complement identity.
a11,a12,a22,b1,b2,d=s.symbols('a11 a12 a22 b1 b2 d')
A=s.Matrix([[a11,a12],[a12,a22]]);b=s.Matrix([b1,b2]);Q=A.row_join(b).col_join(s.Matrix([[b1,b2,d]]))
assert s.simplify(Q.det()-A.det()*(d-(b.T*A.inv()*b)[0]))==0
out={'schema':'marici.voevodsky.minimal-loewner-stationarity.v1','checks':{'off_diagonal_derivative':True,'confluent_derivative':True,'block_schur_identity':True},'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'minimal_loewner_stationarity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
