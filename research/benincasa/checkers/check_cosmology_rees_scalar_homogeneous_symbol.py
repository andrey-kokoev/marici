#!/usr/bin/env python3
"""Rank census for the homogeneous boundary scalar operator."""
import json
from pathlib import Path
P=101
# Q5 terms X^3Y^2 + X^2Y^3. Output coordinates indexed by X exponent 0..n+4.
def col(n,i,axis):
 r={}
 # Q*d_axis monomial
 for a,b in [(3,2),(2,3)]:
  c=i if axis==0 else n-i
  if c:
   x=i-(axis==0)+a;r[x]=(r.get(x,0)+c)%P
 # -d_axis Q * monomial
 terms=[(3,2,3),(2,3,2)] if axis==0 else [(3,2,2),(2,3,3)]
 for a,b,c in terms:
  x=i+a-(axis==0);r[x]=(r.get(x,0)-c)%P
 return {k:v for k,v in r.items() if v}
def rank(cols):
 B={}
 for r in cols:
  while r:
   q=min(r);x=r[q]
   if q not in B:
    z=pow(x,-1,P);B[q]={k:v*z%P for k,v in r.items()};break
   for k,v in B[q].items():r[k]=(r.get(k,0)-x*v)%P
   r={k:v for k,v in r.items() if v}
 return len(B)
rows=[]
for n in range(31):
 rk=rank([col(n,i,a) for a in (0,1) for i in range(n+1)]);rows.append({'input_degree':n,'target_dimension':n+5,'rank':rk,'cokernel_dimension':n+5-rk})
out={'schema':'marici.benincasa.cosmology-rees-scalar-homogeneous-symbol.v1','prime':P,'operator':'(f_x,f_y) maps to Q5 div(f)-grad(Q5) dot f','rows':rows,'stable_cokernel_dimensions':sorted(set(x['cokernel_dimension'] for x in rows[10:]))};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_scalar_homogeneous_symbol.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
