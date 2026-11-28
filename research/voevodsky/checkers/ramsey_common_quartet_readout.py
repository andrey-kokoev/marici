"""Intersect actual labeled attachment sets in each positive count-readout class."""
from collections import defaultdict,Counter
from itertools import combinations
from ramsey_plan_total_probes import plan
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D
import json


def audit():
    index=defaultdict(set)
    for sq,c,rs in run():index[sq,c].add(rs)
    hist=Counter();classes=[]
    for sq,_,cycles in charts():
        edges,rows,read,kind=plan(sq);U=set().union(*sq);W=set(range(1,11))-U;groups=defaultdict(list)
        for c in cycles:groups[tuple(e not in c for e in edges)].append(c)
        for bits,cs in groups.items():
            sets=[index[sq,tuple(sorted(c))] for c in cs];total=read[bits];assert all(len(s)==total for s in sets)
            if not total:continue
            common=set.intersection(*sets);hist[len(cs),bool(common)]+=1
            further=None
            if not common:
                for e in combinations(sorted(W),2):
                    if len({e in c for c in cs})==1:continue
                    sub=[set.intersection(*(s for c,s in zip(cs,sets) if (e in c)==v)) for v in (False,True)]
                    if all(sub):
                        mov=U-set.intersection(*map(set,sq));z=min(i for i in mov if all(abs(i-j)>1 for j in e));further=dict(edge=e,row=sorted((*e,z)),if_blue=min(sub[0]),if_red=min(sub[1]));break
                assert further
            classes.append(dict(square=sq,tests=rows,bits=bits,total=total,cycles=len(cs),common_count=len(common),common_example=min(common) if common else None,further=further))
    out=dict(classes_by_size_and_common={str(k):v for k,v in hist.items()},classes=classes);print(hist);print([(c['square'],c['total'],c['common_count']) for c in classes if c['cycles']>1]);(D/'ramsey_common_quartet_readout.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
