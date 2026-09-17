#!/usr/bin/env python3
"""Focused second-order Taylor certificate for one rank-two determinant cell."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'));sys.path.append(str(ROOT/'research/flavor/.venv/Lib/site-packages'))
from flint import arb,acb,ctx
from sympy import primerange
ctx.prec=160;PI=arb.pi();I=acb(0,1);U=arb(50);N=50000;pp=[]
for p in primerange(2,N+1):
 q=p;lp=arb(p).log()
 while q<=N:pp.append((arb(q).log(),lp/arb(q).sqrt()));q*=p
def lag(k,y):
 a=-arb(1)/2;l0=arb(1)
 if k==0:return l0
 l1=arb(1)+a-y
 for n in range(1,k):l0,l1=l1,((arb(2*n)+arb(1)+a-y)*l1-(arb(n)+a)*l0)/arb(n+1)
 return l1
def jet(t,k):
 poch=arb(1)/2
 for j in range(1,k):poch*=arb(2*j+1)/2
 g=-(PI.log()/(4*PI.sqrt()))*poch*t**(-arb(k)-arb(1)/2)
 def f(x,analytic):return x**(2*k)*(-t*x*x).exp()*(acb(arb(1)/4)+I*x/2).digamma().real
 integ=acb.integral(f,0,U,rel_tol=arb(2)**-105,abs_tol=arb(2)**-105).real/(2*PI);sm=arb(0)
 for ln,w in pp:
  y=ln*ln/(4*t);sm+=w*(-y).exp()*lag(k,y)
 return g-arb(math.factorial(k))*sm/(2*PI.sqrt()*t**(arb(k)+arb(1)/2))+integ
a=.050001;b=.050002;m=(a+b)/2;r=(b-a)/2
c=[jet(arb(str(m)),k) for k in range(1,7)]
D=c[0]*c[2]-c[1]*c[1];D1=c[1]*c[2]-c[0]*c[3];D2=c[0]*c[4]-c[2]*c[2]
D_rank3=c[0]*c[2]*c[4]-c[0]*c[3]*c[3]-c[1]*c[1]*c[4]+2*c[1]*c[2]*c[3]-c[2]*c[2]*c[2]
t=arb(f'[{m} +/- {r}]');q=[jet(t,k) for k in range(1,7)];D3=-q[0]*q[5]-q[1]*q[4]+2*q[2]*q[3]
D_rank3_prime=-q[0]*q[2]*q[5]+q[0]*q[3]*q[4]+q[1]*q[1]*q[5]-q[1]*q[2]*q[4]-q[1]*q[3]*q[3]+q[2]*q[2]*q[3]
absup=lambda x:max(abs(float(x.lower())),abs(float(x.upper())))
moment_upper=max(absup(x) for x in c+q)
lower=float(D.lower())-r*absup(D1)-r*r*absup(D2)/2-r**3*absup(D3)/6
rank3_lower=float(D_rank3.lower())-r*absup(D_rank3_prime)
out={'schema':'marici.voevodsky.rank-two-second-order-cell.v1','interval':[a,b],'center':m,'D_center':str(D),'rank3_center_determinant':str(D_rank3),'rank3_center_strictly_positive':float(D_rank3.lower())>0,'rank3_derivative_interval':str(D_rank3_prime),'rank3_Taylor_lower':rank3_lower,'rank3_cell_positive':rank3_lower>0,'D1_center':str(D1),'D2_center':str(D2),'D3_interval':str(D3),'moment_absolute_upper':moment_upper,'Taylor_lower':lower,'finite_core_positive':lower>0,
 'cutoffs':{'prime_power':N,'u':50},'scope':'Finite core on one cell; omitted order-1..6 tails not attached.','passed':lower>0,'rh_proved':False}
p=ROOT/'research/voevodsky/results/rank_two_second_order_cell.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
