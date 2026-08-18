#!/usr/bin/env python3
"""Compute the A3 miniversal discriminant without a CAS dependency."""

import itertools
import json


ZERO = {}
ONE = {(0, 0, 0): 1}  # monomials are powers of (t0,t1,t2)
t0 = {(1, 0, 0): 1}
t1 = {(0, 1, 0): 1}
t2 = {(0, 0, 1): 1}


def add(left, right):
    out = dict(left)
    for m, c in right.items():
        out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}


def scale(c, poly):
    return {m: c * v for m, v in poly.items() if c * v}


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            m = tuple(a + b for a, b in zip(lm, rm))
            out[m] = out.get(m, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


def determinant(matrix):
    n = len(matrix)
    total = ZERO
    for perm in itertools.permutations(range(n)):
        term = ONE
        for row, col in enumerate(perm):
            term = mul(term, matrix[row][col])
            if not term:
                break
        if not term:
            continue
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        total = add(total, scale(-1 if inversions % 2 else 1, term))
    return total


# Sylvester matrix of f=a^4+t2*a^2+t1*a+t0 and f'.
f = [ONE, ZERO, t2, t1, t0]
fp = [scale(4, ONE), ZERO, scale(2, t2), t1]
matrix = []
for shift in range(3):
    matrix.append([ZERO] * shift + f + [ZERO] * (2 - shift))
for shift in range(4):
    matrix.append([ZERO] * shift + fp + [ZERO] * (3 - shift))
disc = determinant(matrix)

expected = {}
for coefficient, powers in [
    (256, (3, 0, 0)),
    (-128, (2, 0, 2)),
    (144, (1, 2, 1)),
    (-27, (0, 4, 0)),
    (16, (1, 0, 4)),
    (-4, (0, 2, 3)),
]:
    expected[powers] = coefficient
assert disc == expected

print(json.dumps({
    "miniversal_family": "a^4+t2*a^2+t1*a+t0",
    "discriminant": "256*t0^3-128*t2^2*t0^2+144*t2*t1^2*t0-27*t1^4+16*t2^4*t0-4*t2^3*t1^2",
    "required_source_map": "J: positive physical regulator cone -> (t0,t1,t2)",
    "uniqueness_gate": "J(cone) must determine one homotopy class in the discriminant complement",
}, indent=2))
