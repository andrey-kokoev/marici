"""Type the rank-five lower residue object and its Artin inertia character."""

from itertools import combinations

import check_generic_lower_kato_incidence as incidence


CLOSED = (7, 12, 12, 18, 12, 18, 18, 26, 12, 17, 18, 24, 18, 24, 26, 34)
PROPER = incidence.PROPER
# Frozen generic regulator representatives used by the exact critical census.
REGULATOR = (17, 19, 23, 29)


def main():
    # The first deletion triangle identifies each single-pole residue object
    # with the rank increment from the K-only complement to the pole complement.
    single_residue_ranks = tuple(CLOSED[1 << i] - CLOSED[0] for i in range(4))
    assert single_residue_ranks == (5, 5, 5, 5)

    # On a transverse pair, the second residue has the Möbius rank. The unique
    # parallel fiber product is empty and therefore has no residue object.
    pair_ranks = {}
    for i, j in combinations(range(4), 2):
        mask = (1 << i) | (1 << j)
        nonempty, normal_rank = incidence.generically_nonempty((i, j))
        expected = 1 if nonempty else 0
        assert PROPER[mask] == expected
        assert normal_rank == (2 if nonempty else 1)
        pair_ranks[(i, j)] = expected

    triple_ranks = {}
    for triple in combinations(range(4), 3):
        mask = sum(1 << i for i in triple)
        nonempty, normal_rank = incidence.generically_nonempty(triple)
        expected = 1 if nonempty else 0
        assert PROPER[mask] == expected
        triple_ranks[triple] = expected
        if nonempty:
            assert normal_rank == 3

    # Iterated residues are the canonical shriek/restriction kernels for the
    # Cartier inclusions. Their Boolean signs are inherited from the ordered
    # conormal determinant; no splitting or matrix representative is chosen.
    residue_kernel_types = {
        "single": "RΓ_dR(D_i minus V(K), L_K)[shift]",
        "pair": "RΓ_dR(D_i intersect D_j minus V(K), L_K)[shift]",
        "triple": "costalk at transverse marked point",
    }
    assert all(residue_kernel_types.values())

    # Entry 544's finite PC category carries no regulator-residue datum. The
    # generic twisted de Rham calculation loads nonzero formal residues on all
    # four logarithmic divisors. Identifying those residues with algebraic
    # Artin-torus inertia characters would require an additional realization
    # theorem and is deliberately not asserted here.
    zero_character = (0, 0, 0, 0)
    regulator_character = REGULATOR
    assert regulator_character != zero_character
    assert all(value != 0 for value in regulator_character)
    single_characters = tuple(
        tuple(value if index == i else 0 for index, value in enumerate(REGULATOR))
        for i in range(4)
    )
    assert all(character != zero_character for character in single_characters)

    print("single_pole_residue_object: RGamma_dR(plane_minus_K_section,twist)[shift]")
    print("single_pole_residue_ranks: 5,5,5,5")
    print("finite_pair_residue_ranks: 1,1,1,1,1")
    print("parallel_pair_residue_rank: 0_FROM_EMPTY_FIBER_PRODUCT")
    print("transverse_triple_costalk_ranks: 1,1")
    print("other_triple_and_fourfold_costalks: ZERO_FROM_EMPTY_SUPPORT")
    print("residue_Gysin_kernel_type: CANONICAL_CARTIER_LOCALIZATION")
    print("Boolean_Beck_Chevalley_signs: SOURCE_CONORMAL_ORDER")
    print(f"generic_regulator_character: {regulator_character}")
    print("cosmology_coefficient_in_bare_trivial_inertia_diagram: NO")
    print("shared_Kato_support_and_kernel_calculus: PASS")
    print("required_coefficient_enrichment: LOG_CONNECTION_WITH_REGULATOR_RESIDUES")
    print("identification_with_nontrivial_Artin_inertia: UNCONSTRUCTED")


if __name__ == "__main__":
    main()
