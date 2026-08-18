"""Rank audit for boundary valuations and marked residue rows."""

from fractions import Fraction


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    left - factor * right
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def apply(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main():
    # Columns: D+, D-, E+, E-, gamma.
    valuations = [
        [-4, -4, -2, -2, 0],  # K
        [-1, -1, 0, -1, 0],   # q_g2
        [-1, -1, -1, 0, 0],   # q_g3
    ]
    pair_rows = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    observable = valuations + pair_rows

    sheet_difference = [1, -1, 0, 0, 0]
    graph_cycle = [0, 0, 0, 0, 1]
    assert rank(valuations) == 2
    assert rank(observable) == 3
    assert apply(observable, sheet_difference) == [0] * len(observable)
    assert apply(observable, graph_cycle) == [0] * len(observable)

    weights = [5, 19, 23]
    full_residue = [
        sum(weights[row] * valuations[row][column] for row in range(3))
        for column in range(5)
    ]
    assert full_residue == [-62, -62, -33, -29, 0]

    print("boundary_basis: D_plus,D_minus,E_plus,E_minus,gamma")
    print("factor_valuation_rank: 2")
    print("valuation_plus_pair_row_rank: 3")
    print("invisible_plane_equals_deck_odd_sector: span(D_plus-D_minus,gamma)")
    print("full_regulator_residue: -62,-62,-33,-29,0")
    print("comparison_map_determined_by_current_data: NO")
    print("required_extra_rows: DECK_NORMALIZATION_TRANSITION,CONDUCTOR_TRACE")


if __name__ == "__main__":
    main()
