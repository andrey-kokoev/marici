#!/usr/bin/env python3
"""Finite exact/local and bounded global audit of centered Euler currents."""

from fractions import Fraction
from math import log


def centered_current(r: Fraction) -> Fraction:
    return Fraction(1, 2) * (1 + r) / (1 - r)


for numerator in range(1, 12):
    r = Fraction(numerator, numerator + 5)
    assert centered_current(1 / r) == -centered_current(r)


def primes_through(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


cutoffs = (10, 30, 100, 300, 1000)
vacuum_charges = [sum(log(p) / 2 for p in primes_through(cutoff)) for cutoff in cutoffs]
assert all(right > left for left, right in zip(vacuum_charges, vacuum_charges[1:]))
assert vacuum_charges[-1] > 200

print("comparison_ratio_coordinate=r=p^(-z)")
print("comparison_current=C_p(z)=coth(z*log(p)/2)/2")
print("local_reciprocity=C_p(-z)=-C_p(z)")
print("comparison_zeros_and_poles=critical_axis")
print("global_half_charge=sum_p log(p)/2_diverges")
print("ordinary_global_centered_current=does_not_exist")
print("required_completion=relative_comparison_frame")
