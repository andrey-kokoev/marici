"""Three tests: induced matching surgery, joint fringe deletion, and depth-seven bottlenecks."""
from collections import Counter
from itertools import combinations,product
from pathlib import Path
import csv
from ramsey_mutual_repair_conjecture import sevens
from ramsey_hall_center_conjecture import independent
from ramsey_simplex_complement_routes import orders,layer

def surgery():
    n=38;F=(1<<n)-1;ds=(1,3,5,12,19);A=[sum(1<<u for u in {(v+sign*d)%n for d in ds for sign in (1,-1)}) for v in range(n)];E=list((a,b) for a,b in combinations(range(n),2) if A[a]>>b&1);counts=Counter();witness=None
    def extend(edges,start,forbid,S):
        nonlocal witness
        k=len(edges)
        if k>=2:
            counts[k,'tested']+=1
            if not independent(A,F^S,9):
                counts[k,'hits old nines']+=1;B=A[:]+[S]
                for a,b in edges:B[a]^=1<<b;B[b]^=1<<a;B[a]|=1<<n;B[b]|=1<<n
                if not independent(B,(1<<39)-1,10):witness=edges[:];counts[k,'valid']+=1
        if k<4:
            for j in range(start,len(E)):
                a,b=E[j];p=(1<<a)|(1<<b)
                if not p&forbid:extend(edges+[(a,b)],j+1,forbid|p|A[a]|A[b],S|p)
    for d in ds:
        p=1|(1<<d);extend([(0,d)],0,p|A[0]|A[d],p)
    print('anchored surgery (possibly repeated orbits)',counts,'witness',witness)

def fringe():
    A=[sum(int(x)<<j for j,x in enumerate(row)) for row in csv.reader(Path(__file__).with_name('ramsey_3_10_witness_39.csv').read_text().splitlines()) if row];E=[(a,b) for a,b in combinations(range(39),2) if A[a]>>b&1];F=(1<<39)-1
    def bad(D):
        B=A[:]
        for a,b in D:B[a]^=1<<b;B[b]^=1<<a
        return next(sevens(B,k=10),None)
    assert bad([]) is None
    removable=[e for e in E if bad([e]) is None];print('fringe',removable);counts=Counter();first=None
    for k in range(len(removable)+1):
        for D in combinations(removable,k):
            t=bad(D)
            if t:counts[k]+=1;first=first or (D,[v for v in range(39) if t>>v&1])
    print('failing deletions',counts,'first',first)

def depth():
    target={1,7,11,16};hist=Counter();example=None;records=[(x,i,orders(x,i)) for x in layer(7) for i in range(4) if x[i]]
    for v in product(range(35),repeat=3):
        w=(0,)+v;ds=[(w[(i+1)%4]-w[i])%35 for i in range(4)];dist=[min(d,35-d) for d in ds]
        if set(dist)!=target:continue
        best={}
        for x,i,k in records:
            p=sum(z*t for z,t in zip(w,x))%35;q=(p+ds[i])%35;e=tuple(sorted((p,q)));best[e]=max(k,best.get(e,0))
        weak=[(p,q) for p in range(35) for q in range(p+1,35) if min(q-p,35-q+p) in target and best.get((p,q),0)<2];sig=tuple(sorted(min(q-p,35-q+p) for p,q in weak));hist[sig]+=1
        if sig!=(7,) and example is None:example=(w,weak)
    print('weak distance profiles',hist,'example',example)
if __name__=='__main__':surgery();fringe();depth()
