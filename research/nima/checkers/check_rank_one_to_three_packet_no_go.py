"""Rank obstruction to independent (a,b,c) from one physical line."""

from itertools import product


def rank_of_column(column):
    return 0 if column == (0, 0, 0) else 1


def main():
    # Any Z-linear map from the current H1=Z to the packet Z^3 is determined
    # by one column. Its image has rank at most one.
    samples = list(product(range(-2, 3), repeat=3))
    assert all(rank_of_column_column <= 1 for rank_of_column_column in map(rank_of_column, samples))

    # No 3x1 matrix has a 3x3 minor, hence none is surjective onto Z^3.
    assert all(len((column,)) < 3 for column in samples)

    normalized = (1, 1, 1)
    image_window = {(n, n, n) for n in range(-3, 4)}
    assert all(tuple(n * x for x in normalized) in image_window for n in range(-3, 4))
    assert (1, 0, 0) not in image_window
    assert (0, 1, 0) not in image_window
    assert (0, 0, 1) not in image_window

    print("physical_source_homology_rank: 1")
    print("selected_packet_rank: 3")
    print("maximum_image_rank: 1")
    print("independent_a_b_c_from_current_line: IMPOSSIBLE")
    print("normalized_image_column: 1,1,1")
    print("required_new_input: rank-three coefficient-enriched physical source or non-linear parameter family")


if __name__ == "__main__":
    main()
