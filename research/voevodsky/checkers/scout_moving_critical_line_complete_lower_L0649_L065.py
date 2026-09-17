#!/usr/bin/env python3
"""Moving critical eigenline and robust gap for degree-8 complete lower-form interpolant."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree8_complete_lower_matrix_L0649_L065.npz')['coefficients'];Cp=np.polynomial.chebyshev.chebder(C,axis=0);grid=np.linspace(-1,1,4001);lam1=[];lam2=[];rot=[];Vprev=None
for t in grid:
 M=np.polynomial.chebyshev.chebval(t,C);e,V=np.linalg.eigh((M+M.T)/2);v=V[:,0];lam1.append(float(e[0]));lam2.append(float(e[1]));D=np.polynomial.chebyshev.chebval(t,Cp);rot.append(float(np.linalg.norm(V[:,1:].T@D@v)/(e[1]-e[0])));Vprev=v
# Scalar Chebyshev coefficients from a denser Lobatto sampling of interpolated eigenbranches.
tn=np.cos(np.arange(32,-1,-1)*np.pi/32);branches=np.array([np.linalg.eigvalsh((np.polynomial.chebyshev.chebval(t,C)+np.polynomial.chebyshev.chebval(t,C).T)/2)[:2] for t in tn]);cc1=np.polynomial.chebyshev.chebfit(tn,branches[:,0],32);cc2=np.polynomial.chebyshev.chebfit(tn,branches[:,1],32);out={'schema':'marici.voevodsky.moving-critical-line-complete-lower-L0649-L065.v1','minimum_critical_branch':min(lam1),'minimum_robust_branch':min(lam2),'maximum_projective_speed_per_scaled_t':max(rot),'critical_branch_tail_degree9_32_l1':float(sum(abs(cc1[9:]))),'robust_branch_tail_degree9_32_l1':float(sum(abs(cc2[9:]))),'critical_last_coefficient':float(abs(cc1[-1])),'robust_last_coefficient':float(abs(cc2[-1])),'passed':min(lam1)>0 and min(lam2)>0,'status':'floating moving-line scout for polynomial interpolant; directed eigenspace enclosure open','rh_proved':False};p=root/'moving_critical_line_complete_lower_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
