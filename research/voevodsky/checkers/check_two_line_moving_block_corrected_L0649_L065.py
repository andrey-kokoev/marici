#!/usr/bin/env python3
"""Critical/second-line orthogonality and residual Schur budget."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.chebyshev import chebmul
root=Path(__file__).parents[1]/'results';a=np.load(root/'corrected_moving_frame_polynomial_L0649_L065.npz');b=np.load(root/'second_moving_line_corrected_L0649_L065.npz');p=a['frame'];q=b['frame'];cross=np.zeros(65)
for i in range(40):z=chebmul(p[:,i],q[:,i]);cross[:len(z)]+=z
orth=sum(abs(cross));r1=sum(np.linalg.norm(x) for x in a['residual']);r2=sum(np.linalg.norm(x) for x in b['residual']);l1min=1.9142969348170045e-11;l2min=8.968462765343291e-9;# Approximate-line residual losses against the next gaps.
loss1=r1*r1/l2min;loss2=r2*r2/(1.7e-6-l2min);out={'schema':'marici.voevodsky.two-line-moving-block-corrected-L0649-L065.v1','mutual_orthogonality_defect_bound':float(orth),'critical_residual_bound':float(r1),'second_residual_bound':float(r2),'critical_residual_loss':float(loss1),'second_residual_loss_using_1p7e-6_bulk_floor':float(loss2),'critical_branch_lower_after_loss':float(l1min-loss1),'second_branch_lower_after_loss':float(l2min-loss2),'passed_scout':bool(orth<1e-10 and l1min>loss1 and l2min>loss2),'passed':False,'remaining':'directed coefficients and directed third-eigenvalue/bulk floor','rh_proved':False};pout=root/'two_line_moving_block_corrected_L0649_L065.json';pout.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
