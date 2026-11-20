"""All prefix subsets of the eight-address cycle-plus-opposites example."""
from functools import cache
from itertools import combinations
V=range(8); full=255
A=[sum(1<<j for j in V if (i-j)%8 in (1,4,7)) for i in V]
@cache
def leaders(S):
    subs=[t for t in range(256) if not t&~S and all(not(t>>i&1 and A[i]&t) for i in V)]
    opts=[p for p in subs if all(p&t for t in subs if t.bit_count()==3)]
    negpairs=[t for t in subs if t.bit_count()==2]
    score=lambda p:sum(not(p&q) or all((p|q)&t for t in negpairs) for q in opts)
    m=max(map(score,opts));return {p for p in opts if score(p)==m}
@cache
def paths(S):
    if S==full:return 1
    return sum(paths(S|1<<i) for i in V if not S>>i&1 and A[i]&S in leaders(S))
if __name__=='__main__':
    print('paths from empty',paths(0));k=min(S.bit_count() for S in range(256) if paths(S));S=next(S for S in range(256) if S.bit_count()==k and paths(S));print('smallest successful seed', [i+1 for i in V if S>>i&1], 'paths',paths(S))
    while S!=full:
        good=[i for i in V if not S>>i&1 and A[i]&S in leaders(S) and paths(S|1<<i)];i=good[0];print('choose',i+1,'positive to',[j+1 for j in V if (A[i]&S)&(1<<j)], 'other successful choices',[x+1 for x in good[1:]]);S|=1<<i
