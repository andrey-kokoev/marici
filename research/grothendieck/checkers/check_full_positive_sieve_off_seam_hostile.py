import cmath
import math


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


z0 = math.sqrt(math.pi) * cmath.exp(-1j * math.pi / 4)
s0 = 0.5 + 1j * z0
g_hat = cmath.exp(-2 * z0 * z0) + cmath.exp(-z0 * z0)

gate(abs(z0.real) > 1e-12)
gate(z0.imag < -0.5)
gate(s0.real > 1.0)
gate(abs(g_hat) < 1e-12)

# The absolutely convergent Dirichlet factors remain bounded and nonzero in
# finite Euler products; multiplying by the primitive zero stays zero.
for cutoff in [10, 30, 100, 300, 1000, 3000]:
    dirichlet = sum(n ** (-s0) for n in range(1, cutoff + 1))
    gate(abs(dirichlet) > 1e-6)
    gate(abs(g_hat * dirichlet) < 1e-10)

# Exact finite label deletion for nested prime sieves.
primes = [2, 3, 5, 7, 11]
limit = 1000
for mask in range(1 << len(primes)):
    selected = [p for i, p in enumerate(primes) if mask & (1 << i)]
    coefficients = [1 if all(n % p for p in selected) else 0 for n in range(1, limit + 1)]
    gate(coefficients[0] == 1)
    gate(all(c in (0, 1) for c in coefficients))
    if selected:
        gate(sum(coefficients) < limit)
    else:
        gate(sum(coefficients) == limit)

# Positive pointwise arithmetic source at representative truncations.
def base(u):
    return math.exp(-u * u / 8) / math.sqrt(8 * math.pi) + math.exp(-u * u / 4) / math.sqrt(4 * math.pi)


for u in [-8, -4, 0, 4, 8]:
    value = sum(n ** -0.5 * base(u + math.log(n)) for n in range(1, 5000))
    gate(value > 0)

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
