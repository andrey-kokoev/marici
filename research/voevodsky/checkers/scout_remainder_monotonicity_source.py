#!/usr/bin/env python3
"""Numerical source-side scout for the first remainder-cone inequality -R'(t)>=0."""
import json,sys
from pathlib import Path
try:
 import mpmath as mp
 from sympy import primerange
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
 from sympy import primerange
mp.mp.dps=60;pi=mp.pi;N=200000
pp=[]
for p in primerange(2,N+1):
 q=p
 while q<=N:pp.append((q,mp.log(p)));q*=p
def L1(y):return mp.mpf('.5')-y
def c0(t):
 t=mp.mpf(t)
 gamma=-(mp.log(pi)/(4*mp.sqrt(pi)))*mp.mpf('.5')*t**(-mp.mpf('1.5'))
 integ=mp.quad(lambda u:u*u*mp.exp(-t*u*u)*mp.re(mp.digamma(mp.mpf('.25')+.5j*u)),[0,mp.inf])/(2*pi)
 sm=mp.fsum(L/mp.sqrt(n)*mp.exp(-(mp.log(n)**2)/(4*t))*L1((mp.log(n)**2)/(4*t)) for n,L in pp)
 prime=-sm/(2*mp.sqrt(pi)*t**mp.mpf('1.5'))
 return gamma,integ,prime,gamma+integ+prime
Ts=['.005','.0075','.01','.015','.02','.03','.05','.075','.1','.15','.2','.25']
rows=[]
for t in Ts:
 g,i,p,v=c0(t);rows.append({'t':float(t),'gamma_prefactor':float(g),'digamma_integral':float(i),'prime_power':float(p),'minus_R_prime':float(v),'positive':bool(v>0)})
out={'schema':'marici.voevodsky.remainder-monotonicity-source-scout.v1','prime_power_cutoff':N,'rows':rows,
 'all_sampled_positive':all(x['positive'] for x in rows),
 'target':'-R_prime(t)>=0 for every t>0, equivalently the infinitesimal rank-one remainder localizer',
 'scope':'Floating source-form scout only; no interval quadrature, prime-tail bound, continuum coverage, all-rank cone, or RH claim.','rh_proved':False}
p=Path(__file__).parents[1]/'results'/'remainder_monotonicity_source_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
