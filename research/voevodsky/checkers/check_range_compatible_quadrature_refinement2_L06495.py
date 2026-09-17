#!/usr/bin/env python3
"""Second nested refinement of critical/robust quadrature-error components."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';a=np.load(root/'physical_regularized_residual_gram_L06495_matrices.npz')['lower_form'];b=np.load(root/'physical_regularized_residual_gram_L06495_refined_matrices.npz')['lower_form'];c=np.load(root/'physical_regularized_residual_gram_L06495_refined2_matrices.npz')['lower_form'];ec,V=np.linalg.eigh((c+c.T)/2)
def comp(X):
 E=(X-c);E=(E+E.T)/2;return [abs(float(V[:,0]@E@V[:,0])),float(np.linalg.norm(V[:,1:].T@E@V[:,0])),float(np.linalg.norm(V[:,1:].T@E@V[:,1:],2))]
coarse=comp(a);refined=comp(b);out={'schema':'marici.voevodsky.range-compatible-quadrature-refinement2-L06495.v1','critical_margin':float(ec[0]),'robust_floor':float(ec[1]),'coarse_to_refined2_components':coarse,'refined_to_refined2_components':refined,'component_reduction_factors':[coarse[i]/refined[i] if refined[i] else None for i in range(3)],'critical_and_cross_converge':bool(refined[0]<coarse[0] and refined[1]<coarse[1]),'robust_spectral_convergence_monotone':bool(refined[2]<coarse[2]),'passed':False,'rh_proved':False};p=root/'range_compatible_quadrature_refinement2_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
