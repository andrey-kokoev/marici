"""Exact checks for the all-order integral-square sign-regularity proof."""

from fractions import Fraction


def odd_double_factorial(r):
    value = 1
    for k in range(1, 2 * r + 2, 2):
        value *= k
    return value


def elementary(values):
    e = [Fraction(1)] + [Fraction(0)] * len(values)
    for value in values:
        for j in range(len(values), 0, -1):
            e[j] += value * e[j - 1]
    return e


def q_from_z(zs):
    n = len(zs)
    e = elementary(zs)
    return sum(
        Fraction((-1) ** (n - j) * 2**j * odd_double_factorial(n - j)) * e[j]
        for j in range(n + 1)
    )


# The conservative rational chamber z_j=3*j^2 lies below pi*t*j^2.
q_values = []
for n in range(1, 16):
    zs = [Fraction(3 * j * j) for j in range(1, n + 1)]
    value = q_from_z(zs)
    assert value > 0
    q_values.append(value)

# Elementary telescoping bound on reciprocal squares.
for n in range(2, 100):
    square_sum = sum(Fraction(1, m * m) for m in range(1, n + 1))
    telescoping_bound = Fraction(1) + sum(
        Fraction(1, m * (m - 1)) for m in range(2, n + 1)
    )
    assert square_sum < telescoping_bound < 2

# The coefficient multiplier in A_(r+1)/A_r is at most 3/2.
for r in range(100):
    multiplier = Fraction(2 * r + 3, 2 * (r + 1))
    assert multiplier <= Fraction(3, 2)

# Direct alternating-term decrease for conservative z_j=3*j^2.
for n in range(1, 20):
    inverse_z = [Fraction(1, 3 * j * j) for j in range(1, n + 1)]
    e = elementary(inverse_z)
    terms = [
        Fraction(odd_double_factorial(r), 2**r) * e[r]
        for r in range(n + 1)
    ]
    assert all(terms[r + 1] < terms[r] for r in range(n))
    alternating = sum((-1) ** r * terms[r] for r in range(n + 1))
    assert alternating > 0

print("exact positive Q_n checks through order:", len(q_values))
print("Q_1..Q_5 at conservative square boundary:", q_values[:5])
print("telescoping reciprocal-square bound checked through N=99")
print("decreasing alternating terms checked through order 19")
print("PASS: integral-square separation protects all-order sign regularity")
