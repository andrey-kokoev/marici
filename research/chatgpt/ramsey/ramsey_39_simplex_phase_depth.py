"""Test a four-transfer simplex quotient (existential edge readout, not path lifting)."""
from itertools import combinations
from ramsey_hall_center_conjecture import independent
W=(0,1,8,19);M=35
def layer(n):
    for a in range(n+1):
        for b in range(n+1-a):
            for c in range(n+1-a-b):yield (a,b,c,n-a-b-c)
def phase(x):return sum(i*j for i,j in zip(x,W))%M
def test(n):
    nodes=set();edges=set();full=set()
    for x in layer(n):
        p=phase(x);nodes.add(p)
        if all(x):full.add(p)
        for i in range(4):
            if x[i]:
                y=list(x);y[i]-=1;y[(i+1)%4]+=1;q=phase(y);edges.add(tuple(sorted((p,q))))
    return nodes,edges,full
if __name__=='__main__':
    expected={(i,j) for i,j in combinations(range(M),2) if min(j-i,M+i-j) in (1,7,11,16)}
    for n in [*range(1,17),24,32]:
        v,e,f=test(n);assert e<=expected;print(n,len(v),len(e),len(f))
    A=[sum(1<<j for j in range(M) if tuple(sorted((i,j))) in expected) for i in range(M)];assert all(not A[i]&A[j] for i,j in expected) and not independent(A,(1<<M)-1,9)
