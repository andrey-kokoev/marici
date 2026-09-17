#!/usr/bin/env python3
"""Numerical source-form scout for low shifted gamma-prime remainder Hankel ranks."""
import json,sys,math
from pathlib import Path
try:
 import mpmath as mp
 import numpy as np
 from sympy import primerange
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp;import numpy as np
 from sympy import primerange
mp.mp.dps=80;pi=mp.pi
def laguerre(k,a,x):return mp.binomial(k+a,k)*mp.hyp1f1(-k,a+1,x)
def prime_powers(N):
 out=[]
 for p in primerange(2,N+1):
  q=p
  while q<=N:out.append((q,mp.log(p)));q*=p
 return out
def moments(t,K,N):
 pp=prime_powers(N);vals=[]
 for k in range(1,K+2):
  poch=mp.rf(mp.mpf('.5'),k)
  gamma=-(mp.log(pi)/(4*mp.sqrt(pi)))*poch*t**(-k-mp.mpf('.5'))
  integ=2*mp.quad(lambda u:u**(2*k)*mp.exp(-t*u*u)*mp.re(mp.digamma(mp.mpf('.25')+.5j*u)),[0,mp.inf])/(4*pi)
  sm=mp.fsum(L/mp.sqrt(n)*mp.exp(-(mp.log(n)**2)/(4*t))*laguerre(k,mp.mpf('-.5'),(mp.log(n)**2)/(4*t)) for n,L in pp)
  prime=-mp.factorial(k)*sm/(2*mp.sqrt(pi)*t**(k+mp.mpf('.5')))
  vals.append(gamma+integ+prime) # c_(k-1)=D_k^G+D_k^P
 return vals
def audit(t,N,rmax=3):
 c=moments(t,2*rmax,N);rows=[]
 for r in range(rmax+1):
  H=np.array([[float(c[i+j]) for j in range(r+1)] for i in range(r+1)]);ev=np.linalg.eigvalsh(H)
  rows.append({'rank':r,'minimum_eigenvalue':float(ev[0]),'eigenvalues':[float(x) for x in ev],'positive':bool(ev[0]>0)})
 return {'prime_power_cutoff':N,'moments':[float(x) for x in c],'ranks':rows}
t=mp.mpf('.01');runs=[audit(t,N) for N in (50000,200000)]
out={'schema':'marici.voevodsky.shifted-remainder-hankel-scout.v1','t0':float(t),'runs':runs,
 'formula':'c_k=D_(k+1)^Gamma+D_(k+1)^Prime for R=Theta-e^(t/4)',
 'all_sampled_positive':all(y['positive'] for x in runs for y in x['ranks']),
 'scope':'Numerical truncated-prime scout only; no rigorous prime tail, quadrature interval, all-rank positivity, Stieltjes, or RH claim.','rh_proved':False}
p=Path(__file__).parents[1]/'results'/'shifted_remainder_hankel_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
