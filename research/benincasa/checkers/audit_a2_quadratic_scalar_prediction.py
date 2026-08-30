#!/usr/bin/env python3
"""Exact hostile test for the first cyclic scalar on the A2 occurrence sector."""

from fractions import Fraction as F


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(x) for x in zip(*a)]


def mv(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0]) if a else 0):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


R = [[F(0), F(-1)], [F(1), F(-1)]]
I = [[F(1), F(0)], [F(0), F(1)]]
C = [[F(2), F(-1)], [F(-1), F(2)]]

# Invariant covectors h obey hR=h.  The two equations have full rank.
linear_constraints = [[R[j][i] - I[j][i] for j in range(2)] for i in range(2)]
linear_invariant_dimension = 2 - rank(linear_constraints)

# For S=[[a,b],[b,d]], impose R^T S R-S=0 and compute the exact rank.
basis_symmetric = [
    [[F(1), F(0)], [F(0), F(0)]],
    [[F(0), F(1)], [F(1), F(0)]],
    [[F(0), F(0)], [F(0), F(1)]],
]
quadratic_constraints = []
for i, j in [(0, 0), (0, 1), (1, 1)]:
    quadratic_constraints.append([
        (mm(mm(tr(R), s), R)[i][j] - s[i][j]) for s in basis_symmetric
    ])
quadratic_invariant_dimension = 3 - rank(quadratic_constraints)

root = [F(1), F(0)]
orbit = [root]
for _ in range(2):
    orbit.append(mv(R, orbit[-1]))
root_norms = [sum(x[i] * C[i][j] * x[j] for i in range(2) for j in range(2))
              for x in orbit]

# Site-coordinate observer L=3*pi_A2: y=3b on sum-zero vectors.
b = [F(2), F(-3), F(1)]
y = [3 * z for z in b]
observer_linear_sum = sum(y)
observer_norm_ratio = sum(z * z for z in y) / sum(z * z for z in b)

# A hostile anisotropic form must fail cyclic invariance.
S_bad = [[F(1), F(0)], [F(0), F(0)]]
anisotropic_defect = [[mm(mm(tr(R), S_bad), R)[i][j] - S_bad[i][j]
                       for j in range(2)] for i in range(2)]

checks = {
    "rotation_has_order_three": mm(mm(R, R), R) == I,
    "no_invariant_linear_covector": linear_invariant_dimension == 0,
    "unique_invariant_quadratic_form": quadratic_invariant_dimension == 1,
    "cartan_form_is_invariant": mm(mm(tr(R), C), R) == C,
    "root_orbit_has_constant_norm": root_norms == [F(2), F(2), F(2)],
    "cyclic_linear_aggregate_vanishes": observer_linear_sum == 0,
    "quadratic_observer_reconstructs_norm": observer_norm_ratio == 9,
    "anisotropic_quadratic_is_rejected": anisotropic_defect != [[0, 0], [0, 0]],
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"linear invariant dimension: {linear_invariant_dimension}")
print(f"quadratic invariant dimension: {quadratic_invariant_dimension}")
print(f"root norms: {root_norms}")
print(f"observer norm ratio: {observer_norm_ratio}")
