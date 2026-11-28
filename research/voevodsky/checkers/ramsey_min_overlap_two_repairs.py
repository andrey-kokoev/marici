"""Minimum repeated site incidences for three legal rows requiring two red links."""
from itertools import combinations
from collections import Counter
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D
import json


def audit():
    hist=Counter();examples={};tested=0;disjoint=0
    for sq,_,cycles in charts():
        if any(10 in r for r in sq):continue
        for cyc in cycles:
            queries=[(s,) for s in combinations(range(1,11),3) if s not in sq and not any(e in path for e in combinations(s,2))]
            rows=sorted(s for s, in evaluate(10,sq,cyc,queries));E=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r};blue={r:set(range(1,11))-set(r)|{11+j for j,s in enumerate(sq) if set(s)&set(r)} for r in rows}
            required={};allowed={}
            for p in combinations(rows,2):
                a,b=p;required[p]=next((q for q in combinations(sorted(blue[a]&blue[b]),5) if not any(e in E for e in combinations(q,2))),None);allowed[p]=not set(a)&set(b) and all(set(s)&(set(a)|set(b)) for s in sq)
                if not set(a)&set(b):
                    disjoint+=1;assert required[p] is None
            for rs in combinations(rows,3):
                if not any(10 in r for r in rs):continue
                tested+=1;need=[p for p in combinations(rs,2) if required[p]]
                if len(need)!=2 or not all(allowed[p] for p in need):continue
                overlap=9-len(set().union(*rs));hist[overlap]+=1
                example=dict(square=sq,cycle=sorted(cyc),rows=rs,repairs=[dict(pair=p,blue_five=required[p]) for p in need]);examples.setdefault(overlap,example)
    out=dict(tested=tested,disjoint_pair_checks=disjoint,two_repairs_by_repeated_sites=hist,examples=examples);print(hist);print(examples.get(min(hist)) if hist else None);(D/'ramsey_min_overlap_two_repairs.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
