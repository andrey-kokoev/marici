#!/usr/bin/env python3
"""Exact 6-direction/pair-promotion Ramsey witness and its obstruction tests.

Standard library only. The 22-vertex construction is classical (Graver-Yackel),
not a proof of R(3,7)<=23 and not derived from the Golay/2048 cycle.
"""
from collections import Counter
from itertools import combinations

BASE = tuple(range(1, 7))
PAIRS = tuple(map(frozenset, combinations(BASE, 2)))
PAIR_ID = {p: i for i, p in enumerate(PAIRS)}


def shift5(i, t):
    return (i - 2 + t) % 5 + 2


def cycle_pairs():
    # Derived from 5-cyclic index formula; no supplied graph adjacency matrix.
    out = []
    for i in range(2, 7):
        out += [
            frozenset((shift5(i, 3), shift5(i, 4))),
            frozenset((1, i)),
            frozenset((shift5(i, 1), shift5(i, 3))),
        ]
    return tuple(out)


def build():
    C = cycle_pairs()
    assert len(C) == len(set(C)) == 15 and set(C) == set(PAIRS)
    removed = {frozenset((C[i], C[(i+1) % 15])) for i in range(15)}
    assert len(removed) == 15
    assert all(not (C[i] & C[(i+1) % 15]) for i in range(15))
    # Every 4-set supports exactly one deleted pair--pair incidence.
    four_supports = [frozenset().union(*e) for e in removed]
    assert len(set(four_supports)) == 15
    assert set(four_supports) == set(map(frozenset, combinations(BASE, 4)))
    # Every 6-set perfect matching is a forbidden KG(6,2) triangle;
    # exactly one of its three edges is deleted.
    matchings = [frozenset(t) for t in combinations(PAIRS, 3)
                 if len(frozenset().union(*t)) == 6]
    assert len(matchings) == 15
    assert all(sum(e <= M for e in removed) == 1 for M in matchings)

    A = [0] * 22
    def edge(u, v):
        assert u != v
        A[u] |= 1 << v
        A[v] |= 1 << u
    # vertex 0=p; vertices 1..6=original six directions;
    # vertices 7..21=the fifteen unordered-pair promoted states.
    for i in BASE:
        edge(0, i)
    for j, pair in enumerate(PAIRS):
        for i in pair:
            edge(i, 7+j)
    for i,j in combinations(range(15), 2):
        x,y = PAIRS[i],PAIRS[j]
        if not (x & y) and frozenset((x,y)) not in removed:
            edge(7+i, 7+j)
    return A, C, removed


def independent_sets(A):
    out=[]
    def search(available, chosen):
        out.append(chosen)
        while available:
            bit=available&-available
            available ^= bit
            i = bit.bit_length()-1
            search(available & ~A[i], chosen|bit)
    search((1<<len(A))-1, 0)
    return out


def act_on_mask(m, perm):
    return sum(1<<perm[i] for i in range(len(perm)) if (m>>i)&1)


def check_automorphism(A,perm):
    assert sorted(perm) == list(range(len(A)))
    assert all(act_on_mask(A[i],perm) == A[perm[i]] for i in range(len(A)))


def orbit_mask(seed, generators):
    reached={seed};pending=[seed]
    while pending:
        v=pending.pop()
        for p in generators:
            z=act_on_mask(v,p)
            if z not in reached:
                reached.add(z);pending.append(z)
    return reached


def check_six_edge_lemma():
    """A 6-edge graph on 6 vertices with every edge degree-sum >=5 has a C4."""
    all_edges=list(combinations(range(6),2))
    accepted=0
    for select in combinations(all_edges, 6):
        deg=Counter(j for e in select for j in e)
        if any(sum(deg[v] for v in e)<5 for e in select):
            continue
        accepted+=1
        edge_set={frozenset(e) for e in select}
        assert any(all(frozenset(e) in edge_set for e in (
            (Q[0],Q[1]),(Q[1],Q[2]),(Q[2],Q[3]),(Q[3],Q[0])))
            for quad in combinations(range(6),4)
            for Q in ((quad[0],quad[1],quad[2],quad[3]),
                      (quad[0],quad[1],quad[3],quad[2]),
                      (quad[0],quad[2],quad[1],quad[3])))
    return accepted


def run():
    A, C, removed = build()
    assert all(a.bit_count()==6 for a in A)
    assert sum(a.bit_count() for a in A)//2 == 66
    assert all(not (A[i]&A[j]) for i in range(22)
               for j in range(i+1,22) if (A[i]>>j)&1)
    independent=independent_sets(A)
    counts=Counter(s.bit_count() for s in independent)
    assert counts == Counter({0:1,1:22,2:165,3:550,4:870,5:612,6:137}), counts
    maxsets=[s for s in independent if s.bit_count()==6]
    # Every candidate new vertex must have an independent red neighborhood S
    # intersecting *all* maximum independent 6-sets. None exists.
    assert all(any((S&I)==0 for I in maxsets) for S in independent)

    # A compact source-symmetry certificate: ten 6-sets suffice to obstruct
    # every candidate S, not the entire 137-set family.
    rot=[0,1]+[shift5(i,1) for i in range(2,7)]+[
        7+PAIR_ID[frozenset(1 if j==1 else shift5(j,1) for j in p)]
        for p in PAIRS]
    swap=[1,0,7,11,10,9,8,2,6,5,4,3,16,20,18,19,12,17,14,15,13,21]
    check_automorphism(A, rot)
    check_automorphism(A, swap)
    seed=next(s for s in maxsets if len(orbit_mask(s,(rot,swap)))==10
              and all(any((S&I)==0 for I in orbit_mask(s,(rot,swap))) for S in maxsets))
    shortcert=orbit_mask(seed,(rot,swap))
    assert len(shortcert)==10
    assert all(any((S&I)==0 for I in shortcert) for S in independent)

    # Non-neighbor common-neighbor defects relative to the impossible
    # hypothetical uniform codegree=2 graph.
    co=Counter((A[i]&A[j]).bit_count()
               for i in range(22) for j in range(i+1,22) if not (A[i]>>j)&1)
    assert co == Counter({1:35, 2:95, 3:35}),co
    assert all((A[0]&A[j]).bit_count()==2 for j in range(1,22)
               if not (A[0]>>j)&1)
    nlemma=check_six_edge_lemma()
    print('15 deleted edges: one per forbidden triangle; one per 4-position support')
    print('22-vertex graph: 6-regular, 66 edges, zero triangles, independence 6')
    print('independent sets by size:',dict(sorted(counts.items())))
    print('23rd-vertex extension candidates:',len(independent),'valid:',0)
    print('compact obstruction certificate:',len(shortcert),'six-sets; seed',tuple(i for i in range(22) if seed>>i&1))
    print('nonadjacent common-neighbor counts:',dict(sorted(co.items())))
    print('six-edge lemma patterns satisfying the degree-sum premise:',nlemma)
    print('PASS')

if __name__ == '__main__':
    run()
