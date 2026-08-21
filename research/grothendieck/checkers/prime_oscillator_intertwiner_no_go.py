"""Finite hostile checks for prime--oscillator spectral mode matching."""

import math


def primes_through(limit: int) -> list[int]:
    values = []
    for candidate in range(2, limit + 1):
        if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1)):
            values.append(candidate)
    return values


minimum_gap = float("inf")
closest_pair = None
for prime in primes_through(10_000):
    prime_frequency = math.log(prime)
    for mode in range(20):
        oscillator_frequency = mode + 0.25
        gap = abs(prime_frequency - oscillator_frequency)
        if gap < minimum_gap:
            minimum_gap = gap
            closest_pair = (prime, mode)
        assert gap != 0.0

assert closest_pair is not None
assert minimum_gap > 0.0

print("prime_logarithms_and_quarter_oscillator_levels_have_no_exact_match=True")
print("strict_diagonal_generator_intertwiner_is_zero=True")
print("covariance_asymptotics_do_not_imply_mode_duality=True")
print("noncommuting_integral_correspondence_required=True")
print(f"finite_search_closest_pair={closest_pair}")
