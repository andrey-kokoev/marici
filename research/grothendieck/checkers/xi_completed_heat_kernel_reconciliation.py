"""Uncertified source/spectral reconciliation probe for the completed xi heat kernel."""

from __future__ import annotations

import math

import mpmath as mp


def von_mangoldt_table(limit: int) -> list[float]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    values = [0.0] * (limit + 1)
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        logp = math.log(p)
        power = p
        while power <= limit:
            values[power] = logp
            if power > limit // p:
                break
            power *= p
    return values


def gamma_kernel(t: mp.mpf) -> mp.mpf:
    integrand = lambda r: (
        mp.exp(-r) - mp.exp(-r / 4 - r * r / (16 * t))
    ) / (-mp.expm1(-r))
    integral = mp.quad(integrand, [0, 1, mp.inf])
    return (-mp.euler - mp.log(mp.pi) + integral) / (4 * mp.sqrt(mp.pi * t))


def prime_kernel(t: mp.mpf, mangoldt: list[float]) -> mp.mpf:
    total = mp.mpf("0")
    for n in range(2, len(mangoldt)):
        weight = mangoldt[n]
        if weight:
            logn = mp.log(n)
            total += weight / mp.sqrt(n) * mp.exp(-(logn * logn) / (4 * t))
    return -total / (2 * mp.sqrt(mp.pi * t))


def main() -> None:
    mp.mp.dps = 70
    prime_limit = 200_000
    zero_count = 80
    mangoldt = von_mangoldt_table(prime_limit)
    ordinates = [mp.im(mp.zetazero(index)) for index in range(1, zero_count + 1)]
    times = [mp.mpf(value) for value in ("0.001", "0.003", "0.01", "0.03", "0.05", "0.1")]

    for t in times:
        endpoint = mp.exp(t / 4)
        gamma = gamma_kernel(t)
        prime = prime_kernel(t, mangoldt)
        source = endpoint + gamma + prime
        spectral = sum(mp.exp(-t * ordinate**2) for ordinate in ordinates)
        residual = source - spectral
        print(
            "t=" + mp.nstr(t, 6)
            + " endpoint=" + mp.nstr(endpoint, 18)
            + " gamma=" + mp.nstr(gamma, 18)
            + " prime=" + mp.nstr(prime, 18)
            + " source=" + mp.nstr(source, 18)
            + " spectral80=" + mp.nstr(spectral, 18)
            + " residual=" + mp.nstr(residual, 8)
        )

    print(f"prime_limit={prime_limit}")
    print(f"spectral_zero_count={zero_count}")
    print("truncation_error_certified=False")
    print("source_uses_zero_locations=False")
    print("spectral_sum_used_for_validation_only=True")


if __name__ == "__main__":
    main()
