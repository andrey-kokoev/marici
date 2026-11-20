"""Infer an incidence-consistent frame map by arc consistency on pairwise relations. Initial domains contain all opposite-type vertices, not just images of known maps."""
from collections import Counter
from ramsey_strip_mixed_cube_exchange import U,V,E,F,cross,ans,r
vertices=U+V

def relation(x,y):
    if x==y:return ('equal',)
    if y==r[x]:return ('row mates',)
    if (x in U)==(y in U):return ('cube',bool(E(x,y) if x in U else F(x,y)))
    return ('cross',cross(x,y) if x in U else cross(y,x))
for nonreturn in (False,True):
    domains={x:set(V if x in U else U) for x in vertices};domains[16]={7}
    if nonreturn:domains[7].discard(16)
    rounds=[]
    while True:
        new={x:{a for a in domains[x] if all(any(relation(x,y)==relation(a,b) for b in domains[y]) for y in vertices if y!=x)} for x in vertices}
        assert all(new.values())
        if new==domains:break
        domains=new;rounds.append(dict(sorted(Counter(map(len,domains.values())).items())))
    print('nonreturn',nonreturn,'round domain-size histograms',rounds,'remaining domain histogram',dict(Counter(map(len,domains.values()))))
    if nonreturn:
        assert all(len(d)==1 for d in domains.values());f={x:next(iter(d)) for x,d in domains.items()};assert all(f[f[x]]==r[x] for x in vertices)
