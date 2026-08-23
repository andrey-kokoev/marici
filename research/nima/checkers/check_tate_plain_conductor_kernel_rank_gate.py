"""Rank gate for the plain three-axis normalization-conductor kernel.

The degree-two contraction of [A+ + A- -> C]^{tensor 3} along a pair of
axes evaluates the two contracted sheet choices by their product sign and
retains only the uncontracted sheet.  This checker asks whether that plain
map can distinguish the 24 maximal-cone/pair BC rows.
"""

from fractions import Fraction
from itertools import product
import json


PAIRS = ((0, 1), (0, 2), (1, 2))
SIGNS = tuple(product((1, -1), repeat=3))
SOURCE = tuple((signs, pair) for signs in SIGNS for pair in PAIRS)
TARGET = tuple((pair, remaining_sign) for pair in PAIRS for remaining_sign in (1, -1))


def rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [a - scale * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def plain_matrix() -> list[list[int]]:
    matrix = [[0 for _ in SOURCE] for _ in TARGET]
    for column, (signs, pair) in enumerate(SOURCE):
        complement = next(axis for axis in range(3) if axis not in pair)
        row = TARGET.index((pair, signs[complement]))
        matrix[row][column] = signs[pair[0]] * signs[pair[1]]
    return matrix


def duplicate_rows(matrix: list[list[int]], copies: int) -> list[list[int]]:
    """External spectator copies without a source-derived routing label.

    Identical duplication does not increase rank.  This is the correct
    negative control for merely tensoring with an unselected free factor.
    """
    return [row[:] for _ in range(copies) for row in matrix]


def main() -> None:
    matrix = plain_matrix()
    plain_rank = rank(matrix)
    assert (len(TARGET), len(SOURCE), plain_rank) == (6, 24, 6)
    assert all(sum(value != 0 for value in row) == 4 for row in matrix)

    # Merely adjoining named copies without a source-derived routing map
    # repeats the same six rows.  Neither one binary spectator nor two such
    # spectators restore the missing rank.
    one_binary_spectator_rank = rank(duplicate_rows(matrix, 2))
    two_binary_spectators_rank = rank(duplicate_rows(matrix, 4))
    assert one_binary_spectator_rank == two_binary_spectators_rank == 6

    packet = {
        "claim": (
            "The plain tensor-cube normalization-conductor difference map "
            "from 24 maximal-cone/pair rows to pairwise conductor outputs "
            "has rank 6 and an 18-dimensional kernel."
        ),
        "status": "proved_scoped_sufficiency_no_go",
        "source_rows": 24,
        "plain_target_rows": 6,
        "plain_rank": plain_rank,
        "plain_kernel_dimension": len(SOURCE) - plain_rank,
        "one_unrouted_binary_spectator_rank": one_binary_spectator_rank,
        "two_unrouted_binary_spectators_rank": two_binary_spectators_rank,
        "consequence": (
            "The universal conductor difference complex supplies the mixed-"
            "variance type but is not by itself the 24-row realization.  "
            "Boolean-replacement and Tor labels must be retained with source-"
            "derived routing maps; merely tensoring spectator copies cannot "
            "restore the lost information."
        ),
        "next_test": (
            "Derive the two routing bits from the full-log exceptional and "
            "Cartier filtrations, then recompute the 24x24 rank and the global "
            "six-short-facet boundary."
        ),
    }
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
