"""Construct the three target detector rows on the labelled pullback basis."""

from itertools import product

D2 = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, -1],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
]
Z = [1, 0, 1, 0, 0]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def col(m, j):
    return [row[j] for row in m]


def closed(row):
    return all(dot(row, col(D2, j)) == 0 for j in range(4))


def main():
    # Global Q descent: C3 invariance forces equal values on the three roads;
    # no endpoint component and primitive D03 normalization fix the row.
    s_row = [0, 0, 1, 1, 1]
    s_candidates = [
        list(row) for row in product(range(-1, 2), repeat=5)
        if closed(row) and row[0] == row[1] == 0
        and row[2] == 1 and row[2] == row[3] == row[4]
    ]
    assert s_candidates == [s_row]

    # The selected relation detector rho0 has value one on the D03 road.
    # Its C3/Cech-compatible extension is the same global road row.
    v_row = [0, 0, 1, 1, 1]

    # The reciprocal endpoint detector is the oriented branch difference,
    # fixed by the unimodular ray-to-sheet swap and zero on road generators.
    W_row = [1, -1, 0, 0, 0]
    W_candidates = [
        list(row) for row in product(range(-1, 2), repeat=5)
        if closed(row) and row[0] == 1 and row[1] == -1
        and row[2] == row[3] == row[4] == 0
    ]
    assert W_candidates == [W_row]

    for row in (s_row, W_row, v_row):
        assert closed(row)
        assert dot(row, Z) == 1

    print("s_detector_row: 0,0,1,1,1")
    print("W_detector_row: 1,-1,0,0,0")
    print("v_detector_row: 0,0,1,1,1")
    print("all_rows_annihilate_d2: YES")
    print("detector_values_on_z: 1,1,1")
    print("normalized_supported_image: s+W+v")
    print("scope: C3-invariant normalized six-point primitive")


if __name__ == "__main__":
    main()
