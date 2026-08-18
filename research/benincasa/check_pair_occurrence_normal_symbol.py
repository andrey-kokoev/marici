"""Audit the labelled pair-occurrence to square-free normal discriminant symbol."""

import sympy as sp

x, y, z = sp.symbols("x y z")
l1 = x - y - z
l2 = x - y + z
l3 = x + y - z
l4 = x + y + z

c12 = 4 * l1**2 * l2**2 * l3 * l4
c13 = 4 * l1**2 * l2 * l3**2 * l4
c23m = -4 * l1 * l2**2 * l3**2 * l4
c23p = -4 * l1**2 * l2 * l3 * l4**2

# Columns: [12], [13], [23], [2,23], [3,23].
# Rows: nu1 nu2, nu1 nu3, nu2 nu3.
matrix = sp.Matrix(
    [
        [c12, 0, 0, 0, 0],
        [0, c13, 0, 0, 0],
        [0, 0, c23m, c23p, c23p],
    ]
)

k_same_plus = sp.Matrix([0, 0, 0, 1, -1])
k_signed = sp.Matrix([0, 0, c23p, -c23m, 0])

assert matrix * k_same_plus == sp.zeros(3, 1)
assert matrix * k_signed == sp.zeros(3, 1)
assert matrix.rank() == 3
assert sp.Matrix.hstack(k_same_plus, k_signed).rank() == 2

q_quartic = -16 * (x * y) ** 2 - 8 * x * y * (x + y + z) ** 2
q_quartic += 8 * (x + y) * (x + y + z) ** 3 - 5 * (x + y + z) ** 4
assert all(sp.gcd(coefficient, q_quartic) == 1 for coefficient in (c12, c13, c23m, c23p))

print("PAIR_OCCURRENCE_NORMAL_SYMBOL_RANK=3")
print("KERNEL_DIMENSION=2")
print("KERNEL_1=[2,23]-[3,23]")
print("KERNEL_2=C23plus*[23]-C23minus*[2,23]")
print("ALL_NONZERO_COEFFICIENTS_Q_COPRIME=true")
