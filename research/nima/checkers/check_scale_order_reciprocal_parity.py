from fractions import Fraction

Lambda = ((Fraction(-1), 0), (0, Fraction(1)))
S = ((0, -1), (1, 0))
R = ((0, 1), (1, 0))


def multiply(a, b):
    return tuple(
        tuple(
            sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def subtract(a, b):
    return tuple(
        tuple(x - y for x, y in zip(row_a, row_b))
        for row_a, row_b in zip(a, b)
    )


def negate(a):
    return tuple(tuple(-x for x in row) for row in a)


def conjugate(a):
    return multiply(multiply(R, a), R)


virial = subtract(multiply(Lambda, S), multiply(S, Lambda))

assert conjugate(Lambda) == negate(Lambda)
assert conjugate(S) == negate(S)
assert conjugate(virial) == virial

both_reversed = subtract(
    multiply(negate(Lambda), negate(S)),
    multiply(negate(S), negate(Lambda)),
)
assert both_reversed == virial

order_only_reversed = subtract(
    multiply(Lambda, negate(S)),
    multiply(negate(S), Lambda),
)
assert order_only_reversed == negate(virial)

print("reciprocal exchange reverses scale and order together")
print("scale-order commutator is reciprocal-even")
print("opposite virial sign requires an incomplete transport")
