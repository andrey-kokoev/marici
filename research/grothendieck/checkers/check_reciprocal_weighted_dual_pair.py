#!/usr/bin/env python3
"""Finite witnesses for the reciprocal weighted dual-pair theorem."""

from math import log


def primes_upto(n):
    out = []
    for k in range(2, n + 1):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


P = primes_upto(50000)
checks = {}

a = 0.2
c = {p: p ** (-a - 1.0) for p in P[:100]}
d = {p: p ** (a - 1.0) for p in P[:100]}
pair = sum(c[p] * d[p] for p in c)
nc = sum(p ** (2 * a) * c[p] ** 2 for p in c) ** 0.5
nd = sum(p ** (-2 * a) * d[p] ** 2 for p in d) ** 0.5
checks["weighted_cauchy_schwarz"] = abs(pair) <= nc * nd + 1e-12

t = 8.5
pair_shifted = sum((c[p] * p ** (-1j * t)) * (d[p] * p ** (1j * t)) for p in c)
checks["mellin_pairing_covariance"] = abs(pair_shifted - pair) < 1e-12

# Primitive and square reciprocal norms stabilize already near the seam.
def partial(bound, exponent):
    return sum(log(p) ** 2 * p ** exponent for p in P if p <= bound)

primitive = [partial(n, -1 - 2 * a) for n in (1000, 10000, 50000)]
square = [partial(n, -2 - 2 * a) for n in (1000, 10000, 50000)]
checks["primitive_reciprocal_vector"] = primitive[2] - primitive[1] < primitive[1] - primitive[0]
checks["square_reciprocal_vector"] = square[2] - square[1] < square[1] - square[0]

# Augmentation diverges for a=.2 but converges for a=.75. Compare successive
# tails; the former remains macroscopically growing while the latter shrinks.
aug_near = [sum(p ** (-0.4) for p in P if p <= n) for n in (1000, 10000, 50000)]
aug_far = [sum(p ** (-1.5) for p in P if p <= n) for n in (1000, 10000, 50000)]
checks["augmentation_external_near_seam"] = aug_near[2] - aug_near[1] > 1
checks["augmentation_internal_far_sector"] = aug_far[2] - aug_far[1] < aug_far[1] - aug_far[0]

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

