#!/usr/bin/env python3
"""Directed coefficient-norm checks for the stored moving-frame polynomial."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';d=np.load(root/'corrected_moving_frame_polynomial_L0649_L065.npz');R=d['residual'];q=d['normalization_defect'];
def A(x):return arb(repr(float(x)))
res=arb(0)
for row in R:res+=sum((A(x)*A(x) for x in row),arb(0)).sqrt()
norm=sum((abs(A(x)) for x in q),arb(0));gap=arb('8.968462242850897e-9');corr=res*res/gap;margin=arb('1.9148642329984542e-11');out={'schema':'marici.voevodsky.corrected-moving-frame-polynomial-arb-L0649-L065.v1','precision_bits':flint.ctx.prec,'normalization_defect_l1':str(norm),'eigen_residual_vector_coefficient_l1':str(res),'schur_correction_using_directed_robust_polynomial_floor':str(corr),'critical_margin':str(margin),'passed_stored_bundle':norm.upper()<arb('1e-12') and corr.upper()<margin.lower()/10,'source_matrix_enclosed':False,'passed':False,'scope':'stored decimal polynomial bundle is directed; generation rounding and true source-to-interpolant error remain open','rh_proved':False};p=root/'corrected_moving_frame_polynomial_arb_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_bundle']
