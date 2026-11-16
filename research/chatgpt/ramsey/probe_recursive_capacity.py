from itertools import combinations
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import ramsey_37_five_way_exact_verifier as r
profiles=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(4,0)]
tables=dict(r.pair_tables())
# R(3, t-1-k) for t=7: k=1 14, k=2 9, k=3 6,k=4 3,k=5 1
bounds={1:4,2:6,3:10,4:14,5:19}

def fail(D):
    masks=[sum(1<<x for x in d) for d in D]
    sizes=[m.bit_count() for m in masks]
    for k in range(2,6):
        upper=bounds[k]
        for C in combinations(range(16),k):
            if sum(sizes[u] for u in C)<=upper:continue
            if all(masks[u]&masks[v] for u,v in combinations(C,2)):
                return k,C
    return None

cc=Counter();examples={};survivors=0
for p in profiles:
    n3,n4=p
    gen=r.low_support_cases(*p) if p in {(0,0),(1,0),(0,1)} else r.high_support_cases(n3,n4,tables[2+n3+2*n4])
    for j,(_,D) in enumerate(gen):
        v=fail(D)
        cc[(p,'total')]+=1
        cc[('all','total')]+=1
        if v:
            cc[(p,'excluded')]+=1
            cc[('all','excluded')]+=1
            cc[('all','arity_'+str(v[0]))]+=1
            examples.setdefault(v[0],(p,j,v,D))
        else: survivors+=1
        four,_=r.feasible(D,4)
        if four:
            cc[('four','total')]+=1
            if v:cc[('four','excluded')]+=1
print('COUNTS',cc)
print('survivors',survivors)
for k,(p,j,(arity,C),D) in examples.items():
 print('EXAMPLE',k,p,j,'C',C,'D',[sorted(x) for x in (D[v] for v in C)])
