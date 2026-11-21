"""Broaden depth-two search using phase degree ceilings, deficiency and simultaneous constraints."""
from itertools import combinations
from collections import Counter
from random import Random
from pathlib import Path
import json,sys
from ramsey_39_twelve_order_sat import test
from ramsey_39_depth_two_edge_bound import bound
from functools import lru_cache
B=[bound(38-d,9) for d in range(10)]
@lru_cache(None)
def deficiency(caps,max_degree_sum=288):
    # Among profiles of total degree s, minimize sum(d^2+B[38-d]).
    dp={0:0}
    for cap in caps:
        nxt={}
        for s,t in dp.items():
            for d in range(3,cap+1): # R(3,9)=36 implies minimum degree three
                q=t+d*d+B[d];k=s+d
                if q<nxt.get(k,float('inf')):nxt[k]=q
        dp=nxt
    return any(s%2==0 and 272<=s<=max_degree_sum and 39*(s//2)>=c for s,c in dp.items())

def run(n):
    rng=Random(31012);seen=set();stats=Counter();survivors=[]
    while len(seen)<n:
        W=tuple(sorted([0,1]+rng.sample(range(2,39),10)))
        if W in seen:continue
        seen.add(W);h=[0]*39
        for a in W:
            for b in W:h[(a+b)%39]+=1
        caps=tuple(sorted(min(9,2*x) for x in h))
        if not min(h):key='not covering'
        elif min(caps)<3:key='low degree'
        elif sum(caps)<272:key='insufficient capped degree sum'
        elif not deficiency(caps):key='degree deficiency'
        else:
            key=test(W,degree_budget=True)
            if key.startswith('candidate'):survivors.append((W,key))
        stats[key]+=1
    print(n,stats,survivors);Path(__file__).with_suffix('.json').write_text(json.dumps({'seed':31012,'samples':n,'stats':dict(stats),'survivors':survivors},indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]))
