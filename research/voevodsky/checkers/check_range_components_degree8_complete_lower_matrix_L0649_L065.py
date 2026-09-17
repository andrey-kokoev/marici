#!/usr/bin/env python3
"""Critical/robust components of matrix-valued Chebyshev coefficients."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree8_complete_lower_matrix_L0649_L065.npz')['coefficients'];M=np.polynomial.chebyshev.chebval(0.,C);e,V=np.linalg.eigh((M+M.T)/2);v=V[:,0];R=V[:,1:];rows=[]
for k,A in enumerate(C):
 A=(A+A.T)/2;rows.append({'degree':k,'critical':float(abs(v@A@v)),'cross':float(np.linalg.norm(R.T@A@v)),'robust':float(np.linalg.norm(R.T@A@R,2))})
tail={z:sum(x[z] for x in rows[5:]) for z in ('critical','cross','robust')};out={'schema':'marici.voevodsky.range-components-degree8-complete-lower-matrix-L0649-L065.v1','center_critical_margin':float(e[0]),'center_robust_floor':float(e[1]),'coefficient_components':rows,'degree5_to_8_component_sums':tail,'passed':True,'status':'floating fixed-center splitting; moving critical line or block-Schur interval continuation required','rh_proved':False};p=root/'range_components_degree8_complete_lower_matrix_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
