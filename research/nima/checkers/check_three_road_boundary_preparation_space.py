"""Recover the rank-three road boundary preparation space before road gluing."""

D2 = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, -1],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
]
D1 = [[1, -1, -1, -1, -1]]


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def column(matrix, j):
    return [row[j] for row in matrix]


def sub(x, y):
    return [a - b for a, b in zip(x, y)]


def main():
    # C1 basis: conductor+, conductor-, road_D03, road_D25, road_D14.
    # The joint road trace is the projection Gamma:C1 -> Z^3.
    def gamma(x):
        return tuple(x[2:])

    # Three closed lifts give a right inverse of Gamma on ker(d1).
    p03 = [1, 0, 1, 0, 0]
    p25 = [1, 0, 0, 1, 0]
    p14 = [1, 0, 0, 0, 1]
    preparations = (p03, p25, p14)
    assert all(matvec(D1, p) == [0] for p in preparations)
    assert [gamma(p) for p in preparations] == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    # The conductor boundary lies in ker Gamma, so Gamma descends after quotienting
    # by the internal conductor relation but before quotienting by road gluing.
    conductor_boundary = column(D2, 0)
    assert conductor_boundary == [1, 1, 0, 0, 0]
    assert gamma(conductor_boundary) == (0, 0, 0)

    # The remaining d2 columns are exactly the two road-difference relations
    # (with one redundant cyclic closure). They identify the three preparations.
    road_boundaries = [column(D2, j) for j in range(1, 4)]
    assert road_boundaries == [
        [0, 0, 1, -1, 0],
        [0, 0, 0, 1, -1],
        [0, 0, -1, 0, 1],
    ]
    assert sub(p03, p25) == road_boundaries[0]
    assert sub(p25, p14) == road_boundaries[1]
    assert sub(p14, p03) == road_boundaries[2]
    assert [sum(gamma(b)) for b in road_boundaries] == [0, 0, 0]

    # Therefore pre-gluing boundary preparations are Z^3; full road descent
    # applies the augmentation (a,b,c) |-> a+b+c and leaves one physical line.
    for a, b, c in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -3, 5)):
        lift = [a + b + c, 0, a, b, c]
        assert matvec(D1, lift) == [0]
        assert gamma(lift) == (a, b, c)

    print("joint_road_trace_rank_on_cycles: 3")
    print("pre_gluing_boundary_preparation_space: Z^3")
    print("boundary_basis: p_D03,p_D25,p_D14")
    print("road_gluing_kernel: augmentation_ideal_rank_2")
    print("full_physical_descent: (a,b,c)->a+b+c")
    print("normalized_primitive: p_D03=(1,0,1,0,0)")


if __name__ == "__main__":
    main()
