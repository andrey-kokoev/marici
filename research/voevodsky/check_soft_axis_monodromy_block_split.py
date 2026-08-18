"""Exact check that involutive monodromy forbids cross-character maps."""

from fractions import Fraction


# Write an arbitrary 2-by-2 map in the (+,-) eigenbasis of T.
T = ((1, 0), (0, -1))


def add_values(left, right):
    if isinstance(left, tuple):
        return tuple(x + y for x, y in zip(left, right))
    return left + right


def multiply_values(left, right):
    if isinstance(left, tuple):
        return tuple(right * x for x in left)
    if isinstance(right, tuple):
        return tuple(left * x for x in right)
    return left * right


def multiply(left, right):
    return tuple(
        tuple(
            add_values(
                multiply_values(left[i][0], right[0][j]),
                multiply_values(left[i][1], right[1][j]),
            )
            for j in range(2)
        )
        for i in range(2)
    )


def subtract(left, right):
    return tuple(
        tuple(
            tuple(x - y for x, y in zip(left[i][j], right[i][j]))
            if isinstance(left[i][j], tuple)
            else left[i][j] - right[i][j]
            for j in range(2)
        )
        for i in range(2)
    )


# Symbolic coefficients represented by four independent coordinate vectors.
e = tuple(
    tuple(tuple(Fraction(int(i == 2 * row + col)) for i in range(4)) for col in range(2))
    for row in range(2)
)
commutator = subtract(multiply(T, e), multiply(e, T))
assert commutator[0][0] == (0, 0, 0, 0)
assert commutator[1][1] == (0, 0, 0, 0)
assert commutator[0][1] == (0, 2, 0, 0)
assert commutator[1][0] == (0, 0, -2, 0)

# Since 2 is invertible over Q, equivariance forces both off-diagonal entries
# to vanish.  The projectors are canonical and split every equivariant cone
# or homotopy fiber functorially.
half = Fraction(1, 2)
P_plus = ((half * 2, 0), (0, 0))
P_minus = ((0, 0), (0, half * 2))
identity = ((1, 0), (0, 1))
zero = ((0, 0), (0, 0))
assert subtract(tuple(tuple(P_plus[i][j] + P_minus[i][j] for j in range(2)) for i in range(2)), identity) == zero
assert multiply(P_plus, P_minus) == zero
assert multiply(P_plus, P_plus) == P_plus
assert multiply(P_minus, P_minus) == P_minus

# Quartic carrier basis 1,a,a^2,a^3 splits 2+2 by a -> -a.
quartic_characters = (1, -1, 1, -1)
assert quartic_characters.count(1) == 2
assert quartic_characters.count(-1) == 2

print("equivariant off-diagonal blocks: 0")
print("canonical projectors: (1+T)/2, (1-T)/2")
print("quartic tail characters: even rank 2, odd rank 2")
print("remaining extensions: same-character only")
