"""Finite reader test, not a Ramsey or physical PE-pair realization."""
from itertools import combinations

sites = frozenset(range(1, 7))
partitions = {frozenset((a, sites - a)) for t in combinations(sites, 3)
              for a in [frozenset(t)]}
queries = list(combinations(sorted(sites), 2))


def readings(blocks):
    return tuple(any(x in b and y in b for b in blocks) for x, y in queries)


assert len(partitions) == len({readings(p) for p in partitions}) == 10
assert {frozenset.union(*p) for p in partitions} == {sites}
for p in partitions:
    a, b = p
    for x in a:
        for y in b:
            q = frozenset(((a - {x}) | {y}, (b - {y}) | {x}))
            assert q in partitions
            assert sum(i != j for i, j in zip(readings(p), readings(q))) == 8
print('10 partitions; 1 underlying set; 10 same-triple signatures; '
      '8 of 15 pair readings change per cross-triple swap.')
