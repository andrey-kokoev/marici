"""Keep the 3x4 cross block. Append each possible row at address 8."""
from itertools import combinations, product

A, B = (1, 2, 3, 8), (4, 5, 6, 7)
edges = list(combinations(range(1, 9), 2))
def bit(i, j): return 1 << edges.index(tuple(sorted((i, j))))
def mask(es): return sum(bit(i, j) for i, j in es)
quads = [mask(combinations(q, 2)) for q in combinations(range(1, 9), 4)]
inside = list(combinations(A, 2)) + list(combinations(B, 2))
fill = [mask(es) for k in range(13) for es in combinations(inside, k)]
base = mask(((1, 5), (2, 6), (3, 4), (3, 7)))
for row in product((0, 1), repeat=4):
    cross = base | mask((8, j) for j, x in zip(B, row) if x)
    valid = [cross | f for f in fill if all((cross | f) & q not in (0, q) for q in quads)]
    print(row, len(valid))
    if row == (1, 0, 0, 1):
        assert all(not (g & bit(4,7)) or not (g & bit(3,8)) for g in valid)
        assert all(g & (bit(4,7) | bit(1,2)) for g in valid)
        print('both signs possible for every internal pair:', all({bool(g & bit(*p)) for g in valid} == {True, False} for p in inside))
