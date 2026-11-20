"""Audit private neighbors of the four negative witnesses in every order-17 host."""
from collections import Counter
from itertools import combinations
from urllib.request import urlopen

def audit(s):
    n=s[0]-63;assert n==17
    bits=''.join(f'{c-63:06b}' for c in s[1:]);adj=[0]*n
    for j in range(n):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':adj[i]|=1<<j;adj[j]|=1<<i
    counts=Counter();doubles=Counter()
    for i,j in combinations(range(n),2):
        if not adj[i]>>j&1:continue
        for rs in combinations([v for v in range(n) if v not in (i,j) and not ((adj[i]|adj[j])>>v&1)],4):
            R=sum(1<<r for r in rs);ends=(1<<i)|(1<<j)
            if any(adj[r]&R for r in rs):continue
            groups={r:[] for r in rs}
            for v in range(n):
                if ((ends|R)>>v)&1:continue
                p=adj[v]&R;assert p
                if p.bit_count()==1:groups[p.bit_length()-1].append(v)
            for g in groups.values():
                assert len(g)<=2
                if len(g)==2:assert {adj[v]&ends for v in g}=={1<<i,1<<j}
            counts[sum(map(len,groups.values()))]+=1;doubles[sum(len(g)==2 for g in groups.values())]+=1
    return counts,doubles
if __name__=='__main__':
    a=Counter();b=Counter()
    for s in urlopen('https://users.cecs.anu.edu.au/~bdm/data/r36_17.g6',timeout=20).read().splitlines():
        x,y=audit(s);a+=x;b+=y
    print('singletons:',sorted(a.items()),'doubled witnesses:',sorted(b.items()),'reservations',sum(a.values()))
