"""Realize the eight distinct binary types on three terms, pairwise and jointly."""
from itertools import combinations
from collections import Counter

def audit():
    types=range(8);pairs=list(combinations(types,2));free=[(p,q) for p,q in pairs if not p&q]
    # The 111 column forces the three old terms to have only negative mutual links.
    # Bitset of positive graph neighbors on the 11 distinct addresses.
    adj=[0]*11
    for p in types:
        for i in range(3):
            if p>>i&1:adj[i]|=1<<(3+p);adj[3+p]|=1<<i
    octets=[sum(1<<i for i in t) for t in combinations(range(11),8) if all(not(adj[i]>>j&1) for i,j in combinations(t,2))]
    hits=[sum(1<<j for j,(p,q) in enumerate(free) if m>>(3+p)&m>>(3+q)&1) for m in octets]
    tr=[]
    for t in combinations(types,3):
        es=list(combinations(t,2))
        if all(e in free for e in es):tr.append(sum(1<<free.index(e) for e in es))
    sols=[m for m in range(1<<len(free)) if all(m&h for h in hits) and not any(m&t==t for t in tr)]
    print('forced negative, free in pairs, solutions',len(pairs)-len(free),len(free),len(sols));print('possible signs across joint solutions',Counter(len({(m>>i)&1 for m in sols}) for i in range(len(free))));print('one-edge solutions', [free[m.bit_length()-1] for m in sols if m.bit_count()==1]);print('minimum',min(m.bit_count() for m in sols))
if __name__=='__main__':audit()
