"""All distinct triples left by erasing a port in the 1699 maximal completions. Find every minimal independent fourth support, with no maximality assumption on that support."""
from collections import defaultdict,Counter
from functools import lru_cache,reduce
from operator import and_
from ramsey_final_miss_levels import levels,bits,attach,D,json

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=attach(p['stem_graphs'][-1],p['alternate']['to34']);quads=[];levels(H,quads.append);groups=defaultdict(set)
    for Q in quads:
        for j,s in enumerate(Q):groups[tuple(sorted(Q[:j]+Q[j+1:]))].add(s)
    I=[0]
    for v,r in enumerate(H):I += [x|1<<v for x in I if not x&r]
    T=sorted((x for x in I if x.bit_count()>=6),key=int.bit_count);masks=[sum(1<<i for i,t in enumerate(T) if t.bit_count()==k) for k in (6,7,8)];col=[sum(1<<i for i,t in enumerate(T) if not t>>v&1) for v in range(34)]
    @lru_cache(None)
    def miss(s):return reduce(and_,(col[j] for j in bits(s)),(1<<len(T))-1)
    hist=Counter();forced=Counter();freq=Counter();unique=Counter();samples={};kernelsets=Counter();pairs=set();single_set=Counter()
    for fixed,opts in groups.items():
        a,b,c=map(miss,fixed);tight=(a&b&c&masks[0])|(((a&b)|(b&c)|(a&c))&masks[1])|((a|b|c)&masks[2]);todo=list(opts);seen=set();minimal=[]
        while todo:
            s=todo.pop()
            if s in seen:continue
            seen.add(s);children=[s^(1<<v) for v in bits(s) if not miss(s^(1<<v))&tight];todo.extend(children)
            if not children:minimal.append(s)
        hist[len(minimal)]+=1;kernel=reduce(and_,minimal);forced[kernel.bit_count()]+=1;freq.update(bits(kernel));kernelsets[kernel]+=1
        if len(minimal)==1:unique[kernel.bit_count()]+=1;single_set[kernel]+=1
        pairs.update(minimal);samples.setdefault(len(minimal),{'triple':fixed,'minimal':minimal})
    common=Counter(s for q in quads for s in set(q));heavy=[s for s,_ in common.most_common(3)];assert all(set(q)&set(heavy) for q in quads)
    assert all(not set.intersection(*(set(q) for q in quads if s not in q)) for s in quads[0]) # no pair hits all tuples
    return dict(min_cover=heavy,cover_frequencies=[common[s] for s in heavy],quads=len(quads),triples=len(groups),minimal_count_hist=dict(hist),forced_size_hist=dict(forced),single_size_hist=dict(unique),forced_vertex_counts=dict(freq),distinct_minimal_supports=len(pairs),forced_intersections=kernelsets.most_common(),unique_minima=single_set.most_common(),samples=samples)
if __name__=='__main__':
    res=run();(D/'ramsey_all_last_port_kernels.json').write_text(json.dumps(res)+'\n');print({k:v for k,v in res.items() if k not in ('samples','forced_intersections','unique_minima')});print('most common forced intersections',res['forced_intersections'][:5])
