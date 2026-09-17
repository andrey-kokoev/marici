#!/usr/bin/env python3
"""Directed Arb evaluation of the exact rank-80 physical prime overlaps."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
flint.ctx.prec=192;N=80;Q=80;L=arb('0.55')
def legs(x):
 out=[arb(1),x]
 for n in range(1,N-1):out.append(((2*n+1)*x*out[n]-n*out[n-1])/(n+1))
 return out
P=arb_mat(N,N)
for prime in (2,3):
 a=arb(prime).log();lo=-L;hi=L-a;rows=[];srows=[]
 for k in range(Q):
  z,w=arb.legendre_p_root(Q,k,weight=True);t=(lo+hi)/2+(hi-lo)*z/2;wt=(hi-lo)*w/2
  x=t/L;y=(t+a)/L;px=legs(x);py=legs(y);bx=[];by=[]
  for n in range(N):
   norm=((2*n+1)/(2*L)).sqrt();bx.append(norm*px[n]);by.append(norm*py[n])
  rows.append(bx);srows.append([wt*v for v in by])
 T=arb_mat(rows).transpose()*arb_mat(srows);coef=a/arb(prime).sqrt()
 P-=coef*(T+T.transpose())/2
maxrad=max(float(P[i,j].rad()) for i in range(N) for j in range(N));maxabs=max(max(abs(float(P[i,j].lower())),abs(float(P[i,j].upper()))) for i in range(N) for j in range(N))
out={'schema':'marici.voevodsky.two-prime-overlap-arb.v1','precision_bits':flint.ctx.prec,'dimension':N,'gauss_order':Q,'polynomial_degree_exactness':159,'active_primes':[2,3],'maximum_entry_radius':maxrad,'maximum_entry_absolute_upper':maxabs,'budget':'2e-11','budget_met':maxrad<2e-11,'matrix':[[str(P[i,j]) for j in range(N)] for i in range(N)],'passed':maxrad<2e-11,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_overlap_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
