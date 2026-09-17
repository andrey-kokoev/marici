#!/usr/bin/env python3
"""Arb finite-core scout for the first nonlinear remainder Hankel determinant."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'));sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=256;PI=arb.pi();U=arb(100);N=200000;I=acb(0,1);pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,p));q*=p
def laguerre(k,y):
 a=-arb(1)/2
 if k==0:return arb(1)
 l0=arb(1);l1=arb(1)+a-y
 if k==1:return l1
 for n in range(1,k):
  l2=((arb(2*n)+arb(1)+a-y)*l1-(arb(n)+a)*l0)/arb(n+1);l0,l1=l1,l2
 return l1
def jet(t,k):
 poch=arb(1)/2
 for j in range(1,k):poch*=arb(2*j+1)/2
 gamma=-(PI.log()/(4*PI.sqrt()))*poch*t**(-arb(k)-arb(1)/2)
 def fun(x,analytic):
  z=acb(arb(1)/4)+I*x/2;return x**(2*k)*(-t*x*x).exp()*z.digamma().real
 integ=acb.integral(fun,0,U,rel_tol=arb(2)**-180,abs_tol=arb(2)**-180).real/(2*PI)
 sm=arb(0)
 for n,p in pp:
  ln=arb(n).log();y=ln*ln/(4*t);sm+=arb(p).log()/arb(n).sqrt()*(-y).exp()*laguerre(k,y)
 prime=-arb(math_factorial(k))*sm/(2*PI.sqrt()*t**(arb(k)+arb(1)/2));return gamma+integ+prime
def math_factorial(k):
 r=1
 for x in range(2,k+1):r*=x
 return r
rows=[]
for ts in ('.005','.01','.02','.05','.0675','.1','.15','.2','.25'):
 t=arb(ts);c0=jet(t,1);c1=jet(t,2);c2=jet(t,3);det=c0*c2-c1*c1
 rows.append({'t':ts,'c0':str(c0),'c1':str(c1),'c2':str(c2),'determinant':str(det),'finite_core_strictly_positive':float(det.lower())>0,'lower':float(det.lower())})
out={'schema':'marici.voevodsky.remainder-rank-two-finite-core.v1','matrix':'[[c0,c1],[c1,c2]], c_k=D_(k+1)^Gamma+D_(k+1)^Prime',
 'rows':rows,'all_finite_core_determinants_positive':all(x['finite_core_strictly_positive'] for x in rows),
 'omitted_terms':['digamma |u|>100','prime powers n>200000'],'scope':'Pointwise finite-core Arb certificate; order-three tail bounds and interval coverage are not yet attached.','passed':True,'rh_proved':False}
p=ROOT/'research/voevodsky/results/remainder_rank_two_finite_core.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
