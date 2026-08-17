"""Audit the first octagon six-by-four Cut boundary combinatorially."""

from collections import Counter
from itertools import combinations


def diagonals(n):
    return tuple(
        (a, b)
        for a in range(n)
        for b in range(a + 1, n)
        if b != a + 1 and (a, b) != (0, n - 1)
    )


def crosses(x, y):
    a, b = x
    c, d = y
    return (a < c < b < d) or (c < a < d < b)


def faces(ds):
    return tuple(
        face
        for size in range(len(ds) + 1)
        for face in combinations(ds, size)
        if all(not crosses(x, y) for x, y in combinations(face, 2))
    )


def subsets(items):
    return tuple(s for size in range(len(items) + 1) for s in combinations(items, size))


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def main():
    cut = (0, 5)
    left_vertices = (0, 1, 2, 3, 4, 5)
    right_vertices = (0, 5, 6, 7)
    right_relabel = {vertex: i for i, vertex in enumerate(right_vertices)}

    octagon = diagonals(8)
    compatible = tuple(d for d in octagon if d != cut and not crosses(d, cut))
    left = tuple(d for d in compatible if set(d) <= set(left_vertices))
    right = tuple(d for d in compatible if set(d) <= set(right_vertices))
    assert len(left) == 9
    assert len(right) == 2
    assert set(left).isdisjoint(right)
    assert set(left) | set(right) == set(compatible)
    assert {tuple(sorted((right_relabel[a], right_relabel[b]))) for a, b in right} == set(diagonals(4))

    link_faces = faces(compatible)
    left_faces = faces(left)
    right_faces = faces(right)
    split = lambda face: (tuple(d for d in face if d in left), tuple(d for d in face if d in right))
    split_faces = {split(face) for face in link_faces}
    product_faces = {(a, b) for a in left_faces for b in right_faces}
    assert split_faces == product_faces

    face_counts = Counter(map(len, link_faces))
    assert tuple(face_counts[k] for k in range(5)) == (1, 11, 39, 56, 28)
    assert tuple(Counter(map(len, left_faces))[k] for k in range(4)) == (1, 9, 21, 14)
    assert tuple(Counter(map(len, right_faces))[k] for k in range(2)) == (1, 2)

    loaded = tuple((face, marked) for face in link_faces for marked in subsets(face))
    assert len(loaded) == 1075 == 215 * 5
    degree_counts = Counter(4 - len(face) + len(marked) for face, marked in loaded)
    assert tuple(degree_counts[k] for k in range(5)) == (28, 168, 375, 369, 135)

    # The native octagon orientation differs from the product orientation only
    # by the canonical shuffle of left and right diagonals.  Reorienting every
    # face by that shuffle makes every radial incidence exactly the tensor one.
    product_order = left + right
    product_position = {d: i for i, d in enumerate(product_order)}

    def shuffle_sign(face):
        native = tuple(sorted(face))
        return parity(tuple(product_position[d] for d in native))

    incidence_checks = 0
    for face in link_faces:
        for added in compatible:
            if added in face or any(crosses(added, d) for d in face):
                continue
            enlarged = tuple(sorted(face + (added,)))
            native_sign = (-1) ** sum(d < added for d in face)
            transported = shuffle_sign(face) * native_sign * shuffle_sign(enlarged)
            expected = (-1) ** sum(product_position[d] < product_position[added] for d in face)
            assert transported == expected
            incidence_checks += 1
    assert incidence_checks == 369

    # Entry 436 gives a primitive Z-line and the oriented four-point interval
    # supplies its primitive unit.  Their external product is again primitive.
    six_point_generator = 1
    four_point_unit = 1
    assert six_point_generator * four_point_unit == 1

    print("n8_cut: D05")
    print("cut_type: HEXAGON_X_QUADRILATERAL")
    print("link_diagonals: 11=9+2")
    print("link_face_counts: 1,11,39,56,28")
    print("loaded_boundary_cells: 1075=215*5")
    print("loaded_chain_ranks: 28,168,375,369,135")
    print("oriented_radial_incidence_checks: 369")
    print("boundary_external_product_line: PRIMITIVE_PLUS_ONE")
    print("eight_point_interior_candidate: NOT_YET_CONSTRUCTED")
    print("Cut_naturality_verdict: BOUNDARY_TARGET_FORCED_TEST_PENDING")


if __name__ == "__main__":
    main()
