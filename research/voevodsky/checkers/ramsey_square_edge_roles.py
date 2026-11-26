"""For each original edge, hit every saturated eight-clique that uses that edge in a given octahedral role. Deduplicate cliques before the test."""
from collections import defaultdict,Counter
from itertools import combinations
import json
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import D,decode
P=D.parent;g=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,9)));n=len(g);buckets=defaultdict(lambda:defaultdict(set));allq=set()
for x in range(n):
 for a in range(n):
  if not g[x]>>a&1:continue
  for b in range(n):
   if x==b or g[x]>>b&1:continue
   c=g[b]&~g[a]&~((1<<a)|(1<<b)|(1<<x));
   if c.bit_count()!=7:continue
   q=c|1<<a;allq.add(q)
   for y in range(n):
    if not c>>y&1:continue
    for role,pairs in [('pole',[(x,y),(a,b)]),('equator',[(x,a),(a,y),(y,b),(b,x)])]:
     for u,v in pairs:buckets[role][tuple(sorted((u,v)))].add(q)
assert len(allq)==315
import sys
if '--export' in sys.argv:
 (P/'ramsey_square_edge_families.json').write_text(json.dumps([[r,*e,sorted(q)] for r,B in buckets.items() for e,q in B.items()]));sys.exit()
enc={d:CardEnc.atmost(list(range(1,n+1)),d).clauses for d in range(1,10)}
def hit(qs):
 cs=[[i+1 for i in range(n) if q>>i&1] for q in qs];
 for d in range(1,10):
  with Solver(name='g4',bootstrap_with=cs+enc[d]) as s:
   if s.solve():return d
out={}
for role,by in buckets.items():
 h=Counter();
 for (i,j),qs in by.items():h[('red' if g[i]>>j&1 else 'blue',len(qs),hit(qs))]+=1
 out[role]=[dict(color=c,cliques=m,cut=t,edges=f) for (c,m,t),f in sorted(h.items())];print(role,out[role],flush=True)
extra=Counter()
for role,by in buckets.items():
 for (i,j),qs in by.items():
  e=(1<<i)|(1<<j);extra[role,('red' if g[i]>>j&1 else 'blue'),all(e&q for q in qs)]+=1
out['endpoints_hit_all']=[dict(role=r,color=c,cover=bool(ok),edges=v) for (r,c,ok),v in extra.items()];print(out['endpoints_hit_all']);(P/'ramsey_square_edge_roles.json').write_text(json.dumps(out,indent=1)+'\n')
