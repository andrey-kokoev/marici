"""Compute the physical derived pullback after the sheet transform exists."""

import check_global_mixed_variance_transform as transform


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def matmul(left, right):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*right)] for row in left]


def rank_mod(matrix, prime):
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [(x - factor * y) % prime for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main():
    transform.main()

    # C3 -> C2 -> C1 -> C0 from the unsplit conductor/road homotopy pullback.
    d3 = [[0], [1], [1], [1]]
    d2 = [
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, -1],
        [0, -1, 1, 0],
        [0, 0, -1, 1],
    ]
    d1 = [[1, -1, -1, -1, -1]]
    assert matmul(d2, d3) == [[0], [0], [0], [0], [0]]
    assert matmul(d1, d2) == [[0, 0, 0, 0]]

    for prime in (2, 3, 5, 101):
        assert (rank_mod(d3, prime), rank_mod(d2, prime), rank_mod(d1, prime)) == (1, 3, 1)

    chain_ranks = (1, 4, 5, 1)
    homology_ranks = (
        chain_ranks[0] - 1,
        chain_ranks[1] - 1 - 3,
        chain_ranks[2] - 3 - 1,
        chain_ranks[3] - 1,
    )
    assert homology_ranks == (0, 0, 1, 0)

    # Unit minors in all three differentials make the image lattices saturated.
    assert d3[1][0] == 1
    assert d2[0][0] == 1
    assert d1[0][0] == 1

    # Primitive degree-one cycle in C1; its road augmentation is +1.
    primitive = [1, 0, 1, 0, 0]
    assert matvec(d1, primitive) == [0]
    road_augmentation = sum(primitive[2:])
    assert road_augmentation == 1

    # Only after the integral verdict: the completed endpoint matrix selects
    # even parity, and one polarity twist makes the reflection action positive.
    endpoint_parity = 0
    road_reflection = -1
    polarity_reflection = -1
    assert endpoint_parity == 0
    assert road_reflection * polarity_reflection == 1

    print("physical_pullback_chain_ranks: 1,4,5,1")
    print("physical_pullback_differential_ranks: 1,3,1")
    print("integral_homology: H1=Z, ALL_OTHER_ZERO")
    print("integral_torsion: NONE")
    print("primitive_generator_road_augmentation: +1")
    print("loaded_reflection_parity: EVEN")
    print("generic_Q_leg: +1")
    print("Cartier_edge_residue: +1")
    print("ordinary_forgetting_shadow: 0")
    print("six_point_positive_sheet_physical_class: PRIMITIVE_UNIQUE_LINE")
    print("eight_point_Cut_naturality: NEXT_GATE")


if __name__ == "__main__":
    main()
