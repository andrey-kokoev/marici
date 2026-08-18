#!/usr/bin/env python3
"""Check the Entry 850 marked-relative extension acceptance contract."""

from fractions import Fraction
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKET = HERE / "marked-relative-extension-acceptance-contract.json"


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def block(a, b, c, d):
    return [ar + br for ar, br in zip(a, b)] + [cr + dr for cr, dr in zip(c, d)]


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def zero(m, n):
    return [[Fraction(0) for _ in range(n)] for _ in range(m)]


def main():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    assert packet["entry"] == 850
    assert packet["exact_sequence"]["dimensions"] == {"M9": 9, "M12": 12, "W3": 3}
    assert packet["adapted_frame"]["extension_block_shape"] == [9, 3]
    assert packet["adapted_frame"]["temporary_only"] is True
    assert packet["acceptance_order"][-1] == "intrinsic support factorization"

    # Exact finite-dimensional audit of the stated triangular gauge law in a
    # 2+1 test model.  dG is retained independently, so this checks the sign
    # convention rather than only constant conjugation.
    a9 = [[Fraction(2), Fraction(1)], [Fraction(0), Fraction(3)]]
    a3 = [[Fraction(5)]]
    b = [[Fraction(7)], [Fraction(11)]]
    h = [[Fraction(13)], [Fraction(17)]]
    dh = [[Fraction(19)], [Fraction(23)]]
    connection = block(a9, b, zero(1, 2), a3)
    gauge = block(eye(2), h, zero(1, 2), eye(1))
    gauge_inv = block(eye(2), [[-x for x in row] for row in h], zero(1, 2), eye(1))
    dg = block(zero(2, 2), dh, zero(1, 2), zero(1, 1))
    transformed = add(mul(mul(gauge_inv, connection), gauge), mul(gauge_inv, dg))
    expected_b = add(b, add(dh, sub(mul(a9, h), mul(h, a3))))
    actual_b = [[transformed[i][2]] for i in range(2)]
    assert actual_b == expected_b
    assert transformed[2][:2] == [Fraction(0), Fraction(0)]

    print("marked-relative extension acceptance contract: PASS")
    print("exact sequence dimensions: 9 -> 12 -> 3")
    print("triangular gauge law: B' = B + dh + A9 h - h A3")
    print("Q test occurs only after exactness, horizontality, flatness, and gauge quotient")


if __name__ == "__main__":
    main()
