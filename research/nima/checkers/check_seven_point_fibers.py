"""Bounded monomial-fiber connectivity certificate for the local ideal."""
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
from pathlib import Path
import json
@lru_cache(None)
def faces(v):
    if len(v)<3:return (frozenset(),)
    return tuple(a|b|{(v[0],v[k],v[-1])} for k in range(1,len(v)-1) for a in faces(v[:k+1]) for b in faces(v[k:]))
F=faces(tuple(range(7)));assert len(F)==42
bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
T=[frozenset(e for q in f for e in combinations(q,2))-bd for f in F]
Q=list(combinations(range(7),3));moves=set()
for c in sorted(set().union(*T)):
    inside=set(range(c[0],c[1]+1));cells={}
    for k,t in enumerate(T):
        if c in t:
            a=frozenset(e for e in t-{c} if set(e)<=inside);cells[a,(t-{c})-a]=k
    ls=sorted({a for a,b in cells},key=repr);rs=sorted({b for a,b in cells},key=repr)
    for a,b in combinations(ls,2):
        for c,d in combinations(rs,2):moves.add(tuple(sorted((tuple(sorted((cells[a,c],cells[b,d]))),tuple(sorted((cells[a,d],cells[b,c])))))))
records=[]
for degree in [2,3]:
    mons=list(combinations_with_replacement(range(42),degree));index={v:i for i,v in enumerate(mons)};parent=list(range(len(mons)))
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for a,b in moves:
        for tail in combinations_with_replacement(range(42),degree-2):
            i=root(index[tuple(sorted(a+tail))]);j=root(index[tuple(sorted(b+tail))]);parent[i]=j
    seen={};witness=None;fiber_count=set()
    for i,m in enumerate(mons):
        key=tuple(sum(q in F[j] for j in m) for q in Q);fiber_count.add(key)
        if key in seen and root(i)!=root(seen[key]):witness=[mons[seen[key]],m];break
        seen[key]=i
    records.append({'degree':degree,'monomials':len(mons),'witness':witness,'fibers_scanned':len(fiber_count)})
    if witness:break
result={'status':'passed','local_moves':len(moves),'records':records,'triangulations':[sorted(t) for t in T],'scope':'Connectivity of every degree-two and, if reached, degree-three triangle fiber under all local rectangle moves. No higher-degree conclusion.'}
Path('research/nima/results/seven_point_fibers.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='triangulations'}))
