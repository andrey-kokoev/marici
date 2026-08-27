#!/usr/bin/env python3
"""Dependency-free checks for the arithmetic test-rigging theorem."""

from math import log


def primes_upto(n):
    out = []
    for k in range(2, n + 1):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


P = primes_upto(20000)
checks = {}

# Mellin phases preserve every diagonal weighted norm coefficientwise.
t = 7.25
checks["mellin_isometry"] = all(abs((p ** (1j * t)).real ** 2 + (p ** (1j * t)).imag ** 2 - 1) < 1e-12 for p in P[:100])

# Dual comparison sums stabilize for the stated exponents.
def partial(weight):
    return sum(weight(p) for p in P)

checks["augmentation_dual_bound"] = partial(lambda p: p ** -2.0) < 1.0
checks["primitive_dual_bound"] = partial(lambda p: log(p) ** 2 * p ** -1.5) < 10.0
checks["square_dual_bound"] = partial(lambda p: log(p) ** 2 * p ** -2.5) < 2.0

# The primitive coefficient vector is not a test vector: already its delta=1
# weighted partial norm grows monotonically and rapidly.
primitive_norms = []
for cutoff in (100, 1000, 10000):
    primitive_norms.append(sum(p * log(p) ** 2 for p in P if p <= cutoff))
checks["primitive_not_test_state"] = primitive_norms[0] < primitive_norms[1] < primitive_norms[2] and primitive_norms[2] > 1e8

# Finite cutoff tails vanish in each fixed seminorm for an explicit rapid
# packet c_p=p^-4, here checked at delta=1.
tails = []
for cutoff in (100, 1000, 10000):
    tails.append(sum(p ** -6 for p in P if p > cutoff))
checks["cutoff_density_witness"] = tails[0] > tails[1] > tails[2] >= 0

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))
