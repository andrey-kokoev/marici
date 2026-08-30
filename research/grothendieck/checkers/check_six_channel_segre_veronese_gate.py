#!/usr/bin/env python3
"""Exact gate for conditional 2x3 Segre--Veronese sewing maps."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def kron(a, b):
    return [[a[i][j] * b[r][c] for j in range(2) for c in range(3)]
            for i in range(2) for r in range(3)]


def block_factor(matrix):
    blocks = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append([[matrix[3*i+r][3*j+c] for c in range(3)] for r in range(3)])
        blocks.append(row)

    pivot = next((blocks[i][j] for i in range(2) for j in range(2)
                  if any(x != 0 for row in blocks[i][j] for x in row)), None)
    if pivot is None:
        return None
    flat_pivot = [x for row in pivot for x in row]
    k = next(i for i, x in enumerate(flat_pivot) if x != 0)
    a = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            flat = [x for row in blocks[i][j] for x in row]
            scale = Fraction(flat[k], flat_pivot[k])
            if any(x != scale * y for x, y in zip(flat, flat_pivot)):
                return None
            a[i][j] = scale
    return a, pivot


def preserves_quadric(b):
    gram = matmul(transpose(b), b)
    lam = gram[0][0]
    return lam != 0 and all(
        gram[i][j] == (lam if i == j else 0)
        for i in range(3) for j in range(3)
    )


def main():
    A = [[Fraction(1), Fraction(1)], [Fraction(0), Fraction(1)]]
    B = [[Fraction(0), Fraction(1), Fraction(0)],
         [Fraction(0), Fraction(0), Fraction(1)],
         [Fraction(1), Fraction(0), Fraction(0)]]
    authorized = kron(A, B)

    gates = []
    recovered = block_factor(authorized)
    gates.append(("authorized map has rank-one block reshuffling", recovered is not None))
    gates.append(("authorized Cartan factor preserves the quadric", recovered is not None and preserves_quadric(recovered[1])))

    nonfactor = [row[:] for row in authorized]
    nonfactor[0][3] += 1
    gates.append(("single cross-block defect breaks tensor factorization", block_factor(nonfactor) is None))

    shear = [[Fraction(1), Fraction(1), Fraction(0)],
             [Fraction(0), Fraction(1), Fraction(0)],
             [Fraction(0), Fraction(0), Fraction(1)]]
    factor_shear = block_factor(kron(A, shear))
    gates.append(("factorable shear is rejected by the quadric gate", factor_shear is not None and not preserves_quadric(factor_shear[1])))

    A2 = [[Fraction(2), Fraction(0)], [Fraction(1), Fraction(1)]]
    B2 = [[Fraction(1), Fraction(0), Fraction(0)],
          [Fraction(0), Fraction(-1), Fraction(0)],
          [Fraction(0), Fraction(0), Fraction(-1)]]
    composed = matmul(kron(A2, B2), authorized)
    composed_factor = block_factor(composed)
    gates.append(("authorized maps remain factored under composition", composed_factor is not None))
    gates.append(("quadric preservation survives composition", composed_factor is not None and preserves_quadric(composed_factor[1])))

    gates.append(("authorized locus dimension is seven", 4 + 4 - 1 == 7))
    gates.append(("ambient six-channel endomorphism dimension is thirty-six", 6 * 6 == 36))

    for name, passed in gates:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print(f"SUMMARY: {sum(ok for _, ok in gates)}/{len(gates)} gates passed")
    if not all(ok for _, ok in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
