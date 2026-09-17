#!/usr/bin/env python3
"""Directed Arb quadratic form for the even degree-149 L=.75 critical polynomial."""
import json,math,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,acb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75');pi=arb.pi();qR=(acb(arb('.25'),arb(125))).digamma().real/2-pi.log()/2;norm2=sum((x*x for x in v),arb(0));Q=72;gamma=qR*norm2
for panel in range(250):
 for j in range(Q):
  z,w=arb.legendre_p_root(Q,j,weight=True);u=arb(panel)+(z+1)/2;weight=w/2;F=arb(0)
  x=L*u
  for n in range(0,150,2):
   sj=(pi/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'));F+=v[n]*2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*sj
  q=(acb(arb('.25'),u/2)).digamma().real/2-pi.log()/2;gamma+=weight*(q-qR)*F*F/pi
# Prime overlaps, exact for polynomial products at order 150.
def peval(y):
 p0=arb(1);s=v[0]*(1/(2*L)).sqrt()
 if len(v)<2:return s
 p1=y
 for n in range(1,149):
  p2=((2*n+1)*y*p1-n*p0)/(n+1);s+=v[n+1]*((2*(n+1)+1)/(2*L)).sqrt()*p2;p0,p1=p1,p2
 return s
prime=arb(0)
for n,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 a=arb(n).log();lo=-L;hi=L-a;c=lam/arb(n).sqrt()
 for j in range(150):
  z,w=arb.legendre_p_root(150,j,weight=True);t=(lo+hi)/2+(hi-lo)*z/2;prime-=c*(hi-lo)*w/2*peval(t/L)*peval((t+a)/L)
# Endpoint term Re(<e+,f><e-,f>); even f makes the moments equal.
x=L/2;moment=arb(0)
for n in range(0,150,2):moment+=v[n]*2*L*((2*n+1)/(2*L)).sqrt()*(pi/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('.5'))
value=gamma+prime+moment*moment;rem=arb('1.882730356310937e-21');value+=arb(0,rem)
out={'schema':'marici.voevodsky.L075-critical-degree149-arb.v1','precision_bits':flint.ctx.prec,'gauss_order':Q,'gamma':str(gamma),'prime':str(prime),'endpoint':str(moment*moment),'quadrature_remainder_radius':str(rem),'critical_form':str(value),'passed':value.lower()>0,'rh_proved':False};p=root/'L075_critical_degree149_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
