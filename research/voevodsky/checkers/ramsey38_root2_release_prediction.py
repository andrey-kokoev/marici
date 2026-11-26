"""Predict single releases from forced nonplanar subgraphs, then test ball realizations."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from ramsey38_global_shell import N,sub
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary

P=N[2]; rows={v:frozenset(P&n) for v,n in N.items() if v not in P|{2}}
short={v:r for v,r in rows.items() if len(r)<4}; forced=frozenset(rows.values())-set(short.values());F=sub(P,3);T=sub(P,4)

def obstruction(req):
    edges=set.union(*(sub(r,2) for r in req))
    # The center of a required triangular face and its three spokes also lie
    # on the sphere. Disjoint connected branch sets model graph contractions.
    points=set(P)
    for i,f in enumerate(sorted((r for r in req if len(r)==3),key=sorted),100):
        points.add(i);edges.update(frozenset((i,v)) for v in f)
    @lru_cache(None)
    def planar(ps,es):
        # Wagner: a simple graph is planar iff it has no K5 or K3,3 minor.
        # Edge deletion is unnecessary: at each stage check non-induced copies.
        ns={v:set() for v in ps}
        for i,j in es:ns[i].add(j);ns[j].add(i)
        if any(len(set.intersection(*(ns[v] for v in part)))>=3 for part in combinations(ps,3)):return False
        if any(all(b in ns[a] for a,b in combinations(s,2)) for s in combinations([v for v in ps if len(ns[v])>=4],5)):return False
        if len(ps)<=5:return True
        # Remove low-degree vertices, suppress degree two (both operations preserve planarity).
        for v in ps:
            if len(ns[v])<=2:
                h={e for e in es if v not in e}
                if len(ns[v])==2:h.add(tuple(sorted(ns[v])))
                return planar(ps-{v},frozenset(h))
        for a,b in es:
            h=frozenset(tuple(sorted(a if v==b else v for v in e)) for e in es if e!=(a,b))
            if not planar(ps-{b},h):return False
        return True
    return not planar(frozenset(points),frozenset(tuple(sorted(e)) for e in edges))

def test(drop):
    req=set(r for v,r in short.items() if v!=drop);seed=frozenset(r for r in req if len(r)==3); balls=set();spheres=set()
    @lru_cache(None)
    def grow(fs):
        hits=Counter(e for f in fs for e in sub(f,2));open_e={e for e,h in hits.items() if h==1};closed=set(hits)-open_e
        if open_e:
            if len(fs)>=10:return
            opts=min(({f for f in F-fs if e<=f and not sub(f,2)&closed} for e in open_e),key=len)
            for f in opts:grow(fs|{f})
            return
        if not all(any(r<=f for f in fs) for r in req):return
        # All seven vertices are required for this root even after a single release.
        if set.union(set(),*fs)!=P or len(fs)!=10:return
        # Reject closed pseudomanifolds with disconnected vertex links.
        for v in P:
            es=[f-{v} for f in fs if v in f];seen=set(es[0]);
            for _ in es:
                for e in es:
                    if e&seen:seen.update(e)
            if seen!=set.union(set(),*es):return
        spheres.add(fs)
        @lru_cache(None)
        def fill(ts):
            h=Counter(f for t in ts for f in sub(t,3));quota=lambda f:1 if f in fs else 2
            if any(n>quota(f) for f,n in h.items()):return
            done={f for f,n in h.items() if n==quota(f)};need=(fs|set(h))-done
            if need:
                opts=min(({t for t in T-ts if f<=t and not sub(t,3)&done} for f in need),key=len)
                for t in opts:fill(ts|{t})
            elif all(any(r<=t for t in ts) for r in rows.values()) and shelling(ts):
                assert boundary(ts)==fs;balls.add(ts)
        fill(forced)
    assert seed and all(n<=2 for n in Counter(e for f in seed for e in sub(f,2)).values()) and set.union(set(),*req)==P
    grow(seed);return spheres,balls
if __name__=='__main__':
    # Rows 16 and 9 make a closed disk with rim 3--5--8--17--3.
    # Paths through 18 and 13 connect alternating endpoints outside it.
    assert rows[16]=={3,5,17} and rows[9]=={5,8,17}
    assert rows[6]=={5,18} and rows[21]=={17,18}
    assert {3,13}<=rows[7] and {8,13}<=rows[4]
    for d in short:
        blocked=obstruction(set(r for v,r in short.items() if v!=d));s,b=test(d);assert not blocked or not s
        print(d,sorted(short[d]),'minor' if blocked else 'pass',len(s),dict(sorted(Counter(map(len,b)).items())),flush=True)
        if b:
            ts=min(b,key=lambda t:(len(t),sorted(map(sorted,t))))
            print('shelling:',[sorted(t) for t in shelling(ts)])
