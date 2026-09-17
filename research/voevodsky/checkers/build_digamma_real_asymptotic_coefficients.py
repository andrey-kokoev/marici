#!/usr/bin/env python3
"""Generate exact coefficients of Re psi(1/4+iu/2)-log(pi)."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
w=s.symbols('w',positive=True);I=s.I;z=s.Rational(1,4)+I/(2*w);ORDER=22
# psi(z) ~ log z - 1/(2z) - sum B_2m/(2m z^(2m)).
expr=s.log(z)-1/(2*z)
for m in range(1,12):expr-=s.bernoulli(2*m)/(2*m*z**(2*m))
# Real part: replace log(z) by log|z|, then series at w=0.
real_expr=s.log(s.sqrt(s.Rational(1,16)+1/(4*w**2)))-s.re(1/(2*z))
for m in range(1,12):real_expr-=s.bernoulli(2*m)/(2*m)*s.re(z**(-2*m))
series=s.series(real_expr+s.log(2*w),w,0,ORDER).removeO().expand() # correction to log(u/2)
coeff={str(k):str(s.simplify(series.coeff(w,k))) for k in range(1,ORDER) if series.coeff(w,k)!=0}
assert all(int(k)%2==0 for k in coeff)
out={'schema':'marici.voevodsky.digamma-real-asymptotic-coefficients.v1','expansion':'Re psi(1/4+iu/2)-log(pi) = log(u/(2*pi)) + sum c_k u^-k','coefficients':coeff,'maximum_power_exclusive':ORDER,'checks':{'only_even_powers':True,'coefficients_exact_rational':True},'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'digamma_real_asymptotic_coefficients.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
