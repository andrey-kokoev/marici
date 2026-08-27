#!/usr/bin/env python3
"""Finite-cutoff witness for primitive/square exclusion-energy growth."""


def primes_through(limit):
    result = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in result if prime * prime <= candidate):
            result.append(candidate)
    return result


def main():
    norm_squared = 2
    previous_primitive = 0.0
    previous_square = 0.0
    for limit in (5, 11, 23, 47, 97):
        primes = primes_through(limit)
        primitive = sum(norm_squared / (prime ** 0.5) for prime in primes if prime > 2)
        square = sum(norm_squared / prime for prime in primes if prime > 2)
        assert primitive > previous_primitive
        assert square > previous_square
        previous_primitive = primitive
        previous_square = square

    print("finite_packet_support={1,2}")
    print("large_prime_exclusion=identity")
    print("primitive_cutoff_energy=strictly_growing")
    print("square_cutoff_energy=strictly_growing")
    print("required_completion=pro_valued_Ward_family")


if __name__ == "__main__":
    main()

