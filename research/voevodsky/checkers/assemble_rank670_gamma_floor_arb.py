#!/usr/bin/env python3
"""Assemble directed gamma-floor, prime, and endpoint rank-670 blocks."""
import json,sys,glob
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';N=670;A=[[arb(0) for _ in range(N)] for _ in range(N)];deps=[]
for lo in range(0,250,50):
 p=root/f'modified_gamma_arb_670_{lo}_{lo+50}.json';d=json.loads(p.read_text());deps.append(p.name)
 for parity in (0,1):
  for i in range(335):
   for j in range(335):A[2*i+parity][2*j+parity]+=arb(d['blocks'][parity][i][j])
qR=arb(json.loads((root/'gamma_floor_250_arb.json').read_text())['q_R']);
for i in range(N):A[i][i]+=qR
# Prefer the ten-row chunks and ignore the diagnostic 0_0 duplicate.
for lo in range(0,670,10):
 p=root/f'prime_overlap_arb_670_rows_{lo}_{lo+9}.json';d=json.loads(p.read_text());deps.append(p.name)
 for i in range(lo,lo+10):
  for j,s in enumerate(d['rows'][str(i)]):A[i][j]+=arb(s)
ep=json.loads((root/'endpoint_vectors_arb_670.json').read_text());av=[arb(x) for x in ep['a_plus']];deps.append('endpoint_vectors_arb_670.json')
for i in range(N):
 for j in range(i%2,N,2):A[i][j]+=av[i]*av[j]*(1 if j%2==0 else -1)
mid=np.array([[float(A[i][j].mid()) for j in range(N)] for i in range(N)]);mid=(mid+mid.T)/2;np.savez(root/'rank670_gamma_floor_midpoint.npz',matrix=mid);mins={};
for parity,label in ((0,'even'),(1,'odd')):mins[label]=float(np.linalg.eigvalsh(mid[parity::2,parity::2])[0])
maxrad=max(A[i][j].rad() for i in range(N) for j in range(N));radius_norm_upper=N*float(maxrad.upper())
out={'schema':'marici.voevodsky.rank670-gamma-floor-arb-assembly.v1','dimension':N,'parity_min_midpoint_eigenvalues':mins,'maximum_assembled_ball_radius':str(maxrad),'uniform_radius_spectral_norm_upper':radius_norm_upper,'quadrature_error_included':False,'dependencies':deps,'passed_node_arithmetic':radius_norm_upper<min(mins.values()),'passed':False,'status':'node-arithmetic assembly complete; Bernstein quadrature remainder not yet added','rh_proved':False};p=root/'rank670_gamma_floor_arb_assembly.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('dimension','parity_min_midpoint_eigenvalues','maximum_assembled_ball_radius','uniform_radius_spectral_norm_upper','quadrature_error_included','passed_node_arithmetic','passed','status')},indent=2))
