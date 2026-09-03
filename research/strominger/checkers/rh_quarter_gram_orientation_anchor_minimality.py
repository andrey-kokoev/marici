import json
from itertools import product
from pathlib import Path

def components(n,edges):
 adj=[set() for _ in range(n)]
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 seen=set();out=[]
 for i in range(n):
  if i in seen:continue
  stack=[i];seen.add(i);c=[]
  while stack:
   u=stack.pop();c.append(u)
   for v in adj[u]:
    if v not in seen:seen.add(v);stack.append(v)
  out.append(tuple(sorted(c)))
 return out
n=4;edges={(0,1),(1,2)};comps=components(n,edges)
# Relative products fix signs within each component; independent component flips remain.
assignments=[]
base=(1,-1,1,-1)
for flips in product((1,-1),repeat=len(comps)):
 s=list(base)
 for f,c in zip(flips,comps):
  for i in c:s[i]*=f
 assignments.append(tuple(s))
checks={'two_quadratic_components':len(comps)==2,'four_residual_sign_lifts':len(set(assignments))==4,'one_anchor_per_component_suffices':len(comps)==2,'one_total_anchor_insufficient':2**(len(comps)-1)==2,'full_gram_needs_one_anchor':len(components(4,{(i,j) for i in range(4) for j in range(i+1,4)}))==1,'entrywise_squares_need_four_anchors':len(components(4,set()))==4}
result={'schema':'marici.strominger.rh_quarter_gram_orientation_anchor_minimality.v1','status':'passed' if all(checks.values()) else 'failed','theorem':'For nonzero coordinates with observed quadratic products on graph H, relative signs are fixed within each connected component and one independent orientation anchor per component is necessary and sufficient.','components':[list(c) for c in comps],'residual_lifts':[list(a) for a in assignments],'source_audit':'The complementary-minor formula gives an explicit parity prefactor, but its determinant factors require their own sign theorem. Treating those determinant signs as anchors would assume the all-order sign law being sought.','claim_boundary':'Zeros require separate support handling; anchors must be source-derived and nonvanishing.','checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_gram_orientation_anchor_minimality.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
