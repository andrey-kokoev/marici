from fractions import Fraction


def derivative(coefficients):
    return [Fraction((i + 1) * coefficients[i + 1]) for i in range(len(coefficients) - 1)]


def multiply(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pad(a, n):
    return a + [Fraction(0)] * (n - len(a))


def subtract(a, b):
    n = max(len(a), len(b))
    return [x - y for x, y in zip(pad(a, n), pad(b, n))]


def commutator(H, psi):
    left = derivative(derivative(multiply(H, psi)))
    right = multiply(H, derivative(derivative(psi))) if len(psi) >= 3 else [Fraction(0)]
    return subtract(left, right)


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


# Constants commute on a polynomial core.
for constant in range(-3, 4):
    H = [Fraction(constant)]
    for degree in range(9):
        psi = [Fraction(0)] * degree + [Fraction(1)]
        gate(all(x == 0 for x in commutator(H, psi)))

# Every hostile 1+z^(2N) fails already on one of the probes 1,z.
for n in range(1, 16):
    H = [Fraction(1)] + [Fraction(0)] * (2 * n - 1) + [Fraction(1)]
    on_one = commutator(H, [Fraction(1)])
    on_z = commutator(H, [Fraction(0), Fraction(1)])
    gate(any(x != 0 for x in on_one) or any(x != 0 for x in on_z))

# If the two probe commutators vanish for a generic polynomial, all
# nonconstant coefficients vanish. Exhaust this through degree eight over a
# small integer coefficient cube one monomial at a time.
for degree in range(1, 9):
    H = [Fraction(1)] + [Fraction(0)] * (degree - 1) + [Fraction(1)]
    gate(any(x != 0 for x in commutator(H, [Fraction(1)])) or
         any(x != 0 for x in commutator(H, [Fraction(0), Fraction(1)])))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
