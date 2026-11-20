"""Joint erase/refill at fixed labels for every r37_22 graph6 record."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from functools import lru_cache
E=list(combinations(range(22),2));ALL=(1<<22)-1

def cliques(adj,k):
    def rec(m,s,k):
        if not k:yield s;return
        while m.bit_count()>=k:
            b=m&-m;m^=b;yield from rec(m&adj[b.bit_length()-1],s|b,k-1)
    yield from rec(ALL,0,k)

def audit(line):
    assert line[0]==85
    bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':N[i]|=1<<j;N[j]|=1<<i
    B=[ALL^r^(1<<i) for i,r in enumerate(N)];assert not any(cliques(N,3)) and not any(cliques(B,7))
    five=list(cliques(B,5));F=[(i,j) for i,j in E if not N[i]&N[j] and not any(s&(B[i]&B[j])==s for s in five if not s&((1<<i)|(1<<j)))]
    clauses=[]
    for adj,k in [(N,3),(B,7)]:
        a=adj[:]
        for i,j in F:a[i]|=1<<j;a[j]|=1<<i
        masks={sum(1<<h for h,(i,j) in enumerate(F) if s>>i&s>>j&1) for s in cliques(a,k)};assert 0 not in masks
        clauses.append(tuple(sorted(m for m in masks if not any(t!=m and t&m==t for t in masks))))
    @lru_cache(None)
    def count(n,R,B):
        if 0 in R or 0 in B:return 0
        if not R and not B:return 1<<n
        return count(n-1,tuple(m>>1 for m in R),tuple(m>>1 for m in B if not m&1))+count(n-1,tuple(m>>1 for m in R if not m&1),tuple(m>>1 for m in B))
    ways=count(len(F),*clauses);return len(F),ways,tuple(tuple(sorted(m.bit_count() for m in side)) for side in clauses)
if __name__=='__main__':
    rows=[audit(line) for line in Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines()];print('records',len(rows),'free range',min(r[0] for r in rows),max(r[0] for r in rows),'ways range',min(r[1] for r in rows),max(r[1] for r in rows));print('restricted',sum(w!=1<<f for f,w,c in rows),'higher',sum(any(k>2 for a in c for k in a) for f,w,c in rows));print('first',rows[0]);print('first higher',next(((i+1,r) for i,r in enumerate(rows) if any(k>2 for a in r[2] for k in a)),None))
