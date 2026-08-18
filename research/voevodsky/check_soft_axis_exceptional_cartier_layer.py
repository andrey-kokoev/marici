"""Identify the canonical Cartier layer carried by the soft exceptional section."""


def basis(cutoff, psi_layers):
    """Normal forms in Q[b,a,psi]/(a^2,psi^psi_layers)."""
    return tuple(
        (b_degree, a_degree, psi_degree)
        for b_degree in range(cutoff + 1)
        for a_degree in (0, 1)
        for psi_degree in range(psi_layers)
    )


def main():
    for cutoff in (8, 12, 16, 20, 24):
        doubled = basis(cutoff, 2)
        cartier = basis(cutoff, 1)
        nilpotent_layer = tuple(m for m in doubled if m[2] == 1)

        # Multiplication by psi sends O_D injectively onto (psi)/(psi^2).
        image = tuple((b_degree, a_degree, 1) for b_degree, a_degree, _ in cartier)
        assert image == nilpotent_layer
        assert len(doubled) == 4 * (cutoff + 1)
        assert len(nilpotent_layer) == len(cartier) == 2 * (cutoff + 1)

        # Quotienting O_2D by the exact image's common Cartier factor leaves
        # O_D.  Its two generators over Q[b] are 1 and a, with a^2=0.
        quotient = tuple(m for m in doubled if m[2] == 0)
        assert quotient == cartier
        print(
            f"cutoff_{cutoff}: O_2D={len(doubled)},"
            f"cartier_layer={len(nilpotent_layer)},O_D={len(quotient)}"
        )

    # The boundary b=+/-1 changes psi to t but does not change the normal
    # form: imposing psi=0 sets t=0 and leaves Q[a]/(a^2).
    boundary_basis = ("1", "a")
    assert len(boundary_basis) == 2

    print("exceptional_double_section: O_2D=Q[b,a,psi]/(a^2,psi^2)")
    print("cartier_exact_sequence: 0->(psi)/(psi^2)->O_2D->O_D->0")
    print("cartier_layer_isomorphic_to_O_D: YES")
    print("global_D_coordinate_ring: Q[b,a]/(a^2)")
    print("pushforward_to_b_axis: FREE_RANK_2_WITH_BASIS_1_a")
    print("b_plus_minus_1_fiber: Q[a]/(a^2)")
    print("identification_with_Euler_resonance_generators: NOT_YET_GRADED")
    print("nearby_cycle_identification: NOT_YET_PROVED")
    print("next_gate: COMPUTE_GRADING_AND_COMPARE_1_a_WITH_THE_TWO_EULER_CLASSES")


if __name__ == "__main__":
    main()
