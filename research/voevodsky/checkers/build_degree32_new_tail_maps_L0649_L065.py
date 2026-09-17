#!/usr/bin/env python3
"""Tail maps and Schur forms at the 16 new degree-32 Chebyshev nodes."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';tags=[];Ls=[]
for j in range(1,32,2):
 x=math.cos((32-j)*math.pi/32);L=.6495+.0005*x;tags.append('L'+f'{L:.10f}'.replace('.',''));Ls.append(L)
d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];Q=np.linalg.qr(U,mode='complete')[0][:,40:];D=[];S=[];rows=[]
for tag,L in zip(tags,Ls):
 A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];F=U.T@A@U;B=U.T@A@Q;C=Q.T@A@Q;Y=np.linalg.solve(C,B.T);sch=F-B@Y;sch=(sch+sch.T)/2;D.append(Q@Y);S.append(sch);rows.append({'tag':tag,'L':L,'tail_floor':float(np.linalg.eigvalsh(C)[0]),'schur_min':float(np.linalg.eigvalsh(sch)[0]),'tail_map_norm':float(np.linalg.norm(Q@Y,2))})
np.savez_compressed(root/'degree32_new_tail_maps_L0649_L065.npz',tail_maps=np.array(D),schur=np.array(S),L=np.array(Ls));out={'schema':'marici.voevodsky.degree32-new-tail-maps-L0649-L065.v1','rows':rows,'minimum_tail_floor':min(x['tail_floor'] for x in rows),'minimum_schur':min(x['schur_min'] for x in rows),'passed_scout':min(x['schur_min'] for x in rows)>0,'passed':False,'rh_proved':False};p=root/'degree32_new_tail_maps_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
