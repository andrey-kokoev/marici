from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _derive_gd_sympy import *


def derive(block, target, du, dv):
    return solve_target(block, target - 1, du, dv, False, False)[0]


rows = {
    6: derive("ee", 6, 5, 3),
    7: derive("ee", 7, 0, 3),
    8: derive("ee", 8, 0, 3),
    9: derive("ee", 9, 0, 3),
}
A = sp.Matrix([rows[index] for index in range(6, 10)])

c7 = sp.expand((X**2 - Y**2) * (X**2 * Y**2 - E**4))
c8 = sp.expand(2 * X**2 * (E**2 + Y**2))
c9 = sp.expand(-2 * Y**2 * (E**2 + X**2))
c = sp.Matrix([[0, c7, c8, c9]])
dc = c.applyfunc(lambda entry: sp.diff(entry, lam))
transport = (dc + c * A).applyfunc(sp.factor)
kappa = sp.factor(transport[0, 1] / c7)
mu = sp.factor(transport[0, 0])

print("KAPPA", kappa)
print("MU", mu)
print("KERNEL_CHECK_8", sp.factor(transport[0, 2] - kappa * c8))
print("KERNEL_CHECK_9", sp.factor(transport[0, 3] - kappa * c9))
print("F6", sp.factor(A[0, 0]))
print("H", sp.factor(K.subs({aa: 0, bb: 0})))
print("KAPPA_PLUS_HALF_DLOG_H", sp.factor(kappa + sp.diff(K.subs({aa: 0, bb: 0}), lam)/(2*K.subs({aa: 0, bb: 0}))))

# Does a change v -> v + g e6 split the rank-two algebraic kernel?  It solves
# g' + (f6-kappa)g = -mu.  Print the raw coefficients for exact inspection.
print("F6_MINUS_KAPPA", sp.factor(A[0, 0] - kappa))

# Contracted quotient matrix in (e7,e8,e9), plus trace/determinant diagnostics.
Bmat = A[1:, 1:]
print("B_TRACE", sp.factor(sp.trace(Bmat)))
print("B_DET", sp.factor(Bmat.det()))

u = E**2 + Y**2
v = E**2 + X**2
T = sp.Matrix([
    [0, 0],
    [1, 0],
    [u / 2, -v / 2],
    [v / 2, -X**2 * u / (2 * Y**2)],
])
rhs = A * T - T.applyfunc(lambda entry: sp.diff(entry, lam))
Tsel = T[1:3, :]
G = (Tsel.inv() * rhs[1:3, :]).applyfunc(sp.factor)
print("G00", G[0, 0])
print("G01", G[0, 1])
print("G10", G[1, 0])
print("G11", G[1, 1])
print("GYSIN_COMPAT", (T * G - rhs).applyfunc(sp.factor))

g00, g01, g10, g11 = G[0, 0], G[0, 1], G[1, 0], G[1, 1]
c1 = sp.diff(g00, lam) + g00**2 + g01 * g10
c2 = g00 * g01 + sp.diff(g01, lam) + g01 * g11
pf_p = sp.factor(-c2 / g01)
pf_q = sp.factor(-(c1 - c2 * g00 / g01))
Aell = (X - Y)**2 - 1
Bell = (X + Y)**2 - 1
published_p = (5 * Aell * Bell + 2 * (Aell + Bell)) / (lam * Aell * Bell)
published_q = (3 * (rho**2 - 1)**2 * lam**2 - 2 * (rho**2 + 1)) / (Aell * Bell)
print("PF_P", pf_p)
print("PF_Q", pf_q)
print("PF_P_DIFF", sp.factor(pf_p - published_p))
print("PF_Q_DIFF", sp.factor(pf_q - published_q))
