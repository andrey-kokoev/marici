"""Start with the square alone: unconditional initial repair vs one permanent row read."""
from collections import defaultdict,Counter
from itertools import combinations
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D,evaluate
import json


def audit():
    quartets=defaultdict(set);bases=defaultdict(set)
    for sq,c,rs in run():
        quartets[sq,c].add(rs);opts=[p for p in combinations(rs,2) if set(p[0]).isdisjoint(p[1]) and all(set(s)&set(p[0]+p[1]) for s in sq)];m,=[(p,q) for p,q in combinations(opts,2) if set(p).isdisjoint(q)];bases[sq,c].update(m)
    records=[];hist=Counter()
    for sq,_,cs in charts():
        qs=[quartets[sq,tuple(sorted(c))] for c in cs];bs=[bases[sq,tuple(sorted(c))] for c in cs];queries=[(r,) for r in combinations(range(1,11),3) if r not in sq and not any(e in path for e in combinations(r,2))];reads=[evaluate(10,sq,c,queries) for c in cs]
        for promise in [False,True]:
            ids=[i for i,g in enumerate(qs) if not promise or g];
            if not ids:continue
            common=set.intersection(*(qs[i] for i in ids));pairs=set.intersection(*(bs[i] for i in ids));some=any(qs[i] for i in ids);plans=[]
            if some and not common:
                for r, in queries:
                    yes=[i for i in ids if (r,) in reads[i]];no=[i for i in ids if i not in yes]
                    if not yes or not no:continue
                    accept=[g for g in set.intersection(*(qs[i] for i in yes)) if r in g];reject=set.intersection(*(qs[i] for i in no));none=not any(qs[i] for i in no)
                    if accept and (reject or none):plans.append(dict(probe=r,yes=min(accept),no=None if none else min(reject),branch_sizes=(len(yes),len(no))))
            label='none' if not some else 'common' if common else 'first row' if plans else 'no first-row plan';hist[promise,label,bool(pairs)]+=1;records.append(dict(square=sq,promise=promise,counts=[len(qs[i]) for i in ids],safe_links=sorted(pairs),outcome=label,example=plans[:1]))
    result=dict(hist={str(k):v for k,v in hist.items()},records=records);print(hist);print(next((r for r in records if r['outcome']=='no first-row plan'),None));print(next((r for r in records if r['example'] and not r['safe_links']),None));(D/'ramsey_square_first_move.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
