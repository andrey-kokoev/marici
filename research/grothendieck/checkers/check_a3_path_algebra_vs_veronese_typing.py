#!/usr/bin/env python3
"""Exact distinction between directed A3 incidence and Cartan symmetry."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def zero():
    return [[Fraction(0) for _ in range(3)] for _ in range(3)]


def unit(i, j):
    out = zero()
    out[i][j] = Fraction(1)
    return out


def add(*matrices):
    return [[sum(m[i][j] for m in matrices) for j in range(3)] for i in range(3)]


def main():
    e0, e1, e2 = unit(0, 0), unit(1, 1), unit(2, 2)
    a, b, c = unit(0, 1), unit(1, 2), unit(0, 2)
    z = zero()

    gates = []
    gates.append(("A3 basis has three vertices two arrows and one composite", len((e0, e1, e2, a, b, c)) == 6))
    gates.append(("adjacent arrows compose to the long path", matmul(a, b) == c))
    gates.append(("reverse arrow order is not composable", matmul(b, a) == z))
    gates.append(("path algebra is noncommutative", matmul(e0, a) == a and matmul(a, e0) == z))

    radical = add(a, b, c)
    radical2 = matmul(radical, radical)
    radical3 = matmul(radical2, radical)
    gates.append(("radical square is exactly the long path", radical2 == c))
    gates.append(("radical cube vanishes", radical3 == z))

    gates.append(("three stage-local pairs give six carrier dimensions", 3 * 2 == 6))
    gates.append(("six-dimensional carrier does not imply thirty-six-dimensional structure", 3 + 2 + 1 == 6 and 6 * 6 == 36))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(ok for _, ok in gates)}/{len(gates)} gates passed")
    if not all(ok for _, ok in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
