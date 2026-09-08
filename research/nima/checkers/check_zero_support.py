"""Exhaust all 2^14 six-point supports using monomial support closure."""
import json
from pathlib import Path
from itertools import combinations
p=json.loads(Path('research/nima/results/local_global_torus_lattice.json').read_text())
assert p['status']=='passed'
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
C=sorted(set().union(*T));boundary={tuple(sorted((i,(i+1)%6))) for i in range(6)}
Q=list(combinations(range(6),3))
F=[frozenset(q for q in Q if all(e in t|boundary for e in combinations(q,2))) for t in T]
rect=[]
for c in C:
    inside=set(range(c[0],c[1]+1));cells={}
    for k,t in enumerate(T):
        if c in t:
            left=frozenset(e for e in t-{c} if set(e)<=inside)
            cells[left,(t-{c})-left]=k
    ls=sorted({a for a,b in cells},key=repr);rs=sorted({b for a,b in cells},key=repr)
    for a in ls[1:]:
        for b in rs[1:]:rect.append([cells[a,b],cells[ls[0],rs[0]],cells[a,rs[0]],cells[ls[0],b]])
assert len(rect)==3
# A positive monomial forces all its factors nonzero; the union gives the least allowed factor set.
def closure(mask,features):
    allowed=set().union(*(features[i] for i in range(14) if mask>>i&1))
    return sum(1<<i for i,f in enumerate(features) if f<=allowed)
local=set();tri=set();chan=set()
for mask in range(1<<14):
    bit=lambda i:(mask>>i)&1
    if all(bit(a)*bit(b)==bit(c)*bit(d) for a,b,c,d in rect):local.add(mask)
    if closure(mask,F)==mask:tri.add(mask)
    if closure(mask,T)==mask:chan.add(mask)
assert chan<=tri<=local
sep=sorted(local-tri,key=lambda m:(m.bit_count(),m))
sep2=sorted(tri-chan,key=lambda m:(m.bit_count(),m))
def witness(m,features):return {'mask':m,'positive_indices':[i for i in range(14) if m>>i&1],'forced_extra_indices':[i for i in range(14) if (closure(m,features)&~m)>>i&1]}
result={'status':'passed','counts':{'all':1<<14,'local':len(local),'triangle':len(tri),'channel':len(chan)},'minimal_local_not_triangle':witness(sep[0],F) if sep else None,'minimal_triangle_not_channel':witness(sep2[0],T) if sep2 else None,'rectangles':rect,'triangulations':p['triangulations'],'scope':'Exhaustive Boolean six-point supports over a field, not arbitrary nonzero coefficient assignments or higher n.'}
Path('research/nima/results/zero_support.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='triangulations'}))
