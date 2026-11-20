"""All labelled (3,4) completions of seven consecutive positive joins; stdlib only."""
from collections import Counter
from itertools import combinations


def completions(rows=()):
    n=len(rows)
    if n==8:
        yield rows
        return
    for p in range(1<<n):
        if n and not p & (1<<(n-1)):continue
        if any(p>>i&1 and p&rows[i] for i in range(n)):continue
        neg=[i for i in range(n) if not (p>>i&1)]
        if any(not ((rows[j]>>i | rows[k]>>i | rows[k]>>j)&1) for i,j,k in combinations(neg,3)):continue
        yield from completions(rows+(p,))

if __name__=='__main__':
    cs=list(completions());print('labelled completions',len(cs));print('M14 (+ = 1)',Counter(r[3]&1 for r in cs))
    for d in range(1,8):print('distance',d,'positive counts',[sum((r[i+d]>>i)&1 for r in cs) for i in range(8-d)])
    for value in (0,1):
        r=next(r for r in cs if r[3]&1==value);print('M14',value,'extra positive links',[(i+1,j+1) for i,j in combinations(range(8),2) if j>i+1 and r[j]>>i&1])
