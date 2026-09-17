#!/usr/bin/env python3
"""Assess direct determinant arc enclosure requirements on the rho=5 ellipse."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho5_scout64.json').read_text());r=d['samples'];z=np.array([complex(x['L_real'],x['L_imag']) for x in r]);det=np.array([complex(x['robust_det_real'],x['robust_det_imag']) for x in r]);der=max(abs((det[(i+1)%len(det)]-det[i])/(z[(i+1)%len(z)]-z[i])) for i in range(len(z)));half=max(abs(z[(i+1)%len(z)]-z[i]) for i in range(len(z)))/2;mn=min(abs(det));# Required derivative for disk exclusion around every sample.
required=mn/half;out={'schema':'marici.voevodsky.rho5-determinant-arc-budget.v1','minimum_sampled_modulus':float(mn),'maximum_secant_derivative':float(der),'maximum_half_chord':float(half),'required_derivative_bound_for_direct_disk_exclusion':float(required),'secant_to_required_ratio':float(der/required),'direct_modulus_cover_viable':bool(der<required),'passed':True,'rh_proved':False};p=root/'rho5_determinant_arc_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
