#!/usr/bin/env python3
"""Exact finite audit: quaternion quarter-turns and disjoint positive-braid cells.

Uses integer quaternion numerators divided by (sqrt(2))**degree; no floating
point is used. Mod-2 cellular ranks are computed by sparse integer bitsets.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def numerator_product(a, b):
    w, x, y, z = a
    W, X, Y, Z = b
    return (
        w*W-x*X-y*Y-z*Z,
        w*X+x*W+y*Z-z*Y,
        w*Y-x*Z+y*W+z*X,
        w*Z+x*Y-y*X+z*W,
    )


def normalize(v):
    # q = (a+b*i+c*j+d*k) / sqrt(2)**degree
    numerator, degree = v
    while degree >= 2 and all(c % 2 == 0 for c in numerator):
        numerator = tuple(c // 2 for c in numerator)
        degree -= 2
    return (numerator, degree)


def multiply(a, b):
    return normalize((numerator_product(a[0], b[0]), a[1] + b[1]))


def negative(a):
    return (tuple(-x for x in a[0]), a[1])


def spatial_key(a):
    return min(a, negative(a))


I = ((1, 0, 0, 0), 0)
NEG_I = negative(I)
I_QUAT = ((0, 1, 0, 0), 0)
J_QUAT = ((0, 0, 1, 0), 0)
X = ((1, 1, 0, 0), 1)
Y = ((1, 0, 1, 0), 1)
Z = ((1, 0, 0, 1), 1)
X_INV = ((1, -1, 0, 0), 1)
DELTA = ((0, 1, 1, 0), 1)


def word_value(word):
    q = I
    for letter in word:
        q = multiply(q, X if letter == 'X' else Y)
    return q


def check_quaternions():
    assert multiply(X, X_INV) == I
    assert multiply(multiply(X, Y), X_INV) == Z
    assert word_value('XYX') == word_value('YXY') == DELTA
    for a, b in ((X, Y), (X, Z), (Y, Z)):
        assert multiply(multiply(a, b), a) == multiply(multiply(b, a), b)
    assert multiply(DELTA, DELTA) == NEG_I
    assert multiply(NEG_I, NEG_I) == I
    assert word_value('XXXX') == word_value('YYYY') == NEG_I
    assert multiply(multiply(multiply(Z, X), Y), X) == J_QUAT
    assert multiply(multiply(J_QUAT, J_QUAT), I) == NEG_I
    exact_by_length = {I}
    cumulative = {I}
    records = []
    for n in range(8):
        if n:
            exact_by_length = {
                multiply(q, generator)
                for q in exact_by_length
                for generator in (X, Y)
            }
            cumulative |= exact_by_length
        records.append((n, len(exact_by_length), len(cumulative),
                        len({spatial_key(q) for q in cumulative})))
    expected = [
        (0, 1, 1, 1), (1, 2, 3, 3), (2, 4, 7, 7),
        (3, 7, 14, 14), (4, 11, 23, 21),
        (5, 16, 33, 24), (6, 21, 43, 24), (7, 23, 48, 24),
    ]
    assert records == expected, (records, expected)
    return records


def cells_of_dimension(n, dimension):
    """Each selected disjoint triple is XYX↔YXY; all other letters are free.

    A cell is (starts, baseline_integer_word), baseline XYX=010.
    Words are length-n binary strings with X=0 and Y=1.
    """
    p = dimension
    if p == 0:
        for w in range(2**n):
            yield ((), w)
        return
    for starts in combinations(range(n-2), p):
        if any(b-a < 3 for a, b in zip(starts, starts[1:])):
            continue
        consumed = {j for start in starts for j in (start, start+1, start+2)}
        free = [j for j in range(n) if j not in consumed]
        for bits in range(1 << len(free)):
            word = 0
            for start in starts:
                word |= 1 << (n-2-start)  # XYX = 010
            for pos, j in enumerate(free):
                if bits >> pos & 1:
                    word |= 1 << (n-1-j)
            yield (starts, word)


def face(cell, removed, flip, n):
    starts, word = cell
    start = starts[removed]
    smaller = starts[:removed] + starts[removed+1:]
    if flip:
        word ^= 7 << (n-3-start)  # XYX=010 <-> YXY=101
    return smaller, word


def mod2_rank(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length()-1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                break
    return len(pivots)


def cell_homology(n):
    cells = [list(cells_of_dimension(n, p)) for p in range(n//3+1)]
    counts = [len(level) for level in cells]
    assert all(counts[p] == comb(n-2*p, p)*2**(n-3*p)
               for p in range(len(cells)))
    ranks = [0]
    for p in range(1, len(cells)):
        target_index = {cell: j for j, cell in enumerate(cells[p-1])}
        columns = []
        for cell in cells[p]:
            boundary = 0
            for removed in range(p):
                for flip in (0, 1):
                    boundary ^= 1 << target_index[face(cell, removed, flip, n)]
            columns.append(boundary)
        ranks.append(mod2_rank(columns))
    ranks.append(0)
    betti = [counts[p]-ranks[p]-ranks[p+1] for p in range(len(cells))]
    assert all(b == 0 for b in betti[1:]), (n, counts, ranks, betti)
    return counts, ranks, betti


def braid_classes_and_endpoint_count(n):
    words = [''.join(w) for w in product('XY', repeat=n)]
    w_index = {w: j for j, w in enumerate(words)}
    parent = list(range(len(words)))

    def find(j):
        while parent[j] != j:
            parent[j] = parent[parent[j]]
            j = parent[j]
        return j

    def merge(j, k):
        parent[find(j)] = find(k)

    for word in words:
        for i in range(n-2):
            if word[i:i+3] in ('XYX', 'YXY'):
                flipped = 'YXY' if word[i:i+3] == 'XYX' else 'XYX'
                merge(w_index[word], w_index[word[:i]+flipped+word[i+3:]])
    comps = defaultdict(set)
    for i, word in enumerate(words):
        comps[find(i)].add(word)
    endpoints = defaultdict(set)
    for component_id, words_in_component in comps.items():
        values = {word_value(word) for word in words_in_component}
        assert len(values) == 1
        endpoints[next(iter(values))].add(component_id)
    if n == 4:
        collisions = [
            {w for i in ids for w in comps[i]}
            for ids in endpoints.values() if len(ids) > 1
        ]
        assert collisions == [{'XXXX', 'YYYY'}]
    return len(comps), len(endpoints)


def main():
    spatial = check_quaternions()
    print('QUATERNION BFS: (word_length, exact_length_states, cumulative_spinor, cumulative_spatial)')
    for record in spatial:
        print(' ', record)
    print('WORD LENGTH | BRAID CLASSES | SPINOR ENDPOINTS | CELL COUNTS | BOUNDARY RANKS | MOD2 BETTI')
    for n in range(3, 13):
        comps, endpoints = braid_classes_and_endpoint_count(n)
        counts, ranks, betti = cell_homology(n)
        assert comps == betti[0]
        print(f'{n:>2} | {comps:>3} | {endpoints:>2} | {counts} | {ranks} | {betti}')
    print('PASS: exact quaternion identities, endpoint collision, component counts, mod-2 cell homology n=3..12')

if __name__ == '__main__':
    main()
