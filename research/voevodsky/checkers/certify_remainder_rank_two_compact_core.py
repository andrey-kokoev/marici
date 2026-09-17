#!/usr/bin/env python3
"""Adaptive Arb/Taylor finite-core certificate for the rank-two determinant on [0.05,0.1]."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'));sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=160;PI=arb.pi();U=arb(100);N=200000;I=acb(0,1);pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,p));q*=p
def lag(k,y):
 a=-arb(1)/2;l0=arb(1)
 if k==0:return l0
 l1=arb(1)+a-y
 for n in range(1,k):l0,l1=l1,((arb(2*n)+arb(1)+a-y)*l1-(arb(n)+a)*l0)/arb(n+1)
 return l1
def jet(t,k):
 poch=arb(1)/2
 for j in range(1,k):poch*=arb(2*j+1)/2
 gamma=-(PI.log()/(4*PI.sqrt()))*poch*t**(-arb(k)-arb(1)/2)
 def fun(x,analytic):return x**(2*k)*(-t*x*x).exp()*(acb(arb(1)/4)+I*x/2).digamma().real
 integ=acb.integral(fun,0,U,rel_tol=arb(2)**-110,abs_tol=arb(2)**-110).real/(2*PI);sm=arb(0)
 for n,p in pp:
  ln=arb(n).log();y=ln*ln/(4*t);sm+=arb(p).log()/arb(n).sqrt()*(-y).exp()*lag(k,y)
 return gamma-arb(math.factorial(k))*sm/(2*PI.sqrt()*t**(arb(k)+arb(1)/2))+integ
cache={};cells=[];failed=[];evals=0
def center(m):
 key=f'{m:.17g}'
 if key not in cache:
  t=arb(key);cache[key]=[jet(t,k) for k in range(1,5)]
 return cache[key]
def visit(a,b,d=0):
 global evals
 m=(a+b)/2;r=(b-a)/2;c=center(m);det=c[0]*c[2]-c[1]*c[1]
 ti=arb(f'[{m:.17g} +/- {r:.17g}]');q=[jet(ti,k) for k in range(1,5)];evals+=1
 deriv=q[1]*q[2]-q[0]*q[3];M=max(abs(float(deriv.lower())),abs(float(deriv.upper())));lb=float(det.lower())-r*M
 if lb>0:cells.append({'interval':[a,b],'depth':d,'center_det_lower':float(det.lower()),'det_derivative_upper':M,'Taylor_lower':lb});return
 if d>=8:failed.append({'interval':[a,b],'lower':lb});return
 visit(a,m,d+1);visit(m,b,d+1)
for a,b in zip([.05,.0675,.075,.0875,.1],[.0675,.075,.0875,.1,.1][0:4]):visit(a,b)
cells.sort();passed=not failed
out={'schema':'marici.voevodsky.remainder-rank-two-compact-core.v1','interval':[.05,.1],'method':'adaptive Taylor bound on det=c0*c2-c1^2 with det prime=c1*c2-c0*c3',
 'evaluations':evals,'accepted_cells':len(cells),'failed':failed,'cells':cells,'finite_core_positive_on_interval':passed,'passed':passed,'rh_proved':False,
 'scope':'Finite source core only; uniform order-1..4 omitted-tail perturbation bounds remain to be attached.'}
p=ROOT/'research/voevodsky/results/remainder_rank_two_compact_core.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
