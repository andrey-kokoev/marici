#!/usr/bin/env python3
"""Separate six robust normalized defect modes from the single critical mode."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';m=np.load(root/'normalized_prime_codefect_L075_modes.npz');V=m['vectors'];A=np.load(root/'gamma_floor_L075_prime4_decomposition.npz')['total'];B=V.T@A@V;B=(B+B.T)/2;# eigh returned ascending codefect: critical direction is final column.
F=B[:-1,:-1];b=B[:-1,-1];c=float(B[-1,-1]);schur=c-float(b@np.linalg.solve(F,b));tail=np.linalg.norm(V[150:,-1]);out={'schema':'marici.voevodsky.L075-codefect-block-schur-scout.v1','block_dimension':7,'robust_block_min':float(np.linalg.eigvalsh(F)[0]),'critical_diagonal':c,'critical_cross_norm':float(np.linalg.norm(b)),'critical_schur_margin':schur,'critical_vector_tail_after_degree149':float(tail),'full_block_eigenvalues':[float(x) for x in np.linalg.eigvalsh(B)],'status':'floating; isolates one critical direction','passed':float(np.linalg.eigvalsh(F)[0])>1e-13 and schur>0,'rh_proved':False};p=root/'L075_codefect_block_schur_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
