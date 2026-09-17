#!/usr/bin/env python3
"""Operator-norm error budget for interval promotion of the exact-decimal span."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'two_prime_regularized_exact_span_midpoint.npz');P=d['retained'];Z=d['schur_vectors'];A=np.load(root/'rank670_gamma_floor_midpoint.npz')['matrix'];m=np.load(root/'physical_regularized_residual_gram_exact_span_matrices.npz');margin=float(np.linalg.eigvalsh(m['lower_form'])[0]);deltaA=float(json.loads((root/'rank670_gamma_floor_positive.json').read_text())['quadrature_error_spectral_norm']);G=P.T@P;C=P.T@A@Z;pinv=np.linalg.inv(G);pn=np.linalg.norm(P,2);zn=np.linalg.norm(Z,2);cn=np.linalg.norm(C,2);gin=np.linalg.norm(pinv,2);# J and C^*G^-1 C sensitivity, first order plus quadratic term.
dC=pn*zn*deltaA;a_budget=zn*zn*deltaA+2*cn*gin*dC+gin*dC*dC;alpha=.5897761979384148;half=margin/2;residual_allowance=alpha*(half-a_budget)
out={'schema':'marici.voevodsky.exact-span-lower-form-error-budget.v1','floating_margin':margin,'A_operator_error':deltaA,'norms':{'P':pn,'Z':zn,'C':cn,'Gram_inverse':gin},'lower_form_error_from_A':a_budget,'half_margin_target':half,'allowable_residual_gram_operator_error_after_A_budget':residual_allowance,'passed':bool(residual_allowance>0),'rh_proved':False};p=root/'exact_span_lower_form_error_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
