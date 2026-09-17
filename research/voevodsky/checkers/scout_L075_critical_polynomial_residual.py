#!/usr/bin/env python3
"""Degree-truncated critical-mode residual certificate scout at L=.75."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:,-1];A=np.load(root/'gamma_floor_L075_prime4_Q400_decomposition.npz')['total'];alpha=.08457851972191266*.26338577235124017;rows=[]
for n in (50,75,100,150,200):
 w=v.copy();w[n:]=0;J=float(w@A@w);r=A@w;r[:n]=0;rn=float(np.linalg.norm(r));lower=J-rn*rn/alpha;rows.append({'degree_exclusive':n,'candidate_form':J,'residual_norm':rn,'complement_floor':alpha,'a_posteriori_lower':lower})
out={'schema':'marici.voevodsky.L075-critical-polynomial-residual-scout.v1','rows':rows,'selected_degree_exclusive':150,'selected_lower':rows[3]['a_posteriori_lower'],'status':'floating; reduced polynomial architecture for directed assembly','passed':rows[3]['a_posteriori_lower']>0,'rh_proved':False};p=root/'L075_critical_polynomial_residual_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
