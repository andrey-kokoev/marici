"""Paired, reproducible 13/14 samples at depth two. SAT decisions exact; timeouts separate."""
from itertools import combinations
from collections import Counter
from random import Random
from pathlib import Path
import json,sys
from ramsey_39_twelve_order_sat import test
from ramsey_39_depth_two_edge_bound import bound
B=[bound(38-d,9) for d in range(10)]
def gate(W):
    h=Counter((a+b)%39 for a in W for b in W)
    if len(h)<39:return 'coverage',None
    cap=[min(9,2*h[p]) for p in range(39)]
    if min(cap)<3 or sum(cap)<272:return 'degree',None
    f=lambda d:2*(d*d+B[d])-39*d
    lo=[min(f(d) for d in range(3,c+1)) for c in cap];slack=-sum(lo)
    if slack<0:return 'deficiency',None
    return 'survives',[min(d for d in range(3,c+1) if f(d)-a<=slack) for c,a in zip(cap,lo)]

def run(r,n,quota):
    rng=Random(131439);seen=set();stats=Counter();results=[]
    while len(seen)<n:
        tail=rng.sample(range(39),14);W13=tuple(sorted(tail[:13]));W14=tuple(sorted(tail));key=(W13,W14)
        if key in seen:continue
        seen.add(key);W=W13 if r==13 else W14;typ,floors=gate(W);stats[typ]+=1
        if floors and len(results)<quota:
            status=test(W,degree_budget=True,degree_floors=floors,connected_ramsey=True,seconds=3);results.append((W,status))
            if status.startswith('witness'):break
    data={'r':r,'paired_draws':len(seen),'gates':stats,'order_tests':results};Path(__file__).with_name(f'ramsey_39_long_cycle_{r}.json').write_text(json.dumps(data,indent=2));print(r,stats,Counter(s for w,s in results));print('distinct SAT inputs',len(set(w for w,s in results)))
if __name__=='__main__':run(*map(int,sys.argv[1:]))
