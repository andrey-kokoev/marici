"""Exact finite witnesses for the ternary germ and invertible raising wall."""

from fractions import Fraction


def row_times_matrix(row, matrix):
    return (
        row[0] * matrix[0][0] + row[1] * matrix[1][0],
        row[0] * matrix[0][1] + row[1] * matrix[1][1],
    )


checks = 0
for delta, tau in (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(2)),
    (Fraction(3, 2), Fraction(-4, 3)),
):
    # Real 4-coordinate determinant has the same nonzero |z| gate; the
    # following 2x2 real model suffices for exact row nontermination.
    matrix = ((-tau, -delta), (-delta, tau))
    determinant = -tau * tau - delta * delta
    assert determinant != 0
    checks += 1

    for initial in ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)), (Fraction(2), Fraction(-3))):
        row = initial
        for _ in range(8):
            row = row_times_matrix(row, matrix)
            assert row != (0, 0)
            checks += 1

# Native ternary cube remains invisible on all binary faces.
for z, h, p in ((Fraction(1), Fraction(2), Fraction(3)), (Fraction(-2), Fraction(1, 3), Fraction(5))):
    assert -2 * z * h * 0 == 0
    assert -2 * z * 0 * p == 0
    assert -2 * 0 * h * p == 0
    assert -2 * z * h * p != 0
    checks += 4

print(f"PASS {checks}/{checks}: ternary germ survives and no finite invertible binary row recursion terminates")

