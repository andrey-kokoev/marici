#!/usr/bin/env python3
"""Exact audit: the A2 norm exists, but linear source transport cannot activate it."""

from fractions import Fraction as F


def kron(x, y):
    return [a * b for a in x for b in y]


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


e1 = [F(1), F(0)]
e2 = [F(0), F(1)]
e12 = add(e1, e2)

# Any linear diagonal agreeing with v -> v tensor v on the basis would obey
# Delta(e1+e2)=Delta(e1)+Delta(e2).  The actual quadratic diagonal has two
# nonzero cross terms, giving an exact contradiction.
linear_prediction = add(kron(e1, e1), kron(e2, e2))
quadratic_diagonal = kron(e12, e12)
copy_defect = [a - b for a, b in zip(quadratic_diagonal, linear_prediction)]

# The source metric itself is unobstructed and nondegenerate.
C = [[F(2), F(-1)], [F(-1), F(2)]]
det_C = C[0][0] * C[1][1] - C[0][1] * C[1][0]
q1 = sum(e1[i] * C[i][j] * e1[j] for i in range(2) for j in range(2))
q2 = sum(e2[i] * C[i][j] * e2[j] for i in range(2) for j in range(2))
q12 = sum(e12[i] * C[i][j] * e12[j] for i in range(2) for j in range(2))
polar_cross = q12 - q1 - q2

# No linear scalar can equal the quadratic norm: values at e1,e2 force its
# value at e1+e2 by additivity, contradicting the Cartan norm.
linear_scalar_prediction = q1 + q2

checks = {
    "source_metric_is_nondegenerate": det_C == 3,
    "quadratic_norm_is_nonzero": q1 == 2 and q2 == 2 and q12 == 2,
    "quadratic_diagonal_is_not_linear": copy_defect == [0, 1, 1, 0],
    "polarization_detects_cross_term": polar_cross == -2,
    "no_linear_scalar_realizes_the_norm": linear_scalar_prediction != q12,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"copy defect: {copy_defect}")
print(f"Cartan norms q(e1), q(e2), q(e1+e2): {(q1, q2, q12)}")
