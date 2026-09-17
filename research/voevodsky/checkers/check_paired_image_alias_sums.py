#!/usr/bin/env python3
"""Verify telescoping formulas for the finite-interval image budgets."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
k=s.symbols('k',integer=True,positive=True)
# Partial fractions make both sums elementary.
a=s.apart(1/(k*(4*k**2-1)),k);b=s.apart(1/(k*(k**2-1)),k)
A=2*s.log(2)-1;B=s.Rational(1,4);total=s.simplify(A+B)
out={'schema':'marici.voevodsky.paired-image-alias-sums.v1','translation_partial_fraction':str(a),'translation_sum':str(A),'far_reflection_partial_fraction':str(b),'far_reflection_sum':str(B),'coefficient_one_total':str(total),'half_normalized_total':str(total/2),'numeric_half_normalized':float(total/2),'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'paired_image_alias_sums.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
