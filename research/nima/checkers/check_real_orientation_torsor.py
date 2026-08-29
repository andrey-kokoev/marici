from fractions import Fraction


c_plus = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(-1)),
)
c_minus = (
    (Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
identity = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def apply(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


# Both realifications are orthogonal involutions with identical trace and
# determinant data.
for real_structure in (c_plus, c_minus):
    assert multiply(real_structure, real_structure) == identity
    assert real_structure[0][0] + real_structure[1][1] == 0
    determinant = real_structure[0][0] * real_structure[1][1]
    assert determinant == -1

real_anchor = (Fraction(1), Fraction(0))
assert apply(c_plus, real_anchor) == real_anchor
assert apply(c_minus, real_anchor) == (-real_anchor[0], -real_anchor[1])

print("isometry and involutivity: do not select a Real orientation")
print("local orientations: C2 torsor")
print("source anchor: separates the two Real frames")
