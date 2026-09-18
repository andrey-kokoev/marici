#!/usr/bin/env python3
"""Exact finite checks for the arbitrary-m associahedral order-complex resolution."""
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
def data(m):
 n=m+3; boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
 ds=[(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in boundary]
 def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
 faces=[]
 for r in range(m+1):
  faces += [frozenset(c) for c in combinations(ds,r) if all(not cross(a,b) for a,b in combinations(c,2))]
 faces=sorted(faces,key=lambda x:(len(x),sorted(x)));idx={x:i for i,x in enumerate(faces)}
 chains=[]
 def extend(ch):
  chains.append(tuple(ch));last=ch[-1]
  for f in faces:
   if last < f:extend(ch+[f])
 for f in faces:extend([f])
 chains_by_deg={k:[] for k in range(m+1)}
 for c in chains:chains_by_deg[len(c)-1].append(c)
 def bd(c):
  if len(c)==1:return {():1}
  out={}
  for i in range(len(c)):
   q=c[:i]+c[i+1:];out[q]=out.get(q,0)+(-1)**i
  return {q:v for q,v in out.items() if v}
 apex=frozenset()
 def h(c):
  if c==():return {(apex,):1}
  if c[0]==apex:return {}
  return {(apex,)+c:1}
 def lin_apply(vec,op):
  out={}
  for c,a in vec.items():
   for q,b in op(c).items():out[q]=out.get(q,0)+a*b
  return {q:v for q,v in out.items() if v}
 ok=True
 for c in [()]+chains:
  lhs=lin_apply(lin_apply({c:1},h),bd);rhs=lin_apply(lin_apply({c:1},bd),h)
  total=dict(lhs)
  for q,v in rhs.items():total[q]=total.get(q,0)+v
  total={q:v for q,v in total.items() if v};ok &= total=={c:1}
 return {'m':m,'polygon_vertices':n,'face_poset_objects':len(faces),'chain_counts':{str(k):len(v) for k,v in chains_by_deg.items()},'d_squared_zero':all(lin_apply(bd(c),bd)=={} for c in chains if len(c)>1),'contracting_homotopy_identity':ok}
rows=[data(m) for m in range(1,5)]
checks={'tested_A1_through_A4':len(rows)==4,'all_d_squared_zero':all(r['d_squared_zero'] for r in rows),'all_contracted_to_empty_face_apex':all(r['contracting_homotopy_identity'] for r in rows)}
out={'schema':'marici.nima.arbitrary-m-coherent-resolution.v1','definition':'For every m>=1, take the augmented simplicial chain complex of strict chains in the inclusion poset of noncrossing diagonal sets of an (m+3)-gon.','differential':'alternating deletion of one poset element','contraction':'h(1)=[empty]; h(sigma)=[empty<sigma] if sigma omits empty, and 0 otherwise','theorem':'The empty partial triangulation is a cone point, so dh+hd=id. Hence the augmented complex is exact for every finite m.','rows':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'Arbitrary m means one exact finite resolution for each m. No cofinal limit, canonical-form coefficient system, or physical comparison map is inferred.'};p=ROOT/'research/nima/results/arbitrary-m-coherent-resolution.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
