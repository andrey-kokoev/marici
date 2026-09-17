#!/usr/bin/env python3
"""Range-compatible Q300/Q400 source-matrix difference at L=.6495."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';A=np.load(root/'gamma_floor_L06495_rank1000_midpoint.npz')['matrix'];B=np.load(root/'gamma_floor_L06495_Q400_rank1000_midpoint.npz')['matrix'];md=np.load(root/'physical_regularized_residual_gram_L06495_refined2_matrices.npz');e,V=np.linalg.eigh((md['lower_form']+md['lower_form'].T)/2);Z=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');W=Z['packet']-Z['tail_maps'][4];E=W.T@(B-A)@W;E=(E+E.T)/2;crit=abs(float(V[:,0]@E@V[:,0]));cross=float(np.linalg.norm(V[:,1:].T@E@V[:,0]));rob=float(np.linalg.norm(V[:,1:].T@E@V[:,1:],2));corr=crit+cross*cross/(float(e[1])-rob) if rob<float(e[1]) else float('inf');out={'schema':'marici.voevodsky.source-matrix-refinement-range-components-L06495.v1','full_source_spectral_difference':float(np.linalg.norm(B-A,2)),'trial_critical_component':crit,'trial_cross_component':cross,'trial_robust_component':rob,'lower_form_robust_floor':float(e[1]),'range_compatible_source_correction':corr,'critical_margin':float(e[0]),'correction_to_margin_ratio':corr/float(e[0]),'passed':corr<float(e[0])/10,'rh_proved':False};p=root/'source_matrix_refinement_range_components_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
