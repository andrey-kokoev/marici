#!/usr/bin/env python3
"""Validated interval-subdivision enclosure of the finite Evans integral."""
import json,math,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb
flint.ctx.prec=160
PI=acb.pi()
def xi(x):
 s=acb(arb('0.5'),x)
 return arb('0.5')*s*(s-1)*(PI**(-s/2))*(s/2).gamma()*s.zeta()
def integrate_segment(a,b,step,t):
 total=arb(0);n=math.ceil((b-a)/step)
 for j in range(n):
  l=a+(b-a)*j/n;r=a+(b-a)*(j+1)/n
  X=arb(repr((l+r)/2),repr((r-l)/2))
  density=abs(xi(X))**2
  kernel=2*t/(X*X-t*t)
  total += density*kernel*arb(repr(r-l))
 return total,n
z=acb.zeta_zero(1);t=z.imag;tm=float(t.mid());h=1e-5;cutoff=30.;step=.001
left,n1=integrate_segment(0.,tm-h,step,t)
right,n2=integrate_segment(tm+h,cutoff,step,t)
# Cauchy on radius 0.1: |xi'| <= sup_|z-z0|<=.1 |xi(z)|/.1.
box=acb(arb('0.5','0.1'),arb(str(t.mid()),'0.1'))
M=abs(arb('0.5')*box*(box-1)*(PI**(-box/2))*(box/2).gamma()*box.zeta())/arb('0.1')
# On |x-t|<=h, |2t(x-t)/(x+t)|<=2h and |g_t|<=M.
central_error=arb(4)*arb(repr(h*h))*M*M
finite=left+right+arb(0,central_error.upper())
out={'schema':'marici.voevodsky.first-zero-evans-arb-finite-integral.v1','precision_bits':flint.ctx.prec,'zero_ordinate':str(t),'cutoff':cutoff,'cell_step':step,'ordinary_cells':n1+n2,'excluded_half_width':h,'xi_derivative_cauchy_bound':str(M),'central_integral_error':str(central_error),'left_integral':str(left),'right_integral':str(right),'finite_integral_enclosure':str(finite),'upper_arb':str(finite.upper()),'upper':float(finite.upper()),'passed_negative_finite':bool(finite.upper()<0),'tail_included':False,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'first_zero_evans_arb_finite_integral.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_negative_finite']
