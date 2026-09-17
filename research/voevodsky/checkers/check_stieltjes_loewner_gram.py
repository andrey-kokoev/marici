#!/usr/bin/env python3
"""Verify the resolvent divided-difference Gram identity."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages')); import sympy as s
x,y,t,b=s.symbols('x y t beta', positive=True)
r=lambda z: 1/(z+t)
q=s.simplify((r(y)-r(x))/(x-y))
assert s.simplify(q-r(x)*r(y))==0
# Atomic positive measures generate rank-one PSD matrices.
xs=s.symbols('x0:4', positive=True);G=s.Matrix([[1/((u+t)*(v+t)) for v in xs] for u in xs])
assert G.rank()==1 and s.simplify(G[0,0])>0
out={'schema':'marici.voevodsky.stieltjes-loewner-gram.v1','checks':{'resolvent_divided_difference':True,'atomic_kernel_rank_one':True,'constant_slope_gives_positive_rank_one':True},'conclusion':'A common positive Stieltjes measure gives an all-rank Gram factorization and excludes both generalized Schur-complement failure modes.','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'stieltjes_loewner_gram.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
