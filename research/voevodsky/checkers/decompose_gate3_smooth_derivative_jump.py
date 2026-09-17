#!/usr/bin/env python3
"""Subtract the combined first-derivative-jump Legendre coefficients from Gate-3 smooth rows."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import eval_legendre
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';base=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=base['packet']-base['tail_maps'][4];L=.6495;k=np.arange(1000);sc=np.sqrt((2*k+1)/(2*L));dend=k*(k+1)/(2*L)
dp=np.array([legval(1,Z[:,j]*sc*dend) for j in range(40)]);dm=np.array([legval(-1,Z[:,j]*sc*dend) for j in range(40)])
atoms=[]
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p);atoms += [((L-a)/L,.5*c*L*dp),((-L+a)/L,-.5*c*L*dm)]
ns=np.arange(1000,5000);J1=np.zeros((4000,40));A=np.sqrt(L*(2*ns+1)/2)/(2*ns+1)
# A*R_n is the twice-integrated orthonormal Legendre coefficient kernel.
for y,row in atoms:
 ker=eval_legendre(ns+2,y)/(2*ns+3)-eval_legendre(ns,y)*(1/(2*ns+3)+1/(2*ns-1))+eval_legendre(ns-2,y)/(2*ns-1)
 J1+=(A*ker)[:,None]*row
S=np.load(root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.npz')['smooth'];E=S-J1;rows=[]
for q in range(4):
 sl=slice(q*1000,(q+1)*1000);rows.append({'m':q+1,'smooth_norm':float(np.linalg.norm(S[sl],2)),'derivative_jump_norm':float(np.linalg.norm(J1[sl],2)),'post_derivative_jump_norm':float(np.linalg.norm(E[sl],2))})
out={'schema':'marici.voevodsky.gate3-smooth-derivative-jump-decomposition.v1','rows':rows,'sign_selected':'S-J1','passed_scout':rows[-1]['post_derivative_jump_norm']<rows[-1]['smooth_norm'],'passed':False,'next':'port combined J1 kernel to Arb and continue with second derivative jumps','rh_proved':False};p=root/'gate3_smooth_derivative_jump_decomposition.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'gate3_smooth_derivative_jump_decomposition.npz',derivative_jump=J1,remainder=E);print(json.dumps(out,indent=2))
