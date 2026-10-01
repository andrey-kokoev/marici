"""Exact dynamics checks for comparison projections and a reversible extension.

The extension is an added model choice. Projection updates themselves contain
neither inertia nor a physical clock. Uses only Python's standard library.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy

source = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = source['rows']
N = 6

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def mv(A, x):
    return [dot(row, x) for row in A]

# The existing projection divides each row by its squared norm. Thus its
# weak-update generator uses A, not the unnormalized H from equal storage.
A = [[sum(F(r[i]*r[j], dot(r, r)) for r in rows)
      for j in range(N)] for i in range(N)]
a, b, c = A[0][0], A[0][1], A[0][3]
assert A == [[a if i == j else b if i//3 == j//3 else c
              for j in range(N)] for i in range(N)]
eigenvalues = [a+2*b+3*c, a+2*b-3*c] + [a-b]*4
for (_, v), lam in zip(source['modes'], eigenvalues):
    assert mv(A, v) == [lam*x for x in v]
assert sum(eigenvalues) == 153
assert all(lam > 0 for lam in eigenvalues)

# A full projection loses information: P_r r = 0.
r = rows[0]
assert [x - F(t*dot(r, r), dot(r, r)) for x, t in zip(r, r)] == [0]*N

# Reversible, symplectic discrete extension:
# p' = p - eta*A*q; q' = q + eta*p'.
# Its EXACT quadratic invariant is
# I = (p.p + q.A.q - eta*q.A.p)/2.
# It is positive definite iff eta^2*lambda_max < 4.
eta = F(1, 10)
assert eta**2 * max(eigenvalues) < 4

def invariant(q, p):
    return (dot(p, p) + dot(q, mv(A, q)) - eta*dot(q, mv(A, p)))/2

q = list(map(F, [1, 0, -1, 2, 0, 1]))
p = list(map(F, [0, 1, 0, -1, 1, 0]))
initial = invariant(q, p)
for _ in range(12):
    oldq, oldp = q, p
    p = [x-eta*y for x, y in zip(p, mv(A, q))]
    q = [x+eta*y for x, y in zip(q, p)]
    assert invariant(q, p) == initial
    recovered_q = [x-eta*y for x, y in zip(q, p)]
    recovered_p = [x+eta*y for x, y in zip(p, mv(A, recovered_q))]
    assert (recovered_q, recovered_p) == (oldq, oldp)

print('Normalized projection generator entries:', a, b, c)
print('Normalized spectrum:', ', '.join(map(str, eigenvalues)))
print('Projection is singular; its mean weak-update dynamics is relaxation.')
print('Added reversible extension: exact invariant and inverse checked for 12 steps.')
print('eta=1/10 is a test choice. Clock duration and physical energy scale remain inputs.')
