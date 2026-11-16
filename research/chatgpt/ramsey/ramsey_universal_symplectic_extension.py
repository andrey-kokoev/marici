#!/usr/bin/env python3
"""Universal symplectic lifting and exact one-vertex Ramsey extension.

No external packages. Finite 22-vertex checks concern a specific
1+6+15 witness family, not every 22-vertex critical coloring.
"""
from itertools import combinations
from collections import Counter


def pairing(x, y):
    q, p = x
    Q, P = y
    return ((q & P).bit_count() + (p & Q).bit_count()) % 2


def canonical_factor(adjacency):
    """An explicit graph-to-symplectic-factor realization over F2."""
    n = len(adjacency)
    return [(1 << i, sum(((adjacency[i] >> j) & 1) << j for j in range(i)))
            for i in range(n)]


def assert_arbitrary_hyperbolic_extension(adjacency):
    n = len(adjacency)
    old = canonical_factor(adjacency)
    assert all(pairing(old[i], old[j]) == ((adjacency[i] >> j) & 1)
               for i in range(n) for j in range(n))
    for b in range(1 << n):
        extended = [(q, p | (((b >> i) & 1) << n))
                    for i, (q, p) in enumerate(old)]
        new = (1 << n, 0)
        assert all(pairing(extended[i], extended[j]) == ((adjacency[i] >> j) & 1)
                   for i in range(n) for j in range(n))
        assert all(pairing(new, extended[i]) == ((b >> i) & 1)
                   for i in range(n))
    return 1 << n


def independent_levels(adjacency, max_size):
    levels = [[] for _ in range(max_size + 1)]
    def visit(candidates, chosen, size):
        levels[size].append(chosen)
        if size == max_size:
            return
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            i = bit.bit_length() - 1
            visit(candidates & ~adjacency[i], chosen | bit, size + 1)
    visit((1 << len(adjacency)) - 1, 0, 0)
    return levels


def transversal_summary(adjacency, forbidden_blue_size):
    n = len(adjacency)
    levels = independent_levels(adjacency, forbidden_blue_size - 1)
    large = levels[forbidden_blue_size - 1]
    valid = [s for level in levels for s in level
             if all(s & u for u in large)]
    return len(large), len(valid)


def witness_graph_representatives():
    directions = range(6)
    pairs = list(combinations(directions, 2))
    lines = [tri for tri in combinations(range(15), 3)
             if all(set(pairs[i]).isdisjoint(pairs[j])
                    for i, j in combinations(tri, 2))]
    assert len(lines) == 15
    def find_matchings(k, used, record):
        if k == len(lines):
            yield tuple(record)
        else:
            for w in lines[k]:
                if not (used >> w & 1):
                    yield from find_matchings(k+1, used | (1 << w), record+[w])
    def graph(chosen):
        a = [0] * 22
        def edge(u,v):
            a[u] |= 1<<v
            a[v] |= 1<<u
        for s in range(6):
            edge(0,1+s)
        for i,(s,t) in enumerate(pairs):
            edge(7+i,1+s)
            edge(7+i,1+t)
        deleted = set()
        for line,distinguished in zip(lines,chosen):
            deleted.add(tuple(sorted(x for x in line if x!=distinguished)))
        for i,j in combinations(range(15),2):
            if set(pairs[i]).isdisjoint(pairs[j]) and (i,j) not in deleted:
                edge(7+i,7+j)
        return a
    def binary_rank(a):
        pivots={}
        for x in a:
            while x:
                b=x.bit_length()-1
                if b not in pivots:
                    pivots[b]=x
                    break
                x ^= pivots[b]
        return len(pivots)
    reps={}
    for m in find_matchings(0,0,[]):
        a=graph(m)
        reps.setdefault(binary_rank(a),a)
        if len(reps)==2:
            break
    return reps


def quantify_hitting_six(a):
    six=independent_levels(a,6)[6]
    # A 5-element transversal does not exist in either test graph.
    # Any smaller transversal could be extended to a 5-element one.
    assert not any(all(sum(1<<i for i in c) & I for I in six)
                   for c in combinations(range(len(a)),5))
    hits=[]
    for c in combinations(range(len(a)),6):
        s=sum(1<<i for i in c)
        if all(s & I for I in six):
            e=sum((a[i]&s).bit_count() for i in c)//2
            hits.append(e)
    return len(six),len(hits),dict(sorted(Counter(hits).items()))


def main():
    c5=[(1<<((i-1)%5))|(1<<((i+1)%5)) for i in range(5)]
    tested=assert_arbitrary_hyperbolic_extension(c5)
    num_pairs,extensions=transversal_summary(c5,3)
    assert (tested,num_pairs,extensions)==(32,5,0)
    print(f'C5: all {tested} neighborhoods symplectically realizable; '
          f'{num_pairs} independent pairs; {extensions} Ramsey-admissible extensions.')
    for rank,a in sorted(witness_graph_representatives().items()):
        assert all(v.bit_count()==6 for v in a)
        num_I,num_ext=transversal_summary(a,7)
        N,hits,hist=quantify_hitting_six(a)
        assert N==num_I and num_ext==0
        print(f'22-vertex witness, binary rank {rank}: {N} independent six-sets, '
              f'{num_ext} independent transversals; {hits} six-element transversals '
              f'with induced red-edge counts {hist}.')
    print('Exact checks complete. No universal R(3,7) upper bound inferred.')

if __name__=='__main__':
    main()
