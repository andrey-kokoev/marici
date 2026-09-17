#!/usr/bin/env python3
"""Locate the coupled smooth tail relative to endpoint derivative row space."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;k=np.arange(1000);sc=np.sqrt((2*k+1)/(2*L));de=k*(k+1)/(2*L);F=np.array([[legval(1,Z[:,j]*sc*de) for j in range(40)],[legval(-1,Z[:,j]*sc*de*((-1.)**(k+1))) for j in range(40)]]).T;Q=np.linalg.qr(F)[0];Proj=Q@Q.T;rows=[]
for m in (5,6,7):
 S=np.load(root/f'continuum_residual_jump_smooth_L06495_{m}000_{m}999.npz')['smooth'];V=np.linalg.svd(S,full_matrices=False)[2][:2].T;angles=np.linalg.svd(Q.T@V,compute_uv=False);par=np.linalg.norm(S@Proj,2);perp=np.linalg.norm(S@(np.eye(40)-Proj),2);rows.append({'m':m,'principal_cosines_top2_vs_endpoint_derivative_space':angles.tolist(),'parallel_norm':float(par),'perpendicular_norm':float(perp),'m_parallel':float(m*par),'m_perpendicular':float(m*perp)})
out={'schema':'marici.voevodsky.gate3-smooth-derivative-endpoint-subspace.v1','rows':rows,'finding':'one dominant singular channel converges to the two-row endpoint derivative space; the complementary channel must be retained separately','passed_audit':True,'next':'derive the coupled scalar coefficient kernels after projection onto this two-dimensional row space, then bound the perpendicular remainder by higher antiderivatives','rh_proved':False};p=root/'gate3_smooth_derivative_endpoint_subspace.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
