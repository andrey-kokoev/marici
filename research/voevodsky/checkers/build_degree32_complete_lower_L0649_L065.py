#!/usr/bin/env python3
"""Assemble the 33-node corrected complete-lower matrix interpolant."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';old=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['node_matrices'];new=np.load(root/'degree32_new_tail_maps_L0649_L065.npz');tags=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];alpha=1.067569476012246;F=[];rows=[]
for k in range(33):
 if k%2==0:H=old[k//2];tag='existing'
 else:
  i=k//2;tag=tags[i];a=np.load(root/f'physical_regularized_residual_gram_{tag}_degree32new_refined_matrices.npz');H=new['schur'][i]-a['residual_gram']/alpha;H=(H+H.T)/2
 F.append(H);rows.append({'position':k,'tag':tag,'minimum':float(np.linalg.eigvalsh(H)[0])})
F=np.array(F);t=np.cos(np.arange(32,-1,-1)*np.pi/32);C=np.polynomial.chebyshev.chebfit(t,F.reshape(33,-1),32).reshape(33,40,40);norms=[float(np.linalg.norm(x,2)) for x in C];tail=sum(norms[17:]);delta=max(float(np.linalg.norm(np.polynomial.chebyshev.chebval(x,C)-np.polynomial.chebyshev.chebval(x,np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients']),2)) for x in np.linspace(-1,1,4001));out={'schema':'marici.voevodsky.degree32-complete-lower-L0649-L065.v1','rows':rows,'coefficient_spectral_norms':norms,'degree17_32_l1':tail,'dense_degree32_minus_degree16_max':delta,'critical_source_error_target':5.00066667380444e-12,'passed_scout':bool(tail<5.00066667380444e-12),'passed':False,'reason_not_certificate':'tail beyond degree 32 remains open','rh_proved':False};np.savez_compressed(root/'degree32_complete_lower_L0649_L065.npz',node_matrices=F,coefficients=C);p=root/'degree32_complete_lower_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
