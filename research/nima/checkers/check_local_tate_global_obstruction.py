"""Cutoff witness for failure of the raw product of local Tate seam phases."""

import cmath
import math


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            sieve[n * n : limit + 1 : n] = b"\x00" * (
                (limit - n * n) // n + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def seam_deviation_sum(limit, t):
    total = 0.0
    for p in primes_up_to(limit):
        a = p ** -0.5
        theta = t * math.log(p)
        gamma = (1 - a * cmath.exp(-1j * theta)) / (
            1 - a * cmath.exp(1j * theta)
        )
        assert abs(abs(gamma) - 1.0) < 1e-12
        total += abs(1 - gamma) ** 2
    return total


cutoffs = (1_000, 10_000, 100_000, 1_000_000)
at_t_one = [seam_deviation_sum(x, 1.0) for x in cutoffs]
at_t_zero = [seam_deviation_sum(x, 0.0) for x in cutoffs]

assert all(b > a for a, b in zip(at_t_one, at_t_one[1:]))
# Finite cutoffs are only a hostile witness; the PNT argument supplies
# divergence.  Require clear growth without fitting the asymptotic rate.
assert at_t_one[-1] > at_t_one[0] + 1.0
assert at_t_zero == [0.0] * len(cutoffs)

witness = {
    "code": "local_unitaries_not_raw_restricted_product",
    "reference": "canonical_local_vacua",
    "parameter_t": 1.0,
    "cutoffs": cutoffs,
    "partial_sums": [round(x, 6) for x in at_t_one],
}

print("t=1 partial sums:", witness["partial_sums"])
print("t=0 partial sums:", at_t_zero)
print("rejection witness:", witness)
print("PASS: local unitarity does not yield a raw global tensor product")
