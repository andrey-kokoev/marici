"""Exact detector lattice of the Entry-436 physical pullback complex."""

# C3 -> C2 -> C1 -> C0. Columns of d2 are boundaries in C1.
d2 = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, -1],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
]
d1 = [1, -1, -1, -1, -1]
z = [1, 0, 1, 0, 0]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def column(matrix, j):
    return [row[j] for row in matrix]


def main():
    # Two primitive cocycles spanning the full integral annihilator of im(d2).
    endpoint = [1, -1, 0, 0, 0]
    road = [0, 0, 1, 1, 1]
    for detector in (endpoint, road):
        assert all(dot(detector, column(d2, j)) == 0 for j in range(4))

    # The only cocycle equations are l1=-l0 and l2=l3=l4, so every integral
    # cocycle is a unique integer combination of these two rows.
    for a in range(-3, 4):
        for c in range(-3, 4):
            row = [a, -a, c, c, c]
            assert row == [a * x + c * y for x, y in zip(endpoint, road)]

    # d1 is the coboundary endpoint-road. Hence H^1-dual is one primitive
    # line and endpoint and road induce the same oriented detector.
    assert d1 == [x - y for x, y in zip(endpoint, road)]
    assert dot(endpoint, z) == dot(road, z) == 1

    print("integral_cocycle_lattice: Z<endpoint> + Z<road>")
    print("coboundary_relation: endpoint-road=d1")
    print("dual_homology_detector: PRIMITIVE_RANK_ONE")
    print("endpoint_detector_on_z: +1")
    print("road_detector_on_z: +1")
    print("coordinate_consequence: every_oriented_primitive_detector_on_H1_reads_+1")
    print("scope: detector must descend through this physical pullback complex")


if __name__ == "__main__":
    main()
