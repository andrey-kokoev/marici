"""Check the two completions of every blue triple in the cyclic (3,5) witness."""
from itertools import combinations
from collections import Counter


def main():
    vertices = set(range(13))
    red = {v: {(v+d) % 13 for d in (-5, -1, 1, 5)} for v in vertices}
    def blue(s):
        return all(v not in red[u] for u, v in combinations(s, 2))
    incidence = Counter()
    for triple in combinations(range(13), 3):
        if not blue(triple):
            continue
        ends = sorted(v for v in vertices.difference(triple) if blue((*triple, v)))
        assert len(ends) == 2 and ends[1] in red[ends[0]]
        for v in ends:
            incidence[tuple(sorted((*triple, v)))] += 1
        if triple == (0, 2, 4):
            print(triple, '->', ends)
    assert len(incidence) == 39 and set(incidence.values()) == {4}
    assert sum(incidence.values()) // 2 == 78
    print('78 blue triples; 39 blue four-sets; two red-adjacent completions per triple')

if __name__ == '__main__':
    main()
