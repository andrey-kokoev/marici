#!/usr/bin/env python3
"""Full moving eigenframe scout for the corrected degree-16 matrix polynomial."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.chebyshev import chebfit,chebmul
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];t=np.cos(np.arange(32,-1,-1)*np.pi/32);frames=[];vals=[];prev=None
for x in t:
 H=np.polynomial.chebyshev.chebval(x,C);e,V=np.linalg.eigh((H+H.T)/2)
 if prev is not None:
  # sign alignment only; sorted eigenvalues are well separated in this scout.
  sg=np.sign(np.sum(prev*V,axis=0));sg[sg==0]=1;V=V*sg
 frames.append(V);vals.append(e);prev=V
P=chebfit(t,np.array(frames).reshape(33,-1),32).reshape(33,40,40);lam=chebfit(t,np.array(vals),32);# coefficient convolution residual H P-P diag(lambda)
R=np.zeros((65,40,40))
for i in range(40):
 for j in range(40):
  for k in range(40):
   q=chebmul(C[:,i,k],P[:,k,j]);R[:len(q),i,j]+=q
  q=chebmul(P[:,i,j],lam[:,j]);R[:len(q),i,j]-=q
res=sum(np.linalg.norm(x,2) for x in R);# orthogonality defect coefficients
O=np.zeros((65,40,40))
for i in range(40):
 for j in range(40):
  for k in range(40):
   q=chebmul(P[:,k,i],P[:,k,j]);O[:len(q),i,j]+=q
O[0]-=np.eye(40);orth=sum(np.linalg.norm(x,2) for x in O);grid=np.linspace(-1,1,2001);mine=min(np.min(np.polynomial.chebyshev.chebval(x,lam)) for x in grid);out={'schema':'marici.voevodsky.full-moving-eigenframe-corrected-L0649-L065.v1','degree':32,'orthogonality_defect_coefficient_bound':float(orth),'eigen_residual_coefficient_bound':float(res),'minimum_interpolated_eigenvalue':float(mine),'passed_scout':bool(orth<1e-8 and res<1e-8 and mine>0),'passed':False,'scope':'floating full-frame scout; eigenvalue crossings may require block alignment and directed coefficients','rh_proved':False};np.savez_compressed(root/'full_moving_eigenframe_corrected_L0649_L065.npz',frame=P,eigenvalues=lam,residual=R,orthogonality=O);p=root/'full_moving_eigenframe_corrected_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
