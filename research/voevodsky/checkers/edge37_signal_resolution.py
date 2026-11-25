"""Earliest move with both directions implied, with a fixed gap for each implied, or with both gaps directly read. Use only count-law completions of the alternating probe prefix."""
from itertools import combinations
from collections import Counter
words=[sum(1<<i for i in a) for a in combinations(range(10),3)]
order=[0,9,1,8,2,7,3,6,4,5]
def gaps(w):return ((~w & (w>>1))&511,(w & ~(w>>1))&511)
sign={w:gaps(w) for w in words};hist=[Counter() for _ in range(3)];ex={};allgap=511
for w in words:
    if not all(sign[w]):continue
    seen=0;times=[None]*3
    for t,i in enumerate(order,1):
        seen|=1<<i; pool=[v for v in words if not ((v^w)&seen)]
        common=[allgap,allgap]
        for v in pool:
            for j in range(2):common[j]&=sign[v][j]
        tested=seen&(seen>>1)
        for j,flag in enumerate([all(all(sign[v]) for v in pool),all(common),all(g&tested for g in sign[w])]):
            if flag and times[j] is None:times[j]=t
    assert times[0]<=times[1]<=times[2];ex.setdefault(tuple(times),w)
    for h,t in zip(hist,times):h[t]+=1
print([sorted(h.items()) for h in hist]);print([(k,format(v,'010b')[::-1]) for k,v in ex.items() if k[0]<k[1]<k[2]][:6]);print('distinct second-third',sum(1 for k in ex if k[1]!=k[2]))
