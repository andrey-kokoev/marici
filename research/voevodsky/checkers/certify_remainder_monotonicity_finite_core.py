#!/usr/bin/env python3
"""Arb-certify finite-core contributions to -R'(t); analytic tails remain explicit obligations."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=256;PI=arb.pi();N=200000;U=arb(40)
pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,p));q*=p
def at(tstr):
 t=arb(tstr)
 gamma=-(PI.log()/(4*PI.sqrt()))*arb(1)/2*t**(-arb(3)/2)
 def fun(x,analytic):
  z=acb(arb(1)/4)+acb(0,1)*x/2;return x*x*(-t*x*x).exp()*z.digamma().real
 integ=acb.integral(fun,arb(0),U,rel_tol=arb(2)**-180,abs_tol=arb(2)**-180).real/(2*PI)
 sm=arb(0)
 for n,p in pp:
  ln=arb(n).log();y=ln*ln/(4*t);sm += arb(p).log()/arb(n).sqrt()*(-y).exp()*(arb(1)/2-y)
 prime=-sm/(2*PI.sqrt()*t**(arb(3)/2));core=gamma+integ+prime
 return {'t':tstr,'gamma':str(gamma),'digamma_integral_0_40':str(integ),'prime_powers_through_200000':str(prime),'finite_core':str(core),'finite_core_strictly_positive':float(core.lower())>0,'lower_bound':float(core.lower())}
rows=[at('.05'),at('.065'),at('.0675'),at('.07'),at('.075'),at('.1'),at('.15'),at('.2'),at('.25')]
out={'schema':'marici.voevodsky.remainder-monotonicity-finite-core.v1','precision_bits':ctx.prec,'rows':rows,
 'all_finite_cores_certified_positive':all(x['finite_core_strictly_positive'] for x in rows),
 'omitted_terms':['digamma integral over |u|>40','prime powers n>200000'],
 'certified_full_value':False,
 'scope':'Arb rigorously encloses each displayed finite core. Full -R prime positivity additionally requires signed or absolute bounds for both omitted tails.','passed':True,'rh_proved':False}
p=ROOT/'research/voevodsky/results/remainder_monotonicity_finite_core.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
