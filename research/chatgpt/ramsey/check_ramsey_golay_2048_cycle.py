#!/usr/bin/env python3
"""Exact GF(2) checks for the 7 -> 23 / 2047 -> 2048 distinctions.

This does not derive a Ramsey-number formula or a source-selected Golay promotion.
"""
from itertools import combinations

F = (1 << 11) | (1 << 9) | (1 << 7) | (1 << 6) | (1 << 5) | (1 << 1) | 1
DEGREE = 11
SIZE = 1 << DEGREE


def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & SIZE:
            a ^= F
    return z


def power(a, n):
    r = 1
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r


def rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            i = v.bit_length() - 1
            if i not in pivots:
                pivots[i] = v
                break
            v ^= pivots[i]
    return len(pivots)


def cycshift(v, n):
    return ((v << 1) & ((1 << n) - 1)) | (v >> (n - 1))


def check_seven():
    x = sum(1 << j for j in (0, 2, 4))
    shifts = []
    for _ in range(7):
        shifts.append(x)
        x = cycshift(x, 7)
    assert rank(shifts) == 7
    xor_sum = 0
    for v in shifts:
        xor_sum ^= v
    assert xor_sum == 127
    # The quotient by all-ones is represented by eliminating the last coordinate.
    h = [v ^ (127 if v & (1 << 6) else 0) for v in shifts]
    assert rank(h) == 6
    values = set()
    for t in range(4):
        for indices in combinations(range(7), t):
            s = 0
            for i in indices:
                s ^= h[i]
            values.add(s)
    assert len(values) == 64
    print('Seven-position cyclic quotient: 7 translates; rank 7 -> quotient rank 6; 64 unique <=3 sums.')


def check_23():
    zeta, g = 2, 1 ^ 2
    assert power(zeta, 23) == 1 and zeta != 1
    assert power(g, 2047) == 1
    assert power(g, 23) != 1 and power(g, 89) != 1
    assert rank([power(zeta, j) for j in range(23)]) == 11
    syndromes = set()
    cols = [power(zeta, j) for j in range(23)]
    for t in range(4):
        for indices in combinations(range(23), t):
            s = 0
            for i in indices:
                s ^= cols[i]
            assert s not in syndromes
            syndromes.add(s)
    assert len(syndromes) == SIZE
    print('23 cyclic columns: rank 11; 2048 distinct <=3 syndromes; [23,12,7] perfect code.')
    nonzero = []
    v = 1
    for _ in range(SIZE - 1):
        assert v not in nonzero  # tiny exact check
        nonzero.append(v)
        v = mul(v, g)
    assert v == 1 and len(set(nonzero)) == SIZE - 1
    print('U=I+T, T(v)=zeta*v: nonzero orbit has 2047 states; zero is fixed.')
    def successor(v):
        if v == 0:
            return 1
        if v == power(g, SIZE - 2):
            return 0
        return mul(v, g)
    seen = set()
    v = 0
    for _ in range(SIZE):
        assert v not in seen
        seen.add(v)
        v = successor(v)
    assert v == 0 and len(seen) == SIZE
    assert successor(0) != 0
    print('After two-transition nonlinear splice: one 2048-state cycle, returning to 0.')
    print('Splice is an extra choice and does NOT follow from the original R/G/0 primitive.')


if __name__ == '__main__':
    check_seven()
    check_23()
    print('PASS')
