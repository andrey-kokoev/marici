#!/usr/bin/env python3
"""Floating cutoff/dimension stability scout for the L=.55 two-prime form."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv
from numpy.polynomial.legendre import leggauss
L=.55;N=320;Q=240;edges=[0,1,2,4,8,16,32,64,128,250,500,1000,2000]
nodes,weights=leggauss(Q);H=np.zeros((N,N));records=[]
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(N)]);am=ap*np.array([(-1)**n for n in range(N)]);endpoint=(np.outer(ap,am)+np.outer(am,ap))/2
for aa,bb in zip(edges[:-1],edges[1:]):
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*weights/2
 symbol=(digamma(.25+.5j*u).real-math.log(math.pi))/2-sum(math.log(p)/math.sqrt(p)*np.cos(u*math.log(p)) for p in (2,3))
 V=np.array([2*L*math.sqrt((2*n+1)/(2*L))*((-1)**(n//2))*spherical_jn(n,L*u) for n in range(N)]).T
 block=(V.T*(w*symbol/math.pi))@V;block[0::2,1::2]=0;block[1::2,0::2]=0;H+=block
 if bb in (250,500,1000,2000):
  row={'cutoff':bb}
  for n in (160,240,320):row[f'min_eigenvalue_dim_{n}']=float(np.linalg.eigvalsh((H[:n,:n]+endpoint[:n,:n]+(H[:n,:n]+endpoint[:n,:n]).T)/2)[0])
  records.append(row)
out={'schema':'marici.voevodsky.two-prime-legendre-convergence-scout.v1','L':L,'gauss_nodes_per_panel':Q,'records':records,'status':'floating stability scout; no directed tail enclosure','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_legendre_convergence_320_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
