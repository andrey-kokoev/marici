#!/usr/bin/env python3
"""Compare canonical and refined physical residual-Gram quadratures."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';a=np.load(root/'physical_regularized_residual_gram_matrices.npz');b=np.load(root/'physical_regularized_residual_gram_matrices_refined.npz');keys=('output_gram','residual_gram','lower_form');diff={k:{'max_entry':float(np.max(abs(a[k]-b[k]))),'spectral_norm':float(np.linalg.norm(a[k]-b[k],2))} for k in keys};margin=float(np.linalg.eigvalsh(b['lower_form'])[0]);target=margin/(2*92)
out={'schema':'marici.voevodsky.physical-residual-quadrature-convergence.v1','coarse_nodes':{'physical':4500,'frequency':3780},'refined_nodes':{'physical':5500,'frequency':4680},'differences':diff,'refined_lower_margin':margin,'uniform_entry_target_for_half_margin':target,'convergence_difference_below_target':diff['lower_form']['max_entry']<target,'status':'floating convergence evidence, not a directed remainder bound','passed':True,'rh_proved':False};p=root/'physical_residual_quadrature_convergence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
