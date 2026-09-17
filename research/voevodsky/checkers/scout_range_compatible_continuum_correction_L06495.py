#!/usr/bin/env python3
"""Apply the continuum residual Gram as a matrix, preserving critical-range compatibility."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['schur'][4];R=np.load(root/'regularized_union_continuum_residual_L06495.npz')['residual'];alpha=1.067569476012246;lower=S-R.T@R/alpha;lower=(lower+lower.T)/2;es=np.linalg.eigvalsh(S);el=np.linalg.eigvalsh(lower);out={'schema':'marici.voevodsky.range-compatible-continuum-correction-L06495.v1','uncorrected_min':float(es[0]),'corrected_min_modes_through_1999':float(el[0]),'minimum_loss':float(es[0]-el[0]),'negative_eigenvalues':int(np.sum(el<0)),'status':'floating; modes >=2000 omitted','passed':float(el[0])>0,'rh_proved':False};p=root/'range_compatible_continuum_correction_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
