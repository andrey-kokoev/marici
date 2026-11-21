"""Exhaust linear Z/39 phase weights, testing every partially filled layer of the four-transfer readout."""
from itertools import product,combinations
from math import gcd
from collections import Counter
import json
from pathlib import Path
from ramsey_hall_center_conjecture import independent
M=39;F=(1<<M)-1;units=[i for i in range(M) if gcd(i,M)==1]
def rot(m,k):return ((m<<k)|(m>>(M-k)))&F

def orbit(w):
    for z in (w,w[::-1]):
        for j in range(4):
            v=z[j:]+z[:j]
            for u in units:yield tuple((u*(a-v[0]))%M for a in v)

def adjacency(w,S):
    A=[0]*M
    for i,a in enumerate(w):
        b=w[(i+1)%4]
        if a==b:continue  # permissive: discard loops
        m=S
        while m:
            h=m&-m;m-=h;k=h.bit_length()-1;p=(k+a)%M;q=(k+b)%M;A[p]|=1<<q;A[q]|=1<<p
    return A

def run():
    seen=set();counts=Counter();weighted=Counter();best=0;examples=[];transient=0
    for v in product(range(M),repeat=3):
        w=(0,)+v
        if w in seen:continue
        orb=set(orbit(w));seen.update(orb);weight=len(orb)
        if gcd(M,*v)!=1:weighted['unreachable']+=weight;continue
        S=1;n=0;latest=None
        while True:
            n+=1;nextS=S|rot(S,v[0])|rot(S,v[1])|rot(S,v[2])
            if nextS==F:
                A=adjacency(w,S);tri=any(A[p]&A[q] for p,q in combinations(range(M),2) if A[p]>>q&1)
                if tri:
                    if latest is not None:transient+=weight
                    break
                latest=(n,A)
            if nextS==S:break
            S=nextS
        # Edge sets grow. Only the last full-vertex triangle-free layer needs an independence test.
        if latest is None:key='triangle by first full-vertex layer'
        else:
            n,A=latest;key='independent ten' if independent(A,F,10) else 'witness'
            if key=='witness':examples.append((w,n))
            best=max(best,sum(m.bit_count() for m in A)//2)
        counts[key]+=1;weighted[key]+=weight
    assert len(seen)==M**3 and sum(weighted.values())==M**3
    report={'modulus':M,'normalized_weight_counts':dict(weighted),'generating_orbit_counts':dict(counts),'max_triangle_free_edges_at_full_coverage':best,'triangle_free_at_coverage_but_triangle_later':transient,'witnesses':examples};print(report);Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':run()
