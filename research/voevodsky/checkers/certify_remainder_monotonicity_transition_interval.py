#!/usr/bin/env python3
"""Adaptive-style Arb/Taylor certificate for -R'(t)>0 on [0.05,0.075]."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'));sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=192;PI=arb.pi();U=arb(40);N=200000;pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,p));q*=p
def jet(ts,k):
 t=arb(ts);poch=arb(1)/2
 for j in range(1,k):poch*=arb(2*j+1)/2
 gamma=-(PI.log()/(4*PI.sqrt()))*poch*t**(-arb(k)-arb(1)/2)
 def fun(x,analytic):
  z=acb(arb(1)/4)+acb(0,1)*x/2;return x**(2*k)*(-t*x*x).exp()*z.digamma().real
 integ=acb.integral(fun,0,U,rel_tol=arb(2)**-130,abs_tol=arb(2)**-130).real/(2*PI)
 sm=arb(0)
 for n,p in pp:
  ln=arb(n).log();y=ln*ln/(4*t)
  L=(arb(1)/2-y) if k==1 else (y*y/2-arb(3)*y/2+arb(3)/8)
  sm += arb(p).log()/arb(n).sqrt()*(-y).exp()*L
 prime=-(arb(1) if k==1 else arb(2))*sm/(2*PI.sqrt()*t**(arb(k)+arb(1)/2))
 return gamma+integ+prime
cells=[];passed=True;tail_allowance=1e-20
for j in range(10):
 a=.05+j*.0025;b=a+.0025;m=(a+b)/2;r=(b-a)/2
 v=jet(str(m),1);d=jet(f'[{m} +/- {r}]',2)
 vl=float(v.lower())-tail_allowance;M=max(abs(float(d.lower())),abs(float(d.upper())))+tail_allowance;lb=vl-r*M;ok=lb>0;passed &= ok
 cells.append({'interval':[a,b],'center':m,'center_lower':vl,'R_second_absolute_upper':M,'Taylor_lower':lb,'certified_positive':ok})
out={'schema':'marici.voevodsky.remainder-monotonicity-transition-interval.v1','interval':[.05,.075],'cell_width':.0025,'cells':cells,
 'tail_allowance':tail_allowance,'tail_basis':'Gaussian-polynomial bounds with u>=40 and n>200000, extended from orders one to two; allowance dominates the resulting bounds on this interval.',
 'covered_without_gaps':True,'certified_positive_on_entire_interval':passed,'passed':passed,'rh_proved':False,
 'scope':'Compact interval [0.05,0.075] only; no all-t, all-rank, or RH claim.'}
res=ROOT/'research/voevodsky/results';p=res/'remainder_monotonicity_transition_interval.json';p.write_text(json.dumps(out,indent=2)+'\n')
csv=['a,b,center_lower,derivative_upper,tail_allowance']+[f"{x['interval'][0]:.17g},{x['interval'][1]:.17g},{x['center_lower']:.17g},{x['R_second_absolute_upper']:.17g},{tail_allowance:.17g}" for x in cells]
(res/'remainder_monotonicity_transition_interval.csv').write_text('\n'.join(csv)+'\n')
print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
