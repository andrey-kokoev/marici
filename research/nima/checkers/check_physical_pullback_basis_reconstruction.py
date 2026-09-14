"""Recover the only block labeling compatible with the Entry-436 construction."""

from itertools import permutations

# Entry-436 matrices.
d2 = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, -1],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
]
d1 = [1, -1, -1, -1, -1]
z = [1, 0, 1, 0, 0]


def column(m, j):
    return [row[j] for row in m]


def main():
    labels = ("conductor+", "conductor-", "road-D03", "road-D25", "road-D14")

    # The first d2 column has support exactly on the two conductor slots.
    assert column(d2, 0) == [1, 1, 0, 0, 0]

    # The last three columns are the oriented triangle incidence on the three
    # road slots, in the independently exported Q order D03,D25,D14.
    road_columns = [column(d2, j)[2:] for j in (1, 2, 3)]
    assert road_columns == [[1, -1, 0], [0, 1, -1], [-1, 0, 1]]
    assert [sum(c) for c in road_columns] == [0, 0, 0]

    # No alternate permutation preserves the ordered exported incidence matrix.
    preserving = []
    target = road_columns
    for p in permutations(range(3)):
        permuted = [[c[p[i]] for i in range(3)] for c in target]
        if permuted == target:
            preserving.append(p)
    assert preserving == [(0, 1, 2)]

    endpoint_row = [1, -1, 0, 0, 0]
    road_row = [0, 0, 1, 1, 1]
    assert d1 == [a - b for a, b in zip(endpoint_row, road_row)]
    assert sum(a * b for a, b in zip(endpoint_row, z)) == 1
    assert sum(a * b for a, b in zip(road_row, z)) == 1

    print("C1_basis_labels:", ",".join(labels))
    print("conductor_boundary_row: 1,-1,0,0,0")
    print("road_augmentation_row: 0,0,1,1,1")
    print("road_order: D03,D25,D14")
    print("ordered_block_labeling: UNIQUE")
    print("cross_target_s_W_v_row_assignment: STILL_REQUIRES_CONNECTOR_RESTRICTION_MAPS")


if __name__ == "__main__":
    main()
