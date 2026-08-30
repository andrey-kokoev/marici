"""High-precision finite modular-jet nullspace witness."""

from decimal import Decimal as D
from decimal import getcontext
from fractions import Fraction

getcontext().prec = 90
PI = D("3.141592653589793238462643383279502884197169399375105820974944")


def derivative(coefficients):
    # P -> 2[(5/4-q)P + q P'] in ascending coefficient order.
    out = [Fraction(0)] * (len(coefficients) + 1)
    for degree, coefficient in enumerate(coefficients):
        out[degree] += Fraction(5, 2) * coefficient
        if degree:
            out[degree] += 2 * degree * coefficient
        out[degree + 1] -= 2 * coefficient
    return out


polynomials = [[Fraction(-3), Fraction(2)]]
for _ in range(3):
    polynomials.append(derivative(polynomials[-1]))


def evaluate(coefficients, q):
    value = D(0)
    for coefficient in reversed(coefficients):
        value = value * q + D(coefficient.numerator) / D(coefficient.denominator)
    return value


def jet(order, mode):
    x = D(mode * mode)
    q = PI * x
    return x * (-q).exp() * evaluate(polynomials[order], q)


orders = [0, 1, 3]
matrix = [[jet(order, mode) for mode in range(1, 6)] for order in orders]

# RREF of the 3x5 Decimal matrix.
a = [row[:] for row in matrix]
pivots = []
row = 0
for column in range(5):
    pivot = next((r for r in range(row, 3) if a[r][column] != 0), None)
    if pivot is None:
        continue
    a[row], a[pivot] = a[pivot], a[row]
    scale = a[row][column]
    a[row] = [v / scale for v in a[row]]
    for r in range(3):
        if r != row:
            scale = a[r][column]
            a[r] = [x - scale * y for x, y in zip(a[r], a[row])]
    pivots.append(column)
    row += 1
    if row == 3:
        break

free = next(column for column in range(5) if column not in pivots)
h = [D(0)] * 5
h[free] = D(1)
for r, pivot in reversed(list(enumerate(pivots))):
    h[pivot] = -sum(a[r][c] * h[c] for c in range(pivot + 1, 5))

scale = max(abs(v) for v in h)
h = [v / scale for v in h]
epsilon = D(1) / D(4)
plus = [D(1) + epsilon * v for v in h]
minus = [D(1) - epsilon * v for v in h]
assert min(plus + minus) >= D(3) / D(4)
assert plus != minus


def observations(weights):
    return [sum(value * weight for value, weight in zip(row, weights)) for row in matrix]


obs_plus = observations(plus)
obs_minus = observations(minus)
residuals = [abs(x - y) for x, y in zip(obs_plus, obs_minus)]
assert max(residuals) < D("1e-80")

print("jet orders:", orders)
print("RREF pivots:", pivots, "free column:", free)
print("normalized hostile weight direction:", h)
print("minimum perturbed weight:", min(plus + minus))
print("equal-jet residuals:", residuals)
print("PASS: no finite modular-jet certificate selects the positive weights")
