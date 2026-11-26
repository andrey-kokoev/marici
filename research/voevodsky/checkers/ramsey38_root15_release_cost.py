"""Root 15: why no single release can work, and which pairs work on original labels."""
from ramsey38_release_census import N,sub,templates,first_ball,bits

P=N[15];rows={v:P&n for v,n in N.items() if v not in P|{15}};short={v:r for v,r in rows.items() if len(r)<4}

def lower_bound():
    # At label 1 the boundary requests force the rim path 6--22--10 and put 3 on the return arc.
    assert rows[5]=={1,6,22} and rows[27]=={1,22,10} and rows[20]=={1,3}
    assert {1,6,10}<=rows[23] and {1,22,3}<=rows[14]
    # Releasing one of those requests eliminates that proof, but leaves K3,3.
    for d,left,right,via in [(5,(1,6,17),(26,10,3),22),(20,(1,10,17),(26,6,22),3),(27,(1,6,17),(26,3,22),None)]:
        edges=set.union(*(sub(r,2) for v,r in short.items() if v!=d));miss=[(a,b) for a in left for b in right if frozenset((a,b)) not in edges];assert not set(left)&set(right)
        if via is None:assert not miss
        else:assert via not in left+right and len(miss)==1 and all(frozenset((v,via)) in edges for v in miss[0])
        print('release',d,'K3,3:',left,right,'missing',miss,'via',via)

def scan():
    labels=sorted(P);mask=lambda r:sum(1<<i for i,v in enumerate(labels) if v in r);buckets={}
    for bd,closure in templates():
        hidden=tuple(v for v,r in short.items() if mask(r) not in closure)
        if len(hidden)==2 and set(hidden)&{5,20,27}:buckets.setdefault(hidden,[]).append(bd)
    for hidden,bs in sorted(buckets.items()):
        for bd in bs:
            order=first_ball(bd,{mask(r) for r in rows.values()})
            if order:
                print('release pair',hidden,'shelling', [sorted(labels[i] for i in t) for t in order]);break
        else:print('release pair',hidden,'no shellable ball')
if __name__=='__main__':lower_bound();scan()
