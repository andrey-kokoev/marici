#!/usr/bin/env python3
"""Solve the reflection-equivariant log-ray to normalization-sheet map."""


def matvec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


def main() -> None:
    solutions = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            matrix = [[a, b], [b, a]]  # commutes with sheet/ray reflection
            boundary_ok = matvec(matrix, [-1, 1]) == [1, -1]
            counit_ok = [sum(column) for column in zip(*matrix)] == [1, 1]
            if boundary_ok and counit_ok:
                solutions.append((a, b, matrix))

    assert solutions == [(0, 1, [[0, 1], [1, 0]])]
    a, b, matrix = solutions[0]
    determinant = a * a - b * b
    assert determinant == -1

    # Thus r_D maps to e_minus and r_1 maps to e_plus in the fixed convention.
    assert matvec(matrix, [1, 0]) == [0, 1]
    assert matvec(matrix, [0, 1]) == [1, 0]

    # Instantiate the previously conditional reduced endpoint equation.
    # The normalized odd counit is b=1 and 2a+b=1.
    assert 2 * a + b == 1
    p_partial_q = a % 2
    polarity_bockstein = p_partial_q
    assert p_partial_q == 0
    assert polarity_bockstein == 0

    print("ray_to_sheet_matrix: [[0,1],[1,0]]")
    print("determinant: -1 (unimodular)")
    print("branch_labels: r_D03->e_minus, r_1->e_plus")
    print("endpoint_mapping_fiber: INSTANTIATED")
    print("p_partial_Q: 0")
    print("polarity_Bockstein: 0")


if __name__ == "__main__":
    main()
