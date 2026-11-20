"""Exhaust invariant undirected pair colors on the oriented 12 FCC roots. Read the target in the unique transported frame of the source before coarsening signs."""
from itertools import combinations, product
from collections import defaultdict, Counter
from math import prod
from pathlib import Path
import json

base=(1,1,0)
G=[(k,s) for k in range(3) for s in product((1,-1),repeat=3) if prod(s)==1]
def act(g,x):
    k,s=g
    return tuple(s[i]*x[(i-k)%3] for i in range(3))
frames={act(g,base):g for g in G};V=sorted(frames);assert len(V)==12
inv={x:{act(g,y):y for y in V} for x,g in frames.items()}
def sign(v):
    a,b=[t for t in v if t];return ('++' if a==1 else '--') if a==b else 'mixed'
edges=list(combinations(V,2));parts=defaultdict(set);coarse=defaultdict(set)
for x,y in edges:
    p,q=inv[x][y],inv[y][x];parts[tuple(sorted((p,q)))].add((x,y));coarse[tuple(sorted((sign(p),sign(q))))].add((x,y))
assert all({tuple(sorted((act(g,x),act(g,y)))) for g in G}==part for part in parts.values() for x,y in part)

def audit(groups):
    # A vertex subset is independent iff its internal edge mask misses red.
    edge_masks={e:1<<i for i,e in enumerate(edges)}
    def mask(es):return sum(edge_masks[e] for e in es)
    cliques=[[mask(combinations(vs,2)) for vs in combinations(V,k)] for k in range(13)]
    keys=list(groups);blocks=[mask(groups[key]) for key in keys];hist=Counter();witness=None;best=13;triangle_free=0
    for m in range(1<<len(keys)):
        red=sum(b for i,b in enumerate(blocks) if m>>i&1)
        if any(red&t==t for t in cliques[3]):continue
        triangle_free+=1;alpha=next(k for k in range(12,0,-1) if any(not(red&t) for t in cliques[k]));hist[alpha]+=1
        if alpha<best:best=alpha;witness=[keys[i] for i in range(len(keys)) if m>>i&1]
    return dict(classes=len(keys),rules=1<<len(keys),triangle_free=triangle_free,hist=dict(sorted(hist.items())),best_alpha=best,example=witness)
nearest={k:v for k,v in parts.items() if all(sum(a*b for a,b in zip(x,y))==1 for x,y in v)}
result={name:audit(group) for name,group in [('all_orbits',parts),('two_ended_signs',coarse),('nearest_only',nearest)]};print(json.dumps(result,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
