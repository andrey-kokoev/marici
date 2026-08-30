"""Exact algebraic check for reciprocal off-seam zeros of an even source."""

from fractions import Fraction


# Elements a + b*sqrt(6).
def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    return (
        left[0] * right[0] + 6 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def scale(value, scalar):
    return value[0] * scalar, value[1] * scalar


y = (Fraction(-2), Fraction(-1))  # -2 - sqrt(6)
zero = add(add(multiply(y, y), scale(y, Fraction(4))), (Fraction(-2), Fraction(0)))

checks = 0
assert zero == (0, 0)  # y^2 + 4y - 2 = 0
checks += 1

# F = y + (y^2 - 2)/4.
transform = add(y, scale(add(multiply(y, y), (Fraction(-2), Fraction(0))), Fraction(1, 4)))
assert transform == (0, 0)
checks += 1

# Since sqrt(6)>0, y=-2-sqrt(6)<-2. The quadratic x^2-yx+1
# has two distinct negative real reciprocal roots, neither on the unit circle.
assert y[0] == -2 and y[1] < 0
checks += 2

# Palindromic Laurent coefficients certify evenness and positive weights.
coefficients = {
    -2: Fraction(1, 4),
    -1: Fraction(1),
    1: Fraction(1),
    2: Fraction(1, 4),
}
assert all(weight > 0 for weight in coefficients.values())
assert all(coefficients[k] == coefficients[-k] for k in coefficients)
checks += 2

print(f"PASS {checks}/{checks}: positive even four-atom source has reciprocal off-seam zeros")

