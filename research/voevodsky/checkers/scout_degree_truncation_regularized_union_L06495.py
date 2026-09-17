#!/usr/bin/env python3
"""Degree-truncate regularized union vectors and apply finite residual correction."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];D=d['tail_maps'][4];A=np.load(root/'gamma_floor_L06495_rank1000_midpoint.npz')['matrix'];alpha=1.067569476012246;rows=[]
for degree in (100,150,200,300,400,500,670,800):
 Z=U-D;Z[degree:]=0;J=Z.T@A@Z;PA=U.T@A@Z;# residual orthogonal to packet in the rank-1000 ambient space
 R=A@Z-U@PA;G=R.T@R;lower=J-G/alpha;lower=(lower+lower.T)/2;rows.append({'degree_exclusive':degree,'U_tail_norm':float(np.linalg.norm(U[degree:],2)),'D_tail_norm':float(np.linalg.norm(D[degree:],2)),'candidate_min':float(np.linalg.eigvalsh((J+J.T)/2)[0]),'residual_norm':float(np.linalg.norm(R,2)),'corrected_min':float(np.linalg.eigvalsh(lower)[0])})
out={'schema':'marici.voevodsky.degree-truncation-regularized-union-L06495.v1','rows':rows,'positive_degrees':[x['degree_exclusive'] for x in rows if x['corrected_min']>0],'passed':any(x['corrected_min']>0 for x in rows),'rh_proved':False};p=root/'degree_truncation_regularized_union_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
