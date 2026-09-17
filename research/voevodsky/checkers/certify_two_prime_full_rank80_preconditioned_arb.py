#!/usr/bin/env python3
"""Certify rank-80 parity blocks by decimal Cholesky congruence and Arb Gershgorin."""
import json,sys,hashlib
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,arb_mat
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';names=['two_prime_finite_gamma_arb.json','gamma_tail_250_arb_matrix.json','two_prime_overlap_arb.json','two_prime_endpoint_arb.json'];ds=[json.loads((root/n).read_text()) for n in names];A=arb_mat(80,80)
for d in ds:
 for i in range(80):
  for j in range(80):A[i,j]+=arb(d['matrix'][i][j])
res={};allok=True
for parity,label in ((0,'even'),(1,'odd')):
 B=arb_mat([[A[i,j] for j in range(parity,80,2)] for i in range(parity,80,2)]);mid=np.array([[float(B[i,j].mid()) for j in range(40)] for i in range(40)]);chol=np.linalg.cholesky(mid);C0=np.linalg.inv(chol.T);C=arb_mat([[arb(repr(float(C0[i,j]))) for j in range(40)] for i in range(40)]);T=C.transpose()*B*C;lower=[]
 for i in range(40):
  off=sum(max(abs(float(T[i,j].lower())),abs(float(T[i,j].upper()))) for j in range(40) if j!=i);lower.append(float(T[i,i].lower())-off)
 ok=min(lower)>0;allok&=ok;res[label]={'passed':ok,'minimum_gershgorin_lower':min(lower),'minimum_row':int(np.argmin(lower)),'maximum_diagonal_deviation_from_one':max(abs(float(T[i,i].mid())-1) for i in range(40))}
out={'schema':'marici.voevodsky.two-prime-full-rank80-preconditioned-arb.v1','L':'0.55','dimension':80,'method':'exact decimal midpoint-Cholesky congruence followed by Arb Gershgorin','parity_blocks':res,'passed':allok,'rh_proved':False}
p=root/'two_prime_full_rank80_preconditioned_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
