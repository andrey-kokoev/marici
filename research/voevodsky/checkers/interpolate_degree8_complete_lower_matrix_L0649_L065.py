#!/usr/bin/env python3
"""Matrix-valued degree-8 Chebyshev interpolation of complete lower forms."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';tags=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];F=np.stack([np.load(root/f'physical_regularized_residual_gram_{x}_refined_matrices.npz')['lower_form'] for x in tags]);t=np.cos(np.arange(8,-1,-1)*np.pi/8);# Fit all entries simultaneously.
C=np.polynomial.chebyshev.chebfit(t,F.reshape(9,-1),8).reshape(9,40,40);norms=[float(np.linalg.norm((x+x.T)/2,2)) for x in C];tail=sum(norms[5:]);grid=np.linspace(-1,1,2001);mins=[]
for x in grid:
 M=np.polynomial.chebyshev.chebval(x,C);mins.append(float(np.linalg.eigvalsh((M+M.T)/2)[0]))
out={'schema':'marici.voevodsky.degree8-complete-lower-matrix-L0649-L065.v1','coefficient_spectral_norms':norms,'degree4_to_8_tail_operator_bound':tail,'dense_min':min(mins),'dense_min_L':float(.6495+.0005*grid[int(np.argmin(mins))]),'minimum_node_margin':float(min(np.linalg.eigvalsh((x+x.T)/2)[0] for x in F)),'tail_to_margin_ratio':tail/min(mins),'passed':min(mins)>0,'status':'floating matrix interpolation; directed ellipse remainder beyond degree 8 open','rh_proved':False};p=root/'degree8_complete_lower_matrix_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(root/'degree8_complete_lower_matrix_L0649_L065.npz',coefficients=C);print(json.dumps(out,indent=2));assert out['passed']
