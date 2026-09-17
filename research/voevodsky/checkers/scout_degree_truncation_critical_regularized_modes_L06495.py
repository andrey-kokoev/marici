#!/usr/bin/env python3
"""Degree truncation applied only after reducing to the two critical regularized modes."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];D=d['tail_maps'][4];Sall=d['schur'];e,T=np.linalg.eigh(Sall[0]+Sall[-1]);Tc=T[:,:2];P=U@Tc;Z=(U-D)@Tc;A=np.load(root/'gamma_floor_L06495_rank1000_midpoint.npz')['matrix'];alpha=1.067569476012246;rows=[]
for degree in (50,75,100,150,200,300,400):
 W=Z.copy();W[degree:]=0;J=W.T@A@W;PA=P.T@A@W;R=A@W-P@PA;lower=(J-R.T@R/alpha);lower=(lower+lower.T)/2;rows.append({'degree_exclusive':degree,'critical_tail_norm':float(np.linalg.norm(Z[degree:],2)),'candidate_min':float(np.linalg.eigvalsh((J+J.T)/2)[0]),'residual_norm':float(np.linalg.norm(R,2)),'corrected_min':float(np.linalg.eigvalsh(lower)[0])})
out={'schema':'marici.voevodsky.degree-truncation-critical-regularized-modes-L06495.v1','rows':rows,'positive_degrees':[x['degree_exclusive'] for x in rows if x['corrected_min']>0],'status':'exploratory only: residual projection omits the retained robust 38-mode Schur elimination','passed':False,'rh_proved':False};p=root/'degree_truncation_critical_regularized_modes_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
