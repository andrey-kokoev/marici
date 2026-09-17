#!/usr/bin/env python3
"""Matrix-oriented reserve for a second-variation tail using the last smooth block shape."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['schur'][4];J=np.load(root/'residual_jump_variation_gram_L06495.npz')['tail_gram'];Sm=np.load(root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.npz')['smooth'][-1000:];G=Sm.T@Sm;alpha=1.067569476012246;rows=[]
for m in (1.1,2,4,8,16,32):
 M=S-(J+m*G)/alpha;M=(M+M.T)/2;rows.append({'smooth_last_block_multiplier':m,'lower':float(np.linalg.eigvalsh(M)[0])})
out={'schema':'marici.voevodsky.matrix-oriented-smooth-tail-budget-L06495.v1','last_smooth_block_gram_norm':float(np.linalg.norm(G,2)),'n_minus_2_coefficient_model_tail_to_last_block_ratio':1/(5**3)/(1/(4**3)-1/(5**3)),'rows':rows,'status':'floating shape scout; directed second-variation Gram still required','passed_empirically':rows[3]['lower']>0,'passed':False,'rh_proved':False};p=root/'matrix_oriented_smooth_tail_budget_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_empirically']
