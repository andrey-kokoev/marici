"""Test whether the three road ports can be identified with selected s,W,v channels."""

S = (0, 0, 1, 1, 1)
W = (1, -1, 0, 0, 0)
V = (0, 0, 1, 1, 1)
PREPARATIONS = (
    (1, 0, 1, 0, 0),
    (1, 0, 0, 1, 0),
    (1, 0, 0, 0, 1),
)


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def rank(matrix):
    a = [[float(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    # Rows are channels; columns are labelled road preparations.
    selected_readout = [[dot(row, p) for p in PREPARATIONS] for row in (S, W, V)]
    assert selected_readout == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert rank(selected_readout) == 1

    # In particular no permutation matrix can equal this readout, so no road
    # can be assigned separately to s, W, or v using the established maps.
    assert all(sum(x != 0 for x in row) == 3 for row in selected_readout)

    print("selected_readout_on_road_preparations:")
    for row in selected_readout:
        print(" ", row)
    print("selected_readout_rank: 1")
    print("road_to_s_W_v_assignment: IMPOSSIBLE_WITH_ESTABLISHED_ROWS")
    print("reason: roads_are_C3_permuted_but_s_W_v_are_distinct_detector_types")
    print("correct_symbolic_gate: three_independent_target_typed_boundary_maps")


if __name__ == "__main__":
    main()
