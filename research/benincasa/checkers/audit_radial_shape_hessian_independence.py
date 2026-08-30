#!/usr/bin/env python3
"""Exact gate: radial second-jet data does not determine the A2 shape Hessian."""

from fractions import Fraction as F


def mv(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(x) for x in zip(*a)]


P = [[F(0), F(0), F(1)], [F(1), F(0), F(0)], [F(0), F(1), F(0)]]
I = [[F(i == j) for j in range(3)] for i in range(3)]
J3 = [[F(1) for _ in range(3)] for _ in range(3)]
H_shape = I
H_radial = [[x / 3 for x in row] for row in J3]

n = [F(1), F(1), F(1)]
b1 = [F(1), F(-1), F(0)]
b2 = [F(0), F(1), F(-1)]


def q(h, x):
    return dot(x, mv(h, x))


checks = {
    "both_hessians_are_cyclic": all(mm(mm(tr(P), h), P) == h for h in [H_shape, H_radial]),
    "radial_second_responses_agree": q(H_shape, n) == q(H_radial, n) == 3,
    "radial_shape_mixed_terms_vanish": all(dot(n, mv(h, b)) == 0 for h in [H_shape, H_radial] for b in [b1, b2]),
    "shape_second_responses_disagree": q(H_shape, b1) == 2 and q(H_radial, b1) == 0,
    "second_shape_direction_replicates": q(H_shape, b2) == 2 and q(H_radial, b2) == 0,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"common radial value: {q(H_shape, n)}")
print(f"shape values: {(q(H_shape, b1), q(H_radial, b1))}")
