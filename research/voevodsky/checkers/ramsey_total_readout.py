"""Read a two-repair total rather than identify a pentagon. All probes are counterfactual."""
from itertools import combinations
from collections import Counter,defaultdict
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D,evaluate
from ramsey_square_repair_counts import predict, count
import json


def audit():
    hist=Counter();examples={};records=[]
    for sq,_,cs in charts():
        flank,v=predict(sq);tot=[sum(count(sq,c,e) for e in flank if e not in c) for c in cs]
        if len(set(tot))<2:continue
        U=set().union(*sq);W=set(range(1,11))-U;mov=U-set.intersection(*map(set,sq));rows=[r for r in combinations(range(1,11),3) if r not in sq and not any(e in path for e in combinations(r,2))];ok=[{s for s, in evaluate(10,sq,c,[(r,) for r in rows])} for c in cs];probes=[]
        for e in combinations(sorted(W),2):
            if e in path:continue
            r=next(r for r in rows if set(e)<=set(r) and set(r)&mov);assert all((r in legal)==(e not in c) for legal,c in zip(ok,cs));probes.append((r,e))
        mask=lambda r:tuple(r in legal for legal in ok)
        def choose(pool):
            for n in range(1,len(cs)):
                best=None;score=len(cs)+1
                for tests in combinations(pool,n):
                    groups=defaultdict(set)
                    for i,k in enumerate(tot):groups[tuple(mask(r)[i] for r in tests)].add(k)
                    if len(groups)<score and all(len(s)==1 for s in groups.values()):best=tests;score=len(groups)
                    if score==len(set(tot)):break
                if best:return best
        chosen=choose([r for r,e in probes]);generic=choose(rows);only_flanks=choose([r for r,e in probes if e in flank]);assert chosen and generic
        groups=defaultdict(list)
        for i,k in enumerate(tot):groups[tuple(mask(r)[i] for r in chosen)].append(k)
        record=dict(square=sq,possible=sorted(set(tot)),queries=chosen,edges=[e for r,e in probes if r in chosen],outcomes=[dict(bits=b,total=g[0],cycles=len(g)) for b,g in groups.items()],best_any_row=len(generic),best_flank_only=len(only_flanks) if only_flanks else None)
        key=(len(set(tot)),len(chosen),len(generic));hist[key]+=1;examples.setdefault(key,record);records.append(record)
    out=dict(by_distinct_totals_edge_queries_any_queries={str(k):v for k,v in hist.items()},squares=records);print(hist);print(examples);(D/'ramsey_total_readout.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
