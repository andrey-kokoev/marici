#!/usr/bin/env python3
"""Directed fifth-derivative jump tail from degree 1500 via six Legendre antiderivatives."""
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
flint.ctx.prec=256;ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research/voevodsky/results';N=ROOT/'research/nima/results';vv=np.load(V/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
# P_n^(5)(1)=(n-4)...(n+5)/(2^5 5!)=(...)/3840.
d5=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb((n-4)*(n-3)*(n-2)*(n-1)*n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5))/3840 for n in range(6,150,2)),arb(0));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;D=lam/arb(nn).sqrt()/2*d5;data += [(y,D),(-y,D)]
def integ(p):
 q={}
 for k,c in p.items():q[k+1]=q.get(k+1,arb(0))+c/(2*k+1);q[k-1]=q.get(k-1,arb(0))-c/(2*k+1)
 return q
def ev(y,p):return sum((c*y.legendre_p(k) for k,c in p.items()),arb(0))
def R(n):return {n+2:arb(1)/(2*n+3),n:-arb(1)/(2*n+3)-arb(1)/(2*n-1),n-2:arb(1)/(2*n-1)}
M=50000;sq=arb(0)
for n in range(1500,M):
 A=(L*(2*n+1)/2).sqrt()/(2*n+1);p=R(n)
 for _ in range(4):p=integ(p)
 c=sum((A*D*ev(y,p) for y,D in data),arb(0));sq+=c*c
# Continuation of safe Bernstein constants 4^(m+1); squared tail behaves as sum n^-12.
C=sum((1024*(L/arb.pi()).sqrt()*abs(D)*(1-y*y)**arb('-.25') for y,D in data),arb(0));rem=C/(11*arb(M-1)**11).sqrt();total=(sq+rem*rem).sqrt();reserve=arb('6.504953226958228950914887071656391179759772401786e-10')
out={'schema':'marici.nima.L075-directed-fifth-derivative-jump-tail-from1500.v1','endpoint_scaled_fifth_derivative':str(d5),'finite_range':[1500,M],'finite_norm':str(sq.sqrt()),'infinite_remainder_bound':str(rem),'total_bound':str(total),'available_reserve':str(reserve),'passed':total.upper()<reserve.lower(),'scope':'fifth-derivative jumps; six-times-continuous prime remainder and analytic gamma/endpoint rows remain','rh_proved':False};p=N/'L075-directed-fifth-derivative-jump-tail-from1500.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
