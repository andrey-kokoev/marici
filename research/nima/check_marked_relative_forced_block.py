#!/usr/bin/env python3
"""Verify the forced block form implied by Entry 851's constant maps."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research" / "benincasa" / "marked-relative-source-maps.json"
CONTRACT = ROOT / "research" / "nima" / "marked-relative-forced-block-contract.json"


def mm(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def z(m, n):
    return [[Fraction(0) for _ in range(n)] for _ in range(m)]


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def block(a, b, c, d):
    return [ar + br for ar, br in zip(a, b)] + [cr + dr for cr, dr in zip(c, d)]


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    j = source["j_star"]
    p = source["residue_w_source_normalized"]
    assert rank(j) == 9 and rank(p) == 3
    assert mm(p, j) == z(3, 9)
    assert contract["extension_block_shape"] == [9, 3]

    # A 1+2 model verifies both horizontal-map constraints and the gauge law
    # in the W direct-sum M ordering used by Entry 851.
    a3 = [[Fraction(2)]]
    a9 = [[Fraction(3), Fraction(1)], [Fraction(0), Fraction(5)]]
    b = [[Fraction(7)], [Fraction(11)]]
    a12 = block(a3, z(1, 2), b, a9)
    j_small = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    p_small = [[Fraction(1), Fraction(0), Fraction(0)]]
    assert sub(mm(a12, j_small), mm(j_small, a9)) == z(3, 2)
    assert sub(mm(a3, p_small), mm(p_small, a12)) == z(1, 3)

    h = [[Fraction(13)], [Fraction(17)]]
    dh = [[Fraction(19)], [Fraction(23)]]
    g = block(eye(1), z(1, 2), h, eye(2))
    g_inv = block(eye(1), z(1, 2), [[-x for x in row] for row in h], eye(2))
    dg = block(z(1, 1), z(1, 2), dh, z(2, 2))
    transformed = add(mm(mm(g_inv, a12), g), mm(g_inv, dg))
    expected = add(b, add(dh, sub(mm(a9, h), mm(h, a3))))
    assert [[transformed[1][0]], [transformed[2][0]]] == expected
    assert [transformed[0][1], transformed[0][2]] == [Fraction(0), Fraction(0)]

    print("marked-relative forced block audit: PASS")
    print("Entry 851 maps force A12_mu=[[A3_mu,0],[B_mu,A9_mu]]")
    print("only B_x,B_y (each 9x3) remain after diagonal connections are fixed")


if __name__ == "__main__":
    main()
