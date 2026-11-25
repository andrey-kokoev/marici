"""Minimum old-edge cuts for the fixed 49 triangles, via reciprocal choices."""
from r312_endpoint_repair_gate import cover,adj,n
from functools import lru_cache
choices={v:(a,b) for a,b in cover for v in range(n) if adj[a]&adj[b]&(1<<v)}
mutual=sorted((v,w) for v,opts in choices.items() for w in opts if v<w and v in choices[w])
@lru_cache(None)
def match(i,used):
    if i==len(mutual):return ()
    a,b=mutual[i]; bits=(1<<a)|(1<<b)
    skip=match(i+1,used)
    return skip if bits&used else max(skip,((a,b),)+match(i+1,used|bits),key=len)
pairs=match(0,0)
print('reciprocal cuts',mutual,'maximum matching',pairs,'minimum triangle cuts',n-len(pairs))
# Seek a minimum cut attaining the degree bound too. Matching is fixed here;
# unmatched centers choose one incident leg. Prune once a degree cannot recover.
used=set(v for e in pairs for v in e); order=sorted(set(range(n))-used)
ends=set(v for e in cover for v in e)
def solve(i,cuts):
    degree=[0]*n
    for a,b in cuts:degree[a]+=1;degree[b]+=1
    need={v:max(0,1+(v in ends)-degree[v]-(v in order[i:])) for v in range(n)}
    if any(need[v]>sum(v in choices[w] for w in order[i:]) for v in ends):return
    if i==len(order):return cuts if not any(need.values()) else None
    v=order[i]
    for w in sorted(choices[v],key=lambda w:-need[w]):
        r=solve(i+1,cuts+[(v,w)])
        if r:return r
cuts=solve(0,list(pairs)); print('degree-compatible minimum found:',cuts is not None)
if cuts:
    from search_r312_circulants import independent
    g=adj.copy()
    for a,b in cover:g[a]|=1<<b;g[b]|=1<<a
    for a,b in cuts:g[a]&=~(1<<b);g[b]&=~(1<<a)
    assert max(x.bit_count() for x in g)<=11 and not any(g[a]&g[b] for a in range(n) for b in range(a) if g[a]>>b&1)
    print('alpha',next(k for k in range(11,50) if not independent((1<<n)-1,k+1,g)))
