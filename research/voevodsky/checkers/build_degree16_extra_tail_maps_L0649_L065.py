#!/usr/bin/env python3
"""Tail maps at the eight odd degree-16 Lobatto nodes."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649010_rank1000_midpoint.npz','gamma_floor_L0649084_rank1000_midpoint.npz','gamma_floor_L0649222_rank1000_midpoint.npz','gamma_floor_L0649402_rank1000_midpoint.npz','gamma_floor_L0649598_rank1000_midpoint.npz','gamma_floor_L0649778_rank1000_midpoint.npz','gamma_floor_L0649916_rank1000_midpoint.npz','gamma_floor_L0649990_rank1000_midpoint.npz'];U=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(U,mode='complete')[0][:,40:];D=[];S=[];rows=[]
for n in names:
 A=np.load(root/n)['matrix'];F=U.T@A@U;B=U.T@A@Q;C=Q.T@A@Q;Y=np.linalg.solve(C,B.T);sch=(F-B@Y);sch=(sch+sch.T)/2;D.append(Q@Y);S.append(sch);rows.append({'file':n,'tail_floor':float(np.linalg.eigvalsh(C)[0]),'schur_min':float(np.linalg.eigvalsh(sch)[0]),'tail_map_norm':float(np.linalg.norm(Q@Y,2))})
np.savez(root/'regularized_union_tail_maps_L0649_L065_degree16_extra.npz',tail_maps=np.array(D),schur=np.array(S));out={'schema':'marici.voevodsky.regularized-union-tail-maps-degree16-extra.v1','rows':rows,'passed':min(x['tail_floor'] for x in rows)>0 and min(x['schur_min'] for x in rows)>0,'rh_proved':False};p=root/'regularized_union_tail_maps_L0649_L065_degree16_extra.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
