#!/usr/bin/env python3
"""Arb finite-core evaluation of R''(t), the Taylor derivative for -R'(t)."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'));sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=256;PI=arb.pi();N=200000;U=arb(40);pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,p));q*=p
def at(ts):
 t=arb(ts);gamma=-(PI.log()/(4*PI.sqrt()))*(arb(3)/4)*t**(-arb(5)/2)
 def fun(x,analytic):
  z=acb(arb(1)/4)+acb(0,1)*x/2;return x**4*(-t*x*x).exp()*z.digamma().real
 integ=acb.integral(fun,0,U,rel_tol=arb(2)**-180,abs_tol=arb(2)**-180).real/(2*PI)
 sm=arb(0)
 for n,p in pp:
  ln=arb(n).log();y=ln*ln/(4*t);L2=y*y/2-arb(3)*y/2+arb(3)/8
  sm += arb(p).log()/arb(n).sqrt()*(-y).exp()*L2
 prime=-sm/(PI.sqrt()*t**(arb(5)/2));v=gamma+integ+prime
 return {'t':ts,'R_second_finite_core':str(v),'absolute_upper':max(abs(float(v.lower())),abs(float(v.upper())))}
rows=[at(x) for x in ('.05','.0525','.055','.0575','.06','.0625','.065','.0675','.07','.0725','.075','.1','.15','.2','.25')]
out={'schema':'marici.voevodsky.remainder-second-derivative-finite-core.v1','rows':rows,
 'omitted_terms':['digamma |u|>40','prime powers n>200000'],'certified_complete_derivative':False,
 'scope':'Arb-certified finite cores at fifteen centers, refined across [0.05,0.075]; tail bounds and interval neighborhoods remain to be attached.','passed':True,'rh_proved':False}
p=ROOT/'research/voevodsky/results/remainder_second_derivative_finite_core.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
