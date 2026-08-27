#!/usr/bin/env python3
"""Finite graded audit of the external five-cell controller."""


def mat_vec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


z = complex(0.4, 0.7)
alpha = 3.0
K = 1 / ((alpha - z) * (alpha + z))
xp = 1 / (alpha - z)
xm = 1 / (alpha + z)

# Controller coordinates: phi, constant, delta, centered-tail, PV.
a = [complex(2), complex(3), complex(5), complex(7), complex(11)]
i0 = [a[0] * K] + a[1:]
ip = [a[0] * xp] + a[1:]
im = [a[0] * xm] + a[1:]

dplus = [[0j] * 5 for _ in range(5)]
dminus = [[0j] * 5 for _ in range(5)]
dplus[0][0] = alpha + z
dminus[0][0] = alpha - z
for j in range(1, 5):
    dplus[j][j] = 1
    dminus[j][j] = 1

checks = {
    "positive_face_square": all(abs(x - y) < 1e-12 for x, y in zip(mat_vec(dplus, i0), ip)),
    "negative_face_square": all(abs(x - y) < 1e-12 for x, y in zip(mat_vec(dminus, i0), im)),
    "boundary_capabilities_retained": i0[1:] == a[1:] == ip[1:] == im[1:],
}

# Fourier action on phi, 1, delta, K, V.
F = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, -1],
    [0, 0, 0, 1, 0],
]
Fa = mat_vec(F, a)
checks["fourier_fixes_bulk_source_line"] = Fa[0] == a[0]
checks["fourier_preserves_boundary_subspace"] = Fa[1:] == [a[2], a[1], -a[4], a[3]]

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

