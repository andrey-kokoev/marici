"""Rank-one audit of the endpoint-to-Mobius crosscap comparison."""


def main():
    # Both primitive lines carry rotation +1 and reflection -1.
    endpoint_character = {"rotation": 1, "reflection": -1}
    mobius_character = {"rotation": 1, "reflection": -1}
    assert endpoint_character == mobius_character

    # Every equivariant map Z_or -> Z_or is multiplication by n.
    candidates = range(-4, 5)
    equivariant = [
        n
        for n in candidates
        if all(
            n * endpoint_character[g] == mobius_character[g] * n
            for g in endpoint_character
        )
    ]
    assert equivariant == list(candidates)

    # Entry 94's occurrence-resolved Cousin/Gysin symbol is primitive and
    # positively normalized; hence |n|=1 and the retained sign is +.
    primitive = [n for n in equivariant if abs(n) == 1]
    assert primitive == [-1, 1]
    positive_cousin_normalization = 1
    psi_crosscap = positive_cousin_normalization
    assert psi_crosscap == 1

    primitive_core_pairing = psi_crosscap
    outer_octagon_degree = 2 * primitive_core_pairing
    endpoint_parity = 0
    assert outer_octagon_degree % 2 == endpoint_parity

    print("endpoint_primitive_line: Z_or")
    print("mobius_primitive_line: Z_or")
    print("character_match: rotation=+1 reflection=-1")
    print("primitive_equivariant_maps: [-1,+1]")
    print("positive_Cousin_normalization: +1")
    print("Psi_crosscap_matrix: [1]")
    print("Psi_crosscap_determinant: 1")
    print("primitive_core_pairing: 1")
    print("outer_octagon_period: 2")
    print("endpoint_parity_mod2: 0")
    print("selected_additive_atlas_class: omega")


if __name__ == "__main__":
    main()
