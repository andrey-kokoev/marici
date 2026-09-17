#!/usr/bin/env python3
"""Interpolate only the two lowest source eigenbranches at 17 Lobatto nodes."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];odd=['L0649010','L0649084','L0649222','L0649402','L0649598','L0649778','L0649916','L0649990'];vals=[]
for k in range(17):
 if k%2==0:fn=root/f'physical_regularized_residual_gram_{even[k//2]}_refined_matrices.npz'
 else:fn=root/f'physical_regularized_residual_gram_{odd[k//2]}_degree16_refined_matrices.npz'
 H=np.load(fn)['lower_form'];vals.append(np.linalg.eigvalsh((H+H.T)/2)[:2])
vals=np.array(vals);t=np.cos(np.arange(16,-1,-1)*np.pi/16);c1=np.polynomial.chebyshev.chebfit(t,vals[:,0],16);c2=np.polynomial.chebyshev.chebfit(t,vals[:,1],16);grid=np.linspace(-1,1,10001);y1=np.polynomial.chebyshev.chebval(grid,c1);y2=np.polynomial.chebyshev.chebval(grid,c2);out={'schema':'marici.voevodsky.degree16-source-eigenbranches-L0649-L065.v1','critical_coefficients':[float(x) for x in c1],'robust_coefficients':[float(x) for x in c2],'critical_degree9_16_l1':float(sum(abs(c1[9:]))),'robust_degree9_16_l1':float(sum(abs(c2[9:]))),'critical_dense_min':float(min(y1)),'robust_dense_min':float(min(y2)),'critical_last_coefficient':float(abs(c1[-1])),'robust_last_coefficient':float(abs(c2[-1])),'passed_scout':bool(min(y1)>0 and min(y2)>0),'passed':False,'reason_not_certificate':'scalar source-node interpolation; directed analytic branch remainder open','rh_proved':False};p=root/'degree16_source_eigenbranches_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
