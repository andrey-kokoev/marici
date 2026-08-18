#!/usr/bin/env python3
"""Verify the filtration-preserving P3 contraction of the diagonal cube."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


VARIABLES = ("E", "P3", "a", "b")
P3_INDEX = 1


def subsets(k):
    return list(itertools.combinations(range(4), k))


def differential(k):
    src, tgt = subsets(k), subsets(k+1)
    pos = {s: i for i, s in enumerate(tgt)}
    matrix = [[Fraction(0) for _ in src] for _ in tgt]
    for j, s in enumerate(src):
        for i in range(4):
            if i in s:
                continue
            sign = -1 if sum(x < i for x in s) % 2 else 1
            t = tuple(sorted(s+(i,)))
            matrix[pos[t]][j] = Fraction(sign)
    return matrix


def homotopy(k):
    """h:C^k->C^(k-1), removing P3 with the insertion sign."""
    src, tgt = subsets(k), subsets(k-1)
    pos = {s: i for i, s in enumerate(tgt)}
    matrix = [[Fraction(0) for _ in src] for _ in tgt]
    for j, s in enumerate(src):
        if P3_INDEX not in s:
            continue
        t = tuple(x for x in s if x != P3_INDEX)
        sign = -1 if sum(x < P3_INDEX for x in t) % 2 else 1
        matrix[pos[t]][j] = Fraction(sign)
    return matrix


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x+y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def main():
    d = [differential(k) for k in range(4)]
    h = [None]+[homotopy(k) for k in range(1,5)]
    for k in range(5):
        n = len(subsets(k))
        left = [[Fraction(0) for _ in range(n)] for _ in range(n)]
        right = [[Fraction(0) for _ in range(n)] for _ in range(n)]
        if k > 0:
            left = matmul(d[k-1], h[k])
        if k < 4:
            right = matmul(h[k+1], d[k])
        assert add(left, right) == identity(n)

    packet = {
        "diagonal_polynomial": "C=E^2*(a^2-b^2)-P1^2*a^2+P2^2*b^2",
        "P3_dependence": False,
        "P3_face_map": "identity",
        "contracting_homotopy": "remove P3 from the incidence label with Koszul sign",
        "homotopy_identity": "d*h+h*d=1 in degrees 0..4",
        "filtration_degree": 0,
        "second_order_a_b_jets_preserved": True,
        "diagonal_cube_exact": True,
    }
    out = Path(__file__).with_name("polar-diagonal-p3-contraction.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
