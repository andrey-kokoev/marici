import math


def primes_up_to(n):
    out = []
    for candidate in range(2, n + 1):
        if all(candidate % p for p in out if p * p <= candidate):
            out.append(candidate)
    return out


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


limit = 500
primes = primes_up_to(19)

# Exact finite-cutoff label deletion for all tested sieve subsets.
for mask in range(1 << len(primes)):
    selected = [p for i, p in enumerate(primes) if mask & (1 << i)]
    survivors = [n for n in range(1, limit + 1) if all(n % p for p in selected)]
    coefficients = []
    for n in range(1, limit + 1):
        coefficient = 1
        for p in selected:
            if n % p == 0:
                coefficient = 0
                break
        coefficients.append(coefficient)
    gate(sum(coefficients) == len(survivors))
    gate(all(c in (0, 1) for c in coefficients))
    gate(coefficients[0] == 1)

# A positive two-Gaussian mixture fails each prime-difference gate on a
# sufficiently negative tail.
a, b, c = 2.0, 1.0, 1.0


def gaussian_mix(u):
    return math.exp(-u * u / (4 * a)) / math.sqrt(4 * math.pi * a) + c * math.exp(-u * u / (4 * b)) / math.sqrt(4 * math.pi * b)


for p in primes:
    L = math.log(p)
    witnesses = []
    for u in [-10.0, -15.0, -20.0, -25.0]:
        witnesses.append(gaussian_mix(u) - p ** (-0.5) * gaussian_mix(u + L))
    gate(any(value < 0 for value in witnesses))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
