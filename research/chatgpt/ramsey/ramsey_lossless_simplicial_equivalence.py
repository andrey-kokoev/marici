"""Enumerate ALL two-colorings of K_N for N<=6.

The canonical two-color flag-complex representation adds no conditions:
- A-clique simplices are all cliques of the A-edge graph.
- B-clique simplices are all cliques of the complementary graph.
- The two marked 1-skeleta recover the original edge colors exactly.
Also checks exact vertex-extension equivalence.
"""
from itertools import combinations


def pairs(n):
    return list(combinations(range(n), 2))


def admissible(n, bits, p=3, q=3):
    E = pairs(n)
    mask = {(i, j): (bits >> k) & 1 for k, (i, j) in enumerate(E)}
    for r, color in [(p, 1), (q, 0)]:
        for S in combinations(range(n), r):
            if all(mask[(i, j)] == color for i, j in combinations(S, 2)):
                return False
    return True


def admissible_new_vertex(n, bits, contact_mask, p=3, q=3):
    # bit=1 means A; contact_mask specifies A-connections from new vertex n.
    D = {(i, j): (bits >> k) & 1 for k, (i, j) in enumerate(pairs(n))}
    D.update({(i, n): (contact_mask >> i) & 1 for i in range(n)})
    full = sum(D[(i, j)] << k for k, (i, j) in enumerate(pairs(n + 1)))
    return admissible(n + 1, full, p, q)


def link_extension(n, bits, contact_mask, p=3, q=3):
    # Only checks new forbidden monochrome simplices. Assumes base admissible.
    E = pairs(n)
    D = {(i, j): (bits >> k) & 1 for k, (i, j) in enumerate(E)}
    S = [i for i in range(n) if (contact_mask >> i) & 1]
    T = [i for i in range(n) if not ((contact_mask >> i) & 1)]
    good_A = all(not all(D[(i, j)] for i, j in combinations(group, 2))
                 for group in combinations(S, p - 1))
    good_B = all(not all(not D[(i, j)] for i, j in combinations(group, 2))
                 for group in combinations(T, q - 1))
    return good_A and good_B


if __name__ == '__main__':
    for n in range(1, 7):
        good = [x for x in range(1 << len(pairs(n))) if admissible(n, x)]
        print(f'n={n}: all={1 << len(pairs(n))}, admissible={len(good)}')
        if n <= 5:
            ext = 0
            extendible = 0
            for bits in good:
                count = 0
                for S in range(1 << n):
                    assert admissible_new_vertex(n, bits, S) == link_extension(n, bits, S)
                    count += link_extension(n, bits, S)
                ext += count
                extendible += (count > 0)
            print(f'  extendible bases={extendible}/{len(good)}; total extensions={ext}')
        if n == 4:
            from collections import Counter
            classes = Counter()
            for bits in good:
                deg = tuple(sorted(sum((bits >> k) & 1
                                       for k, (i, j) in enumerate(pairs(n))
                                       if v in (i, j)) for v in range(n)))
                exts = sum(link_extension(n, bits, S) for S in range(1 << n))
                classes[(deg, exts)] += 1
            assert classes == {
                ((1, 1, 2, 2), 1): 12,  # A=P4
                ((1, 1, 1, 1), 0): 3,  # A=2K2
                ((2, 2, 2, 2), 0): 3,  # A=C4
            }
            print('  classified: 12 A=P4 extend; 3 A=2K2 and 3 A=C4 cannot extend')
        if n == 5:
            assert len(good) == 12
            for bits in good:
                A = {(i, j) for k, (i, j) in enumerate(pairs(n)) if (bits >> k) & 1}
                assert len(A) == 5
                assert all(sum(((min(i, j), max(i, j)) in A) for j in range(n) if i != j) == 2
                           for i in range(n))
        if n == 6:
            assert len(good) == 0
    print('PASS: lossless edge labeling; no spurious extension condition; R(3,3)=6')
