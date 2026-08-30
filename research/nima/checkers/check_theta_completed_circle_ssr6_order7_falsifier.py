"""General Wronskian coefficients, SSR6 induction, and order-7 witness."""

from decimal import Decimal as D
from decimal import getcontext
from math import comb


def odd_double_factorial(r):
    value = 1
    for k in range(1, 2 * r + 2, 2):
        value *= k
    return value


def boundary_q(n, boundary=3):
    return sum(
        (-1) ** r
        * comb(n, r)
        * (2 * boundary) ** (n - r)
        * odd_double_factorial(r)
        for r in range(n + 1)
    )


expected_q = [3, 15, 57, 369, 891, 15903, -78975]
assert [boundary_q(n) for n in range(1, 8)] == expected_q

# Coefficient-level verification of dQ_n/dz_i = 2 Q_(n-1):
# the coefficient of e_l after differentiating e_(l+1) equals twice
# the coefficient of e_l at order n-1.
for n in range(2, 9):
    for ell in range(n):
        derivative_coefficient = (
            (-1) ** (n - (ell + 1))
            * 2 ** (ell + 1)
            * odd_double_factorial(n - ell - 1)
        )
        lower_coefficient = (
            2
            * (-1) ** ((n - 1) - ell)
            * 2**ell
            * odd_double_factorial((n - 1) - ell)
        )
        assert derivative_coefficient == lower_coefficient

getcontext().prec = 220
PI = D(
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286"
)


def b(t, x):
    return t ** (D(5) / D(4)) * x * (2 * PI * t * x - 3) * (-PI * t * x).exp()


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum(
        ((-1) ** j)
        * a[0][j]
        * determinant([row[:j] + row[j + 1 :] for row in a[1:]])
        for j in range(len(a))
    )


ts = [D(1) + D(i) / D(1000) for i in range(7)]
continuous_xs = [D(1) + D(i) / D(1000) for i in range(7)]
discrete_xs = [D((i + 1) ** 2) for i in range(7)]

continuous_det = determinant([[b(t, x) for x in continuous_xs] for t in ts])
discrete_det = determinant([[b(t, x) for x in discrete_xs] for t in ts])

assert continuous_det > 0  # Wrong: order seven requires negative.
assert discrete_det < 0  # This particular physical-spectrum witness passes.

print("boundary Q values n=1..7:", expected_q)
print("continuous order-seven determinant:", continuous_det)
print("required order-seven sign:", -1)
print("discrete-square determinant sign:", (discrete_det > 0) - (discrete_det < 0))
print("PASS: global SSR6; continuous SSR7 has a finite wrong-sign minor")
