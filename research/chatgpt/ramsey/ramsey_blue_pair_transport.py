"""Alternate the two exchanges with a fixed blue pair in the cyclic (3,5) witness."""
from collections import Counter
from itertools import combinations


def blue(i, j):
    return (i-j) % 13 not in (0, 1, 5, 8, 12)


def main():
    histogram = Counter()
    for i, j in combinations(range(13), 2):
        if not blue(i, j):
            continue
        pool = [x for x in range(13) if blue(i, x) and blue(j, x)]
        starts = [(x, y) for x in pool for y in pool if blue(x, y)]
        m = len(pool)
        for start in starts:
            slots = list(start)
            seen = {frozenset(slots)}
            for step in range(1, 2*m+1):
                s = (step-1) % 2
                replacement, = [x for x in pool if x != slots[s] and blue(x, slots[1-s])]
                slots[s] = replacement
                if step < m:
                    assert frozenset(slots) not in seen
                    seen.add(frozenset(slots))
                if step == m:
                    assert tuple(slots) == (start[::-1] if m%2 else start)
                if step < (2 if m%2 else 1)*m:
                    assert tuple(slots) != start
            assert tuple(slots) == start
        histogram[m] += 1
    assert histogram == {4:26, 5:26}
    print(histogram)

if __name__ == '__main__':
    main()
