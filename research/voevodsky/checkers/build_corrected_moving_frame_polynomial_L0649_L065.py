#!/usr/bin/env python3
"""Polynomial moving frame and exact coefficient-norm residual bounds for the degree-8 matrix interpolant."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.chebyshev import chebfit,chebmul
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];t=np.cos(np.arange(32,-1,-1)*np.pi/32);vec=[];lam=[];prev=None
for x in t:
 M=np.polynomial.chebyshev.chebval(x,C);e,V=np.linalg.eigh((M+M.T)/2);v=V[:,0]
 if prev is not None and v@prev<0:v=-v
 vec.append(v);lam.append(e[0]);prev=v
P=chebfit(t,np.array(vec),32);lc=chebfit(t,np.array(lam),32);# M(t)P(t)-lambda(t)P(t)
R=np.zeros((max(len(C)+len(P)-1,2*len(P)-1),40))
for i in range(40):
 for j in range(40):R[:,i][:len(chebmul(C[:,i,j],P[:,j]))]+=chebmul(C[:,i,j],P[:,j])
LP=np.stack([chebmul(lc,P[:,i]) for i in range(40)],axis=1);R[:len(LP)]-=LP
# coefficient triangle bounds; normalization defect polynomial.
res_bound=float(sum(np.linalg.norm(row) for row in R));normpoly=np.array([0.]);
for i in range(40):
 q=chebmul(P[:,i],P[:,i]);normpoly=np.pad(normpoly,(0,max(0,len(q)-len(normpoly))));normpoly[:len(q)]+=q
normpoly[0]-=1;norm_def=float(sum(abs(normpoly)));tail=float(sum(np.linalg.norm(row) for row in P[9:]));gap=8.968462242850897e-9;margin=1.9148642329984542e-11;schur=res_bound**2/gap;out={'schema':'marici.voevodsky.corrected-moving-frame-polynomial-residual-L0649-L065.v1','frame_degree':32,'post_degree8_frame_coefficient_l1':tail,'normalization_defect_l1_bound':norm_def,'eigen_residual_l1_bound':res_bound,'residual_schur_correction':schur,'critical_margin':margin,'correction_to_margin_ratio':schur/margin,'passed_polynomial_bundle':norm_def<1e-8 and schur<margin/10,'passed':False,'scope':'floating coefficient construction with rigorous-for-stored-coefficients triangle bounds; directed coefficient/source enclosure open','rh_proved':False};np.savez_compressed(root/'corrected_moving_frame_polynomial_L0649_L065.npz',frame=P,eigenvalue=lc,residual=R,normalization_defect=normpoly);p=root/'corrected_moving_frame_polynomial_residual_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_polynomial_bundle']
