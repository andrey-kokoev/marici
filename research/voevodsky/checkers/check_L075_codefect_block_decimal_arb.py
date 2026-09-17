#!/usr/bin/env python3
"""Exact-decimal Arb arithmetic audit of the floating L=.75 seven-mode block."""
import json,sys
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
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';V0=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'];A0=np.load(root/'gamma_floor_L075_prime4_decomposition.npz')['total'];V=arb_mat([[arb(repr(float(x))) for x in row] for row in V0]);A=arb_mat([[arb(repr(float(x))) for x in row] for row in A0]);B=V.transpose()*A*V;F=arb_mat(6,6);b=arb_mat(6,1)
for i in range(6):
 b[i,0]=B[i,6]
 for j in range(6):F[i,j]=B[i,j]
s=B[6,6]-(b.transpose()*F.inv()*b)[0,0];out={'schema':'marici.voevodsky.L075-codefect-block-decimal-arb.v1','precision_bits':flint.ctx.prec,'critical_schur_decimal_midpoint':str(s),'positive_for_exact_decimal_inputs':s.lower()>0,'scope':'arithmetic audit only; source matrix enclosure not yet attached','passed':s.lower()>0,'rh_proved':False};p=root/'L075_codefect_block_decimal_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
