#!/usr/bin/env python3
"""Observed E2 component tails from the independent degree-32 node grid."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'gate2_source_FB_degree32_L0649_L065.npz');R=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];rho=2.;tk=[(rho**k+rho**-k)/2 for k in range(33)]
def report(C):
 n=[float(np.linalg.norm(C[k],2)) for k in range(17,33)];return {'spectral_norms_17_32':n,'real_interval_l1':sum(n),'E2_triangle':sum(n[i]*tk[i+17] for i in range(16))}
f=report(d['F']);b=report(d['B']);r=report(R);# perturb Schur norm using stored bounds and C inverse; this is diagnostic, with generous cross charging.
base=json.loads((root/'gate2_component_coefficient_bounds_L0649_L065.json').read_text());F0=base['E2_F_triangle_bound'];B0=base['E2_B_triangle_bound'];ci=base['tail_inverse_bound'];delta=f['E2_triangle']+(2*B0*b['E2_triangle']+b['E2_triangle']**2)*ci+r['E2_triangle']/1.067569476012246;reserve=base['admissible_source_norm']-base['complete_schur_triangle_bound'];out={'schema':'marici.voevodsky.gate2-degree17-32-component-tail-E2.v1','F':f,'B':b,'residual':r,'combined_observed_E2_correction_bound':delta,'stored_component_reserve':reserve,'reserve_ratio':reserve/delta if delta else None,'passed_scout':delta<reserve,'passed':False,'reason_not_certificate':'degree17-32 coefficients include floating noise and do not bound the analytic tail beyond32','rh_proved':False};p=root/'gate2_degree17_32_component_tail_E2.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
