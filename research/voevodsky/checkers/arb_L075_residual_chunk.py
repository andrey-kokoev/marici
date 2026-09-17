#!/usr/bin/env python3
"""Directed even-mode chunk of the L=.75 degree-149 residual."""
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
flint.ctx.prec=256;start=int(sys.argv[1]);stop=int(sys.argv[2]);root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75');pi=arb.pi();qR=(acb(arb('.25'),arb(125))).digamma().real/2-pi.log()/2;inds=list(range(start+(start%2),stop,2));r={m:arb(0) for m in inds};Q=72
for panel in range(250):
 for j in range(Q):
  z,ww=arb.legendre_p_root(Q,j,weight=True);u=arb(panel)+(z+1)/2;weight=ww/2;x=L*u;Fw=arb(0)
  for n in range(0,150,2):Fw+=v[n]*2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*(pi/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'))
  q=(acb(arb('.25'),u/2)).digamma().real/2-pi.log()/2
  for m in inds:
   Fm=2*L*((2*m+1)/(2*L)).sqrt()*((-1)**(m//2))*(pi/(2*x)).sqrt()*x.bessel_j(arb(m)+arb('.5'));r[m]+=weight*(q-qR)*Fw*Fm/pi
# Legendre evaluation.
def vals(y,maxn=999):
 p=[arb(1),y]
 for n in range(1,maxn):p.append(((2*n+1)*y*p[-1]-n*p[-2])/(n+1))
 return p
def weval(P):return sum((v[n]*((2*n+1)/(2*L)).sqrt()*P[n] for n in range(0,150,2)),arb(0))
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 a=arb(nn).log();lo=-L;hi=L-a;c=lam/arb(nn).sqrt()
 for j in range(150):
  z,ww=arb.legendre_p_root(150,j,weight=True);t=(lo+hi)/2+(hi-lo)*z/2;P=vals(t/L);Ps=vals((t+a)/L);fw=weval(P);fws=weval(Ps);fac=-c*(hi-lo)*ww/4
  for m in inds:r[m]+=fac*((2*m+1)/(2*L)).sqrt()*(P[m]*fws+Ps[m]*fw)
# endpoint outer product.
x=L/2;mw=sum((v[n]*2*L*((2*n+1)/(2*L)).sqrt()*(pi/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('.5')) for n in range(0,150,2)),arb(0))
for m in inds:r[m]+=mw*2*L*((2*m+1)/(2*L)).sqrt()*(pi/(2*x)).sqrt()*x.bessel_i(arb(m)+arb('.5'))
sq=sum((z*z for z in r.values()),arb(0));out={'start':start,'stop':stop,'count':len(inds),'squared_norm':str(sq),'passed':True};p=root/f'L075_residual_chunk_{start}_{stop}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
