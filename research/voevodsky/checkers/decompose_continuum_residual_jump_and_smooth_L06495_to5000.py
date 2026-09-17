#!/usr/bin/env python3
"""Subtract exact Legendre value-jump coefficients from modes 1000..3999."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import eval_legendre
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];Z=U-d['tail_maps'][4];L=.6495;N=1000;k=np.arange(N);sc=np.sqrt((2*k+1)/(2*L));from numpy.polynomial.legendre import legval
fp=np.array([legval(1,Z[:,j]*sc) for j in range(40)]);fm=np.array([legval(-1,Z[:,j]*sc) for j in range(40)]);atoms=[]
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p);atoms.extend([((L-a)/L,.5*c*fp),((-L+a)/L,-.5*c*fm)])
ns=np.arange(1000,5000);J=np.zeros((len(ns),40))
for t,row in atoms:
 ker=eval_legendre(ns+1,t)-eval_legendre(ns-1,t);fac=-np.sqrt(L*(2*ns+1)/2)/(2*ns+1);J+=(fac*ker)[:,None]*row
R=np.vstack((np.load(root/'regularized_union_continuum_residual_L06495.npz')['residual'],np.load(root/'regularized_union_continuum_residual_L06495_2000_2999.npz')['residual'],np.load(root/'regularized_union_continuum_residual_L06495_3000_3999.npz')['residual'],np.load(root/'regularized_union_continuum_residual_L06495_4000_4999.npz')['residual']));Sm=R-J;rows=[]
for q in range(4):
 sl=slice(q*1000,(q+1)*1000);rows.append({'mode_range':[1000*(q+1),1000*(q+2)-1],'full_norm':float(np.linalg.norm(R[sl],2)),'jump_norm':float(np.linalg.norm(J[sl],2)),'smooth_remainder_norm':float(np.linalg.norm(Sm[sl],2))})
out={'schema':'marici.voevodsky.continuum-residual-jump-smooth-decomposition-L06495-to5000.v1','rows':rows,'full_minus_jump_frobenius':float(np.linalg.norm(Sm)),'status':'floating exact-formula decomposition','passed':rows[-1]['smooth_remainder_norm']<rows[-1]['full_norm'],'rh_proved':False};p=root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.npz',jump=J,smooth=Sm);print(json.dumps(out,indent=2));assert out['passed']
