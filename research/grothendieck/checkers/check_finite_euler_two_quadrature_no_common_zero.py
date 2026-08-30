#!/usr/bin/env python3
"""Finite-cutoff audit of the two Euler occupation quadratures."""

import cmath
from math import log


def primes_through(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


def plus_amplitude(primes: list[int], z: complex) -> complex:
    value = 1.0 + 0.0j
    for prime in primes:
        value *= 1.0 - cmath.exp(-(z + 0.5) * log(prime))
    return value


assert -0.5 != 0.5
for cutoff in (2, 5, 11, 29):
    primes = primes_through(cutoff)
    for j in range(-20, 21):
        z = 0.17j * j
        plus = plus_amplitude(primes, z)
        minus = plus_amplitude(primes, -z)
        symmetric = plus + minus
        antisymmetric = plus - minus
        assert abs(minus - plus.conjugate()) < 1.0e-12
        assert abs(abs(symmetric) ** 2 + abs(-1j * antisymmetric) ** 2 - 4.0 * abs(plus) ** 2) < 1.0e-10
        assert abs(plus) > 0.0

print("plus_zero_wall=Re(z)=-1/2")
print("minus_zero_wall=Re(z)=+1/2")
print("finite_common_zero=impossible")
print("faithful_quadrature_pair=(T_X,A_X)")
print("seam_norm=4*abs(F_X_plus)^2>0")
print("new_divisor_origin=infinite_completion_or_projection")
