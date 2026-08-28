#!/usr/bin/env python3
"""Exact checks for the first mixed-prime bidisk stability cell."""

from fractions import Fraction


def radial_minimum(a, b, c, d):
    A = a * a - c * c
    B = a * b - c * d
    C = b * b - d * d
    endpoint = min(A, A + C - 2 * abs(B))
    if C > 0 and abs(B) <= C:
        return min(endpoint, A - B * B / C)
    return endpoint


def common_zero_inside(a, b, c, d):
    if b == 0 or d == 0 or a * d != b * c:
        return False
    return a < b and c < d


def main():
    gates = []

    independent = (Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
    gates.append(("independent Fock cell has zero curvature", independent[0] * independent[3] == independent[1] * independent[2]))
    gates.append(("independent Fock cell has nonnegative radial slack", radial_minimum(*independent) >= 0))
    gates.append(("independent Fock cell has no interior common zero", not common_zero_inside(*independent)))

    hostile = (Fraction(1), Fraction(0), Fraction(0), Fraction(4))
    gates.append(("mixed hostile has negative radial slack", radial_minimum(*hostile) < 0))
    u = v = 0.5j
    gates.append(("mixed hostile has its exact interior zero", 1 + 4 * u * v == 0))

    common = (Fraction(1), Fraction(2), Fraction(1), Fraction(2))
    gates.append(("common-factor trap has zero slack", radial_minimum(*common) == 0))
    gates.append(("common-factor gate detects its interior zero", common_zero_inside(*common)))

    boundary = (Fraction(1), Fraction(1), Fraction(1), Fraction(1))
    gates.append(("boundary common factor is allowed in the open bidisk", not common_zero_inside(*boundary)))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(ok for _, ok in gates)}/{len(gates)} gates passed")
    if not all(ok for _, ok in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
