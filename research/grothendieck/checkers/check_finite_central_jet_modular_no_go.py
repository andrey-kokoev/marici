import cmath
import math


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


for n in range(2, 22, 2):
    degree = 2 * n
    # Coefficients of 1+z^(2N): all intermediate central jets vanish.
    coefficients = [0] * (degree + 1)
    coefficients[0] = 1
    coefficients[degree] = 1
    gate(all(coefficients[j] == (1 if j == 0 else 0) for j in range(degree)))
    gate(degree % 2 == 0)

    roots = [cmath.exp(1j * (2 * k + 1) * math.pi / degree) for k in range(degree)]
    gate(all(abs(root ** degree + 1) < 1e-10 for root in roots))
    gate(all(abs(root.real) > 1e-10 for root in roots))
    gate(all(any(abs((-root) - other) < 1e-10 for other in roots) for root in roots))
    gate(all(any(abs(root.conjugate() - other) < 1e-10 for other in roots) for root in roots))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
