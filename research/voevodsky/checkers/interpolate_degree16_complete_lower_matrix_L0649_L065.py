#!/usr/bin/env python3
"""Degree-16 complete lower matrix using all source Lobatto nodes."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];odd=['L0649010','L0649084','L0649222','L0649402','L0649598','L0649778','L0649916','L0649990'];F=[]
for k in range(17):
 if k%2==0:tag=even[k//2];fn=f'physical_regularized_residual_gram_{tag}_refined_matrices.npz'
 else:tag=odd[k//2];fn=f'physical_regularized_residual_gram_{tag}_degree16_refined_matrices.npz'
 F.append(np.load(root/fn)['lower_form'])
F=np.stack(F);t=np.cos(np.arange(16,-1,-1)*np.pi/16);C=np.polynomial.chebyshev.chebfit(t,F.reshape(17,-1),16).reshape(17,40,40);grid=np.linspace(-1,1,4001);e=[]
for x in grid:e.append(np.linalg.eigvalsh((np.polynomial.chebyshev.chebval(x,C)+np.polynomial.chebyshev.chebval(x,C).T)/2)[:2])
e=np.array(e);norms=[float(np.linalg.norm((x+x.T)/2,2)) for x in C];out={'schema':'marici.voevodsky.degree16-complete-lower-matrix-L0649-L065.v1','dense_critical_min':float(e[:,0].min()),'dense_robust_min':float(e[:,1].min()),'coefficient_spectral_norms':norms,'degree9_to_16_operator_l1':sum(norms[9:]),'passed':float(e[:,0].min())>0,'status':'floating degree16 source-node interpolant; directed remainder beyond degree16 open','rh_proved':False};np.savez_compressed(root/'degree16_complete_lower_matrix_L0649_L065.npz',coefficients=C,node_matrices=F);p=root/'degree16_complete_lower_matrix_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
