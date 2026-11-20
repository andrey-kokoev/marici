"""Pairwise consistency of pocket colorings within a flip. Invoked by ramsey_37_lazy_fourfold.py --shared. Only the supplied count oracle can reveal new pocket observations."""
from itertools import combinations
from functools import lru_cache
@lru_cache(None)
def patterns(vertices):
    edges=[1<<(22*i+j) for i,j in combinations(vertices,2)];tri=[sum(1<<(22*i+j) for i,j in combinations(t,2)) for t in combinations(vertices,3)];masks=[0]
    for edge in edges:masks += [s|edge for s in masks]
    return sum(edges),[s for s in masks if all((s&t) not in (0,t) for t in tri)]

def solve(initial,data,oracle,global_support=False,threshold=False):
    from ramsey_37_joint_threshold import feasible
    stages=[]
    from ramsey_37_global_pocket_support import prune
    global_removed=0
    domains={};bits={};B=dict(initial);queries=[];removed=0
    for s,(z,p) in data.items():
        bits[s],allp=patterns(tuple(i for i in range(22) if p>>i&1));lo,hi=B[s];domains[s]=[t for t in allp if lo<=z+t.bit_count()<=hi]
    links=[(s,t,bits[s]&bits[t]) for s,t in combinations(domains,2) if bits[s]&bits[t]]
    while True:
        changed=True
        while changed:
            changed=False
            for s,t,m in links:
                allowed={v&m for v in domains[s]}&{v&m for v in domains[t]}
                for a in (s,t):
                    new=[v for v in domains[a] if v&m in allowed];assert new
                    if len(new)<len(domains[a]):removed+=len(domains[a])-len(new);domains[a]=new;changed=True
        if global_support:global_removed+=prune(domains,bits,links)
        for s,vs in domains.items():
            z=data[s][0];vals=[z+v.bit_count() for v in vs];B[s]=(min(vals),max(vals))
        best=min(B,key=lambda s:B[s][1]);probe=min(B,key=lambda s:B[s]);
        if threshold:
            lo,hi=B[probe][0],B[best][1]
            allmax=feasible(domains,bits,links,data,{s:B[s][1] for s in domains});joint_hi=hi
            if not allmax:
                while joint_hi>lo and not feasible(domains,bits,links,data,{s:joint_hi for s in domains}):joint_hi-=1
            stages.append(dict(lo=lo,hi=hi,joint_hi=joint_hi,allmax=allmax))
        if B[probe][0]==B[best][1]:return dict(stages=stages,queries=queries,cost=B[best][1],witness=best,links=len(links),patterns_pruned=removed,global_removed=global_removed)
        n=oracle(data[probe][1]);queries.append(probe);domains[probe]=[v for v in domains[probe] if v.bit_count()==n];assert domains[probe]
