#!/usr/bin/env python3
"""Exact symbolic ledger for the paired odd-periodization constants."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
k,K=s.symbols('k K',integer=True,positive=True)
one=s.Integer(1);trans_pf=s.apart(one/(k*(4*k**2-1)),k);refl_pf=s.apart(one/(k*(k**2-1)),k);trans=2*s.log(2)-1;refl=s.Rational(1,4);tel=s.simplify(s.summation(s.Rational(1,2)/k-s.Rational(1,2)/(k+1),(k,1,K)));boundary=s.pi/s.sqrt(3)+s.Rational(1,2)*(trans+refl)
assert s.simplify(trans_pf-(one/(2*k+1)+one/(2*k-1)-one/k))==0
assert s.simplify(refl_pf-(one/(2*(k+1))+one/(2*(k-1))-one/k))==0
assert s.simplify(tel-K/(2*(K+1)))==0
assert s.simplify(boundary-(s.pi/s.sqrt(3)+s.log(2)-s.Rational(3,8)))==0
out={'schema':'marici.voevodsky.distributional-image-ledger.v1','translation_alias_sum':str(trans),'far_reflection_sum':str(refl),'finite_telescoping_constant':str(tel),'telescoping_limit':'1/2','half_normalized_boundary_budget':str(boundary),'rank_one_orientation':'positive in K_zero-K_D; discarded in lower bound','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'distributional_image_ledger.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
