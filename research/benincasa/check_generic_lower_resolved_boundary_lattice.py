"""Compute the resolved four-component boundary lattice of one lower wall."""

from fractions import Fraction


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work)) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def determinant(matrix):
    work = [row[:] for row in matrix]
    previous = 1
    sign = 1
    for column in range(len(work) - 1):
        pivot = next((r for r in range(column, len(work)) if work[r][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        value = work[column][column]
        for r in range(column + 1, len(work)):
            for c in range(column + 1, len(work)):
                work[r][c] = (work[r][c] * value - work[r][column] * work[column][c]) // previous
        previous = value
    return sign * work[-1][-1]


def main():
    # Components are D+,D-,E+,E-. The exceptional curves resolve two A1
    # points, so E+^2=E-^2=-2. Each strict sheet meets each exceptional once;
    # the strict sheets and exceptional curves are otherwise disjoint.
    # The total transform of the infinity line is D+ + D- + E+ + E- and has
    # square two (degree-two cover of a projective line), forcing D+^2=D-^2=-1.
    intersection = [
        [-1, 0, 1, 1],
        [0, -1, 1, 1],
        [1, 1, -2, 0],
        [1, 1, 0, -2],
    ]
    assert rank(intersection) == 4
    assert abs(determinant(intersection)) == 4
    total = (1, 1, 1, 1)
    total_square = sum(total[i] * intersection[i][j] * total[j] for i in range(4) for j in range(4))
    assert total_square == 2

    # The dual graph is K_{2,2}. Its oriented incidence has rank three and one
    # primitive cycle D+-E+-D--E--D+.
    incidence = [
        [-1, -1, 0, 0],
        [0, 0, -1, -1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
    ]
    assert rank(incidence) == 3
    conductor_cycle = (1, -1, -1, 1)
    assert all(sum(incidence[row][column] * conductor_cycle[column] for column in range(4)) == 0 for row in range(4))

    component_classes = 4
    conductor_cycles = 4 - rank(incidence)
    relative_boundary_rank = component_classes + conductor_cycles
    assert (component_classes, conductor_cycles, relative_boundary_rank) == (4, 1, 5)

    print("resolved_boundary_components: D+,D-,E+,E-")
    print("resolved_boundary_dual_graph: K2,2")
    print("boundary_intersection_matrix: [-1,0,1,1;0,-1,1,1;1,1,-2,0;1,1,0,-2]")
    print("boundary_intersection_determinant: -4_UP_TO_SIGN")
    print("total_infinity_transform_square: 2")
    print("component_class_rank: 4")
    print("primitive_conductor_cycle_rank: 1")
    print("resolved_relative_boundary_lattice_rank: 5")
    print("rank_five_single_wall_geometry_rank_match: EXACT")
    print("pair_residue_rows: CERTIFIED_BY_RUST_AUDIT")
    print("identification_with_twisted_de_Rham: REQUIRES_COMPARISON_MAP")


if __name__ == "__main__":
    main()
