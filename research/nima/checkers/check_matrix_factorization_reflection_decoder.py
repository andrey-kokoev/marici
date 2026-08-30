#!/usr/bin/env python3
"""Exact rank and homology audit for the reflection-depth decoder."""

from fractions import Fraction


def coefficient(depth):
    return Fraction(-6, 1) if depth % 2 else Fraction(-1, 6)


def differential(depth, branching=4):
    """Matrix over Q for multiplication by a*z from A^b^n to A^b^(n-1).

    Each A coordinate is ordered (constant, z). Multiplication by a*z maps
    the constant input to the z output and annihilates the z input.
    """
    assert depth >= 1
    sources = branching ** depth
    targets = branching ** (depth - 1)
    rows, cols = 2 * targets, 2 * sources
    matrix = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    a = coefficient(depth)
    for child in range(sources):
        parent = child // branching
        matrix[2 * parent + 1][2 * child] = a
    return matrix


def rank(matrix):
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [v / scale for v in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def multiply(left, right):
    assert len(left[0]) == len(right)
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*right)]
        for row in left
    ]


def main():
    branching = 4
    for depth in range(1, 5):
        d = differential(depth, branching)
        assert rank(d) == branching ** (depth - 1)
        if depth >= 2:
            composite = multiply(differential(depth - 1, branching), d)
            assert all(value == 0 for row in composite for value in row)

    stable = {}
    for depth in range(1, 4):
        dim_chain = 2 * branching ** depth
        stable[depth] = (
            dim_chain
            - rank(differential(depth, branching))
            - rank(differential(depth + 1, branching))
        )
        assert stable[depth] == 3 * branching ** (depth - 1)

        top_before = dim_chain - rank(differential(depth, branching))
        killed_next = rank(differential(depth + 1, branching))
        assert top_before == 7 * branching ** (depth - 1)
        assert top_before - killed_next == stable[depth]

    # One branch has no sibling-difference syndrome: positive-degree homology
    # is exactly zero after the next layer arrives.
    for depth in range(1, 4):
        dim_chain = 2
        homology = dim_chain - rank(differential(depth, 1)) - rank(differential(depth + 1, 1))
        assert homology == 0

    print("PASS: alternating source maps square to zero on z^2=0")
    print("PASS: next layer removes exactly the finite-frontier artifact")
    print("PASS: stable H_n has three sibling syndromes per parent")
    print("PASS: the one-branch control is exact in positive depth")


if __name__ == "__main__":
    main()
