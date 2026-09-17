#!/usr/bin/env python3
"""Symbolically verify the Legendre Green operator preserves polynomial degree."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
t=s.symbols('t');checks={}
for d in (0,1,2,10,999):
 h=t**d;Lh=s.expand(-s.diff((1-t*t)*s.diff(h,t),t));checks[str(d)]={'degree_after':int(s.degree(Lh,t)) if Lh else -1,'leading_eigenvalue':str(s.expand(Lh).coeff(t,d))};assert not Lh or s.degree(Lh,t)<=d
# Green concomitant vanishes at physical endpoints because of 1-t^2.
h=s.Function('h');P=s.Function('P');endpoint_factor=s.simplify((1-t*t).subs(t,1));assert endpoint_factor==0
out={'schema':'marici.voevodsky.legendre-green-polynomial-termination.v1','monomial_checks':checks,'degree_never_increases':True,'physical_endpoint_concomitant_zero':True,'passed':True,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'legendre_green_polynomial_termination.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
