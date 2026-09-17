#!/usr/bin/env python3
"""4096-ulp Legendre synthesis perturbation budget for prime overlaps on E10."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from numpy.polynomial.legendre import leggauss
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from numpy.polynomial.legendre import leggauss
root=Path(__file__).parents[1]/'results';A=np.load(root/'gamma_floor_L065_rank1000_midpoint.npz')['matrix'];e,W=np.linalg.eigh(A);W=np.column_stack((W[:,1:20],W[:,0]));N=1000;o=np.arange(N);xg,wg=leggauss(1000);eps=4096*2**-53;rows=[]
def vals(y,L):
 V=np.empty((len(y),N),complex);V[:,0]=1;V[:,1]=y
 for n in range(1,N-1):V[:,n+1]=((2*n+1)*y*V[:,n]-n*V[:,n-1])/(n+1)
 V*=np.sqrt((2*o+1)/(2*L));X=V@W;E=eps*(np.abs(V)@np.abs(W));return X,E
for th in (0,np.pi/2,np.pi,3*np.pi/2):
 z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;err=0
 for p in (2,3):
  aa=math.log(p);lo=-L;hi=L-aa;t=(lo+hi)/2+(hi-lo)*xg/2;ww=(hi-lo)*wg/2;X,EX=vals(t/L,L);Y,EY=vals((t+aa)/L,L);sw=np.sqrt(np.abs(ww));nx=np.linalg.norm(sw[:,None]*X,2);ny=np.linalg.norm(sw[:,None]*Y,2);ex=np.linalg.norm(sw[:,None]*EX,2);ey=np.linalg.norm(sw[:,None]*EY,2);c=math.log(p)/math.sqrt(p);err+=c*(ex*ny+nx*ey+ex*ey)
 rows.append({'theta':float(th),'prime_block_error':float(err)})
out={'schema':'marici.voevodsky.gate3-E10-prime-roundoff.v1','legendre_synthesis_ulp_reserve':4096,'prime_gauss_order':1000,'rows':rows,'maximum_prime_block_error':max(x['prime_block_error'] for x in rows),'strong_block_error_target':1e-8,'passed_scout':max(x['prime_block_error'] for x in rows)<1e-8,'passed':False,'remaining':'endpoint Bessel, ordinary matrix arithmetic, and all-arc promotion','rh_proved':False};p=root/'gate3_E10_prime_roundoff.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
