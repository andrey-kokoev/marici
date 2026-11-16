#!/usr/bin/env python3
"""Exact finite Ramsey support audit for the r=0 and r=1 profiles.

Assumptions: hypothetical 23-vertex, 6-regular, triangle-free graph with
independence <= 6. Fix a vertex v, six independent neighbors S, sixteen
outside vertices T. A vertex t in T retains support N(t) intersection S.
The script tests necessary consequences of those axioms only. The base
regularity reduction is a separate mathematical argument using e(3,6,17)>=40.

No extra clone shape, chosen matching, cyclic closure, or sampled order.
No numerical optimizers or external packages. All searches are finite and exact.
"""
from collections import Counter
from itertools import combinations

S = tuple(range(6))
PAIRS = tuple(combinations(S, 2))
TRIPLES = tuple(combinations(S, 3))

def pair_multisets(degrees, singletons):
    """All pair multisets whose incidence quotas equal degrees.

    Pair occurrence multiplicity <=2 because three occurrences of one
    pair would be an independent triple supported on only two directions.
    If an endpoint has a singleton occurrence, multiplicity <=1, since
    that singleton plus two pair occurrences gives the same contradiction.
    """
    caps = [1 if (a in singletons or b in singletons) else 2
            for a, b in PAIRS]
    remaining = list(degrees)
    values = [0] * len(PAIRS)
    def walk(j):
        if j == len(PAIRS):
            if not any(remaining):
                yield tuple(values)
            return
        a, b = PAIRS[j]
        for k in range(min(caps[j], remaining[a], remaining[b]) + 1):
            remaining[a] -= k
            remaining[b] -= k
            values[j] = k
            if all(remaining[i] <= sum(caps[p] for p in range(j+1,len(PAIRS))
                                       if i in PAIRS[p]) for i in S):
                yield from walk(j+1)
            remaining[a] += k
            remaining[b] += k
    yield from walk(0)

def build(singletons, triples, multiplicities):
    support = [frozenset((a,)) for a in singletons]
    support += [frozenset(p) for i, p in enumerate(PAIRS)
                for _ in range(multiplicities[i])]
    support += [frozenset(t) for t in triples]
    assert len(support) == 16
    assert all(sum(a in t for t in support) == 5 for a in S)
    return tuple(support)

def local_obstruction(support):
    """Simple consequences before constructing any red edges inside T."""
    n = len(support)
    masks = [sum(1<<a for a in x) for x in support]
    for i in range(n):
        possible = sum(not (masks[i]&masks[j]) for j in range(n) if i != j)
        if possible < 6-len(support[i]):
            return 'insufficient_available_degree'
    for U in combinations(range(n), 4):
        union = 0
        for i in U:
            union |= masks[i]
        if union.bit_count() >= 4:
            continue
        if all(masks[i]&masks[j] for i,j in combinations(U,2)):
            return 'four_independent_with_three_supports'
    return None

def propagate(support):
    """Sound unit propagation of Ramsey capacity and exact degree constraints.

    For any U of size k <=4 with fewer than k directions in the union of
    supports, U cannot be internally independent. At least one red edge
    must lie inside U. An internal red edge can join only disjoint supports.
    A forced edge consumes one of exactly 6-|support| red neighbors of t.
    """
    n = len(support)
    masks = [sum(1<<a for a in x) for x in support]
    edges = [e for e in combinations(range(n),2)
             if (masks[e[0]] & masks[e[1]]) == 0]
    edge_index = {e:i for i,e in enumerate(edges)}
    incidence = [[j for j,(a,b) in enumerate(edges) if i==a or i==b]
                 for i in range(n)]
    clauses = []
    for k in (2,3,4):
        for U in combinations(range(n), k):
            union = 0
            for i in U:
                union |= masks[i]
            if union.bit_count() >= k:
                continue
            c = [edge_index[e] for e in combinations(U, 2)
                 if e in edge_index]
            if not c:
                return False
            clauses.append(c)
    status = [-1] * len(edges)  # -1 undecided, 0 absent, 1 present
    for _ in range(len(edges)+1):
        changed = False
        for i in range(n):
            forced = sum(status[j] == 1 for j in incidence[i])
            possible = sum(status[j] != 0 for j in incidence[i])
            target = 6-len(support[i])
            if forced > target or possible < target:
                return False
            if forced == target or possible == target:
                value = 0 if forced == target else 1
                for j in incidence[i]:
                    if status[j] == -1:
                        status[j] = value
                        changed = True
        for clause in clauses:
            if any(status[j] == 1 for j in clause):
                continue
            possible = [j for j in clause if status[j] != 0]
            if not possible:
                return False
            if len(possible) == 1 and status[possible[0]] == -1:
                status[possible[0]] = 1
                changed = True
        if not changed:
            return True
    raise AssertionError('Unit propagation did not terminate')

def enumerated_profiles(r):
    singletons = tuple(range(2+r))
    triples = ((),) if r == 0 else tuple((t,) for t in TRIPLES)
    for Ts in triples:
        pair_degrees = [5-int(a in singletons)-sum(a in t for t in Ts)
                        for a in S]
        for multiplicities in pair_multisets(pair_degrees,set(singletons)):
            yield Ts, multiplicities, build(singletons, Ts, multiplicities)

def final_case_contradiction(support):
    """One r=1 case survives degree/Hall unit propagation.

    Three singleton supports A and a triple A force exactly 3 pair supports
    within B=S\\A and all nine cross pairs. Their B-pair vertices each
    connect to triple A and all 3 singleton vertices, exhausting degree 4.
    No singleton vertices can connect among themselves because their shared
    B-pair neighbors would create red triangles. Hence precisely 6 red edges
    join the singleton vertices to the 9 cross-pair vertices.
    The cross-pair subgraph must have 15 of 18 potential edges. But its six
    edge-disjoint triangles require at least six deletions, not three.
    """
    A = {0,1,2}
    B = {3,4,5}
    expected = [frozenset((a,)) for a in sorted(A)]
    expected += [frozenset((a,b)) for a in sorted(A) for b in sorted(B)]
    expected += [frozenset(pair) for pair in combinations(sorted(B),2)]
    expected += [frozenset(A)]
    assert Counter(support) == Counter(expected)
    cross_edges = [((a,b),(c,d)) for (a,b),(c,d) in
                   combinations([(a,b) for a in sorted(A) for b in sorted(B)],2)
                   if a != c and b != d]
    triangles = [tr for tr in combinations([(a,b) for a in sorted(A)
                                                 for b in sorted(B)],3)
                 if all(a != c and b != d for (a,b),(c,d) in combinations(tr,2))]
    assert len(cross_edges) == 18
    assert len(triangles) == 6
    assert all(sum(set(e).issubset(tr) for tr in triangles)==1 for e in cross_edges)
    assert 18-15 < len(triangles)
    return True

def main():
    counts = {}
    for r in (0,1):
        stats = Counter()
        survivors = []
        for triples, mult, support in enumerated_profiles(r):
            stats['degree_compatible_multisets'] += 1
            obstacle = local_obstruction(support)
            if obstacle:
                stats[obstacle] += 1
                continue
            stats['passes_immediate_obstructions'] += 1
            if propagate(support):
                stats['survives_local_propagation'] += 1
                survivors.append(support)
            else:
                stats['refuted_by_exact_degree_capacity_propagation'] += 1
        counts[r] = dict(stats)
        if r == 0:
            assert not survivors
        if r == 1:
            assert len(survivors) == 1
            assert final_case_contradiction(survivors[0])
        print('r=',r,counts[r])
    print('Both r=0 and r=1 support profiles impossible. Remaining r=2,3,4 OPEN.')

if __name__ == '__main__':
    main()
