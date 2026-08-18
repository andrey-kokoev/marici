"""Decompose the Euler--Cartier boundary divisor into source-derived factors."""


def main():
    # Divisors are ordered as multiplicities at (b=+1,b=-1).
    rees_t = (1, 1)       # t|_D=(b-1)(b+1)/2
    incidence_l1 = (0, 1) # L1|_{u=0}=b+1
    target = (3, 4)

    decompositions = []
    for rees_power in range(8):
        for incidence_power in range(8):
            divisor = (
                rees_power * rees_t[0] + incidence_power * incidence_l1[0],
                rees_power * rees_t[1] + incidence_power * incidence_l1[1],
            )
            if divisor == target:
                decompositions.append((rees_power, incidence_power))
    assert decompositions == [(3, 1)]

    # The same pair is forced directly by a^7*(b+1): three conversions
    # a^2=u*t, one residual a, and one L1 incidence factor.
    relative_a_degree = 7
    assert relative_a_degree == 2 * 3 + 1
    assert (relative_a_degree // 2, 1) == decompositions[0]

    # Available sector incidence exponents differ by at most one because
    # e_a=2-s_a with s_a in {0,1}; the required single L1 factor is legal.
    sector_incidence_exponents = {2 - sa for sa in (0, 1)}
    assert sector_incidence_exponents == {1, 2}
    assert max(sector_incidence_exponents) - min(sector_incidence_exponents) == 1

    print("target_boundary_divisor_(plus,minus): (3,4)")
    print("tautological_Rees_divisor_t: (1,1)")
    print("incidence_L1_divisor: (0,1)")
    print("unique_nonnegative_decomposition: 3*div(t)+1*div(L1)")
    print("Rees_source: three_conversions_a^2=u*t")
    print("incidence_source: L1|u=0=b+1")
    print("boundary_twist_is_source_derived: YES")
    print("Euler_plane_as_Q[b]_module: INVALID_BY_ENTRY_449")
    print("twisted_lattice_identification_implies_cohomology_identification: NO")
    print("next_gate: DERIVE_THE_RESIDUAL_EULER_DIFFERENTIAL_ON_THE_TWISTED_CARTIER_LAYER")


if __name__ == "__main__":
    main()
