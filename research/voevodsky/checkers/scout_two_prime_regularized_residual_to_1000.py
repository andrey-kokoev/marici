#!/usr/bin/env python3
"""Residual-Gram scout for regularized rank-670 vectors in modes 670..999."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';A=np.load(root/'gamma_floor_rank1000_midpoint.npz')['matrix'];d=np.load(root/'two_prime_regularized_rank670_vectors.npz');Z=d['schur_vectors'];S=d['finite_schur'];R=A[670:,:670]@Z;alpha=.5897761979384148;lower=(S-R.T@R/alpha);lower=(lower+lower.T)/2;ev=np.linalg.eigvalsh(lower)
out={'schema':'marici.voevodsky.two-prime-regularized-residual-to-1000-scout.v1','residual_shape':list(R.shape),'residual_norm':float(np.linalg.svd(R,compute_uv=False)[0]),'residual_gram_norm':float(np.linalg.eigvalsh(R.T@R)[-1]),'a_posteriori_lower_form_min':float(ev[0]),'negative_eigenvalues_below_minus_1e-10':int(np.sum(ev<-1e-10)),'status':'floating; modes >=1000 omitted','passed':float(ev[0])>0,'rh_proved':False};p=root/'two_prime_regularized_residual_to_1000_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
