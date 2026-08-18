"""Integral Smith-index audit for the completed lower boundary rows."""

from itertools import combinations
from math import gcd


def determinant(matrix):
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(len(work) - 1):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        value = work[column][column]
        for row in range(column + 1, len(work)):
            for col in range(column + 1, len(work)):
                work[row][col] = (
                    work[row][col] * value
                    - work[row][column] * work[column][col]
                ) // previous
        previous = value
    return sign * work[-1][-1]


def main():
    rows = [
        [-4, -4, -2, -2, 0],
        [-1, -1, 0, -1, 0],
        [-1, -1, -1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, -1, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    maximal_minors = [
        determinant([rows[index] for index in selection])
        for selection in combinations(range(len(rows)), 5)
    ]
    nonzero = [abs(value) for value in maximal_minors if value]
    index = 0
    for value in nonzero:
        index = gcd(index, value)
    assert index == 2

    # A primitive generating subsystem is sheet sum, sheet difference,
    # E+, E-, gamma. Its determinant realizes the same index.
    primitive_rows = [
        [1, 1, 0, 0, 0],
        [1, -1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ]
    assert abs(determinant(primitive_rows)) == 2

    print("completed_boundary_row_rank_over_Q: 5")
    print("gcd_of_nonzero_maximal_minors: 2")
    print("smith_type: 1,1,1,1,2")
    print("integral_cokernel: Z/2")
    print("missing_integral_operation: HALF_SUM_SHEET_SPLITTING")


if __name__ == "__main__":
    main()
