#!/usr/bin/env python3
"""Möbius inversion on the history interval poset as a discrete wave operator."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
rows=[]
for m in range(1,11):
 events=sorted(((i,j) for i in range(1,m+1) for j in range(i,m+1)),key=lambda x:(x[1]-x[0],x[0]))
 def leq(x,y):return y[0]<=x[0] and x[1]<=y[1] # y contains x
 Z=s.Matrix([[1 if leq(x,y) else 0 for y in events] for x in events]);Mu=Z.inv();local=s.zeros(len(events))
 for a,x in enumerate(events):
  for b,y in enumerate(events):
   if leq(x,y):
    dl=x[0]-y[0];dr=y[1]-x[1]
    if dl<=1 and dr<=1:local[a,b]=(-1)**(dl+dr)
 rows.append({'m':m,'events':len(events),'mobius_is_local_mixed_difference':Mu==local,'mobius_nonzeros':sum(1 for v in Mu if v!=0),'zeta_mobius_identity':Z*Mu==s.eye(len(events))})
checks={'tested_ranks_one_through_ten':len(rows)==10,'mobius_is_four_corner_null_operator':all(x['mobius_is_local_mixed_difference'] for x in rows),'mobius_exactly_inverts_causal_sum':all(x['zeta_mobius_identity'] for x in rows)}
out={'schema':'marici.nima.nnmhv-mobius-wave-operator-bridge.v1','poset':'[i,j] <= [k,l] iff [i,j] is contained in [k,l]','zeta':'(Zf)(I) = sum over causal supersets J containing I of f(J)','mobius':'mu([i,j],[k,l])=(-1)^((i-k)+(l-j)) when both endpoint differences are 0 or 1, and 0 otherwise','local_operator':'Box_d f(i,j)=f(i,j)-f(i-1,j)-f(i,j+1)+f(i-1,j+1)=Delta_u Delta_v f','rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Möbius inversion of coherent history summation is exactly the local mixed-null finite difference, the discrete massless d’Alembertian on interval kinematic space.','bridges':['incidence-algebra Möbius inversion','discrete d’Alembertian','causal-set Green functions','inclusion-exclusion as local wave operator','zeta summation as discrete causal integration']};p=ROOT/'research/nima/results/nnmhv-mobius-wave-operator-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'local_operator':out['local_operator'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
