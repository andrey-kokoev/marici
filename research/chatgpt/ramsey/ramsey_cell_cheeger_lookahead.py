"""Classify greedy failures; check exact optimum independently by common kernels."""
from itertools import combinations
from collections import Counter
from functools import reduce
from operator import xor

def main():
    free=(3,5,6,7);B=sorted(sum(1<<i for i,b in enumerate(free) if b in q) for q in combinations(range(8),4) if reduce(xor,q)==0);C=[sum(1<<i for i,b in enumerate(B) if (h&b).bit_count()%2) for h in range(1,16)];full=(1<<len(B))-1
    opt=[0]*(full+1);best=opt.copy();worst=opt.copy();fixed=opt.copy();two=opt.copy();strict=[];ex=None
    for m in range(1,full+1):
        R=[m&~c for c in C];g=min(r.bit_count() for r in R);T=[r for r in R if r.bit_count()==g];opt[m]=1+min(opt[r] for r in R if r!=m);best[m]=1+min(best[r] for r in T);worst[m]=1+max(worst[r] for r in T);fixed[m]=1+fixed[T[0]]
        score=lambda r:min((r&~c).bit_count() for c in C);h=min(T,key=score);two[m]=1+two[h];
        if all(opt[r]+1>opt[m] for r in T):strict.append(m)
        if fixed[m]>opt[m] and (ex is None or m.bit_count()<ex.bit_count()):ex=m
        # existence of one/two complementary halfspaces covering every obstruction
        exact=1 if 0 in R else 2 if any(not(r&~c) for r in R for c in C) else 3;assert exact==opt[m]
    print('fixed-label greedy misses',sum(a>b for a,b in zip(fixed,opt)),'some greedy path fails',sum(a>b for a,b in zip(worst,opt)),'all greedy paths fail',sum(a>b for a,b in zip(best,opt)),'all best first moves strictly bad',len(strict),'two-step tiebreak misses',sum(a>b for a,b in zip(two,opt)))
    m=ex;print('smallest fixed-tie failure, directions',[v for i,v in enumerate(B) if m>>i&1]);R=[m&~c for c in C];print('best first choices (bit, remaining directions, remaining bits)',[(h,[b for i,b in enumerate(B) if r>>i&1],opt[r]) for h,r in enumerate(R,1) if r.bit_count()==min(x.bit_count() for x in R)])
if __name__=='__main__':main()
