"""Root 7: release exactly one short-row boundary demand, never its support."""
from itertools import combinations,permutations
from collections import Counter
from functools import lru_cache
from ramsey38_global_shell import sub
from ramsey38_support_ball_completion import N,shelling
from ramsey38_compare_support_fillings import boundary

p=N[7];rows={v:frozenset(n&p) for v,n in N.items() if v not in p|{7}}
short={v:r for v,r in rows.items() if len(r)<4};fixed=frozenset(rows.values())-set(short.values())
T=sub(p,4);F=sub(p,3)

def test(drop):
    req=set(r for v,r in short.items() if v!=drop);seed=frozenset(r for r in req if len(r)==3)
    assert seed
    balls=set()
    @lru_cache(None)
    def grow(fs):
        hits=Counter(e for f in fs for e in sub(f,2));open_e={e for e,h in hits.items() if h==1};closed=set(hits)-open_e
        if open_e:
            if len(fs)>=10:return
            opts=min(({f for f in F-fs if e<=f and not sub(f,2)&closed} for e in open_e),key=len)
            for f in opts:grow(fs|{f})
            return
        if not all(any(r<=f for f in fs) for r in req):return
        @lru_cache(None)
        def fill(ts):
            count=Counter(f for t in ts for f in sub(t,3));bd_or_internal=lambda f:1 if f in fs else 2
            if any(h>bd_or_internal(f) for f,h in count.items()):return
            done={f for f,h in count.items() if h==bd_or_internal(f)};needed=(fs|set(count))-done
            if needed:
                opts=min(({t for t in T-ts if f<=t and not sub(t,3)&done} for f in needed),key=len)
                for t in opts:fill(ts|{t})
            elif all(any(r<=t for t in ts) for r in rows.values()) and shelling(ts):
                assert boundary(ts)==fs and not any(short[drop]<=f for f in fs)
                balls.add(ts)
        fill(fixed)
    grow(seed)
    return balls
def wheel_hubs(drop):
    E=set.union(*(sub(r,2) for v,r in short.items() if v!=drop)); hubs=set()
    for h in p:
        L=set.union(set(),*(sub(r-{h},2) for r in rows.values() if h in r))
        for n in range(4,len(p)):
            for c in permutations(p-{h},n):
                if c[0]!=min(c) or c[1]>c[-1] or not all(frozenset((a,c[i-1])) in E for i,a in enumerate(c)):continue
                tips=[a for a in c if frozenset((a,h)) in E]
                if any(frozenset((a,d)) in L and frozenset((b,e)) in L for a,b,d,e in combinations(tips,4)):hubs.add(h)
    return sorted(hubs)

if __name__=='__main__':
    for v in short:
        balls=test(v);print(v,sorted(short[v]),len(balls),'remaining wheel hubs',wheel_hubs(v),dict(sorted(Counter(len(b) for b in balls).items())),flush=True)
        if balls:
            ts=min(balls,key=lambda b:(len(b),sorted(map(sorted,b))))
            print(' certificate:',[sorted(t) for t in shelling(ts)])
