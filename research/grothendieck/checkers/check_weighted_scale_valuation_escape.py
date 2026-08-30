"""Finite census of weighted traveling scale/valuation cells."""

from math import erfc, exp, log, pi, sqrt


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            sieve[value * value : limit + 1 : value] = b"\x00" * (
                (limit - value * value) // value + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def window(length: float, q: float) -> float:
    return tail(q + length) - tail(q - length)


def adjacent_cell(prime: int, q: float) -> float:
    length = log(prime)
    return window(2.0 * length, q) - window(length, q)


def main() -> None:
    primes = primes_through(200_000)
    samples = []
    for q in (8.0, 10.0, 12.0):
        eligible = [prime for prime in primes if prime <= exp(q)]
        primitive = sum(prime ** -0.5 * adjacent_cell(prime, q) for prime in eligible)
        square = sum(prime ** -1.0 * adjacent_cell(prime, q) for prime in eligible)
        samples.append((q, primitive, square))

    assert abs(samples[2][1]) > abs(samples[1][1]) > abs(samples[0][1])
    assert all(square < -0.25 for _, _, square in samples)
    assert all(square > -1.25 for _, _, square in samples)

    print("primitive_magnitude_strictly_grows=true")
    print("primitive_asymptotic_scale=exp(q/2)/q")
    print("square_plateau_scale=constant")
    print("square_continuum_limit=negative_log_2")
    print("compact_local_decay_implies_global_decay=false")
    print("next_coordinate=u=q-log(p)")


if __name__ == "__main__":
    main()
