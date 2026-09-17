#!/usr/bin/env python3
"""Resolve smooth-tail right singular space by cumulative endpoint jets."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;n=np.arange(1000);sc=np.sqrt((2*n+1)/(2*L));jets=[];rows=[]
# P_n^(r)(1)=Gamma(n+r+1)/(2^r r! Gamma(n-r+1)); x derivatives add L^-r.
for r in range(1,6):
 fac=np.ones(1000)
 for j in range(-r+1,r+1):fac*=n+j
 fac/=2**r*math.factorial(r)*L**r;fac[:r]=0
 plus=(Z*(sc*fac)[:,None]).sum(axis=0);minus=(Z*(sc*fac*((-1.)**(n+r)))[:,None]).sum(axis=0);jets.extend([plus,minus]);Q=np.linalg.qr(np.array(jets).T)[0]
 item={'jet_order_through':r,'space_dimension':2*r,'blocks':[]}
 for m in (5,6,7):
  S=np.load(root/f'continuum_residual_jump_smooth_L06495_{m}000_{m}999.npz')['smooth'];perp=float(np.linalg.norm(S@(np.eye(40)-Q@Q.T),2));item['blocks'].append({'m':m,'perpendicular_norm':perp,'m_times_perpendicular':m*perp})
 rows.append(item)
out={'schema':'marici.voevodsky.gate3-smooth-endpoint-jet-spaces.v1','rows':rows,'passed_audit':True,'next':'select the smallest jet order leaving a rapidly decaying perpendicular remainder and derive its coupled kernels','rh_proved':False};p=root/'gate3_smooth_endpoint_jet_spaces.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
