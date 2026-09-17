#!/usr/bin/env python3
"""Export top concentration modes in a degree-199 Legendre trial space."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import spherical_jn
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import spherical_jn
from numpy.polynomial.legendre import leggauss
L=.55;R=250.;N=200;M=90;Q=320;z,w=leggauss(Q);orders=np.arange(N);norm=2*L*np.sqrt((2*orders+1)/(2*L));ph=(-1.)**(orders//2);K=np.zeros((N,N))
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*z/2;ww=(bb-aa)*w/2;V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;B=(V.T*(ww/math.pi))@V;B[0::2,1::2]=0;B[1::2,0::2]=0;K+=B
vals,C=np.linalg.eigh((K+K.T)/2);idx=np.argsort(vals)[::-1][:M];vals=vals[idx];C=C[:,idx];capt=float(vals.sum());trace=2*L*R/math.pi
out={'schema':'marici.voevodsky.two-prime-concentration-modes.v1','L':L,'R':R,'legendre_dimension':N,'retained_modes':M,'eigenvalues':[float(x) for x in vals],'coefficients':[[float(x) for x in row] for row in C],'captured_trace':capt,'trace_residual':trace-capt,'passed':trace-capt<.03,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'two_prime_concentration_modes.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('legendre_dimension','retained_modes','captured_trace','trace_residual','passed')},indent=2))
