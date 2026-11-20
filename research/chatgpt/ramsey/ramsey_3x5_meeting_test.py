"""Keep the earlier 3x4 cross signs. Try all fifth columns and internal signs."""
from itertools import combinations, product

A, B = range(1, 4), range(4, 9)
pairs = lambda vs: list(combinations(vs, 2))
internal = pairs(A) + pairs(B)
cross_plus = {(1, 5), (2, 6), (3, 4), (3, 7)}
edges = pairs(range(1, 9))
def mask(es): return sum(1 << edges.index(e) for e in es)
tri, five = ([mask(pairs(s)) for s in combinations(range(1, 9), k)] for k in (3, 5))
for col in product((0, 1), repeat=3):
    pos = cross_plus | {(a, 8) for a, bit in zip(A, col) if bit}
    neighbors = {v: {y for e in pos if v in e for y in e if y != v} for v in range(1,9)}
    forced = {e for e in internal if neighbors[e[0]] & neighbors[e[1]]}
    base = mask(pos); count = 0; any_pos = 0; all_pos = mask(internal)
    for i in range(len(internal)+1):
        for es in combinations(internal,i):
            m = base | mask(es)
            if any(m&t == t for t in tri) or any(not m&t for t in five): continue
            count += 1; any_pos |= m; all_pos &= m
    never = {e for e in internal if not any_pos & mask([e])}
    assert count and forced <= never
    print(col, sorted(forced), count, 'other forced', sorted(never-forced), all_pos.bit_count())
