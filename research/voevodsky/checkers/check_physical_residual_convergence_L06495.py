#!/usr/bin/env python3
"""Coarse/refined convergence of the complete L=.6495 physical residual Gram."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';a=np.load(root/'physical_regularized_residual_gram_L06495_matrices.npz');b=np.load(root/'physical_regularized_residual_gram_L06495_refined_matrices.npz');diff={k:{'spectral':float(np.linalg.norm(a[k]-b[k],2)),'max_entry':float(np.max(abs(a[k]-b[k])))} for k in ('output_gram','residual_gram','lower_form')};eb,V=np.linalg.eigh(b['lower_form']);margin=float(eb[0]);critical_shift=float(abs(V[:,0]@(a['lower_form']-b['lower_form'])@V[:,0]));critical_cross=float(np.linalg.norm(V[:,1:].T@(a['lower_form']-b['lower_form'])@V[:,0]));out={'schema':'marici.voevodsky.physical-residual-convergence-L06495.v1','differences':diff,'refined_lower_margin':margin,'spectral_difference_to_margin_ratio':diff['lower_form']['spectral']/margin,'critical_rayleigh_difference':critical_shift,'critical_cross_difference':critical_cross,'passed':diff['lower_form']['spectral']<margin/100,'rh_proved':False};p=root/'physical_residual_convergence_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
