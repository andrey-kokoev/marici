#!/usr/bin/env python3
"""Exact Ramsey(3,7) five-vertex successor test from all seven 17-vertex parents.

Inputs: seven labelled 17-vertex triangle-free graphs (graph6), alpha=5.
No 22-vertex target graph, target edge count, initial C4 shape, or seed
automorphism enters the conditional K2,t search. The K2,t search itself
restricts the internal five-vertex pattern, so it is NOT a complete search
over unrestricted five-vertex extensions. A separately found non-K2,3
extension is certified below by a full 1024-pattern internal coloring test.

Search protocol:
  * All independent red neighborhoods S,T with total cost <=5, where the
    first two new vertices are blue-adjacent and their pair is valid at k=7.
  * For each pair, derive the maximal permissible next neighborhoods.
  * Seek three jointly compatible right neighborhoods, with no specified
    individual neighborhood labels or sizes, CONDITIONAL on K2,t structure. An independent U is extended to an inclusion-maximal
    independent subset of the residual graph without harming validity;
    searching maximal U is therefore complete for K2,3 continuations.
  * Construct and verify resulting 22-vertex adjacency matrices independently.

The additional no-shape finite MILP tests confirming that selected pairs FORCE
K2,3 are in ramsey_unrestricted_pair_extension_tmp.py, and the core theorem
for all minimum-cost C4 pairs is in ramsey_forced_sector_successor_2026-11-08.py.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import networkx as nx

G17_G6 = [
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
]


def bitset(vertices):
    return sum(1 << v for v in vertices)


def bitvertices(s):
    while s:
        b = s & -s
        yield b.bit_length()-1
        s ^= b


def alpha_table(a):
    dp = bytearray(1 << len(a))
    for mask in range(1, 1 << len(a)):
        b = mask & -mask
        v = b.bit_length()-1
        rem = mask ^ b
        dp[mask] = max(dp[rem], 1 + dp[rem & ~a[v]])
    return dp


def independent_masks(a):
    items = [0]
    for v in range(len(a)):
        items += [m | (1 << v) for m in items if not (a[v] & m)]
    return items


def exact_alpha(a):
    best = 0
    stack = [((1 << len(a))-1, 0)]
    while stack:
        avail, cnt = stack.pop()
        if cnt + avail.bit_count() <= best:
            continue
        if not avail:
            best = max(best,cnt)
            continue
        b=avail&-avail
        v=b.bit_length()-1
        rem=avail^b
        stack.append((rem,cnt))
        stack.append((rem&~a[v],cnt+1))
    return best


def verify_graph(a, alpha_expected):
    assert all((a[u] >> u & 1) == 0 for u in range(len(a)))
    assert all((a[u] >> v & 1) == (a[v] >> u & 1)
               for u in range(len(a)) for v in range(u+1,len(a)))
    assert all((a[u] & a[v]) == 0 for u in range(len(a))
               for v in bitvertices(a[u]) if u < v)
    assert exact_alpha(a) == alpha_expected


def attach(a, neighborhoods, internal_edges):
    n=len(a)
    m=len(neighborhoods)
    h=a[:]+[0]*m
    for t,S in enumerate(neighborhoods):
        for v in bitvertices(S):
            h[n+t] |= 1 << v
            h[v] |= 1 << (n+t)
    for i,j in internal_edges:
        h[n+i] |= 1 << (n+j)
        h[n+j] |= 1 << (n+i)
    return h


def pair_candidates(a, dp, max_cost):
    n=len(a); full=(1<<n)-1
    inds=[s for s in independent_masks(a) if s.bit_count()<=max_cost]
    for j,S in enumerate(inds):
        for T in inds[j:]:
            c=S.bit_count()+T.bit_count()
            if c<=max_cost and dp[full&~(S|T)]<=4:
                yield c,S,T


def matching_right_triple(a,g,dp,S,T):
    """Exact K2,3 completion test by maximal residual independent sets.

    For a fixed blue pair a,b, all right vertices are red to both a and b.
    Then their neighborhoods must be independent in C=G-(S union T), and
    pair/triple independent-capacity tests are necessary and sufficient.
    """
    n=len(a); full=(1<<n)-1
    residual=[v for v in range(n) if not ((S|T)>>v & 1)]
    C=g.subgraph(residual)
    U=[bitset(clique) for clique in nx.find_cliques(nx.complement(C))]
    adjacency=[set() for _ in U]
    for i,j in combinations(range(len(U)),2):
        if dp[full&~(U[i]|U[j])] <= 4:
            adjacency[i].add(j)
            adjacency[j].add(i)
    edges=sum(map(len,adjacency))//2
    triangles=0
    good=[]
    for i in range(len(U)):
        for j in sorted(v for v in adjacency[i] if v>i):
            for t in sorted(v for v in adjacency[i]&adjacency[j] if v>j):
                triangles += 1
                if dp[full&~(U[i]|U[j]|U[t])] <= 3:
                    good.append((U[i],U[j],U[t]))
    return residual, U, edges, triangles, good


def full_extension_family(a,S,T):
    """Determine EXACT valid next neighborhoods after the two blue additions."""
    H=attach(a, (S,T), ())
    dp=alpha_table(H)
    full=(1<<len(H))-1
    return H,{U for U in independent_masks(H) if dp[full&~U]<=5}


def run():
    results=[]
    C4leaf=nx.cycle_graph(4)
    C4leaf.add_edge(0,4)
    for idx,g6 in enumerate(G17_G6,1):
        G=nx.from_graph6_bytes(g6.encode()); a=[bitset(G.neighbors(v)) for v in range(17)]
        verify_graph(a,5)
        dp=alpha_table(a)
        candidates=sorted(pair_candidates(a, dp, 5),key=lambda item:(item[0],item[1],item[2]))
        assert candidates
        costs=Counter(c for c,_,_ in candidates)
        assert costs[4]==[2,2,1,2,2,2,3][idx-1]
        winners=[]
        for cost,S,T in candidates:
            R,U,edges,tris,good=matching_right_triple(a,G,dp,S,T)
            if good:
                winners.append((cost,S,T,R,U,edges,tris,good))
        assert winners, f"graph {idx} lacks a tested five-vertex continuation"
        min_cost=min(x[0] for x in winners)
        win=[x for x in winners if x[0]==min_cost]
        assert min_cost==([4,4,5,5,4,4,4][idx-1])
        if min_cost==5:
            assert len(win)==2
        else:
            assert len(win)==costs[4]-(1 if idx==7 else 0)
        for cost,S,T,R,U,edges,tris,good in win:
            h=attach(a,(S,T,*good[0]),[(i,j) for i in (0,1) for j in (2,3,4)])
            verify_graph(h,6)
            H,actual=full_extension_family(a,S,T)
            expected={(1<<17)|(1<<18)|u for u in independent_masks(a)
                      if u & (S|T)==0}
            assert actual==expected, f"unforced internal graph not derived on {idx}"
            induced=G.subgraph(list(bitvertices(S|T)))
            if cost==4:
                assert nx.is_isomorphic(induced,nx.cycle_graph(4))
                assert len(R)==13 and len(U)==39 and len(good)==4
            else:
                assert nx.is_isomorphic(induced,C4leaf)
                assert len(R)==12 and len(U)==30 and edges==69 and tris==2 and len(good)==1
        shapes=Counter('C4' if cost==4 else 'C4+leaf' for cost,*_ in win)
        print(f"graph {idx}: blue pairs cost4={costs[4]}, cost5={costs[5]}; "
              f"minimum cost reaching 22={min_cost}; winning pairs={len(win)}; "
              f"source shapes={dict(shapes)}",flush=True)
        results.append((idx,min_cost,len(win)))
    assert len(results)==7
    print('PASS: all seven 17-vertex extremal graphs produce a verified 22-vertex witness.')
    print('PASS: five extend using four-point C4 carriers, two require five-point C4+leaf carriers.')
    print('PASS: the internal K2,3 is forced by the exact one-vertex frontier after the selected blue pair.')

    # Explicit counterexample to a UNIVERSAL K2,3-successor rule.
    # The five old neighborhoods below were found by an unrestricted binary
    # mixed-integer model, but that optimizer is NOT required to verify them.
    # Every one of the 2^10 internal edge patterns is checked exactly here.
    alt_neighborhoods = [
        (2,4,6,9), (12,), (1,2,3,5,14), (1,8,10,15), (7,11,13),
    ]
    a=[bitset(nx.from_graph6_bytes(G17_G6[0].encode()).neighbors(v))
       for v in range(17)]
    dp=alpha_table(a)
    N=list(map(bitset,alt_neighborhoods))
    assert all(not any(a[v]&N[i] for v in alt_neighborhoods[i])
               for i in range(5))
    F_edges=list(combinations(range(5),2))
    forced=[]
    for assignment in range(1<<10):
        E=[e for z,e in enumerate(F_edges) if assignment>>z & 1]
        if any(N[i]&N[j] for i,j in E):continue
        if any(all((i,j) in E for i,j in combinations(tri,2))
               for tri in combinations(range(5),3)):continue
        capacities=[]
        for subset in range(1<<5):
            if any((subset>>i&1) and (subset>>j&1) for i,j in E):
                continue
            union=0
            for i in range(5):
                if subset>>i&1:union|=N[i]
            capacities.append(subset.bit_count()+dp[((1<<17)-1)&~union])
        if max(capacities)<=6:forced.append(E)
    assert len(forced)==1
    h=attach(a,N,forced[0])
    verify_graph(h,6)
    # The source support is K_1,4; the new internal sector is C4 with leaf.
    old=nx.from_graph6_bytes(G17_G6[0].encode())
    source=old.subgraph(list(bitvertices(N[0]|N[1])))
    assert nx.is_isomorphic(source,nx.star_graph(4))
    F=nx.Graph();F.add_nodes_from(range(5));F.add_edges_from(forced[0])
    assert nx.is_isomorphic(F,C4leaf)
    assert F.number_of_edges()==5
    print('PASS: unrestricted internal coloring provides a second forced type, C4+leaf.')
    print('PASS: 5 old attachment vertices induce K1,4 and the 5 new vertices induce C4+leaf.')
    print('PASS: exactly 1 / 1024 internal edge colorings works for those fixed neighborhoods.')
    return results

if __name__=='__main__':
    run()
