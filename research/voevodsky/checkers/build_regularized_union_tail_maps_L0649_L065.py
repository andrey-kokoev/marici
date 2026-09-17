#!/usr/bin/env python3
"""Finite rank-1000 exact tail maps for the 40-dimensional union packet."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649_rank1000_midpoint.npz','gamma_floor_L0649038_rank1000_midpoint.npz','gamma_floor_L0649146_rank1000_midpoint.npz','gamma_floor_L0649309_rank1000_midpoint.npz','gamma_floor_L06495_rank1000_midpoint.npz','gamma_floor_L0649691_rank1000_midpoint.npz','gamma_floor_L0649854_rank1000_midpoint.npz','gamma_floor_L0649962_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];A0=np.load(root/names[0])['matrix'];A1=np.load(root/names[-1])['matrix'];e0,U0=np.linalg.eigh(A0);e1,U1=np.linalg.eigh(A1);U=np.linalg.qr(np.column_stack((U0[:,:20],U1[:,:20])))[0];Q=np.linalg.qr(U,mode='complete')[0][:,40:];rows=[];D=[];S=[]
for n in names:
 A=np.load(root/n)['matrix'];F=U.T@A@U;B=U.T@A@Q;C=Q.T@A@Q;Y=np.linalg.solve(C,B.T);sch=F-B@Y;sch=(sch+sch.T)/2;Z=U-Q@Y;res=Q.T@A@Z;rows.append({'file':n,'tail_floor':float(np.linalg.eigvalsh(C)[0]),'schur_min':float(np.linalg.eigvalsh(sch)[0]),'finite_residual_norm':float(np.linalg.norm(res,2)),'tail_map_norm':float(np.linalg.norm(Q@Y,2))});D.append(Q@Y);S.append(sch)
np.savez(root/'regularized_union_tail_maps_L0649_L065.npz',packet=U,tail_maps=np.array(D),schur=np.array(S));out={'schema':'marici.voevodsky.regularized-union-tail-maps-L0649-L065.v1','rows':rows,'minimum_tail_floor':min(x['tail_floor'] for x in rows),'minimum_schur':min(x['schur_min'] for x in rows),'maximum_finite_residual_norm':max(x['finite_residual_norm'] for x in rows),'passed':min(x['tail_floor'] for x in rows)>0 and min(x['schur_min'] for x in rows)>0,'status':'floating finite-rank regularization; continuum residual and interpolation open','rh_proved':False};p=root/'regularized_union_tail_maps_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
