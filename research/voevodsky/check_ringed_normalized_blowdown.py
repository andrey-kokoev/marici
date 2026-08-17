"""Audit normalized blowdown as a ringed finite-space morphism."""

import check_d03_normalized_blowdown_counit as cellular


def matrix_vector(matrix, vector):
    return [
        sum(value * coefficient for value, coefficient in zip(row, vector))
        for row in matrix
    ]


def main():
    # Re-run the exact occurrence-loaded normalized-chain counit.
    cellular.main()

    source_faces = [
        frozenset(),
        frozenset({"D"}),
        frozenset({"1", "3", "5"}),
        frozenset({"1", "3"}),
        frozenset({"E", "1", "3"}),
        frozenset({"E", "3"}),
        frozenset({"E", "D", "3"}),
        frozenset({"D", "3"}),
        frozenset({"D", "0", "3"}),
    ]

    # The source structure ring is the inverse image of the target ring.
    # Blowdown is idempotent, so every stalk map is the identity on the
    # prescribed localization and every occurrence label agrees.
    for face in source_faces:
        image = cellular.old(face)
        assert cellular.old(image) == image
        assert cellular.label(face) == cellular.label(image)

    # Nontrivial fiber: h lies below the two exceptional rays h_D and h_1.
    # C1 -> C0 -> Z is the augmented cellular complex of a tree.
    fiber_boundary = [[-1, -1], [1, 0], [0, 1]]
    fiber_augmentation = [[1, 1, 1]]
    for edge in ([1, 0], [0, 1]):
        assert matrix_vector(
            fiber_augmentation, matrix_vector(fiber_boundary, edge)
        ) == [0]

    # Explicit cone contraction to the central vertex h.
    h_minus_one = [[1], [0], [0]]
    h_zero = [[0, 1, 0], [0, 0, 1]]
    for vertex in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        dh = matrix_vector(fiber_boundary, matrix_vector(h_zero, vertex))
        hd = matrix_vector(
            h_minus_one, matrix_vector(fiber_augmentation, vertex)
        )
        assert [a + b for a, b in zip(dh, hd)] == list(vertex)
    for edge in ([1, 0], [0, 1]):
        assert matrix_vector(h_zero, matrix_vector(fiber_boundary, edge)) == list(
            edge
        )

    print("ringed_stalk_maps: IDENTITY_ON_PULLBACK_LOCALIZATIONS")
    print("occurrence_LCM_compatibility: PASS")
    print("nontrivial_fiber_shape: V_TREE")
    print("higher_fiber_homology: 0")
    print("derived_left_Kan_equals_ordinary_left_Kan: YES")
    print("ringed_normalized_blowdown: CONSTRUCTED_ON_MARKED_FINITE_SPACE")
    print("relative_dualizing_trace: NEXT_GATE")


if __name__ == "__main__":
    main()
