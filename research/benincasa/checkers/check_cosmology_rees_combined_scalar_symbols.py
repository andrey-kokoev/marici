#!/usr/bin/env python3
"""Test whether the lower K-level symbol kills boundary-symbol obstructions."""
import json
from pathlib import Path
P=101;C=(-pow(2,-1,P))%P
Q={(3,2):1,(2,3):1};K={(4,0):9,(2,2):-36,(0,4):36}
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=(r.get(k,0)+v)%P
 return {k:v for k,v in r.items() if v}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=(r.get((i+k,j+l),0)+u*v)%P
 return {k:v for k,v in r.items() if v}
def der(a,axis):
 r={}
 for (i,j),v in a.items():
  z=i if axis==0 else j
  if z:r[(i-1,j) if axis==0 else (i,j-1)]=v*z%P
 return r
def scale(a,c):return {k:v*c%P for k,v in a.items() if v*c%P}
def L(f,axis,lower):
 b=add(mul(Q,der(f,axis)),scale(mul(der(Q,axis),f),-1))
 if not lower:return b
 # K*(Q df-dQ f) + C*Q*dK*f
 return add(mul(K,b),scale(mul(mul(Q,der(K,axis)),f),C))
def rank(cols):
 B={}
 for p in cols:
  r={i:v for (i,j),v in p.items()}
  while r:
   q=min(r);x=r[q]
   if q not in B:
    z=pow(x,-1,P);B[q]={k:v*z%P for k,v in r.items()};break
   for k,v in B[q].items():r[k]=(r.get(k,0)-x*v)%P
   r={k:v for k,v in r.items() if v}
 return len(B)
rows=[]
for m in range(4,51):
 cols=[]
 for lower,deg in [(False,m-4),(True,m-8)]:
  if deg>=0:
   for axis in (0,1):
    for i in range(deg+1):cols.append(L({(i,deg-i):1},axis,lower))
 rk=rank(cols);rows.append({'target_degree':m,'target_dimension':m+1,'combined_rank':rk,'cokernel_dimension':m+1-rk})
out={'schema':'marici.benincasa.cosmology-rees-combined-scalar-symbols.v1','prime':P,'gamma_minus_k_mod_p':C,'rows':rows,'stable_cokernel_dimensions_m_ge_12':sorted(set(r['cokernel_dimension'] for r in rows if r['target_degree']>=12))};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_combined_scalar_symbols.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
