#!/usr/bin/env python3
"""Directed captured concentration trace for the 90 exported modes."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,arb_mat
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';d=json.loads((root/'two_prime_concentration_modes.json').read_text());L=arb('.55');R=arb(250);N=200;M=90;Q=320;edges=(0,1,2,4,8,16,32,64,128,250);rows=[[],[]];srows=[[],[]]
def sj(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'))
for left,right in zip(edges[:-1],edges[1:]):
 a=arb(left);b=arb(right)
 for k in range(Q):
  z,w=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*z/2;fac=(b-a)*w/(2*arb.pi());vals=[2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*sj(n,L*u) for n in range(N)]
  for p in (0,1):v=vals[p::2];rows[p].append(v);srows[p].append([fac*x for x in v])
B=[arb_mat(rows[p]).transpose()*arb_mat(srows[p]) for p in (0,1)];rem=arb('1e-30');K=arb_mat(N,N)
for p in (0,1):
 for i in range(100):
  for j in range(100):K[2*i+p,2*j+p]=B[p][i,j]+arb(0,rem)
C=arb_mat([[arb(repr(d['coefficients'][i][j])) for j in range(M)] for i in range(N)]);G=C.transpose()*C;capt=(G.inv()*(C.transpose()*K*C));trace=sum((capt[i,i] for i in range(M)),arb(0));rho=2*L*R/arb.pi()-trace;qR=arb(json.loads((root/'gamma_floor_250_arb.json').read_text())['q_R']);cp=arb(2).log()/arb(2).sqrt()+arb(3).log()/arb(3).sqrt();q0=(arb('.25').digamma()-arb.pi().log())/2;floor=(qR-cp)-((qR-cp)+(-q0+cp))*rho
out={'schema':'marici.voevodsky.two-prime-concentration-trace-arb.v1','precision_bits':flint.ctx.prec,'legendre_dimension':N,'retained_modes':M,'analytic_entry_remainder':str(rem),'captured_trace':str(trace),'trace_residual':str(rho),'certified_tail_floor':str(floor),'passed':float(rho.upper())<.029 and float(floor.lower())>.58,'rh_proved':False};p=root/'two_prime_concentration_trace_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
