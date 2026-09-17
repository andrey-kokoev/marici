#!/usr/bin/env python3
"""Arb exact-decimal Gram and orthogonality audit for the 92-column span."""
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
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';d=json.loads((root/'two_prime_regularized_decimal_span.json').read_text());P=arb_mat([[arb(x) for x in row] for row in d['retained_coefficients']]);D=arb_mat([[arb(x) for x in row] for row in d['tail_map_coefficients']]);G=P.transpose()*P;Ginv=G.inv();DQ=D-P*(Ginv*(P.transpose()*D));cross=P.transpose()*DQ;Z=P-DQ;max_cross=max(abs(float(cross[i,j].mid()))+float(cross[i,j].rad()) for i in range(92) for j in range(92));max_gram=max(abs(float(G[i,j].mid())-(1 if i==j else 0))+float(G[i,j].rad()) for i in range(92) for j in range(92));# Export midpoint of exact-decimal orthogonalization for downstream scouts.
Pm=np.array([[float(P[i,j].mid()) for j in range(92)] for i in range(670)]);Dm=np.array([[float(DQ[i,j].mid()) for j in range(92)] for i in range(670)]);Zm=Pm-Dm;np.savez(root/'two_prime_regularized_exact_span_midpoint.npz',retained=Pm,tail_map=Dm,schur_vectors=Zm)
out={'schema':'marici.voevodsky.two-prime-regularized-exact-span-arb.v1','precision_bits':flint.ctx.prec,'ambient_dimension':670,'retained_dimension':92,'maximum_retained_gram_deviation':max_gram,'maximum_orthogonalized_cross_entry':max_cross,'passed':max_cross<1e-100 and max_gram<1e-12,'rh_proved':False};p=root/'two_prime_regularized_exact_span_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
