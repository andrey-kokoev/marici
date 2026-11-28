"""Minimum preselected individual row tests to construct a quartet or report none."""
from collections import defaultdict,Counter
from itertools import combinations
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D,evaluate
import json


def search(indices,options,sets,counting):
    for n in range(len(indices)):
        for tests in combinations(options,n):
            groups=defaultdict(list)
            for i in indices:groups[tuple(mask[i] for mask,r in tests)].append(i)
            leaves=[]
            for bits,g in groups.items():
                totals=sorted({len(sets[i]) for i in g});common=set.intersection(*(sets[i] for i in g))
                if (len(totals)>1 if counting else totals!=[0] and not common):break
                leaves.append(dict(bits=bits,totals=totals,quartet=min(common) if common else None))
            else:return dict(rows=[r for mask,r in tests],leaves=leaves)
    raise ValueError('no readout')


def audit():
    index=defaultdict(set)
    for sq,c,rs in run():index[sq,c].add(rs)
    records=[];hist=Counter();examples={}
    for sq,_,cs in charts():
        sets=[index[sq,tuple(sorted(c))] for c in cs];queries=[(r,) for r in combinations(range(1,11),3) if r not in sq and all(e not in path for e in combinations(r,2))];ok=[evaluate(10,sq,c,queries) for c in cs];options={}
        for r, in queries:
            mask=tuple((r,) in opts for opts in ok);options.setdefault(mask,r)
        for promise in [False,True]:
            ids=[i for i,s in enumerate(sets) if not promise or s]
            if not ids:continue
            count=search(ids,options.items(),sets,True);construct=search(ids,options.items(),sets,False);n=len(count['rows']);m=len(construct['rows']);hist[promise,n,m]+=1
            row=dict(square=sq,positive_assumed=promise,count_rows=count['rows'],construct=construct);records.append(row)
            if n>m:examples.setdefault(str((promise,n,m)),row)
    out=dict(by_promise_count_tests_witness_tests={str(k):v for k,v in hist.items()},plans=records);print(hist,examples);(D/'ramsey_one_witness_readout.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
