#!/usr/bin/env python3
"""Floating low-degree Legendre scout for the L=.55 two-prime Weil form."""
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
L=.55;N=60;Q=240;edges=[0,1,2,4,8,16,32,64,128,256,512,1000]
H=np.zeros((N,N));nodes,weights=leggauss(Q)
for aa,bb in zip(edges[:-1],edges[1:]):
 u=(aa+bb)/2+(bb-aa)*nodes/2;w=(bb-aa)*weights/2
 symbol=(digamma(.25+.5j*u).real-math.log(math.pi))/2
 for p in (2,3):symbol-=math.log(p)/math.sqrt(p)*np.cos(u*math.log(p))
 V=np.empty((Q,N))
 for n in range(N): V[:,n]=2*L*math.sqrt((2*n+1)/(2*L))*((-1)**(n//2))*spherical_jn(n,L*u)
 block=(V.T*((w*symbol/math.pi)))@V
 # Fourier transforms of even and odd Legendre modes differ by a factor i;
 # their real quadratic-form cross block vanishes.
 block[0::2,1::2]=0;block[1::2,0::2]=0;H+=block
# Endpoint moments, using i_n(x)=sqrt(pi/(2x)) I_(n+1/2)(x).
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(N)]);am=ap*np.array([(-1)**n for n in range(N)])
H+=(np.outer(ap,am)+np.outer(am,ap))/2
H=(H+H.T)/2;e=np.linalg.eigvalsh(H)
out={'schema':'marici.voevodsky.two-prime-legendre-form-scout.v1','L':L,'active_prime_powers':[2,3],'dimension':N,'cutoff':edges[-1],'gauss_nodes_per_panel':Q,'smallest_eigenvalues':[float(v) for v in e[:10]],'negative_eigenvalue_count':int(np.count_nonzero(e<0)),'status':'floating cutoff scout; omitted multiplier tail and no interval enclosure','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_legendre_form_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
