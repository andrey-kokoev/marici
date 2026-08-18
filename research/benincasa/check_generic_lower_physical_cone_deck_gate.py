"""Deck-character gate for the physical ordinary-contiguity cone."""


def main():
    tangential_rank = 5
    normal_residue_character = 1
    square_root_character = -1
    physical_character = normal_residue_character * square_root_character
    assert physical_character == -1

    source_plus = 0
    source_minus = tangential_rank
    boundary_plus = 3
    boundary_minus = 2

    max_equivariant_rank = min(source_plus, boundary_plus) + min(
        source_minus, boundary_minus
    )
    forced_kernel_rank = tangential_rank - max_equivariant_rank
    assert max_equivariant_rank == 2
    assert forced_kernel_rank == 3

    print("normal_contiguity_residue_character: PLUS")
    print("physical_square_root_character: MINUS")
    print("physical_rank_five_cone_characters: plus=0,minus=5")
    print("raw_boundary_characters: plus=3,minus=2")
    print("max_equivariant_source_to_boundary_rank: 2")
    print("forced_source_kernel_rank: 3")
    print("equivariant_rank_five_isomorphism: IMPOSSIBLE")
    print("required_target_enlargement: THREE_ADDITIONAL_SIGN_DIRECTIONS")


if __name__ == "__main__":
    main()
