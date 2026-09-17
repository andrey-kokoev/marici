#!/usr/bin/env python3
"""Derive exact Taylor derivatives of D=c0*c2-c1^2 from c_k'=-c_(k+1)."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
N=8;c=s.symbols('c0:'+str(N+3))
def deriv(expr):
 return s.expand(sum(s.diff(expr,c[k])*(-c[k+1]) for k in range(N+2)))
forms=[];x=c[0]*c[2]-c[1]**2
for n in range(7):
 forms.append(s.factor(x));x=deriv(x)
assert forms[1]==c[1]*c[2]-c[0]*c[3]
assert forms[2]==c[0]*c[4]-c[2]**2
out={'schema':'marici.voevodsky.rank-two-determinant-taylor-identities.v1',
 'recurrence':'c_k prime=-c_(k+1)','derivatives':{str(i):str(v) for i,v in enumerate(forms)},
 'checks':{'D0':'c0*c2-c1^2','D1':'c1*c2-c0*c3','D2':'c0*c4-c2^2','identities_exact':True},
 'Taylor_strategy':'Evaluate c0..c_(m+2) once at each center; bound only D^(m+1) on a cell. This preserves determinant cancellation and replaces repeated first-derivative bisection.',
 'passed':True}
p=Path(__file__).parents[1]/'results'/'rank_two_determinant_taylor_identities.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
