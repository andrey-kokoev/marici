from fractions import Fraction


def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )


a = Fraction(2)
h = Fraction(5)


def minimal_transfer(s):
    return Fraction(1) - a / s


def augmented_transfer(s):
    # The hidden mode has zero input and output incidence.
    return Fraction(1) - a / s


def augmented_pencil(s):
    return (
        (s, 0, -1),
        (0, s - h, 0),
        (-a, 0, 1),
    )


for s in [Fraction(1), Fraction(3), Fraction(7)]:
    assert minimal_transfer(s) == augmented_transfer(s)
    assert determinant_3x3(augmented_pencil(s)) == (s - h) * (s - a)

assert augmented_transfer(h) != 0
assert determinant_3x3(augmented_pencil(h)) == 0

print("hidden mode leaves the transfer function unchanged")
print("raw Rosenbrock determinant gains the hidden factor s-h")
print("minimality or reduced Fitting data are mandatory")
