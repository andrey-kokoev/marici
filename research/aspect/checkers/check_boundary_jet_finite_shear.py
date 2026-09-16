#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path
checks={};rows=[]
lam=Fraction(3,2)
for N in range(0,12):
 c=[-lam**(-(k+1)) for k in range(N+1)]
 # ell*S-lambda*ell=e0: coefficient 0 is -lambda*c0;
 # coefficient k>=1 is c[k-1]-lambda*c[k].
 coeff=[-lam*c[0]]+[c[k-1]-lam*c[k] for k in range(1,N+1)]
 ok=coeff==[Fraction(1)]+[Fraction(0)]*N
 checks[f'truncation_{N}']=ok;rows.append({'max_jet':N,'cohomological_coefficients':[str(v) for v in coeff],'split':ok})
out={'schema':'marici.aspect.boundary-jet-finite-shear-check.v1','passed':all(checks.values()),'checks':checks,'rows':rows,'verdict':'Every finite jet truncation is exactly triangularly split; passage to the full tower requires continuity of the infinite shear series.'}
p=Path(__file__).resolve().parents[1]/'results/boundary_jet_finite_shear.check.v1.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'truncations':len(rows)}));raise SystemExit(0 if out['passed'] else 1)
