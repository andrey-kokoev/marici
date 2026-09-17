#!/usr/bin/env python3
"""Cellwise Weyl/Lipschitz certificate scout for the fourth eigenvalue."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];cn=np.array([np.linalg.norm((x+x.T)/2,2) for x in C]);D=float(sum(k*k*cn[k] for k in range(1,17)));N=4096;rad=1/N;mins=[];res=[];orth=[]
for j in range(N):
 x=-1+(2*j+1)/N;H=np.polynomial.chebyshev.chebval(x,C);H=(H+H.T)/2;e,V=np.linalg.eigh(H);mins.append(e[3]);res.append(np.linalg.norm(H@V-V*e,2));orth.append(np.linalg.norm(V.T@V-np.eye(40),2))
# Conservative numerical eigensolver allowance, to be replaced by directed LDL/eigendecomposition audit.
roundoff=max(res)+4*max(orth)*float(max(abs(np.array(mins))))+1e-14;lower=min(mins)-D*rad-roundoff;out={'schema':'marici.voevodsky.fourth-eigenvalue-lipschitz-scout-L0649-L065.v1','cells':N,'matrix_chebyshev_derivative_bound':D,'minimum_center_fourth_eigenvalue':float(min(mins)),'maximum_eigen_residual':float(max(res)),'maximum_orthogonality_defect':float(max(orth)),'provisional_roundoff_allowance':float(roundoff),'weyl_cell_lower':float(lower),'passed_scout':bool(lower>0),'passed':False,'remaining':'promote center eigensolver bounds and coefficient norms to directed arithmetic','rh_proved':False};p=root/'fourth_eigenvalue_lipschitz_scout_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
