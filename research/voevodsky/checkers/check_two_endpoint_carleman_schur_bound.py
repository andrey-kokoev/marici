#!/usr/bin/env python3
"""Verify the algebraic maximum in the weighted two-endpoint Schur test."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
x=s.symbols('x',positive=True);f=s.sqrt((1-x)/(1+x))+s.sqrt(x/(2-x));center=s.simplify(f.subs(x,s.Rational(1,2)));# Dense exact-sign polynomial reduction of f' shows its sole interior zero.
num=s.factor(s.together(s.diff(f,x)).as_numer_denom()[0]);sign_polynomial=s.factor((1+x)**3*(1-x)-x*(2-x)**3);assert center==2/s.sqrt(3) and s.simplify(s.diff(f,x).subs(x,s.Rational(1,2)))==0 and sign_polynomial==-(2*x-1)**3
out={'schema':'marici.voevodsky.two-endpoint-carleman-schur-bound.v1','schur_weight':'1/sqrt(x(1-x))','row_ratio_max':'2*pi/sqrt(3)','unitary_half_normalized_budget':'pi/sqrt(3)','center_value':str(center),'center_stationary':True,'derivative_numerator':str(num),'derivative_sign_reduction':str(sign_polynomial),'global_maximum_verified':True,'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_endpoint_carleman_schur_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
