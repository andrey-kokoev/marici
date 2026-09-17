#!/usr/bin/env python3
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import eval_legendre
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;k=np.arange(1000);sc=np.sqrt((2*k+1)/(2*L));fp=np.array([legval(1,Z[:,j]*sc) for j in range(40)]);fm=np.array([legval(-1,Z[:,j]*sc) for j in range(40)]);atoms=[]
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p);atoms += [((L-a)/L,.5*c*fp),((-L+a)/L,-.5*c*fm)]
ns=np.arange(7000,8000);J=np.zeros((1000,40))
for t,row in atoms:
 ker=eval_legendre(ns+1,t)-eval_legendre(ns-1,t);fac=-np.sqrt(L*(2*ns+1)/2)/(2*ns+1);J+=(fac*ker)[:,None]*row
R=np.load(root/'regularized_union_continuum_residual_L06495_7000_7999.npz')['residual'];S=R-J;op=float(np.linalg.norm(S,2));out={'schema':'marici.voevodsky.continuum-residual-jump-smooth-L06495-7000-7999.v1','m':7,'full_norm':float(np.linalg.norm(R,2)),'jump_norm':float(np.linalg.norm(J,2)),'smooth_norm':op,'m_times_smooth_norm':7*op,'target':.015,'passed_scout':7*op<.015,'passed':False,'rh_proved':False};p=root/'continuum_residual_jump_smooth_L06495_7000_7999.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'continuum_residual_jump_smooth_L06495_7000_7999.npz',jump=J,smooth=S);print(json.dumps(out,indent=2));assert out['passed_scout']
