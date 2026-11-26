"""Exhaust boundary spheres, then shellable fillings, on the seven given labels."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from ramsey38_support_ball_completion import N,shelling,fmt

def sub(s,k):return {frozenset(t) for t in combinations(sorted(s),k)}
def audit(root):
    p=N[root]; rows={v:frozenset(p&N[v]) for v in N if v!=root and v not in p}; assert max(map(len,rows.values()))<=4
    forced={s for s in rows.values() if len(s)==4};tri=sub(p,3);tet=sub(p,4);short={s for s in rows.values() if len(s)<4}; required=frozenset(s for s in short if len(s)==3)
    spheres=set(); balls=[]
    @lru_cache(None)
    def grow(fs):
        hits=Counter(e for f in fs for e in sub(f,2)); opened={e for e,h in hits.items() if h==1};closed=set(hits)-opened
        if not opened:
            vertices=set().union(*fs)
            if len(vertices)-len(hits)+len(fs)!=2 or not all(any(s<=f for f in fs) for s in short):return
            # Vertex links must be connected cycles; the triangle adjacency must be connected.
            for v in vertices:
                edges=[f-{v} for f in fs if v in f];seen=set(edges[0]);
                for _ in edges:
                    for edge in edges:
                        if edge&seen:seen.update(edge)
                if seen!=set.union(set(),*edges):return
            seen={next(iter(fs))}
            for _ in fs:seen.update(f for f in fs if any(len(f&g)==2 for g in list(seen)))
            if seen==set(fs):spheres.add(fs)
            return
        if len(fs)>=2*len(p)-4:return
        choices=[{f for f in tri-fs if e<=f and not sub(f,2)&closed} for e in opened]
        for f in min(choices,key=len):grow(fs|{f})
    for seed in ([required] if required else [frozenset([f]) for f in tri]):
        if all(n<=2 for n in Counter(e for f in seed for e in sub(f,2)).values()):grow(seed)
    for bd in spheres:
        @lru_cache(None)
        def fill(ts):
            hits=Counter(f for t in ts for f in sub(t,3));closed={f for f,n in hits.items() if n==(1 if f in bd else 2)}
            if any(n>(1 if f in bd else 2) for f,n in hits.items()):return
            need=(bd|set(hits))-closed
            if not need:
                if shelling(ts):balls.append((bd,ts))
                return
            opts=[{t for t in tet-ts if f<=t and not sub(t,3)&closed} for f in need]
            for t in min(opts,key=len):fill(ts|{t})
        fill(frozenset(forced))
    return spheres,balls
if __name__=='__main__':
    from ramsey38_reroot_obstructions import inspect
    p=N[2]; short=[p&N[v] for v in N if v not in p|{2} and len(p&N[v])<=3];edges=set.union(*(sub(s,2) for s in short))
    left=(3,5,8);right=(11,13,17)
    assert all(frozenset((a,b)) in edges for a in left for b in right if (a,b)!=(5,13))
    assert {frozenset((5,18)),frozenset((18,13))}<=edges
    for r in N:
        if len(N[r])==7 and inspect(r)==('rim',{}):
            s,b=audit(r);print(r,'boundary spheres',len(s),'shellable fillings',len(b))
