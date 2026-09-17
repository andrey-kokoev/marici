#!/usr/bin/env python3
"""Generalized Loewner/co-defect scout at L=.75."""
import json,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.linalg import eigh
 from scipy.special import iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.linalg import eigh
 from scipy.special import iv
root=Path(__file__).parents[1]/'results';d=np.load(root/'gamma_floor_L075_prime4_decomposition.npz');H=d['archimedean'];P=d['prime'];A=d['total'];beta=.5;H=H+beta*np.eye(1000);D=beta*np.eye(1000)-P;eh=np.linalg.eigvalsh(H);# A=H-D=H^{1/2}(I-C)H^{1/2}.
w,V=eigh(D,H,eigvals_only=False,subset_by_index=[990,999]);defect=float(w[-1]);gap=1-defect;retain=w>.9;np.savez(root/'normalized_prime_codefect_L075_modes.npz',eigenvalues=w[retain],vectors=V[:,retain],reference=H);# Generalized smallest total ratio equals gap.
out={'schema':'marici.voevodsky.normalized-prime-codefect-L075-scout.v1','dimension':1000,'archimedean_min':float(eh[0]),'largest_ten_prime_codefect_eigenvalues':[float(x) for x in w],'codefect_operator_norm':defect,'normalized_loewner_gap':gap,'retained_codefect_modes_above_point9':int(np.sum(retain)),'complement_codefect_upper':float(w[np.where(~retain)[0][-1]]),'complement_loewner_gap':float(1-w[np.where(~retain)[0][-1]]),'absolute_total_min':float(np.linalg.eigvalsh(A)[0]),'passed':bool(gap>0 and eh[0]>0),'status':'floating generalized eigenvalue scout','rh_proved':False};p=root/'normalized_prime_codefect_L075_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
