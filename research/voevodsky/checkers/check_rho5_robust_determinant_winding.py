#!/usr/bin/env python3
"""Sampled argument-principle audit for the rho=5 robust-block determinant."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho5_scout64.json').read_text());z=np.array([complex(x['robust_det_real'],x['robust_det_imag']) for x in d['samples']]);phase=np.unwrap(np.angle(np.r_[z,z[0]]));wind=float((phase[-1]-phase[0])/(2*np.pi));jump=float(np.max(abs(np.diff(phase))));out={'schema':'marici.voevodsky.rho5-robust-determinant-winding-scout.v1','samples':len(z),'sampled_winding_number':wind,'maximum_phase_increment':jump,'minimum_sampled_determinant_modulus':float(np.min(abs(z))),'interpretation':'zero winding plus a directed nonvanishing arc enclosure would prove robust-block invertibility inside rho=5','passed':abs(wind)<1e-12 and jump<np.pi,'rh_proved':False};p=root/'rho5_robust_determinant_winding_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
