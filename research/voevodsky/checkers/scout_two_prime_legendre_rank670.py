#!/usr/bin/env python3
"""Floating rank-670 scout at a cutoff scaled beyond the Bessel turning point."""
import json,sys,math,time
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,iv
from numpy.polynomial.legendre import leggauss
L=.55;N=670;Q=260;edges=[0,1,2,4,8,16,32,64,128,250]+list(range(500,20250,250));nodes,weights=leggauss(Q);H=np.zeros((N,N));records=[];orders=np.arange(N);ph=(-1.)**(orders//2);norm=2*L*np.sqrt((2*orders+1)/(2*L));t=time.time()
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(N)]);am=ap*((-1.)**orders);endpoint=(np.outer(ap,am)+np.outer(am,ap))/2
for aa,bb in zip(edges[:-1],edges[1:]):
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*weights/2;symbol=(digamma(.25+.5j*u).real-math.log(math.pi))/2-sum(math.log(p)/math.sqrt(p)*np.cos(u*math.log(p)) for p in (2,3));V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;block=(V.T*(w*symbol/math.pi))@V;block[0::2,1::2]=0;block[1::2,0::2]=0;H+=block
 if bb in (10000,12500,15000,17500,20000):
  A=(H+endpoint+H.T+endpoint.T)/2;row={'cutoff':bb,**{f'min_eigenvalue_dim_{n}':float(np.linalg.eigvalsh(A[:n,:n])[0]) for n in (160,320,500,670)}}
  if bb==20000:
   F=A[:160,:160];B=A[:160,160:];C=A[160:,160:];S=C-B.T@np.linalg.solve(F,B);row['rank510_over_rank160_schur_min_eigenvalue']=float(np.linalg.eigvalsh(S)[0]);row['rank160_condition_number']=float(np.linalg.cond(F))
  records.append(row)
out={'schema':'marici.voevodsky.two-prime-legendre-rank670-scout.v1','L':L,'dimension':N,'gauss_nodes_per_panel':Q,'records':records,'elapsed_seconds':time.time()-t,'status':'floating scout; asymptotic gamma tail omitted','passed':True,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'two_prime_legendre_rank670_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
