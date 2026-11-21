"""Search cyclic degree <=9 graphs, testing only independent tens containing zero."""
from itertools import combinations
from ramsey_hall_center_conjecture import independent

def search(n):
    full=(1<<n)-1
    for k in range(4,-1,-1):
        for ds in combinations(range(1,(n+1)//2),k):
            # In even order the antipode is optional.
            for extra in ([(),(n//2,)] if n%2==0 else [()]):
                D=ds+extra;S=set(D)|{n-d for d in D}
                if any((a+b)%n in S for a in S for b in S):continue
                A=[sum(1<<((v+d)%n) for d in S) for v in range(n)]
                if not independent(A,full&~(A[0]|1),9):
                    assert not independent(A,full,10)
                    assert all(not A[i]&A[j] for i,j in combinations(range(n),2) if A[i]>>j&1)
                    return D,A
if __name__=='__main__':
    for n in (40,39,38,37,36):
        result=search(n);print(n,result[0] if result else 'no cyclic witness',flush=True)
        if result:break
