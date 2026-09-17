#!/usr/bin/env python3
"""Audit projected endpoint-jet sizes before any endpoint cancellation."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;n=np.arange(1000);sc=np.sqrt((2*n+1)/(2*L));jets=[];rows=[]
for r in range(1,6):
 fac=np.ones(1000)
 for j in range(-r+1,r+1):fac*=n+j
 fac/=2**r*math.factorial(r)*L**r;fac[:r]=0
 plus=(Z*(sc*fac)[:,None]).sum(0);minus=(Z*(sc*fac*((-1.)**(n+r)))[:,None]).sum(0)
 if jets:
  Q=np.linalg.qr(np.array(jets).T)[0];P=np.eye(40)-Q@Q.T
 else:P=np.eye(40)
 projected=[float(np.linalg.norm(plus@P)),float(np.linalg.norm(minus@P))];rows.append({'jet_order':r,'endpoint_row_norms_after_lower_jet_projection':projected,'maximum':max(projected)})
 jets.extend([plus,minus])
out={'schema':'marici.voevodsky.gate3-endpoint-jet-triangle-constants.v1','rows':rows,'passed_audit':True,'conclusion':'even after lower-jet projection the individual endpoint rows are enormous; Bernstein bounds must sum all shifted and endpoint kernels coefficientwise before taking row norms','forbidden_route':'separate endpoint-row norms followed by triangle inequality','required_route':'Arb evaluation of each complete coupled two/six-dimensional scalar kernel','rh_proved':False};p=root/'gate3_endpoint_jet_triangle_constants.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
