"""Existential shared-edge CSP at specified lower thresholds on every candidate cost. No oracle colors. Decompose into independent components; memoize after projecting out private edges."""
from functools import lru_cache

def feasible(domains,bits,links,data,floors):
    adj={s:set() for s in domains}
    for u,v,_ in links:adj[u].add(v);adj[v].add(u)
    todo=set(adj)
    while todo:
        comp=[todo.pop()]
        for u in comp:
            for v in adj[u]&todo:todo.remove(v);comp.append(v)
        opts=[];masks=[]
        for u in comp:
            shared=0
            for v in adj[u]:shared|=bits[v]
            shared&=bits[u];masks.append(shared);opts.append({v&shared for v in domains[u] if data[u][0]+v.bit_count()>=floors[u]})
            if not opts[-1]:return False
        @lru_cache(None)
        def ok(rem,known,blue):
            if not rem:return True
            cand=[(i,[v for v in opts[i] if not ((v^blue)&known&masks[i])]) for i in rem];i,vals=min(cand,key=lambda x:len(x[1]));r=tuple(j for j in rem if j!=i);keep=0
            for j in r:keep|=masks[j]
            return any(ok(r,(known|masks[i])&keep,(blue|v)&keep) for v in vals)
        solved=ok(tuple(range(len(comp))),0,0);ok.cache_clear()
        if not solved:return False
    return True
