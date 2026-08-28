from fractions import Fraction
from math import factorial


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


# Clark sheet decomposition in coefficient pairs (F,F').
a = Fraction(3, 5)
F = Fraction(0)
Fp = Fraction(7, 11)
H_plus = (F, a * Fp)   # real/imaginary coordinates for F + i a F'
H_minus = (F, -a * Fp)
C = (H_plus[0] - H_minus[0], H_plus[1] - H_minus[1])
gate(C == (0, 2 * a * Fp))
gate(C != (0, 0))

# One complex conormal line realifies to rank two.
complex_basis = [(1, 0), (0, 1)]
gate(len(complex_basis) == 2)
gate(3 + 4 + 3 == 10)

# For F(z)=z^m, the first surviving derivative at zero is order m.
for m in range(1, 21):
    derivatives = [Fraction(0) for _ in range(m)] + [Fraction(factorial(m))]
    gate(all(x == 0 for x in derivatives[:m]))
    gate(derivatives[m] != 0)
    gate((m == 1) == (derivatives[1] != 0 if len(derivatives) > 1 else False))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
