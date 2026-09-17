#!/usr/bin/env python3
"""Assemble and certify the directed rank-160 two-prime form."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';g=json.loads((root/'rank160_gamma_components.json').read_text());p=json.loads((root/'two_prime_overlap_arb_160.json').read_text());e=json.loads((root/'two_prime_endpoint_arb_160.json').read_text());A=arb_mat(160,160)
for i in range(160):
 for j in range(160):A[i,j]=arb(g['finite_gamma_matrix'][i][j])+arb(g['tail_matrix'][i][j])+arb(p['matrix'][i][j])+arb(e['matrix'][i][j])
res={};okall=True
for parity,label in ((0,'even'),(1,'odd')):
 B=arb_mat([[A[i,j] for j in range(parity,160,2)] for i in range(parity,160,2)]);mid=np.array([[float(B[i,j].mid()) for j in range(80)] for i in range(80)]);chol=np.linalg.cholesky(mid);C0=np.linalg.inv(chol.T);C=arb_mat([[arb(repr(float(C0[i,j]))) for j in range(80)] for i in range(80)]);T=C.transpose()*B*C;lower=[]
 for i in range(80):
  off=sum(max(abs(float(T[i,j].lower())),abs(float(T[i,j].upper()))) for j in range(80) if i!=j);lower.append(float(T[i,i].lower())-off)
 ok=min(lower)>0;okall&=ok;res[label]={'passed':ok,'minimum_gershgorin_lower':min(lower),'minimum_row':int(np.argmin(lower)),'maximum_diagonal_deviation':max(abs(float(T[i,i].mid())-1) for i in range(80))}
out={'schema':'marici.voevodsky.two-prime-full-rank160-preconditioned-arb.v1','L':'.55','dimension':160,'maximum_assembled_entry_radius':max(float(A[i,j].rad()) for i in range(160) for j in range(160)),'parity_blocks':res,'passed':okall,'rh_proved':False};path=root/'two_prime_full_rank160_preconditioned_arb.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
