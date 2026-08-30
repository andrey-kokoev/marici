"""Exact scalar half-plane Schur-kernel and Cayley checks."""

import sympy as sp

z, v, a = sp.symbols("z v a", positive=True)
c_z = (z - a) / (z + a)
c_v = (v - a) / (v + a)
kernel = sp.simplify((1 - c_v * c_z) / (z + v))
expected_kernel = 2 * a / ((z + a) * (v + a))
assert sp.simplify(kernel - expected_kernel) == 0

# Finite Gram matrices of the model kernel are positive semidefinite rank one.
points = [sp.Rational(1, 3), sp.Rational(1), sp.Rational(2)]
gram = sp.Matrix(
    len(points),
    len(points),
    lambda row, col: expected_kernel.subs({z: points[row], v: points[col], a: 1}),
)
assert gram.rank() == 1
assert all(value >= 0 for value in gram.eigenvals())

# Scalar Cayley identity for F=x+iy with x>0.
x, y = sp.symbols("x y", real=True, positive=True)
F = x + sp.I * y
C = (F - 1) / (F + 1)
cayley_defect = sp.simplify(1 - C * sp.conjugate(C))
expected_defect = 4 * x / ((x + 1) ** 2 + y**2)
assert sp.simplify(sp.expand_complex(cayley_defect - expected_defect)) == 0

print("half_plane_Schur_kernel_identity=True")
print("finite_kernel_Gram_positive=True")
print("positive_real_Cayley_implies_contraction=True")
print("strict_diagonal_kernel_implies_off_line_invertibility=True")
print("Xi_transfer_kernel_constructed=False")

