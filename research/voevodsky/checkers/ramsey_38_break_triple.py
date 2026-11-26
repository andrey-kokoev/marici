"""Local repair radius <=2. Keep old root partition, earlier two recolorings and new links. Require legal old graph, legal enlarged core in window, no red triangle or failed singleton/pair. Count remaining demands."""
from itertools import combinations
from collections import Counter
import json
from ramsey_retention_slice import D,decode,check,has
P=D.parent;z=json.loads((P/'ramsey_38_reverse_seed.json').read_text());x=z['root'];C=z['core_mask']|1<<27;J=z['neighbor_mask'];g=decode(next(s['graph6'] for s in json.loads(D.read_text()) if (s['l'],s['k'])==(3,8)));g.append(z['best'][1]['red_core']|(1<<22)|(1<<26));
for i in range(27):
 if g[-1]>>i&1:g[i]|=1<<27
for i,j in [(5,22),(21,26)]:g[i]^=1<<j;g[j]^=1<<i
W=json.loads((P/'ramsey_38_double_link.json').read_text())['tests'][-1]['blue_eight'];target={tuple(sorted(e)) for e in combinations(W,2)};freeze={(5,22),(21,26),(22,27),(26,27)};allE=[e for e in combinations(range(28),2) if x not in e and e not in freeze];out=[];counts=Counter();blockers={str(e): (g[e[0]]&g[e[1]]).bit_count() for e in target};
for first in target:
 for second in [None]+allE:
  if second==first or second in target and second<first:continue
  edits=[first] if second is None else [first,second];b=g.copy();
  for i,j in edits:b[i]^=1<<j;b[j]^=1<<i
  if has(b,(1<<28)-1,3) or not check(b,2**27-1,3,8) or not check(b,C,3,7):continue
  ne=sum((v&C).bit_count() for i,v in enumerate(b) if C>>i&1)//2
  if not 45<=ne<=49:continue
  # Only new-vertex demands can fail because the old graph remains legal.
  qs=[1<<27];
  for i in range(27):
   if C>>i&1:qs += [s|1<<i for s in qs if not s&b[i]]
  h=Counter()
  for s in qs:
   hit=0;t=s
   while t:u=t&-t;t^=u;hit|=b[u.bit_length()-1]&J
   if hit.bit_count()<s.bit_count():h[s.bit_count()]+=1
  if h[1] or h[2]:continue
  counts[len(edits)]+=1;out.append(dict(edits=edits,failures=h))
print(counts,Counter(blockers.values()));print(sorted(out,key=lambda z:(z['failures'][3],sum(z['failures'].values())))[:3]);(P/'ramsey_38_break_triple.json').write_text(json.dumps(dict(blockers=blockers,results=out),indent=1)+'\n')
