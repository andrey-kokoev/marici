import cmath
import math
from fractions import Fraction
from math import factorial


def derivative(coefficients, order=1):
    out = list(map(Fraction, coefficients))
    for _ in range(order):
        out = [Fraction((i + 1) * out[i + 1]) for i in range(len(out) - 1)]
        if not out:
            return [Fraction(0)]
    return out


def add(a, b):
    n = max(len(a), len(b))
    aa = a + [Fraction(0)] * (n - len(a))
    bb = b + [Fraction(0)] * (n - len(b))
    return [x + y for x, y in zip(aa, bb)]


def T(coefficients, n, c=Fraction(1)):
    return add(list(map(Fraction, coefficients)), [c * x for x in derivative(coefficients, 2 * n)])


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


for n in range(2, 14, 2):
    for degree in range(2 * n, 2 * n + 6):
        f = [Fraction(0)] * degree + [Fraction(1)]
        gate(derivative(T(f, n), 2) == T(derivative(f, 2), n))

    f = [Fraction(0)] * (2 * n) + [Fraction(1)]
    transformed = T(f, n)
    gate(transformed[0] == factorial(2 * n))
    gate(transformed[2 * n] == 1)

    radius = factorial(2 * n) ** (1 / (2 * n))
    roots = [radius * cmath.exp(1j * (2 * k + 1) * math.pi / (2 * n)) for k in range(2 * n)]
    gate(all(abs(root.real) > 1e-9 for root in roots))
    gate(all(abs(root ** (2 * n) + factorial(2 * n)) < 1e-5 * factorial(2 * n) for root in roots))
    gate(n % 2 == 0)  # Fourier multiplier 1+u^(2N) is positive.

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
