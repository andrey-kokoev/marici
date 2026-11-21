"""Test five-coordinate transport, singleton replacement, and minimal fringe obstructions."""
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import csv
from ramsey_mutual_repair_conjecture import sevens
D=(-1,3,5,12,19);M=38
@lru_cache(None)
def choices(n):
    rows=[]
    for xs in combinations_with_replacement(range(5),n):
        x=[xs.count(j) for j in range(5)]
        for i in set(xs):
            count=0
            for order in permutations(j for j in range(5) if j!=i):
                y=x[:]
                for j in order:
                    a=(j+1)%5
                    if not y[a]:break
                    y[a]-=1;y[j]+=1
                else:count+=1
                if count==2:break
            assert count;rows.append((x,i,count))
    return rows

def transfer():
    hist=Counter();examples={}
    for tail in permutations(D[1:]): # quotient cyclic reindexing by fixing -1 first
        ds=(-1,)+tail;w=[sum(ds[:i])%M for i in range(5)]
        for n in range(1,M+1):
            best={}
            for x,i,k in choices(n):
                p=sum(a*b for a,b in zip(w,x))%M;q=(p+ds[i])%M;e=tuple(sorted((p,q)));best[e]=max(k,best.get(e,0))
            if len(best)==171:break
        weak=[e for e,k in best.items() if k==1];sig=tuple(sorted(Counter(min(b-a,M+a-b) for a,b in weak).items()));hist[n,sig]+=1;examples.setdefault((n,sig),(ds,weak[:4]))
    print('depth and (distance,count) profiles:',hist);print('examples:',examples)

def replacement():
    A=[sum(1<<u for u in {(v+s*d)%M for s in (-1,1) for d in D}) for v in range(M)];single=[I for I in sevens(A,(1<<M)-2,9) if (I&A[0]).bit_count()==1];print('singleton obstructions',len(single),'example',[v for v in range(M) if single[0]>>v&1],'only blocker',(single[0]&A[0]).bit_length()-1)

def fringe():
    A=[sum(int(x)<<j for j,x in enumerate(row)) for row in csv.reader(Path(__file__).with_name('ramsey_3_10_witness_39.csv').read_text().splitlines()) if row];E=[(i,j) for i,j in combinations(range(39),2) if A[i]>>j&1]
    def witness(sub):
        B=A[:]
        for a,b in sub:B[a]^=1<<b;B[b]^=1<<a
        return next(sevens(B,k=10),None)
    R=[e for e in E if witness([e]) is None];minimal=[];bad=0
    for k in range(8):
        for sub in combinations(R,k):
            I=witness(sub);pred=any(set(c)<=set(sub) for c in minimal)
            assert not pred or I
            if I:
                bad+=1
                if not pred:minimal.append(sub);print('minimal',sub,[v for v in range(39) if I>>v&1])
    print('unsafe',bad,'of',2**len(R))
if __name__=='__main__':transfer();replacement();fringe()
