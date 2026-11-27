"""Gap simplex of ordered three-red rows; distinguish count symmetry from swap symmetry."""
from itertools import combinations, permutations
from collections import Counter

def gaps(t,k):
    a,b,c=t;return a-1,b-a-2,c-b-2,k-c

def rows(k):return {gaps(t,k) for t in combinations(range(1,k+1),3) if min(t[1]-t[0],t[2]-t[1])>=2}
def views(g):
    a,b,c,d=g;return a+b-c-d,a+c-b-d,a+d-b-c

def run():
    for k in range(6,10):
        old=rows(k);new=rows(k+1);ways=Counter(tuple(v+int(i==j) for i,v in enumerate(g)) for g in old for j in range(4));assert set(ways)==new;assert len({views(g) for g in new})==len(new)
        assert all(ways[g]==sum(v>0 for v in g) for g in new)
        ds={tuple(views(tuple(int(i==j) for i in range(4)))) for j in range(4)};assert len(ds)==4
        print(k,len(old),sum(ways.values()),len(new),sorted(Counter(ways.values()).items()))
    path={frozenset((i,i+1)) for i in range(3)};print('swap-preserving gap permutations',[p for p in permutations(range(4)) if {frozenset((p[i],p[i+1])) for i in range(3)}==path]);print('four increments in three signed views',sorted(ds))
if __name__=='__main__':run()
