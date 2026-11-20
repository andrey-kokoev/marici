"""Independent direct check on a fixed 10-vertex residual; no discovery search."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
E={(0,1),(0,6),(0,7),(0,8),(1,3),(1,5),(1,9),(2,3),(2,4),(2,7),(2,8),(3,6),(4,5),(4,6),(4,9),(5,7),(5,8),(7,9),(8,9)}
e=(3,6)
for flipped in [False,True]:
    edges=E-{e} if flipped else E
    assert not any(all(p in edges for p in combinations(t,2)) for t in combinations(range(10),3))
    B=[set(t) for n in range(11) for t in combinations(range(10),n) if not any(p in edges for p in combinations(t,2))];assert max(map(len,B))<=4
    # Include maximal old rows even if they can now be enlarged by adding an endpoint.
    old=[s for s in B if not set(e)<=s];new=[s for s in B if set(e)<=s]
    rows=[s for group in (old,new) for s in group if not any(s<t for t in group)]
    for d in (3,4,5):
        counts=Counter();first={}
        for rr in combinations_with_replacement(rows,d):
            if all(len(b)+sum(b.isdisjoint(r) for r in rr)<=5 for b in B):
                h=sum(set(e)<=r for r in rr);counts[h]+=1;first.setdefault(h,list(map(sorted,rr)))
        print(flipped,d,dict(counts),first if d==4 else '')
        if not counts:break
