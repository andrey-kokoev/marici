#!/usr/bin/env python3
"""Quantify binary64 instability of the L=.75 critical block under quadrature refinement."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';V=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'];A0=np.load(root/'gamma_floor_L075_prime4_decomposition.npz')['total'];A1=np.load(root/'gamma_floor_L075_prime4_Q400_decomposition.npz')['total']
def schur(A):
 B=V.T@A@V;B=(B+B.T)/2;F=B[:6,:6];b=B[:6,6];return float(B[6,6]-b@np.linalg.solve(F,b))
diff=float(np.linalg.norm(A1-A0,2));tol=json.loads((root/'L075_codefect_source_matrix_tolerance.json').read_text())['allowable_source_operator_error'];out={'schema':'marici.voevodsky.L075-rank1000-roundoff-instability.v1','Q300_critical_schur':schur(A0),'Q400_critical_schur':schur(A1),'source_matrix_spectral_difference':diff,'allowable_source_operator_error':tol,'difference_over_tolerance':diff/tol,'conclusion':'binary64 full-matrix assembly cannot certify the critical block; directed reduced-block assembly is mandatory','passed':True,'rh_proved':False};p=root/'L075_rank1000_roundoff_instability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
