#!/usr/bin/env python3
"""Exact polynomial audit for Entry 858, using only the standard library."""

from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(poly, scalar):
    scalar = Fraction(scalar)
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def mul(a, b):
    out = {}
    for (iu, iv), ca in a.items():
        for (ju, jv), cb in b.items():
            m = (iu + ju, iv + jv)
            out[m] = out.get(m, Fraction(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


def power(poly, exponent):
    out = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def degree(poly):
    return max(sum(m) for m in poly)


def main():
    packet = json.loads((HERE / "normalized-q-a3-regularity.json").read_text(encoding="utf-8"))
    one = {(0, 0): Fraction(1)}
    u = {(1, 0): Fraction(1)}
    v = {(0, 1): Fraction(1)}
    y = add(scale(add(u, v), Fraction(1, 2)), scale(one, -1))
    e = u

    q = add(
        scale(power(y, 2), -16),
        scale(mul(y, power(e, 2)), -8),
        scale(mul(add(one, y), power(e, 3)), 8),
        scale(power(e, 4), -5),
    )
    expected = {
        (4, 0): Fraction(-1), (3, 1): Fraction(4), (3, 0): Fraction(-4),
        (2, 1): Fraction(-4), (2, 0): Fraction(4), (1, 1): Fraction(-8),
        (0, 2): Fraction(-4), (1, 0): Fraction(16), (0, 1): Fraction(16),
        (0, 0): Fraction(-16),
    }
    assert q == expected
    assert degree(q) == packet["normalized_degree"] == 4

    d = {
        (0, 0): -4, (1, 0): 12, (1, 1): -6, (0, 1): 4,
        (2, 0): -9, (2, 1): 4, (0, 2): -1,
    }
    h = {
        (0, 0): -2, (1, 0): -3, (1, 1): 2, (0, 1): 1,
        (2, 1): -1, (3, 0): 1,
    }
    linears = [u, add(u, scale(one, -2)), add(v, scale(one, -2)), add(u, v, scale(one, -2))]
    assert max(degree(f) for f in linears + [d, h]) == 3
    assert packet["maximum_factor_degree"] == 3

    print("normalized Q and A3 generic-regularity audit: PASS")
    print("Q_norm degree=4; every A3 denominator factor has degree <=3")
    print("using Entry 178 irreducibility, gcd(Q_norm,den(A3))=1")


if __name__ == "__main__":
    main()
