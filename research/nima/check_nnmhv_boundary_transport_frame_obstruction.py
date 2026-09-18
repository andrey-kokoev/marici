#!/usr/bin/env python3
"""Show why transported boundary spinors do not define global SL(2,C) frames."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import momentum_conserving_kinematics,x_interval
from nnmhv_coherence_paths import compile_nnmhv_histories
lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,8)],[(1,j**3+2*j+1) for j in range(1,6)]);edge=x_interval(x,7,6);affected=[]
for k,h in enumerate(compile_nnmhv_histories(7)):
 if h.inner_prefix and h.inner_prefix[0]==6:affected.append(k)
checks={'adjacent_dual_edge_is_null':s.factor(edge.det())==0,'null_edge_matrix_has_rank_one':edge.rank()==1,'four_histories_use_singular_prefix':affected==[2,3,4,5]}
out={'schema':'marici.nima.nnmhv-boundary-transport-frame-obstruction.v1','edge':'x_(7,6)','determinant':str(s.factor(edge.det())),'rank':edge.rank(),'affected_history_indices':affected,'checks':checks,'passed':all(checks.values()),'conclusion':'Boundary transport acts on projective spinor lines through possibly singular bispinors. It is not a global SL(2,C) frame connection; matrix inversion and loop holonomy are undefined on null-edge cells.'};p=ROOT/'research/nima/results/nnmhv-boundary-transport-frame-obstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
