"""Find the least module containing each pair in each of the eight completions."""
from collections import Counter
from itertools import combinations
from ramsey_blind_start_formulas import seed, check


def closure(rows, i, j):
    group = (1 << i) | (1 << j)
    while True:
        more = sum(1 << v for v, row in enumerate(rows)
                   if not group >> v & 1 and 0 < (row & group) < group)
        if not more:
            return group
        group |= more


def main():
    rows, _, _ = seed(7, 'double')
    free = [(0, 5), (1, 6), (2, 7)]  # a1-b3, a2-b4, a3-b5
    for m in range(8):
        r = rows.copy()
        for t, (i, j) in enumerate(free):
            for x, y in ((i, j), (j, i)):
                r[x] = (r[x] & ~(1 << y)) | ((m >> t & 1) << y)
        assert check(r, 7)
        sizes = Counter(closure(r, i, j).bit_count() for i, j in combinations(range(len(r)), 2))
        print(m, dict(sizes))

if __name__ == '__main__':
    main()
