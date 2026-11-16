#!/usr/bin/env python3
"""Exact witness-polynomial identity, incidence-rank, and cloning checks.

No numerical solver, Ramsey oracle, or geometric representation needed.
"""
from collections import Counter
from itertools import combinations
from math import comb
from ramsey_symplectic_witness_audit import all_line_witness_matchings,red_graph
from ramsey_capacity_resolution_audit import support_classes

def degree_rank(rows):
    piv={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x;break
            x ^=piv[j]
    return len(piv)

def independence_polynomial(adj):
    n=len(adj);p=[0]*(n+1)
    def rec(candidates,k):
        p[k]+=1
        while candidates:
            bit=candidates&-candidates
            candidates^=bit
            v=bit.bit_length()-1
            rec(candidates&~adj[v],k+1)
    rec((1<<n)-1,0)
    return p

def rooted_witness_polynomial(adj,root=0):
    n=len(adj)
    S=[i for i in range(n) if adj[root]>>i&1]
    T=[i for i in range(n) if i!=root and not (adj[root]>>i&1)]
    assert all(not (adj[s]>>u&1) for s,u in combinations(S,2))
    d=len(S)
    sigma=[sum(1<<k for k,s in enumerate(S) if adj[t]>>s&1) for t in T]
    H=[sum(1<<j for j,u in enumerate(T) if adj[t]>>u&1) for t in T]
    # contributions to independent sets NOT using root, with exact support-union
    z=[0]*(n+1)
    def rec(candidates,size,union):
        for k in range(d-union.bit_count()+1):
            z[size+k]+=comb(d-union.bit_count(),k)
        while candidates:
            bit=candidates&-candidates
            candidates^=bit
            t=bit.bit_length()-1
            rec(candidates&~H[t],size+1,union|sigma[t])
    rec((1<<len(T))-1,0,0)
    h=independence_polynomial(H)
    for k,v in enumerate(h):
        z[k+1]+=v
    return z, S, T, sigma

def run():
    c5=[(1<<((i-1)%5))|(1<<((i+1)%5)) for i in range(5)]
    for name,graph in [('C5',c5),('22-vertex rank-18 witness',red_graph(all_line_witness_matchings()[0]))]:
        p=independence_polynomial(graph)
        q,S,T,sigma=rooted_witness_polynomial(graph)
        assert p==q
        print(name,'|S|',len(S),'|T|',len(T),'I_G',p[:9])
    # For the 15 pair witnesses of the 22-vertex graph, the 6x15 support
    # incidence has rank five: each column has exactly two entries and every
    # pair occurs once.
    graph=red_graph(all_line_witness_matchings()[0]);_,S,T,sigma=rooted_witness_polynomial(graph)
    A=[sum(1<<j for j,x in enumerate(sigma) if x>>i&1) for i in range(6)]
    assert degree_rank(A)==5
    # Every incidence support multiset surviving the necessary arithmetic
    # restrictions for the hypothetical 23-vertex configuration has rank six.
    totals=Counter()
    for r in range(5):
        reps=support_classes(r)
        for supports in reps:
            A=[sum(1<<j for j,x in enumerate(supports) if x>>i&1) for i in range(6)]
            totals[degree_rank(A)]+=1
    assert totals=={6:695}
    print('22-vertex S-to-T binary rank:',5)
    print('23-vertex hypothetical support-rank distribution:',dict(totals))
    print('Identity and rank checks passed')
if __name__=='__main__':run()
