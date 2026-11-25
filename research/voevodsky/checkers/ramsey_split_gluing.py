"""Verify the (3,4) split example against forbidden cliques on all eight vertices."""
from itertools import combinations, product


def check(cycle):
    A, B = range(1, 4), range(4, 8)  # vertex 0 is the pivot
    internal = {(4, 5), (5, 6), (6, 7)} | ({(4, 7)} if cycle else set())
    blue_groups = [Y for n in range(1, 5) for Y in combinations(B, n)
                   if internal.isdisjoint(combinations(Y, 2))]
    triangles, fours = ([set(combinations(q, 2)) for q in combinations(range(8), n)] for n in (3, 4))
    count = 0
    for masks in product(range(8), repeat=4):
        S = {v: {a for a in A if mask & (1 << (a-1))} for v, mask in zip(B, masks)}
        law = (all(not S[i] & S[j] for i, j in internal) and
               all(len(set.union(*(S[v] for v in Y))) >= len(Y) for Y in blue_groups))
        red = internal | {(0, a) for a in A} | {(a, v) for v in B for a in S[v]}
        direct = not any(t <= red for t in triangles) and not any(q.isdisjoint(red) for q in fours)
        assert law == direct
        count += direct
    return count


if __name__ == '__main__':
    counts = [check(False), check(True)]
    assert counts == [18, 0]
    print('P4, C4 labeled gluings:', *counts)
