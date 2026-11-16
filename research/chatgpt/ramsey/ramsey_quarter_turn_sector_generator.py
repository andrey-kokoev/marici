#!/usr/bin/env python3
"""Exact four-phase Ramsey-sector construction, no external packages.

Old graph: Cayley(Z/13, {+/-1,+/-5}).
A quarter-turn acts by x -> 5*x mod 13, fixing 0.
The 12 nonzero vertices split into three four-cycles.
Choose an independent transversal S of those cycles.
Attach a red C4, giving each new vertex the red neighborhood 5**t S.
The resulting 17-vertex graph is triangle-free; its independence number
is <=5 iff the seven old vertices outside S and 5**2 S have alpha<=3.
The script derives the survivor count and tests the entire 17-vertex graph.
"""

from itertools import combinations, product
from collections import Counter

N = 13
DIFFS = {1, 5, 8, 12}

def is_independent(adjacency, vertices):
    return all(v not in adjacency[u] for u, v in combinations(vertices, 2))

def independence_number(adjacency, vertices=None):
    vertices = sorted(adjacency if vertices is None else vertices)
    for r in range(len(vertices), -1, -1):
        for subset in combinations(vertices, r):
            if is_independent(adjacency, subset):
                return r
    return 0

def construct_old():
    graph = {u: {(u+d) % N for d in DIFFS} for u in range(N)}
    assert all(is_independent(graph, graph[u]) for u in graph), 'old graph has a triangle'
    assert independence_number(graph) == 4
    assert all({(5*y) % 13 for y in graph[x]} == graph[(5*x)%13] for x in graph)
    return graph

def multiplicative_orbits():
    unseen = set(range(1, 13))
    orbits = []
    while unseen:
        a = min(unseen)
        orbit = tuple(a * pow(5, j, 13) % 13 for j in range(4))
        assert len(set(orbit)) == 4
        unseen -= set(orbit)
        orbits.append(orbit)
    assert len(orbits) == 3
    return orbits

def attach(old, seed):
    phases = [set(x * pow(5, t, 13) % 13 for x in seed) for t in range(4)]
    assert set.union(*phases) == set(range(1, 13))
    assert all(not (a & b) for a, b in combinations(phases, 2))
    G = {u:set(neighbors) for u,neighbors in old.items()}
    for t in range(4):
        v=13+t
        G[v]=set()
        for u in phases[t]:
            G[v].add(u)
            G[u].add(v)
    for t in range(4):
        a,b=13+t,13+(t+1)%4
        G[a].add(b)
        G[b].add(a)
    assert all(is_independent(G,G[u]) for u in G), 'new red triangle'
    return G, phases

def run():
    old=construct_old()
    orbits=multiplicative_orbits()
    counts=Counter()
    success=[]
    classes={}
    for seed in product(*orbits):
        if not is_independent(old, seed):
            counts['not_independent']+=1
            continue
        G,phases=attach(old, seed)
        residual=set(range(13))-phases[0]-phases[2]
        assert len(residual)==7
        alpha_res=independence_number(old, residual)
        # The independent sets among the four new vertices are singletons or opposite pairs.
        # Hence this residual test is equivalent to the full Ramsey bound alpha<=5.
        alpha_new=independence_number(G)
        assert (alpha_res<=3) == (alpha_new<=5)
        assert alpha_res in (3,4)
        counts[f'residual_alpha_{alpha_res}']+=1
        orbit=min(tuple(sorted({x*pow(5,j,13)%13 for x in seed})) for j in range(4))
        classes[orbit]=(alpha_res,alpha_new)
        if alpha_new<=5:
            assert alpha_new==5
            success.append((seed,G,phases))
    assert counts==Counter({'not_independent':44,'residual_alpha_4':16,'residual_alpha_3':4})
    assert len(classes)==5 and len(success)==4
    assert len({min(tuple(sorted({x*pow(5,j,13)%13 for x in seed})) for j in range(4)) for seed,_,_ in success})==1
    for seed,G,phases in success:
        assert sum(map(len,G.values()))//2 == 42
        assert sorted(set(map(len,G.values())))==[4,5]
        rotation={u:(5*u)%13 for u in range(13)}
        rotation.update({13+t:13+(t+1)%4 for t in range(4)})
        assert all({rotation[v] for v in G[u]} == G[rotation[u]] for u in G)
    print('Old graph: C13(+/-1,+/-5), alpha=4')
    print('Quarter-turn orbits on 12 old vertices:',orbits)
    print('Candidate transversals:',4**3)
    print('Independent transversals:',sum(v for k,v in counts.items() if k.startswith('residual')))
    print('Symmetry-inequivalent independent seeds:',len(classes))
    print('Residual seven-vertex test (independence numbers):')
    for seed,(res,new) in sorted(classes.items()):
        print(f'  {seed}: residual alpha={res}, extended alpha={new}')
    print('Successful seeds:',len(success),'one quarter-turn orbit')
    print('Chosen valid example:',success[0][0]);print('Phase neighborhoods:',[sorted(x) for x in success[0][2]])
    print('Target: 17 vertices, 42 red edges, triangle-free, alpha=5')

if __name__=='__main__':
    run()
