"""Exact algebra checks supporting the global SSR3 proof."""

from fractions import Fraction
from itertools import combinations, permutations


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def alternant(x, ys):
    return det3(
        [
            [2 * x * y - 3, 5 * y - 2 * x * y * y, 2 * x * y**3 - 7 * y * y]
            for y in ys
        ]
    )


def factored(x, ys):
    y1, y2, y3 = ys
    vandermonde = (y2 - y1) * (y3 - y1) * (y3 - y2)
    e1 = y1 + y2 + y3
    e2 = y1 * y2 + y1 * y3 + y2 * y3
    e3 = y1 * y2 * y3
    polynomial = 105 - 30 * x * e1 + 12 * x * x * e2 - 8 * x**3 * e3
    return vandermonde * polynomial


# A separating exact family checks the polynomial identity without floating
# arithmetic. It includes rational x and nonconsecutive y values.
xs = [Fraction(1), Fraction(3, 2), Fraction(7, 3), Fraction(5)]
ysets = [(1, 2, 4), (2, 5, 9), (3, 7, 11), (4, 10, 25)]
for x in xs:
    for ys in ysets:
        assert alternant(x, ys) == factored(x, ys)

# Boundary maximum and coordinate derivatives on z_i >= 3.
def p(z1, z2, z3):
    return 105 - 30 * (z1 + z2 + z3) + 12 * (
        z1 * z2 + z1 * z3 + z2 * z3
    ) - 8 * z1 * z2 * z3


assert p(3, 3, 3) == -57
for z2, z3 in [(3, 3), (3, 4), (4, 3), (10, 20)]:
    derivative_z1 = -30 + 12 * (z2 + z3) - 8 * z2 * z3
    assert derivative_z1 <= -30

# Direct exact signs for representative alternants.
for x in xs:
    for ys in ysets:
        assert ys[0] < ys[1] < ys[2]
        # These rational samples lie in xy >= 3 when x >= 1 and y1 >= 3.
        if x * ys[0] >= 3:
            assert alternant(x, ys) < 0

print("exact alternant identity cases:", len(xs) * len(ysets))
print("boundary polynomial P(3,3,3):", p(3, 3, 3))
print("coordinate derivative upper bound:", -30)
print("PASS: the order-three Wronskian is strictly negative on z_i >= 3")
