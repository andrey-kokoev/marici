"""Explore the other monotone direction: strip edges from generated cores to deletion-minimal legal cores. Each rejected deletion remains illegal later; canonicalize sinks against the sparse source family and check all minima directly. No endpoint information."""
import json,random,collections,itertools
import igraph as ig
from ramsey_retention_slice import D,decode,has,check
P=D.parent;R=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];old=[decode(l) for l in (P/'ramsey38_26_e73_hog.g6').read_text().splitlines()];F=(1<<26)-1
def key(a):
 g=ig.Graph(26,[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1]);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(g.canonical_permutation()).get_edgelist()))
known={key(a) for a in old};pool={};rng=random.Random(260072)
for idx,r in enumerate(R):
 for rep in range(4):
  a=r['adj'][:];E=[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1];rng.shuffle(E);b=[F&~(v|1<<i) for i,v in enumerate(a)];
  for i,j in E:
   if not has(b,F&~(a[i]|a[j]),6):a[i]^=1<<j;a[j]^=1<<i;b[i]|=1<<j;b[j]|=1<<i
  k=key(a)
  if k not in pool:
   assert check(a,F,3,8) and all(has(b,F&~(a[i]|a[j]),6) for i in range(26) for j in range(i) if a[i]>>j&1);pool[k]=dict(adj=a,edges=len(k),source=k in known,origins=[])
  pool[k]['origins'].append([idx,rep])
print('unique',len(pool),'known',sum(z['source'] for z in pool.values()),'hist',collections.Counter(z['edges'] for z in pool.values()));(P/'ramsey_gain26_minimal.json').write_text(json.dumps(list(pool.values()))+'\n')
