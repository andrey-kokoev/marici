#!/usr/bin/env python3
"""Directed-style IEEE/Frobenius min-max certificate for the fourth polynomial eigenvalue."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];u=2**-53
def gamma(n): return n*u/(1-n*u)
def up(x): return float(np.nextafter(x,np.inf))
# Frobenius dominates spectral norm; |T'_k| <= k^2 on [-1,1].
D=up(sum(up(k*k*np.linalg.norm(C[k],'fro')) for k in range(1,17))*(1+gamma(2000)));N=4096;worst=1e300;maxE=maxO=0.0
for j in range(N):
 x=-1+(2*j+1)/N;H=np.polynomial.chebyshev.chebval(x,C);H=(H+H.T)/2;e,V=np.linalg.eigh(H);Q=V[:,3:];d=e[3:];E=H@Q-Q*d;O=Q.T@Q-np.eye(37)
 # Inflate Frobenius norms for all evaluation and dot-product rounding. The additive term uses entrywise absolute-operation bounds.
 evalerr=gamma(40)*sum(np.linalg.norm(C[k],'fro') for k in range(17));eb=up(np.linalg.norm(E,'fro')+evalerr+gamma(82)*(np.linalg.norm(H,'fro')*np.linalg.norm(Q,'fro')+np.linalg.norm(Q*d,'fro')));ob=up(np.linalg.norm(O,'fro')+gamma(82)*np.linalg.norm(Q,'fro')**2);center=(float(d[0])-eb)/(1+ob);worst=min(worst,center);maxE=max(maxE,eb);maxO=max(maxO,ob)
lower=worst-D/N;out={'schema':'marici.voevodsky.fourth-eigenvalue-directed-roundoff-L0649-L065.v1','arithmetic_model':'IEEE-754 binary64, unit roundoff 2^-53, standard gamma_n bounds; every norm replaced by Frobenius upper bound and final scalars rounded upward','cells':N,'directed_frobenius_derivative_bound':D,'maximum_inflated_restriction_residual':maxE,'maximum_inflated_orthogonality_defect':maxO,'minimum_center_restricted_rayleigh_lower':worst,'global_fourth_eigenvalue_lower':lower,'passed_stored_polynomial':bool(lower>0),'source_matrix_enclosed':False,'passed':False,'rh_proved':False};p=root/'fourth_eigenvalue_directed_roundoff_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_polynomial']
