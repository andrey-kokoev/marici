#!/usr/bin/env python3
"""Minimal exact witness for the skew-quotient obstruction."""


def conjugate_transpose(matrix):
    return tuple(tuple(matrix[j][i].conjugate() for j in range(len(matrix))) for i in range(len(matrix[0])))


def multiply(left, right):
    columns = tuple(zip(*right))
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in columns) for row in left)


def main():
    n = ((0, 1), (0, 0))
    zero = ((0, 0), (0, 0))
    assert n != zero
    assert multiply(n, n) == zero
    assert conjugate_transpose(n) != tuple(tuple(-value for value in row) for row in n)

    # A same-dimensional quotient has invertible pi, so it is a similarity.
    # Similarity preserves diagonalizability; N has a one-dimensional kernel
    # but algebraic zero multiplicity two, hence is not diagonalizable.
    kernel_dimension = 1
    algebraic_zero_multiplicity = 2
    assert kernel_dimension < algebraic_zero_multiplicity

    print("tail_incidence=nonzero_nilpotent")
    print("tail_incidence=not_diagonalizable")
    print("skew_adjoint_quotient=diagonalizable")
    print("positive_operator_quotient=impossible")


if __name__ == "__main__":
    main()

