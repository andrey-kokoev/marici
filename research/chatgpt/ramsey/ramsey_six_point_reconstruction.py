"""Enumerate six-point wirings from perfect matchings; quotient by S6."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
from ramsey_hall_center_conjecture import decode, independent

pairs=list(combinations(range(6),2))
def disjoint(i,j): return not set(pairs[i]) & set(pairs[j])
edges=[(i,j) for i,j in combinations(range(15),2) if disjoint(i,j)]
tri=[t for t in combinations(range(15),3) if all(disjoint(i,j) for i,j in combinations(t,2))]
choices=[[(i,j,1<<edges.index((i,j))) for i,j in combinations(t,2)] for t in tri]
remaining=[[sum(v in t for t in tri[k:]) for v in range(15)] for k in range(16)]

def wirings(k,mask,deg):
    if k==15:
        yield mask;return
    for i,j,b in choices[k]:
        deg[i]+=1;deg[j]+=1
        if all(d<=2<=d+r for d,r in zip(deg,remaining[k+1])):
            yield from wirings(k+1,mask|b,deg)
        deg[i]-=1;deg[j]-=1

def graph(mask):
    A=[0]*22
    def add(i,j): A[i]|=1<<j;A[j]|=1<<i
    for i in range(6):add(0,i+1)
    for k,p in enumerate(pairs):
        for i in p:add(i+1,k+7)
    for k,(i,j) in enumerate(edges):
        if not mask>>k&1:add(i+7,j+7)
    return A

if __name__=='__main__':
    maps=[]
    for p in permutations(range(6)):
        q=[pairs.index(tuple(sorted((p[i],p[j])))) for i,j in pairs];maps.append([1<<edges.index(tuple(sorted((q[i],q[j])))) for i,j in edges])
    unseen=set(wirings(0,0,[0]*15));print('labelled triangle-free regular',len(unseen));counts=Counter();valid=[]
    while unseen:
        m=min(unseen);bits=[i for i in range(45) if m>>i&1];orbit={sum(p[i] for i in bits) for p in maps};assert orbit<=unseen;unseen-=orbit
        good=not independent(graph(m),(1<<22)-1,7);counts[good]+=1
        if good:valid.append(orbit);print('valid representative omitted mask',hex(m),'orbit size',len(orbit))
    print('orbit counts',counts)
    # Only now compare to Hall191, allowing arbitrary names for its six points.
    H=decode((Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[190]);N=[i for i in range(22) if H[0]>>i&1];L=[next(v for v in range(1,22) if v not in N and H[v]&H[0]==(1<<N[i]|1<<N[j])) for i,j in pairs];m=sum(1<<k for k,(i,j) in enumerate(edges) if not H[L[i]]>>L[j]&1);print('Hall191 matches valid orbit(s)',[i for i,o in enumerate(valid) if m in o])
