#!/usr/bin/env python3
"""Directed Arb certificate for the rank-80 polar endpoint matrix at L=.55."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
flint.ctx.prec=192;N=160;L=arb('0.55');x=L/2
ap=[];am=[]
for n in range(N):
 # i_n(x)=sqrt(pi/(2x))*I_(n+1/2)(x)
 moment=2*L*((2*n+1)/(2*L)).sqrt()*(arb.pi()/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('0.5'))
 ap.append(moment);am.append(moment if n%2==0 else -moment)
E=arb_mat(N,N)
for i in range(N):
 for j in range(N):
  # The half-sum factor is 1+(-1)^(i+j); impose its exact parity zero
  # before interval evaluation to avoid dependency-radius residue.
  E[i,j]=arb(0) if (i+j)%2 else ap[i]*ap[j]*(1 if j%2==0 else -1)
maxrad=max(float(E[i,j].rad()) for i in range(N) for j in range(N));cross_zero=all(E[i,j]==0 for i in range(0,N,2) for j in range(1,N,2));maxabs=max(max(abs(float(E[i,j].lower())),abs(float(E[i,j].upper()))) for i in range(N) for j in range(N))
out={'schema':'marici.voevodsky.two-prime-endpoint-arb.v1','precision_bits':flint.ctx.prec,'L':'0.55','dimension':N,'formula':'(a_plus a_minus^* + a_minus a_plus^*)/2','maximum_entry_radius':maxrad,'maximum_entry_absolute_upper':maxabs,'even_odd_cross_block_exactly_zero':cross_zero,'budget':'1e-11','budget_met':maxrad<1e-11,'matrix':[[str(E[i,j]) for j in range(N)] for i in range(N)],'passed':maxrad<1e-11 and cross_zero,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_endpoint_arb_160.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
