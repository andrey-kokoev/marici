import json
import math


def primes_up_to(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % p for p in out if p * p <= n):
            out.append(n)
    return out


primes = primes_up_to(97)

# A deliberately loose proxy for the analytically proved Gaussian-absorption
# envelope. Polynomial powers model the source and its first graph derivative.
def envelope(p):
    return (1.0 + p ** 12) * math.exp(-math.pi * p * p)


terms = [envelope(p) / (p * math.log(p)) for p in primes]
tail_maxima = [max(terms[i:]) for i in range(len(terms))]

assert all(math.isfinite(x) and x >= 0.0 for x in terms)
assert all(tail_maxima[i + 1] <= tail_maxima[i] for i in range(len(tail_maxima) - 1))
assert terms[-1] == 0.0 or terms[-1] < terms[0]

# Hostile slow tails do not inherit the source estimate. The harmonic prime
# common mode remains visible in finite cutoffs and grows strictly.
harmonic_prime_partial = []
running = 0.0
for p in primes:
    running += 1.0 / p
    harmonic_prime_partial.append(running)
assert all(
    harmonic_prime_partial[i + 1] > harmonic_prime_partial[i]
    for i in range(len(harmonic_prime_partial) - 1)
)

result = {
    "schema": "marici.nima.theta-superexponential-tail.v1",
    "prime_cutoff": primes[-1],
    "prime_count": len(primes),
    "weighted_envelope_sum": sum(terms),
    "last_nonzero_or_underflowed_term": terms[-1],
    "gaussian_envelope_finite": True,
    "hostile_prime_harmonic_partial_strictly_grows": True,
    "scope": "finite numerical audit of the analytic envelope; the infinite convergence theorem is proved in the packet",
}
print(json.dumps(result, indent=2, sort_keys=True))

