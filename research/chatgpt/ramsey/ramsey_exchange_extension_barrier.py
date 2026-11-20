"""Check the overlap descent for the cyclic (3,5) witness, using sets only."""
from collections import defaultdict
from itertools import combinations
from ramsey_blue_pair_transport import blue


def main():
    vertices = range(13)
    neighborhoods = [frozenset(t) for k in range(14) for t in combinations(vertices, k)
                     if all(blue(x, y) for x, y in combinations(t, 2))]
    blocks = [s for s in neighborhoods if len(s) == 4]
    completions = defaultdict(set)
    for s in blocks:
        for x in s:
            completions[s - {x}].add(x)
    assert all(len(c) == 2 and not blue(*c) for c in completions.values())
    for n in neighborhoods:
        for start in blocks:
            s = start
            while s & n:
                x = min(s & n)
                y, = completions[s - {x}] - {x}
                nxt = (s - {x}) | {y}
                assert y not in n and len(nxt & n) == len(s & n) - 1
                s = nxt
            assert s in blocks and s.isdisjoint(n)
    print(len(neighborhoods), 'triangle-safe neighborhoods;', len(blocks), 'starting blocks; all descents verified.')

if __name__ == '__main__': main()
