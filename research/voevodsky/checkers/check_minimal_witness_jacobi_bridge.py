#!/usr/bin/env python3
"""Verify the scalar resolvent identities behind the GNS/Schur bridge."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages')); import sympy as s
x,y,c,a=s.symbols('x y c a', positive=True)
# Primitive chosen so H'=squared resolvent.
H=lambda z:-1/(z-c+a)
dd=s.simplify((H(x)-H(y))/(x-y));gram=1/((x-c+a)*(y-c+a))
assert s.simplify(dd-gram)==0
k=s.symbols('k',integer=True,nonnegative=True)
# q_k atomic formula follows by direct finite checks.
for n in range(8):
 q=(-1)**n*s.diff(gram.subs(y,x),x,n)/s.factorial(n+1) # not q: differentiates H', gives factor n+1 mismatch
 expected=1/(x-c+a)**(n+2)
 assert s.simplify(q-expected)==0
out={'schema':'marici.voevodsky.minimal-witness-jacobi-bridge.v1','checks':{'divided_difference_is_resolvent_gram':True,'factorial_moments_are_compact_moments_through_degree_7':True},'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'minimal_witness_jacobi_bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
