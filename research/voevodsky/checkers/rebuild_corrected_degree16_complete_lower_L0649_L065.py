#!/usr/bin/env python3
"""Rebuild all 17 lower forms from Schur minus residual Gram / alpha."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';ev=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');od=np.load(root/'regularized_union_tail_maps_L0649_L065_degree16_extra.npz');even=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];odd=['L0649010','L0649084','L0649222','L0649402','L0649598','L0649778','L0649916','L0649990'];alpha=1.067569476012246;F=[];rows=[]
for k in range(17):
 if k%2==0:
  i=k//2;tag=even[i];S=ev['schur'][i];a=np.load(root/f'physical_regularized_residual_gram_{tag}_refined_matrices.npz')
 else:
  i=k//2;tag=odd[i];S=od['schur'][i];a=np.load(root/f'physical_regularized_residual_gram_{tag}_degree16_refined_matrices.npz')
 H=S-a['residual_gram']/alpha;H=(H+H.T)/2;F.append(H);e=np.linalg.eigvalsh(H);rows.append({'tag':tag,'critical':float(e[0]),'robust':float(e[1])})
F=np.stack(F);t=np.cos(np.arange(16,-1,-1)*np.pi/16);C=np.polynomial.chebyshev.chebfit(t,F.reshape(17,-1),16).reshape(17,40,40);grid=np.linspace(-1,1,4001);branches=[]
for x in grid:
 H=np.polynomial.chebyshev.chebval(x,C);branches.append(np.linalg.eigvalsh((H+H.T)/2)[:2])
branches=np.array(branches);out={'schema':'marici.voevodsky.corrected-degree16-complete-lower-L0649-L065.v1','nodes':rows,'dense_critical_min':float(branches[:,0].min()),'dense_robust_min':float(branches[:,1].min()),'degree16_matrix_interpolant_positive':bool(branches[:,0].min()>0),'passed':False,'reason_not_certificate':'floating corrected interpolation; directed source and ellipse remainder open','rh_proved':False};np.savez_compressed(root/'corrected_degree16_complete_lower_L0649_L065.npz',node_matrices=F,coefficients=C);p=root/'corrected_degree16_complete_lower_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['degree16_matrix_interpolant_positive']
