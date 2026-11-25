"""For fixed exclusive rows, test a necessary seven-clique among common supports."""
import json
from pathlib import Path
from ramsey310_codegree7_test import sets,F,P,gzip
from itertools import combinations

def residual(n):
    with gzip.open(P,'rb') as f:
        for _ in range(n):b=[v-63 for v in next(f).strip()]
    A=[0]*27;k=0
    for j in range(27):
        for i in range(j):
            if b[1+k//6]>>(5-k%6)&1:A[i]|=1<<j;A[j]|=1<<i
            k+=1
    return A

def kernel(A,E):
    caps=[9-a.bit_count()-sum(r>>i&1 for r in E) for i,a in enumerate(A)]
    cand=[s for s in sets(A,F,7) if all(caps[i]>0 for i in range(27) if s>>i&1)]
    strict=[]
    for k in (6,7):
        for t in sets(A,F,k):
            extra=max(sum(not r&t for r in side) for side in [E[:2],E[2:]])
            if extra+k>=8:strict.append(t)
    miss=[sum(1<<j for j,t in enumerate(strict) if not s&t) for s in cand]; adj=[0]*len(cand)
    once=sum(1<<i for i,c in enumerate(caps) if c==1)
    for j in range(len(cand)):
        for i in range(j):
            both=cand[i]&cand[j]
            if both&once or both.bit_count()>5 or miss[i]&miss[j]:continue
            adj[i]|=1<<j;adj[j]|=1<<i
    return cand,adj,len(strict)

def test(A,E):
    cand,adj,nstrict=kernel(A,E)
    # Greedy proper coloring gives an upper bound on clique size. Exact bounded search if necessary.
    def has(m,k):
        if not k:return True
        order=[];cs=[];color=0
        while m:
            color+=1;q=m
            while q:
                b=q&-q;i=b.bit_length()-1;m^=b;q &= ~b & ~adj[i];order.append(i);cs.append(color)
        m=sum(1<<i for i in order)
        for i,c in zip(reversed(order),reversed(cs)):
            if c<k:return False
            if has(m&adj[i],k-1):return True
            m^=1<<i
        return False
    sizes=[has((1<<len(cand))-1,k) for k in (6,7)]
    return len(cand),nstrict,sum(x.bit_count() for x in adj)//2,sizes
if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]/'results'
    for f in ['ramsey310_codegree7_joint.jsonl','ramsey310_codegree7_five_hits.jsonl']:
        for r in map(json.loads,(root/f).read_text().splitlines()):
            if 'rows' in r:print(f,r['record'],test(residual(r['record']),r['rows'][7:]),flush=True)
