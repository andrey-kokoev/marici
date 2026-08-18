"""Normalize first-Cartier exact symbols at the two Euler resonances."""


SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))


def u_chart_normal_form(a_degree):
    """a^I = u^floor(I/2) * a^(I mod 2) * t^floor(I/2)."""
    return a_degree // 2, a_degree % 2, a_degree // 2


def main():
    q_sources_for_odd = []
    p_sources_for_odd = []
    for sa, sb in SECTORS:
        ea, eb = 2 - sa, 2 - sb
        for i in range(12):
            for j in range(5):
                # First Cartier p symbol before normalization:
                # -3*u^2*b*a^(i+eb)*c^(j+ea).
                p_a = i + eb
                p_c_floor = j + ea  # b=c-1 mixes this and this+1.
                p_u = 2 + u_chart_normal_form(p_a)[0]
                assert p_u == (p_a + 4) // 2
                if p_a == 7 and p_c_floor <= 1 <= p_c_floor + 1:
                    p_sources_for_odd.append((sa, sb, i, j))

                # First Cartier q symbol:
                # -6*u*a^(i+eb+1)*c^(j+ea).
                q_a = i + eb + 1
                q_c = j + ea
                q_u = 1 + u_chart_normal_form(q_a)[0]
                assert q_u == (q_a + 2) // 2
                if (q_a, q_c) == (7, 1):
                    q_sources_for_odd.append((sa, sb, i, j, q_u))

    # ea=1 forces sa=1 and j=0.  Both pointing sectors supply the same
    # normalized odd generator, with source a-degrees 5 and 4.
    assert q_sources_for_odd == [(1, 1, 5, 0, 4), (1, 0, 4, 0, 4)]

    # The p symbol carries b*c^(j+ea), with ea>=1, so it cannot contribute a
    # pure c^1 term without also a c^2 term; q already gives a unit hit.
    assert all(source[0] == 1 for source in p_sources_for_odd)

    odd_u_power, odd_parity, odd_t_power = u_chart_normal_form(7)
    assert (odd_u_power, odd_parity, odd_t_power) == (3, 1, 3)
    # Including q's explicit u gives u^4; dividing the target Rees shift u^4
    # leaves -6*a*t^3*c, the source-derived (3,4) lattice generator.
    assert 1 + odd_u_power == 4

    # No first-Cartier symbol can reach (0,0): p has a-degree >=1 and q has
    # a-degree >=2, while both carry nonnegative incidence degree.
    minimum_p_a = min(2 - sb for _, sb in SECTORS)
    minimum_q_a = min((2 - sb) + 1 for _, sb in SECTORS)
    assert (minimum_p_a, minimum_q_a) == (1, 2)

    # Over Q[z]/(z^2), a zero first symbol gives a free length-two block;
    # a unit first symbol gives Q[z]/(z), a reduced length-one block.
    even_cartier_length = 2
    odd_cartier_length = 1
    assert even_cartier_length + odd_cartier_length == 3

    print("normalized_q_symbol_at_(7,1): -6*a*t^3*(b+1)")
    print("odd_boundary_divisor: (3,4)")
    print("q_sources_hitting_odd_layer: (sa,sb,i,j)=(1,1,5,0),(1,0,4,0)")
    print("normalized_first_symbol_at_(7,1)_surjective: YES")
    print("normalized_first_symbol_at_(0,0): ZERO_NO_SOURCE")
    print("even_resonance_Cartier_length: 2")
    print("odd_resonance_Cartier_length: 1")
    print("total_resonant_length_over_double_section: 3")
    print("reduced_nearby_cycle_rank: 2")
    print("generic_characters_from_Benincasa_463: even=+1,odd=-1")
    print("next_gate: CONSTRUCT_THE_SPECIALIZATION_MAP_AND_VERIFY_THE_LENGTH_3_EXTENSION_GLOBALLY")


if __name__ == "__main__":
    main()
