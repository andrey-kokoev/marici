#!/usr/bin/env python3
"""Exact local-sector successor audit for the seven extremal R(3,6) graphs.

Reproduction: python ramsey_forced_sector_successor_2026-11-08.py
Requires networkx. Source graph6 data: Brendan McKay's Ramsey graph catalogue,
https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

No target graph or Ramsey threshold for k=7 is used to select attachments.
All computations use exact integer bitsets, plus graph isomorphism for the
unique 13-vertex residual core.
"""
from itertools import combinations
from collections import Counter
import networkx as nx

G13_G6 = 'Ls`?XGRQR@B`Kc'
G17_G6 = [
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
]
G13=nx.from_graph6_bytes(G13_G6.encode())

def masks(g):
    return [sum(1<<j for j in g.neighbors(v)) for v in range(g.number_of_nodes())]

def is_ind(a,m):
    r=m
    while r:
        b=r&-r; v=b.bit_length()-1; r^=b
        if a[v]&r: return False
    return True

def independence_dp(a):
    dp=bytearray(1<<len(a))
    for m in range(1,len(dp)):
        b=m&-m; v=b.bit_length()-1; t=m^b
        dp[m]=max(dp[t],1+dp[t&~a[v]])
    return dp

def bits(m):
    return tuple(v for v in range(m.bit_length()) if m>>v&1)

def independent_masks_on(a,vertices):
    sets=[0]
    for v in vertices:
        sets += [s|(1<<v) for s in sets if not (a[v]&s)]
    return sets

def core_four_cycles(g):
    n=g.number_of_nodes()
    for quad in combinations(range(n),4):
        sub=g.subgraph(quad)
        if sub.number_of_edges()!=4 or not all(d==2 for _,d in sub.degree()):continue
        core=g.subgraph([v for v in range(n) if v not in quad])
        if nx.is_isomorphic(core,G13):yield quad

def extend_pair(a,P,Q):
    n=len(a);r=a[:]+[0,0]
    for j,ss in enumerate((P,Q)):
        for v in bits(ss):
            r[n+j]|=1<<v
            r[v]|=1<<(n+j)
    return r

def expected_family(a,core,a_vertex,b_vertex):
    return {(1<<a_vertex)|(1<<b_vertex)|u for u in independent_masks_on(a,core)}

def actual_family(a,k):
    dp=independence_dp(a)
    full=(1<<len(a))-1
    return {s for s in independent_masks_on(a,range(len(a)))
            if dp[full&~s]<=k-2}

def maxind_exact(a):
    best=0;stack=[((1<<len(a))-1,0)]
    while stack:
        available,count=stack.pop()
        if count+available.bit_count()<=best:continue
        if not available:best=max(best,count);continue
        b=available&-available;v=b.bit_length()-1;t=available^b
        stack.append((t,count));stack.append((t&~a[v],count+1))
    return best

records=[]
for graph_ix, g6 in enumerate(G17_G6,1):
    g=nx.from_graph6_bytes(g6.encode())
    a=masks(g);dp=independence_dp(a);full=(1<<17)-1
    assert len(a)==17 and dp[full]==5
    assert all(is_ind(a,a[v]) for v in range(17))
    # All allowed first neighborhoods at k=7, and the terminal k=6 property.
    all_ind=independent_masks_on(a,range(17))
    assert all(dp[full&~s]==5 for s in all_ind)
    # Determine minimal blue pair support without assuming a C4.
    min_weight=999; minimal=[]
    for i,S in enumerate(all_ind):
        for U in all_ind[i:]:
            weight=S.bit_count()+U.bit_count()
            if weight>min_weight:continue
            if dp[full&~(S|U)]>4:continue
            if weight<min_weight:minimal=[];min_weight=weight
            minimal.append((S,U))
    assert min_weight==4
    # Every minimum blue pair is exactly the opposite partition of a C4.
    quads=list(core_four_cycles(g))
    expected_min=[]
    for quad in quads:
        opp=[sum(1<<v for v in ab) for ab in combinations(quad,2) if not g.has_edge(*ab)]
        assert len(opp)==2
        expected_min.append(frozenset(opp))
    assert {frozenset(pair) for pair in minimal}==set(expected_min)
    assert len(minimal)==len(quads)
    for quad in quads:
        opp=[sum(1<<v for v in ab) for ab in combinations(quad,2) if not g.has_edge(*ab)]
        assert len(opp)==2 and (opp[0]&opp[1])==0
        old19=extend_pair(a,*opp)
        assert maxind_exact(old19)==6
        core=sorted(set(range(17))-set(quad))
        expected=expected_family(a,core,17,18)
        observed=actual_family(old19,7)
        assert observed==expected and len(observed)==183
        sizes=Counter(s.bit_count() for s in observed)
        assert sizes=={2:1,3:13,4:52,5:78,6:39}
        max4=[s for s in independent_masks_on(a,core) if s.bit_count()==4]
        assert len(max4)==39
        pair_edges={(i,j) for i,j in combinations(range(39),2)
                    if dp[full&~(max4[i]|max4[j])]<=4}
        pair_triangles={tuple(t) for t in combinations(range(39),3)
                        if all((i,j) in pair_edges for i,j in combinations(t,2))}
        good_triangles={t for t in pair_triangles
                        if dp[full&~(max4[t[0]]|max4[t[1]]|max4[t[2]])]<=3}
        assert pair_triangles==good_triangles
        assert len(good_triangles) in (0,4)
        if good_triangles:
            common=set.intersection(*(set(t) for t in good_triangles))
            assert len(common)==1
            outside=set.union(*(set(t) for t in good_triangles))-common
            assert len(outside)==4
            square=nx.Graph()
            square.add_nodes_from(outside)
            for t in good_triangles:
                y=tuple(set(t)-common)
                assert len(y)==2
                square.add_edge(*y)
            assert nx.is_isomorphic(square,nx.cycle_graph(4))
            # Construct one 22-vertex witness from the source-generated triple.
            trio=next(iter(good_triangles))
            h=old19[:]+[0]*3
            for j,t in enumerate(trio):
                u=max4[t]
                v=19+j
                neighborhood=u|(1<<17)|(1<<18)
                for z in bits(neighborhood):
                    h[v]|=1<<z;h[z]|=1<<v
            assert all(is_ind(h,h[v]) for v in range(22))
            assert maxind_exact(h)==6
        # With no four mutually compatible triples, no fourth right-side
        # vertex can ever be added to an admissible continuation.
        for tri in good_triangles:
            for v in range(39):
                if v in tri:continue
                tet=tuple(sorted((*tri,v)))
                assert not all(tuple(sorted(t)) in good_triangles
                               for t in combinations(tet,3))
        records.append((graph_ix,tuple(quad),len(pair_edges),len(good_triangles)))
    print(f'graph {graph_ix}: independent neighborhoods={len(all_ind)}; '
          f'min-blue-pair C4s={len(quads)}; '
          f'compatible triple counts={[r[3] for r in records if r[0]==graph_ix]}')

assert len(records)==14
assert sum(t>0 for _,_,_,t in records)==10
assert sum(t==0 for _,_,_,t in records)==4
print('All 14 source-local decompositions checked; 10 reach 22, 4 stop at 21.')
print('All successful triple systems have four 2x2-grid faces, none extends to a fourth right vertex.')

# Two independently published 22-vertex extremal graphs rule out a universal
# 17-core + K_{2,3} decomposition. They are records #2 and #9 in the first 20
# graph6 rows of McKay's 191-graph 22-vertex catalogue.
EXCEPTIONAL_22 = [
    ('catalog #2', 'U???GOWH@CAGn?O{hBbHGTQ@y?CHWKSgQPWOgwG?', 6),
    ('catalog #9', 'U???OGPGhwEWI?D?gXKESQDUCedPAAgcFXO?xg??', 5),
]
for label,g6,min_expected in EXCEPTIONAL_22:
    g=nx.from_graph6_bytes(g6.encode())
    a=masks(g)
    assert len(a)==22 and maxind_exact(a)==6
    assert all(is_ind(a,a[v]) for v in range(22))
    # The minimum blue-pair support is the smallest bipartite vertex set that
    # intersects all maximum independent six-sets. Bipartite parts are the
    # two independent red neighborhoods of the new blue-adjacent pair.
    MIS=[sum(1<<v for v in t) for t in combinations(range(22),6)
         if is_ind(a,sum(1<<v for v in t))]
    hit=[sum(1<<j for j,I in enumerate(MIS) if I>>v&1) for v in range(22)]
    every=(1<<len(MIS))-1
    minima=[]
    for m in range(1,7):
        for quad in combinations(range(22),m):
            covered=0
            for v in quad:covered|=hit[v]
            if covered!=every:continue
            if nx.is_bipartite(g.subgraph(quad)):minima.append(quad)
        if minima:break
    assert m==min_expected
    # Every possible induced red K_{2,3} is checked; none has an extremal
    # 17-vertex residual core. This is a complete finite counterexample to
    # universality of that specific deletion/attachment shape.
    count_k23=0;count_core=0
    cores=[nx.from_graph6_bytes(g6.encode()) for g6 in G17_G6]
    for five in combinations(range(22),5):
        sub=g.subgraph(five)
        if sub.number_of_edges()!=6 or sorted(d for _,d in sub.degree())!=[2,2,2,3,3]:
            continue
        count_k23+=1
        residual=g.subgraph([v for v in range(22) if v not in five])
        if any(nx.is_isomorphic(residual,parent) for parent in cores):count_core+=1
    assert count_core==0
    print(f'exception {label}: minimum blue-pair support {m}; '
          f'induced K2,3 = {count_k23}; residual 17-extremal cores = 0')
