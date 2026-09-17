#!/usr/bin/env python3
"""Directed rank-two endpoint representation through Legendre degree 669."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;N=670;L=arb('0.55');x=L/2;ap=[]
for n in range(N):
 moment=2*L*((2*n+1)/(2*L)).sqrt()*(arb.pi()/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('0.5'));ap.append(moment)
maxrad=max(float(v.rad()) for v in ap);# E_ij=(-1)^j ap_i ap_j on equal parity, zero otherwise.
max_matrix_radius=0.0
for parity in (0,1):
 ids=range(parity,N,2)
 for i in ids:
  for j in ids:max_matrix_radius=max(max_matrix_radius,float((ap[i]*ap[j]).rad()))
out={'schema':'marici.voevodsky.endpoint-vectors-arb-670.v1','precision_bits':flint.ctx.prec,'dimension':N,'representation':'E_ij=0 for odd i+j; E_ij=(-1)^j a_i a_j for even i+j','a_plus':[str(v) for v in ap],'maximum_vector_radius':maxrad,'maximum_implied_matrix_entry_radius':max_matrix_radius,'target_entry_radius':1.9451749585801855e-11,'passed':max_matrix_radius<1.9451749585801855e-11,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'endpoint_vectors_arb_670.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('dimension','maximum_vector_radius','maximum_implied_matrix_entry_radius','target_entry_radius','passed')},indent=2));assert out['passed']
