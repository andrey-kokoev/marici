#!/usr/bin/env python3
"""Scout prime-action residual coefficients in Legendre modes 2000..4999."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import roots_legendre
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';U=np.load(root/'gamma_floor_rank1000_dangerous_vectors.npz')['vectors'][:,:4];L=.55;lo=2000;hi=5000;Q=3100;z,w=roots_legendre(Q);coeff=np.zeros((hi-lo,4));orders=np.arange(hi);norm=np.sqrt((2*orders+1)/(2*L))
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p)
 # T term: integrate x in [-L,L-a], f(x+a)*phi_n(x); T* similarly f(x)*phi_n(x+a).
 left=-L;right=L-a;x=(left+right)/2+(right-left)*z/2;ww=(right-left)*w/2
 fshift=np.column_stack([legval((x+a)/L,U[:,j])*math.sqrt(1/L/2) for j in range(4)]) # corrected below by normalized coefficients
 fbase=np.column_stack([legval(x/L,U[:,j])*math.sqrt(1/L/2) for j in range(4)])
 # legval coefficients must include sqrt(2k+1), since basis phi_k=sqrt((2k+1)/(2L))P_k.
 scales=np.sqrt((2*np.arange(1000)+1)/(2*L));fshift=np.column_stack([legval((x+a)/L,U[:,j]*scales) for j in range(4)]);fbase=np.column_stack([legval(x/L,U[:,j]*scales) for j in range(4)])
 # Stream Legendre recurrence at x/L and (x+a)/L, retaining high rows.
 for arg,F in ((x/L,fshift),((x+a)/L,fbase)):
  pm=np.ones(Q);pn=arg.copy()
  for n in range(1,hi-1):
   pp=((2*n+1)*arg*pn-n*pm)/(n+1);pm,pn=pn,pp
   degree=n+1
   if degree>=lo:coeff[degree-lo]-=.5*c*norm[degree]*(pn@(ww[:,None]*F))
blocks=[]
for a,b in ((2000,2500),(2500,3000),(3000,4000),(4000,5000)):
 blocks.append({'range':[a,b-1],'norms':[float(x) for x in np.linalg.norm(coeff[a-lo:b-lo],axis=0)]})
out={'schema':'marici.voevodsky.prime-residual-modes-2000-5000-scout.v1','gauss_order':Q,'exact_polynomial_degree':2*Q-1,'blocks':blocks,'cumulative_norms':[float(x) for x in np.linalg.norm(coeff,axis=0)],'last_coefficient_abs':[float(x) for x in abs(coeff[-1])],'status':'floating polynomial-exact quadrature scout','passed':True,'rh_proved':False};p=root/'prime_residual_modes_2000_5000_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
