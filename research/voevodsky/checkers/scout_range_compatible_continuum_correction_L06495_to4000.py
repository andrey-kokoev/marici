#!/usr/bin/env python3
"""Combined range-compatible residual correction through mode 2999."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['schur'][4];R1=np.load(root/'regularized_union_continuum_residual_L06495.npz')['residual'];R2=np.load(root/'regularized_union_continuum_residual_L06495_2000_2999.npz')['residual'];R3=np.load(root/'regularized_union_continuum_residual_L06495_3000_3999.npz')['residual'];R=np.vstack((R1,R2,R3));alpha=1.067569476012246;lower=S-R.T@R/alpha;lower=(lower+lower.T)/2;es=np.linalg.eigvalsh(S);el=np.linalg.eigvalsh(lower);out={'schema':'marici.voevodsky.range-compatible-continuum-correction-L06495-to4000.v1','mode_range':[1000,3999],'combined_residual_norm':float(np.linalg.norm(R,2)),'uncorrected_min':float(es[0]),'corrected_min':float(el[0]),'minimum_loss':float(es[0]-el[0]),'status':'floating; modes >=4000 omitted','passed':float(el[0])>0,'rh_proved':False};p=root/'range_compatible_continuum_correction_L06495_to4000.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
