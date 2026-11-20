"""Exact natural join support on shared pocket edges. Input contains possible local masks, never true colors. A supported tuple is extendible to a simultaneous choice in its component; disjoint components combine independently."""
def prune(domains,bits,links):
    adj={s:set() for s in domains}
    for s,t,_ in links:adj[s].add(t);adj[t].add(s)
    todo=set(adj);removed=0
    while todo:
        seed=todo.pop();comp=[seed]
        for s in comp:
            for t in adj[s]&todo:todo.remove(t);comp.append(t)
        if len(comp)<3:continue # pairwise propagation already ran
        # Private edge choices never constrain other pockets. Merge them during search.
        shared={s:bits[s]&sum_union(bits[t] for t in adj[s]) for s in comp}
        opts={s:{v&shared[s] for v in domains[s]} for s in comp};supported={s:set() for s in comp}
        def extend(rest,known,blue,path):
            if not rest:
                for s,v in path:supported[s].add(v)
                return True
            sel=None;best=None
            for s in rest:
                m=known&shared[s];vals=[v for v in opts[s] if not ((v^blue)&m)]
                if not vals:return False
                if best is None or len(vals)<len(best):sel,best=s,vals
            return any(extend(rest-{sel},known|shared[sel],blue|v,path+[(sel,v)]) for v in best)
        for s in comp:
            for v in opts[s]-supported[s]:
                if v not in supported[s]:extend(set(comp)-{s},shared[s],v,[(s,v)])
        for s in comp:
            new=[v for v in domains[s] if v&shared[s] in supported[s]];assert new;removed+=len(domains[s])-len(new);domains[s]=new
    return removed

def sum_union(values):
    mask=0
    for v in values:mask|=v
    return mask
