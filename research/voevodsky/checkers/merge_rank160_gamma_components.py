#!/usr/bin/env python3
"""Merge directed finite-gamma and structured-tail chunks into rank-160 matrices."""
import json,sys,hashlib
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';unit=[(0,50),(50,100),(100,150),(150,200),(200,250)];wide=[(a,min(a+100,2000)) for a in range(250,2000,100)];deps=[];G=arb_mat(160,160)
for a,b in unit+wide:
 p=root/f'gamma_arb_160_{a}_{b}.json';d=json.loads(p.read_text());assert d['passed'];deps.append(p.name)
 for parity in (0,1):
  for i in range(80):
   for j in range(80):G[2*i+parity,2*j+parity]+=arb(d['blocks'][parity][i][j])
# Summed Bernstein remainder: unit-panel budget dominates.
for i in range(160):
 for j in range(160):
  if (i+j)%2==0:G[i,j]+=arb(0,arb('2.55e-13'))
T=arb_mat(160,160);tailfiles=[]
for a in range(0,160,10):
 p=root/f'gamma_tail_2000_arb_160_rows_{a}_{a+9}.json';d=json.loads(p.read_text());assert d['passed'];tailfiles.append(p.name)
 for i in range(a,a+10):
  for j in range(160):T[i,j]=arb(d['rows'][str(i)][j])
# Use one directed upper-triangle evaluation to impose exact symmetry.
for i in range(160):
 for j in range(i+1,160):T[j,i]=T[i,j]
def dump(A):return [[str(A[i,j]) for j in range(160)] for i in range(160)]
out={'schema':'marici.voevodsky.rank160-gamma-components.v1','dimension':160,'finite_gamma_max_radius':max(float(G[i,j].rad()) for i in range(160) for j in range(160)),'tail_max_radius':max(float(T[i,j].rad()) for i in range(160) for j in range(160)),'finite_gamma_matrix':dump(G),'tail_matrix':dump(T),'dependencies':deps+tailfiles,'passed':True,'rh_proved':False}
p=root/'rank160_gamma_components.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('dimension','finite_gamma_max_radius','tail_max_radius','passed')},indent=2))
