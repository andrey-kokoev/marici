"""Deck-odd Cech differential for the two lower infinity nodes."""

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


def main():
    # Odd edge generators are the differences of the two sheet-to-node edges
    # at E+ and E-. Both boundaries are the sheet difference, up to a common
    # orientation sign.
    odd_cech_differential = [[1, 1]]
    assert rank(odd_cech_differential) == 1

    graph_cycle = (1, -1)
    assert sum(a * b for a, b in zip(odd_cech_differential[0], graph_cycle)) == 0

    local_node_rank = 2
    global_graph_h1_rank = local_node_rank - rank(odd_cech_differential)
    odd_sheet_target_cokernel_rank = 1 - rank(odd_cech_differential)
    assert global_graph_h1_rank == 1
    assert odd_sheet_target_cokernel_rank == 0

    print("local_odd_node_generators: 2")
    print("odd_Cech_differential: [1,1]")
    print("odd_Cech_differential_rank: 1")
    print("surviving_graph_cycle_rank: 1")
    print("surviving_cycle: node_plus-node_minus")
    print("odd_sheet_target_cokernel_rank: 0")
    print("full_global_de_Rham_Betti_numbers: NOT_YET_ASSERTED")


if __name__ == "__main__":
    main()
