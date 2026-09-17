#!/usr/bin/env python3
"""Schur perturbation budget using critical/robust quadrature-error components."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';a=np.load(root/'physical_regularized_residual_gram_L06495_matrices.npz')['lower_form'];b=np.load(root/'physical_regularized_residual_gram_L06495_refined_matrices.npz')['lower_form'];eb,V=np.linalg.eigh((b+b.T)/2);E=(a-b);E=(E+E.T)/2;da=abs(float(V[:,0]@E@V[:,0]));db=float(np.linalg.norm(V[:,1:].T@E@V[:,0]));dC=float(np.linalg.norm(V[:,1:].T@E@V[:,1:],2));margin=float(eb[0]);beta=float(eb[1]);# Spend 4x observed nested difference as a prospective directed enclosure.
f=4.;den=beta-f*dC;lower=margin-f*da-(f*db)**2/den if den>0 else -math.inf
out={'schema':'marici.voevodsky.range-compatible-quadrature-perturbation-L06495.v1','critical_margin':margin,'robust_floor':beta,'observed_components':{'critical':da,'cross':db,'robust':dC},'safety_factor':f,'robust_denominator_after_budget':den,'conditional_schur_lower':lower,'condition':'directed quadrature errors bounded by four times the coarse/refined component differences','passed_conditionally':lower>0,'passed':False,'rh_proved':False};p=root/'range_compatible_quadrature_perturbation_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
