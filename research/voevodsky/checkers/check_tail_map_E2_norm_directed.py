#!/usr/bin/env python3
"""Coefficient-triangle bound for the stored regularized tail map on E2."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree16_regularized_tail_map_L0649_L065.npz')['coefficients'];u=2**-53;gam=4000*u/(1-4000*u);rho=2.;rows=[];bound=0
for k,A in enumerate(C):
 s=np.linalg.svd(A,compute_uv=False);upper=float(np.nextafter(s[0]+gam*np.linalg.norm(A,'fro'),np.inf));tk=(rho**k+rho**-k)/2;bound+=upper*tk;rows.append({'degree':k,'spectral_upper':upper,'E2_weight':tk,'contribution':upper*tk})
graph=1+bound*bound;raw=json.loads((root/'gate2_raw_source_operator_E2_budget.json').read_text());base=6.690324900504932e-9;formerr=graph*raw['conditional_interpolation_error'];lower=base-formerr;out={'schema':'marici.voevodsky.tail-map-E2-norm-directed.v1','arithmetic_model':'stored binary64 coefficients, SVD spectral norm plus gamma_4000 Frobenius inflation and outward nextafter','rows':rows,'E2_tail_map_norm_upper':bound,'graph_metric_upper':graph,'source_form_error':formerr,'conditional_true_source_robust_lower':lower,'passed_stored_tail_map':bool(lower>0),'passed':False,'remaining':'directed raw-source analytic majorant','rh_proved':False};p=root/'tail_map_E2_norm_directed.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_tail_map']
