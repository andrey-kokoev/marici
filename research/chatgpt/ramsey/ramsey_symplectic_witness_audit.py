#!/usr/bin/env python3
"""Finite symplectic/Ramsey audit on the 22-vertex pair-witness family.

All results concern the declared 1+6+15 incidence family, not every
22-vertex (3,7)-Ramsey graph or a proof of R(3,7)<=23.
No external packages are required.
"""
from collections import Counter
from itertools import combinations

DIRECTIONS = range(6)
PAIRS = list(combinations(DIRECTIONS, 2))
LINES = [
    triple for triple in combinations(range(15), 3)
    if all(set(PAIRS[a]).isdisjoint(PAIRS[b])
           for a, b in combinations(triple, 2))
]
assert len(LINES) == 15

def all_line_witness_matchings():
    def step(k, used, selected):
        if k == len(LINES):
            yield tuple(selected)
            return
        for w in LINES[k]:
            if not (used >> w & 1):
                yield from step(k + 1, used | (1 << w), selected + [w])
    return list(step(0, 0, []))

def red_graph(selection):
    """22 red-graph adjacency bitsets, with pair-pair edges deleted by matching."""
    adj = [0] * 22
    def edge(i, j):
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    for i in DIRECTIONS:
        edge(0, 1 + i)
    for k, (i, j) in enumerate(PAIRS):
        edge(7 + k, 1 + i)
        edge(7 + k, 1 + j)
    missing = set()
    for line, selected in zip(LINES, selection):
        a, b = sorted(p for p in line if p != selected)
        missing.add((a, b))
    for a, b in combinations(range(15), 2):
        if set(PAIRS[a]).isdisjoint(PAIRS[b]) and (a, b) not in missing:
            edge(7 + a, 7 + b)
    return adj

def binary_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            j = row.bit_length() - 1
            if j not in pivots:
                pivots[j] = row
                break
            row ^= pivots[j]
    return len(pivots)

def triangle_count(adj):
    return sum((adj[i] & adj[j]).bit_count()
               for i in range(len(adj))
               for j in range(i + 1, len(adj))
               if (adj[i] >> j) & 1) // 3

def independent_sets(adj, cap):
    items = [[] for _ in range(cap + 1)]
    def visit(candidates, chosen, k):
        items[k].append(chosen)
        if k == cap:
            return
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1
            visit(candidates & ~adj[v], chosen | bit, k + 1)
    visit((1 << len(adj)) - 1, 0, 0)
    return items

def min_uncovered_six(adj):
    levels = independent_sets(adj, 7)
    assert not levels[7]
    sixes = levels[6]
    min_missed = min(
        sum((s & t) == 0 for t in sixes)
        for level in levels[:7] for s in level
    )
    return len(sixes), min_missed, [len(z) for z in levels]

def rank_extension(A, b):
    n = len(A)
    B = [
        A[i] | (((b >> i) & 1) << n)
        for i in range(n)
    ]
    B.append(b)
    return binary_rank(B)

def c5_test():
    A = [
        (1 << ((i - 1) % 5)) | (1 << ((i + 1) % 5))
        for i in range(5)
    ]
    assert triangle_count(A) == 0
    assert not independent_sets(A, 3)[3]
    assert binary_rank(A) == 4
    return binary_rank(A)

def main():
    selections = all_line_witness_matchings()
    assert len(selections) == 288
    ranks = Counter()
    representatives = {}
    for selection in selections:
        A = red_graph(selection)
        assert len(A) == 22
        assert all(row.bit_count() == 6 for row in A)
        assert triangle_count(A) == 0
        assert not independent_sets(A, 7)[7]
        r = binary_rank(A)
        ranks[r] += 1
        representatives.setdefault(r, A)

    assert ranks == {18: 144, 20: 144}
    for r, A in sorted(representatives.items()):
        count6, missed, independent_counts = min_uncovered_six(A)
        expected = (137, 26) if r == 18 else (139, 24)
        assert (count6, missed) == expected
        print(f"rank={r}: independent 6-sets={count6}, "
              f"min unhit by red-independent new neighborhood={missed}, "
              f"independent_set_counts_0_to_7={independent_counts}")

    # The algebraic rank-increase law applies to EVERY alternating matrix;
    # these selected instances are regressions, not the proof of that law.
    for r, A in representatives.items():
        old_rank = binary_rank(A)
        for b in [0, 1, 3, (1 << 22) - 1] + [1 << i for i in range(22)]:
            difference = rank_extension(A, b) - old_rank
            assert difference in (0, 2)

    assert c5_test() == 4
    print(f"perfect_matchings={len(selections)}")
    print(f"binary_symplectic_rank_distribution={dict(sorted(ranks.items()))}")
    print("C5 symplectic dimension=4")
    print("All finite checks passed. No universal Ramsey upper bound inferred.")

if __name__ == "__main__":
    main()
