"""Fixed shuffled orders; same four distances for seed and continuation."""
from itertools import combinations
from random import Random
from functools import lru_cache
from collections import Counter
N=35;full=(1<<N)-1

def graph(d):
    return [sum(1<<((i+s*x)%N) for x in d for s in (-1,1)) for i in range(N)]

def valid(A,P):
    def independent(p,k):
        while p.bit_count()>=k:
            b=p&-p;p^=b
            if k==1 or independent(p&~A[b.bit_length()-1],k-1):return True
        return False
    for i,a in enumerate(A):
        if P>>i&1:
            n=a&P
            while n:
                b=n&-n;n^=b
                if n&A[b.bit_length()-1]:return False
    return not independent(P,9)

def score(A,S):
    p=sum(1<<i for i in S);deg=[(A[i]&p).bit_count() for i in S];return (sum(not(A[i]>>j&1) and not(A[i]&A[j]&p) for i,j in combinations(S,2)),len(S)*sum(x*x for x in deg)-sum(deg)**2)

def main():
    graphs={d:graph(d) for d in combinations(range(1,18),4)};summary=Counter();allrate=[]
    for seed in range(20):
        order=list(range(N));Random(seed).shuffle(order);S=order[:27];p=sum(1<<i for i in S)
        pool={d:score(A,S) for d,A in graphs.items() if valid(A,p)}
        def grow(d):
            q=p
            for n,i in enumerate(order[27:],27):
                q|=1<<i
                if not valid(graphs[d],q):return n
            return 35
        picks=[min(pool,key=lambda d:(pool[d][i],d)) for i in (0,1)];ends=list(map(grow,picks));summary[(picks[0]!=picks[1],ends[0]==35,ends[1]==35)]+=1
        allrate.append(sum(grow(d)==35 for d in pool)/len(pool));print(seed,len(pool),picks,ends,flush=True)
    print(summary,'uniform-seed mean success',sum(allrate)/len(allrate))
if __name__=='__main__':main()
