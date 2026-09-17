#!/usr/bin/env python3
"""Recursive Schur reduction of rho=5 robust-block invertibility."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho5_scout64.json').read_text());r=d['samples'];z=np.array([complex(x['L_real'],x['L_imag']) for x in r]);s=np.array([complex(x['robust_scalar_schur_real'],x['robust_scalar_schur_imag']) for x in r]);ph=np.unwrap(np.angle(np.r_[s,s[0]]));der=max(abs((s[(i+1)%len(s)]-s[i])/(z[(i+1)%len(z)]-z[i])) for i in range(len(z)));half=max(abs(z[(i+1)%len(z)]-z[i]) for i in range(len(z)))/2;mn=min(abs(s));out={'schema':'marici.voevodsky.rho5-recursive-schur-invertibility.v1','strong_18_block_min_sampled_singular':min(x['strong_block_min_singular'] for x in r),'robust_scalar_schur_min_sampled_abs':float(mn),'robust_scalar_schur_max_sampled_abs':float(max(abs(s))),'scalar_winding':float((ph[-1]-ph[0])/(2*np.pi)),'scalar_max_phase_increment':float(max(abs(np.diff(ph)))),'scalar_max_secant_derivative':float(der),'half_chord':float(half),'secant_arc_variation':float(der*half),'direct_scalar_cover_viable_with_observed_secant':bool(der*half<mn),'passed':bool((ph[-1]-ph[0])==0 and min(x['strong_block_min_singular'] for x in r)>1e-8),'rh_proved':False};p=root/'rho5_recursive_schur_invertibility.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
