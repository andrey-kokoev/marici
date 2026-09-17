#!/usr/bin/env python3
"""Directed fourth-derivative jump tail via five Legendre antiderivatives."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=256;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results'
vv=np.load(V/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
# P_n^(4)(1)=(n-3)...(n+4)/384 in the scaled Legendre coordinate.
d4=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb((n-3)*(n-2)*(n-1)*n*(n+1)*(n+2)*(n+3)*(n+4))/384 for n in range(4,150,2)),arb(0));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;D=lam/arb(nn).sqrt()/2*d4;data += [(y,D),(-y,-D)]
def integrate(poly):
 out={}
 for k,c in poly.items():out[k+1]=out.get(k+1,arb(0))+c/(2*k+1);out[k-1]=out.get(k-1,arb(0))-c/(2*k+1)
 return out
def ep(y,p):return sum((c*y.legendre_p(k) for k,c in p.items()),arb(0))
def R(n):return {n+2:arb(1)/(2*n+3),n:-arb(1)/(2*n+3)-arb(1)/(2*n-1),n-2:arb(1)/(2*n-1)}
M=50000;sq=arb(0)
for n in range(1000,M):
 A=(L*(2*n+1)/2).sqrt()/(2*n+1);U=integrate(integrate(integrate(R(n))));c=sum((A*D*ep(y,U) for y,D in data),arb(0));sq+=c*c
# Pattern of safe Bernstein constants: 4,16,64,256 after 2,3,4,5 integrations.
C=sum((256*(L/arb.pi()).sqrt()*abs(D)*(1-y*y)**arb('-.25') for y,D in data),arb(0));rem=C/(9*arb(M-1)**9).sqrt();total=(sq+rem*rem).sqrt();reserve=arb('2.521150533421368279331134257224037022699386903807e-10')
out={'schema':'marici.nima.L075-directed-fourth-derivative-jump-tail.v1','endpoint_scaled_fourth_derivative':str(d4),'finite_range':[1000,M],'finite_norm':str(sq.sqrt()),'infinite_remainder_bound':str(rem),'total_bound':str(total),'available_reserve':str(reserve),'passed':total.upper()<reserve,'scope':'fourth-derivative jumps; five-times-continuous prime remainder and analytic gamma/endpoint rows remain','rh_proved':False};p=N/'L075-directed-fourth-derivative-jump-tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
