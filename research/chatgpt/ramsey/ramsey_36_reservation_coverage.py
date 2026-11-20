"""Which signs in each order-17 host are forced by the other signs?"""
from urllib.request import urlopen
from itertools import combinations
from collections import Counter

def audit(s):
    n=s[0]-63; assert n==17
    bits=''.join(f'{c-63:06b}' for c in s[1:]);edges=list(combinations(range(n),2));pos={(i,j) for i,j in edges if bits[j*(j-1)//2+i]=='1'}
    def inside(S):return set(combinations(sorted(S),2))&pos
    assert all(len(inside(t))<3 for t in combinations(range(n),3))
    witnesses=Counter()
    for six in combinations(range(n),6):
        p=inside(six);assert p
        if len(p)==1:witnesses[next(iter(p))]+=1
    neg=set(edges)-pos
    forced_neg=sum(any({tuple(sorted((i,v))),tuple(sorted((j,v)))}<=pos for v in range(n) if v not in (i,j)) for i,j in neg)
    print(len(pos),len(witnesses),sum(witnesses.values()),len(neg),forced_neg)

if __name__=='__main__':
    for g in urlopen('https://users.cecs.anu.edu.au/~bdm/data/r36_17.g6',timeout=20).read().splitlines():audit(g)
