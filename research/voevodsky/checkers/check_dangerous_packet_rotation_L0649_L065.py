#!/usr/bin/env python3
"""Measure dangerous-subspace rotation across the narrow endpoint slab."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';A=np.load(root/'gamma_floor_L0649_rank1000_midpoint.npz')['matrix'];B=np.load(root/'gamma_floor_L065_rank1000_midpoint.npz')['matrix'];ea,Ua=np.linalg.eigh(A);eb,Ub=np.linalg.eigh(B);Ua=Ua[:,:20];Ub=Ub[:,:20];sv=np.linalg.svd(Ua.T@Ub,compute_uv=False);crit=abs(float(Ua[:,0]@Ub[:,0]));U=np.linalg.qr(np.column_stack((Ua,Ub)))[0];CA=U.T@A@U;CB=U.T@B@U;out={'schema':'marici.voevodsky.dangerous-packet-rotation-L0649-L065.v1','packet_dimension_each':20,'critical_vector_absolute_overlap':crit,'principal_cosines':[float(x) for x in sv],'minimum_principal_cosine':float(sv[-1]),'union_numerical_dimension':int(np.linalg.matrix_rank(np.column_stack((Ua,Ub)),tol=1e-10)),'union_packet_endpoint_minima':[float(np.linalg.eigvalsh(CA)[0]),float(np.linalg.eigvalsh(CB)[0])],'conclusion':'single-endpoint packet misses the rotating near-null direction; continuation must use a union/transported packet and leakage bound','passed':crit>.99,'rh_proved':False};p=root/'dangerous_packet_rotation_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
