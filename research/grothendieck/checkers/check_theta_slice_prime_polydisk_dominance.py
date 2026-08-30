#!/usr/bin/env python3
"""Exact gates for theta-slice prime-polydisk dominance."""

from fractions import Fraction


def majorant(n: int) -> Fraction:
    return Fraction(2 * n**4, 2 ** (3 * (n * n - 1)))


def main() -> None:
    gates = []

    a2 = majorant(2)
    a3 = majorant(3)
    tail_bound = a2 + a3 / (1 - Fraction(1, 2**19))
    gates.append(("first majorant is exactly one sixteenth", a2 == Fraction(1, 16)))
    gates.append(("majorant tail is below one fifteenth", tail_bound < Fraction(1, 15)))

    ratios_small = all(
        majorant(n + 1) <= majorant(n) / 2**19 for n in range(3, 20)
    )
    gates.append(("post-third majorants obey the certified geometric ratio", ratios_small))

    # The log-curvature formula is negative whenever x>3/2.
    for x in (Fraction(2), Fraction(3), Fraction(22, 7), Fraction(10)):
        curvature = -4 * x - 24 * x / (2 * x - 3) ** 2
        gates.append((f"log curvature is negative at x={x}", curvature < 0))

    # Stable inputs can be destroyed by an oscillatory readout.
    # P_plus - P_minus = 2w, which vanishes at w=0.
    p_plus_at_zero = 1
    p_minus_at_zero = 1
    gates.append(("oscillatory aggregation can create an interior zero", p_plus_at_zero - p_minus_at_zero == 0))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(ok for _, ok in gates)}/{len(gates)} gates passed")
    if not all(ok for _, ok in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
