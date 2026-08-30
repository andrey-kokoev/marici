import math


def primes_up_to(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


lower_bound = 2.0 * (1.0 - 1.0 / math.sqrt(2.0))
cutoffs = (10, 100, 1000, 10000)
displacements = []

for cutoff in cutoffs:
    primes = primes_up_to(cutoff)
    displacement = sum(2.0 * (1.0 - 1.0 / math.sqrt(prime)) for prime in primes)
    assert displacement >= lower_bound * len(primes) - 1e-12
    displacements.append(displacement)

assert all(left < right for left, right in zip(displacements, displacements[1:]))
assert displacements[-1] > 2000.0

print("cutoffs:", cutoffs)
print("accumulated vacuum displacements:", displacements)
print("uniform per-prime lower bound:", lower_bound)
print("raw vacuum tensor-product implementability fails")
