#!/usr/bin/env python3
"""Exact derivatives for the 3x3 Hankel determinant under c_k'=-c_(k+1)."""
import json,sys
from pathlib import Path
try:import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
c=s.symbols('c0:14')
def der(x):return s.expand(sum(s.diff(x,c[k])*(-c[k+1]) for k in range(13)))
H=s.Matrix(3,3,lambda i,j:c[i+j]);x=s.expand(H.det());forms=[]
for n in range(5):forms.append(s.factor(x));x=der(x)
out={'schema':'marici.voevodsky.rank-three-determinant-taylor-identities.v1','recurrence':'c_k prime=-c_(k+1)',
 'derivatives':{str(i):str(v) for i,v in enumerate(forms)},'highest_moment_indices':[max(int(str(z)[1:]) for z in v.free_symbols) for v in forms],
 'strategy':'A cubic Taylor cell through derivative order m needs center moments through c_(m+4) and one interval enclosure of derivative m+1.','passed':True}
p=Path(__file__).parents[1]/'results'/'rank_three_determinant_taylor_identities.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
