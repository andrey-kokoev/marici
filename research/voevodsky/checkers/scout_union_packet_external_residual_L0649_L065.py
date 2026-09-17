#!/usr/bin/env python3
"""External residual-Gram scout for the 40-dimensional endpoint-union packet."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649_rank1000_midpoint.npz','gamma_floor_L0649038_rank1000_midpoint.npz','gamma_floor_L0649146_rank1000_midpoint.npz','gamma_floor_L0649309_rank1000_midpoint.npz','gamma_floor_L06495_rank1000_midpoint.npz','gamma_floor_L0649691_rank1000_midpoint.npz','gamma_floor_L0649854_rank1000_midpoint.npz','gamma_floor_L0649962_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];A0=np.load(root/names[0])['matrix'];A1=np.load(root/names[-1])['matrix'];e0,U0=np.linalg.eigh(A0);e1,U1=np.linalg.eigh(A1);U=np.linalg.qr(np.column_stack((U0[:,:20],U1[:,:20])))[0];rows=[]
for n in names:
 A=np.load(root/n)['matrix'];F=U.T@A@U;RG=U.T@A@A@U-F@F;RG=(RG+RG.T)/2;rows.append({'file':n,'residual_norm':float(np.sqrt(max(0,np.linalg.eigvalsh(RG)[-1]))),'residual_gram_norm':float(np.linalg.eigvalsh(RG)[-1]),'packet_min':float(np.linalg.eigvalsh(F)[0])})
out={'schema':'marici.voevodsky.union-packet-external-residual-L0649-L065.v1','rows':rows,'maximum_residual_norm':max(x['residual_norm'] for x in rows),'minimum_packet_min':min(x['packet_min'] for x in rows),'status':'floating; complement floor and regularized tail map not applied','passed':True,'rh_proved':False};p=root/'union_packet_external_residual_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
