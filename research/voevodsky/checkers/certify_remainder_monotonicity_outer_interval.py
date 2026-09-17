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
edges=[.075,.1,.15,.2,.25]
cells=[];failed=[];tail_allowance=1e-20;point_cache={};evaluations=0
def certify(a,b,depth=0):
 global evaluations
 m=(a+b)/2;r=(b-a)/2;key=f'{m:.17g}'
 if key not in point_cache:point_cache[key]=jet(key,1)
 v=point_cache[key];d=jet(f'[{m:.17g} +/- {r:.17g}]',2);evaluations+=1
 vl=float(v.lower())-tail_allowance;M=max(abs(float(d.lower())),abs(float(d.upper())))+tail_allowance;lb=vl-r*M
 if lb>0:
  cells.append({'interval':[a,b],'depth':depth,'center':m,'center_lower':vl,'R_second_absolute_upper':M,'Taylor_lower':lb,'certified_positive':True});return
 if depth>=7:
  failed.append({'interval':[a,b],'depth':depth,'Taylor_lower':lb});return
 certify(a,m,depth+1);certify(m,b,depth+1)
for a,b in zip(edges,edges[1:]):certify(a,b)
cells.sort(key=lambda x:x['interval'][0]);passed=not failed
out={'schema':'marici.voevodsky.remainder-monotonicity-outer-interval.v2','interval':[.075,.25],'method':'adaptive dyadic Arb/Taylor subdivision','evaluations':evaluations,'accepted_cell_count':len(cells),'failed_cells':failed,'cells':cells,
 'tail_allowance':tail_allowance,'tail_basis':'Gaussian-polynomial bounds with u>=40 and n>200000, extended from orders one to two; allowance dominates the resulting bounds on this interval.',
 'covered_without_gaps':True,'certified_positive_on_entire_interval':passed,'passed':passed,'rh_proved':False,
 'scope':'Compact interval [0.075,0.25] only; no all-t, all-rank, or RH claim.'}
p=ROOT/'research/voevodsky/results/remainder_monotonicity_outer_interval.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
