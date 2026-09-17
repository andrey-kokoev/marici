#!/usr/bin/env python3
"""Conservative source-operator tolerance for the seven-mode Schur margin."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';V=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'];A=np.load(root/'gamma_floor_L075_prime4_decomposition.npz')['total'];B=(V.T@A@V);B=(B+B.T)/2;F=B[:6,:6];b=B[:6,6];c=B[6,6];fi=np.linalg.norm(np.linalg.inv(F),2);bn=np.linalg.norm(b);vn=np.linalg.norm(V,2);s=c-b@np.linalg.solve(F,b);# If ||dB||<=e and e*||F^-1||<1, inverse perturbation plus direct terms.
def loss(e):
 if e*fi>=1:return float('inf')
 return e+2*bn*fi*e+e*e*fi+(bn+e)**2*fi*fi*e/(1-e*fi)
target=s/2;lo,hi=0.,min(1/fi*.49,target)
for _ in range(100):
 mid=(lo+hi)/2
 if loss(mid)<=target:lo=mid
 else:hi=mid
source=lo/(vn*vn);q=json.loads((root/'L075_codefect_gauss_order_selection.json').read_text())['selected_spectral_remainder'];out={'schema':'marici.voevodsky.L075-codefect-source-matrix-tolerance.v1','critical_schur_margin':float(s),'retained_map_norm':float(vn),'robust_inverse_norm':float(fi),'critical_cross_norm':float(bn),'allowable_seven_block_operator_error':lo,'allowable_source_operator_error':source,'order68_gamma_spectral_remainder':q,'remainder_below_source_tolerance':bool(q<source),'reserve_factor':source/q,'passed':bool(q<source),'rh_proved':False};p=root/'L075_codefect_source_matrix_tolerance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
