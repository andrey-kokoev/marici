"""Exact hidden-c-parity phase search. State masks store *linear* phases split by parity."""
from itertools import product
from math import gcd
from collections import Counter
from pathlib import Path
import json
from ramsey_hall_center_conjecture import independent
M=39;F=(1<<M)-1
def rot(m,k):
    k%=M;return (m<<k|m>>(M-k))&F

def trial(w,d):
    S=[1,0];moves=[]
    for i in range(4):
        for p in range(2):
            j=(i+1)%4; a=w[i]+d*(p^(i==2));b=w[j]+d*(p^(j==2));moves.append((p,a,(b-a)%M))
    # A triangle at any three specific phases persists at larger depths (pad coordinate 0).
    A=[0]*M;prev=[0,0];full=False
    for n in range(1,33):
        N=[S[p]|rot(S[p],w[1])|rot(S[1-p],w[2])|rot(S[p],w[3]) for p in range(2)]
        diff=[S[p]&~prev[p] for p in range(2)]
        for p,a,k in moves:
            if not k:continue
            starts=rot(diff[p],a)
            while starts:
                h=starts&-starts;starts-=h;u=h.bit_length()-1;v=(u+k)%M
                if A[u]&A[v]:return 'triangle',n
                A[u]|=1<<v;A[v]|=h
        if (N[0]|rot(N[1],d))==F:
            full=True
            if not independent(A,F,10):return 'witness',n
        if N==S:break
        prev,S=S,N
    return ('independent ten' if full else 'incomplete'),n

def run():
    counts=Counter();classes=0
    # Quotient only by common unit multiplication. First normalize the weights,
    # then delta under their stabilizer. No coordinate symmetry assumed.
    units=[u for u in range(1,M) if gcd(u,M)==1];seen=set()
    for v in product(range(M),repeat=3):
        if v in seen:continue
        orb={tuple(u*z%M for z in v) for u in units};seen.update(orb);stab=[u for u in units if all((u-1)*z%M==0 for z in v)];ds=set()
        for d in range(M):
            if d in ds:continue
            do={d*u%M for u in stab};ds.update(do);key,n=trial((0,)+v,d);classes+=1;counts[key]+=len(orb)*len(do)
            if key=='witness':print(v,d,n,flush=True);return
    assert sum(counts.values())==M**4;print(classes,counts);Path(__file__).with_suffix('.json').write_text(json.dumps(dict(counts))+'\n')
if __name__=='__main__':run()
