#!/usr/bin/env python3
"""Construct all 288 six-direction incidence transversals and verify R(3,7) witnesses.

The 15x15 bipartite graph has a quartet node for each 4-subset of six
positions and a syntheme node for each partition into three disjoint pairs.
An edge corresponds to one disjoint-pair adjacency in KG(6,2).
Every perfect matching selects an exact triangle/quartet transversal.

Standard library only. Constructs witnesses for R(3,7)>22; does NOT prove
R(3,7)<=23 or derive a Golay 2048-cycle.
"""
from collections import Counter
from itertools import combinations, permutations
from functools import lru_cache

X=tuple(range(6))
D=tuple(map(frozenset,combinations(X,2)))    # 15 duads
Q=tuple(map(frozenset,combinations(X,4)))    # 15 quartets
KG_EDGES=tuple((i,j) for i,j in combinations(range(15),2) if not(D[i]&D[j]))
M=tuple(frozenset(t) for t in combinations(range(15),3)
        if len(set().union(*(D[j] for j in t)))==6)  # 15 synthemes
D_INDEX={p:i for i,p in enumerate(D)}
assert len(D)==len(Q)==len(M)==15 and len(KG_EDGES)==45

# For each quartet, three choices of a syntheme and one KG(6,2) edge.
OPTIONS=[]
for quartet in Q:
    opts=[]
    for edge in KG_EDGES:
        i,j=edge
        if (D[i]|D[j])==quartet:
            syntheme=next(k for k,s in enumerate(M) if i in s and j in s)
            opts.append((syntheme,edge))
    assert len(opts)==3
    OPTIONS.append(opts)
assert Counter(m for opts in OPTIONS for m,e in opts)==Counter({j:3 for j in range(15)})


def gf2rank(rows):
    basis={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i in basis:row ^= basis[i]
            else:basis[i]=row;break
    return len(basis)


def enumerate_transversals():
    def dfs(q,used,selected):
        if q==15:
            assert used==(1<<15)-1
            yield tuple(selected)
            return
        for m,e in OPTIONS[q]:
            if not (used>>m)&1:
                selected.append(e)
                yield from dfs(q+1,used|1<<m,selected)
                selected.pop()
    yield from dfs(0,0,[])


def cycle_type(deleted):
    N=[[] for _ in range(15)]
    for i,j in deleted:N[i].append(j);N[j].append(i)
    assert all(len(n)==2 for n in N)
    sizes=[];seen=set()
    for i in range(15):
        if i in seen:continue
        stack=[i];seen.add(i);size=0
        while stack:
            v=stack.pop();size+=1
            for w in N[v]:
                if w not in seen:seen.add(w);stack.append(w)
        sizes.append(size)
    return tuple(sorted(sizes))


def graph(deleted):
    A=[0]*22
    def edge(i,j):A[i] |=1<<j;A[j] |=1<<i
    for i in range(6):edge(0,1+i)
    for j,d in enumerate(D):
        for i in d:edge(1+i,7+j)
    missing={frozenset(e) for e in deleted}
    for i,j in KG_EDGES:
        if frozenset((i,j)) not in missing:edge(7+i,7+j)
    return A


def alpha(A):
    @lru_cache(None)
    def recur(bits):
        if not bits:return 0
        b=bits&-bits;i=b.bit_length()-1
        return max(recur(bits^b), 1+recur((bits^b)&~A[i]))
    return recur((1<<len(A))-1)


def trianglefree(A):
    return all(not (A[i]&A[j]) for i in range(len(A))
               for j in range(i+1,len(A)) if (A[i]>>j)&1)


def symmetric_orbit(deleted):
    result=set()
    for perm in permutations(X):
        pi=[D_INDEX[frozenset(perm[i] for i in d)] for d in D]
        image=frozenset(frozenset((pi[i],pi[j])) for i,j in deleted)
        result.add(image)
    return len(result)


def main():
    rows=[sum(1<<m for m,e in opts) for opts in OPTIONS]
    assert gf2rank(rows)==10
    counts=Counter();representatives={};total=0
    for deleted in enumerate_transversals():
        total+=1
        # These properties are forced by the exact transversal constraints.
        degree=Counter(i for e in deleted for i in e)
        assert sorted(degree.values())==[2]*15
        assert len({D[i]|D[j] for i,j in deleted})==15
        assert len({next(k for k,s in enumerate(M) if i in s and j in s)
                    for i,j in deleted})==15
        typ=cycle_type(deleted)
        counts[typ]+=1
        representatives.setdefault(typ,deleted)
    assert total==288 and counts==Counter({(15,):144,(5,10):144})
    for typ, deleted in representatives.items():
        A=graph(deleted)
        assert all(a.bit_count()==6 for a in A)
        assert sum(a.bit_count() for a in A)//2 ==66
        assert trianglefree(A)
        assert alpha(A)==6
        assert symmetric_orbit(deleted)==144
        print('cycle type:',typ,'S6 orbit: 144', 'n=22, edges=66, alpha=6')
    print('quartet-syntheme incidence GF(2) rank:',gf2rank(rows),'(not 11)')
    print('perfect matchings:',total,'type counts:',dict(counts))
    print('PASS')

if __name__=='__main__':main()
