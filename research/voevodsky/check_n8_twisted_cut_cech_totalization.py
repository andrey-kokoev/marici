"""Build the integral scalar and Thom-twisted Cech complexes of the Cut nerve."""

from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd

import check_n8_six_by_four_cut_boundary as polygon
import check_n8_thom_orientation_local_system as thom_local_system


N = 8


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def matrix_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][column]
        work[row] = [value / scale for value in work[row]]
        for r in range(len(work)):
            if r != row and work[r][column]:
                factor = work[r][column]
                work[r] = [a - factor * b for a, b in zip(work[r], work[row])]
        row += 1
    return row


def determinant(matrix):
    """Fraction-free Bareiss determinant."""
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next((r for r in range(column, size) if work[r][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        value = work[column][column]
        for r in range(column + 1, size):
            for c in range(column + 1, size):
                work[r][c] = (work[r][c] * value - work[r][column] * work[column][c]) // previous
        previous = value
    return sign * work[-1][-1]


def maximal_minor_gcd(matrix, rank):
    rows = range(len(matrix))
    columns = range(len(matrix[0]))
    values = []
    for selected_rows in combinations(rows, rank):
        for selected_columns in combinations(columns, rank):
            minor = [[matrix[r][c] for c in selected_columns] for r in selected_rows]
            value = abs(determinant(minor))
            if value:
                values.append(value)
    return reduce(gcd, values), len(values)


def main():
    thom_local_system.main()

    vertices = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    edges = tuple(
        (a, b)
        for a, b in combinations(vertices, 2)
        if not polygon.crosses(a, b)
    )
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}

    # Without the marked-normal line, edge transport is -1 and the Cech
    # differential is the signless incidence matrix: x_b - (-x_a).
    scalar = []
    # Tensoring by the odd Thom-normal line makes transport +1 and recovers
    # the ordinary oriented incidence matrix: x_b - x_a.
    twisted = []
    for a, b in edges:
        scalar_row = [0] * len(vertices)
        scalar_row[vertex_index[a]] = 1
        scalar_row[vertex_index[b]] = 1
        scalar.append(scalar_row)

        twisted_row = [0] * len(vertices)
        twisted_row[vertex_index[a]] = -1
        twisted_row[vertex_index[b]] = 1
        twisted.append(twisted_row)

    assert matrix_rank(scalar) == 8
    scalar_index, scalar_nonzero_minors = maximal_minor_gcd(scalar, 8)
    assert scalar_index == 2
    assert scalar_nonzero_minors > 0

    assert matrix_rank(twisted) == 7
    twisted_index, twisted_nonzero_minors = maximal_minor_gcd(twisted, 7)
    assert twisted_index == 1
    assert twisted_nonzero_minors > 0

    constant_section = [1] * len(vertices)
    assert all(sum(a * b for a, b in zip(row, constant_section)) == 0 for row in twisted)
    assert gcd(*constant_section) == 1
    assert any(sum(a * b for a, b in zip(row, constant_section)) != 0 for row in scalar)

    # Cech cohomology of C0=Z^8 -> C1=Z^12.
    assert len(vertices) - matrix_rank(scalar) == 0
    assert len(edges) - matrix_rank(scalar) == 4
    assert len(vertices) - matrix_rank(twisted) == 1
    assert len(edges) - matrix_rank(twisted) == 5

    print("Cut_Cech_ranks: C0=8,C1=12")
    print("scalar_signless_incidence_rank: 8")
    print("scalar_maximal_minor_gcd: 2")
    print("scalar_Cech_cohomology: H0=0,H1=Z^4_PLUS_Z/2")
    print("Thom_twisted_oriented_incidence_rank: 7")
    print("Thom_twisted_maximal_minor_gcd: 1")
    print("Thom_twisted_Cech_cohomology: H0=Z,H1=Z^5")
    print("Thom_twisted_global_section: CONSTANT_PRIMITIVE")
    print("integral_torsion_after_native_twist: NONE")
    print("twisted_Cech_totalization: CONSTRUCTED")
    print("next_gate: LIFT_COEFFICIENT_LINE_TOTALIZATION_TO_ALL_1075_CELL_CUT_OBJECTS")


if __name__ == "__main__":
    main()
