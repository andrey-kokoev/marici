"""Cross-check census via separate local SAT tests (no forced-edge prefilter); certify canonical survivor against ordinary cube cells. 5+3 and 5+2+1 imply a single 5-cycle via taking powers. A cycle of length >=5 is not a postulated symmetry of the red core."""
import json,itertools,collections,igraph as ig
from ramsey_incidence_first35 import P,solve
from ramsey_retention_slice import check
R=json.loads((P/'ramsey_incidence_cycles_8_71_62_611_5111.json').read_text());out=[];hist=collections.Counter()
for r in R['rows']:
 levels=[]
 for k in (3,4,5,6):
  s=solve(r['m'],False,True,k,False)['status'];levels.append(s)
  if s in ('forced_blue','unsat'):break
 out.append(levels)
 if r.get('solve',{}).get('status')=='witness':
  m=r['m'];w=r['solve'];a=w['core']+[0]*9
  for j,s in enumerate(w['rows'],26):
   a[j]=s|1<<34;a[-1]|=1<<j
   for i in range(26):a[i]|=(s>>i&1)<<j
  assert check(a,(1<<35)-1,3,9);cube=[sum(1<<i for i in range(8) if i&mask==v) for mask in range(1,8) for v in range(8) if not v&~mask];G=lambda m:ig.Graph(34,[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1]);assert G(m).isomorphic_vf2(G(cube),color1=[1]*26+[2]*8,color2=[1]*26+[2]*8);hist.update(r['cycles'])
print([(k,collections.Counter(v[i] if len(v)>i else 'excluded' for v in out)) for i,k in enumerate((3,4,5,6))],hist);(P/'ramsey_long_cycle35_levels.json').write_text(json.dumps(dict(levels=out,winner_cycles=hist))+'\n')
