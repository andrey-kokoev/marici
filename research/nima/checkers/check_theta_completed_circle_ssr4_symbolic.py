"""Exact algebra checks supporting the global SSR4 theorem."""

from fractions import Fraction


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum(
        ((-1) ** j)
        * a[0][j]
        * determinant([row[:j] + row[j + 1 :] for row in a[1:]])
        for j in range(len(a))
    )


def alternant(x, ys):
    return determinant(
        [
            [
                2 * x * y - 3,
                5 * y - 2 * x * y**2,
                2 * x * y**3 - 7 * y**2,
                9 * y**3 - 2 * x * y**4,
            ]
            for y in ys
        ]
    )


def elementary(ys):
    e1 = sum(ys)
    e2 = sum(ys[i] * ys[j] for i in range(4) for j in range(i + 1, 4))
    e3 = sum(
        ys[i] * ys[j] * ys[k]
        for i in range(4)
        for j in range(i + 1, 4)
        for k in range(j + 1, 4)
    )
    e4 = ys[0] * ys[1] * ys[2] * ys[3]
    return e1, e2, e3, e4


def factored(x, ys):
    vandermonde = 1
    for i in range(4):
        for j in range(i + 1, 4):
            vandermonde *= ys[j] - ys[i]
    e1, e2, e3, e4 = elementary(ys)
    polynomial = (
        945
        - 210 * x * e1
        + 60 * x**2 * e2
        - 24 * x**3 * e3
        + 16 * x**4 * e4
    )
    return vandermonde * polynomial


xs = [Fraction(1), Fraction(4, 3), Fraction(5, 2), Fraction(4)]
ysets = [(1, 2, 4, 8), (2, 5, 9, 14), (3, 7, 11, 20), (4, 10, 25, 31)]
for x in xs:
    for ys in ysets:
        assert alternant(x, ys) == factored(x, ys)


def p4(zs):
    e1, e2, e3, e4 = elementary(zs)
    return 945 - 210 * e1 + 60 * e2 - 24 * e3 + 16 * e4


assert p4((3, 3, 3, 3)) == 369

# First partial at the boundary of the other three variables.
first_partial_boundary = -210 + 60 * 9 - 24 * 27 + 16 * 27
assert first_partial_boundary == 114

# Derivative of that partial in one remaining coordinate at b=c=3.
second_partial_boundary = 60 - 24 * 6 + 16 * 9
assert second_partial_boundary == 60

for x in xs:
    for ys in ysets:
        if x * ys[0] >= 3:
            assert alternant(x, ys) > 0

print("exact alternant identity cases:", len(xs) * len(ysets))
print("P4 boundary minimum:", p4((3, 3, 3, 3)))
print("first-partial boundary minimum:", first_partial_boundary)
print("second-partial boundary minimum:", second_partial_boundary)
print("PASS: the order-four Wronskian is strictly positive on z_i >= 3")
