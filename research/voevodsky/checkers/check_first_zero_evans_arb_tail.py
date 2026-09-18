#!/usr/bin/env python3
"""Validated 30..60 quadrature and explicit Stirling/Euler-Maclaurin tail."""
import json,math,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb
flint.ctx.prec=160;PI=acb.pi()
def xi(x):
 s=acb(arb('0.5'),x)
 return arb('0.5')*s*(s-1)*(PI**(-s/2))*(s/2).gamma()*s.zeta()
z=acb.zeta_zero(1);t=z.imag
def integrate(a,b,step):
 total=arb(0);n=math.ceil((b-a)/step)
 for j in range(n):
  l=a+(b-a)*j/n;r=a+(b-a)*(j+1)/n;X=arb(repr((l+r)/2),repr((r-l)/2))
  total += abs(xi(X))**2*(2*t/(X*X-t*t))*arb(repr(r-l))
 return total,n
mid,n=integrate(30.,60.,.01)
# For x>=60: Euler-Maclaurin gives |zeta(1/2+ix)| <= 4 sqrt(x+1).
# Explicit Stirling with remainder gives the resulting safe envelope
# |xi(1/2+ix)|^2 <= 25 x^(9/2) exp(-pi*x/2).
# Also 2t/(x^2-t^2) <= 31/x^2, hence 775*x^(5/2)*exp(-a*x).
a=arb.pi()/2;X=arb(60);analytic=arb(775)*a**arb('-3.5')*(a*X).gamma_upper(arb('3.5'))
results=Path(__file__).parents[1]/'results'
finite=json.loads((results/'first_zero_evans_arb_finite_integral.json').read_text())
constants=json.loads((results/'evans_tail_envelope_constants.json').read_text())
assert finite['passed_negative_finite'] and constants['passed']
total_upper=arb(finite['upper_arb'])+mid.upper()+analytic.upper()
out={'schema':'marici.voevodsky.first-zero-evans-arb-tail.v1','precision_bits':flint.ctx.prec,'quadrature_range':[30,60],'quadrature_cells':n,'quadrature_enclosure':str(mid),'analytic_range':[60,'infinity'],'xi_squared_envelope':'25*x^(9/2)*exp(-pi*x/2)','kernel_envelope':'31/x^2','analytic_tail_upper':str(analytic),'finite_0_30_upper_arb':finite['upper_arb'],'combined_upper_arb':str(total_upper.upper()),'combined_upper':float(total_upper.upper()),'dependencies_passed':True,'passed_negative_total':bool(total_upper<0),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'first_zero_evans_arb_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_negative_total']
