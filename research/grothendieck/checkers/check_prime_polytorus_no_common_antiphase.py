#!/usr/bin/env python3
"""Exact structural checks for the prime-polytorus scope correction."""

from fractions import Fraction


PRIMES = (2, 3, 5, 7, 11)
ODD = (1, 3, 5, 7, 9)


def valuations(n: int) -> tuple[int, ...]:
    out = []
    for p in PRIMES:
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        out.append(power)
    return tuple(out)


def main() -> None:
    gates = []

    no_common_antiphase = all(
        p**a != q**b
        for i, p in enumerate(PRIMES)
        for q in PRIMES[i + 1 :]
        for a in ODD
        for b in ODD
    )
    gates.append(("distinct primes have no common odd-power identity", no_common_antiphase))

    multiplicative = all(
        tuple(x + y for x, y in zip(valuations(m), valuations(n))) == valuations(m * n)
        for m in range(1, 12)
        for n in range(1, 12)
    )
    gates.append(("valuation monomials preserve multiplication", multiplicative))

    inside = all(Fraction(1, p) < 1 for p in PRIMES)
    outside = all(Fraction(p, 1) > 1 for p in PRIMES)
    gates.append(("positive and negative radial chambers map inside and outside", inside and outside))

    u = v = 0.5j
    hostile_zero = 1 + 4 * u * v == 0
    axis_stable = (1 + 4 * u * 0 == 1) and (1 + 4 * 0 * v == 1)
    gates.append(("mixed positive-coefficient hostile vanishes inside bidisk", hostile_zero))
    gates.append(("one-prime axis restrictions miss the hostile zero", axis_stable))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(passed for _, passed in gates)}/{len(gates)} gates passed")
    if not all(passed for _, passed in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
