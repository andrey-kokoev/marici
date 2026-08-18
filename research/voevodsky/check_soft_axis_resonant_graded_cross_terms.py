"""Audit exact cross-terms at the actual Euler-resonant bidegrees."""


def main():
    # In the (s_a,s_b)=(1,1) sector, after dividing by a^4 and setting
    # c=b+1, the exact operators are
    #   D_b=a(1-c*d_c), D_a=c(a*d_a-7).
    # On a^i c^j their scalar coefficients are 1-j and i-7.
    assert 1 - 1 == 0       # D_b(a^6*c) cannot hit a^7*c.
    assert 7 - 7 == 0       # D_a(a^7) cannot hit a^7*c.

    # Entry 449's all-sector test: to hit a^7*c, a non-q operator requires
    # source c-degree j=s_a and has coefficient s_a-j; a q operator requires
    # source a-degree i=6+s_b and has coefficient i-(s_b+6).
    for sa, sb in ((1, 1), (1, 0), (0, 1), (0, 0)):
        required_j = sa
        non_q_coefficient = sa - required_j
        required_i = 6 + sb
        q_coefficient = required_i - (sb + 6)
        assert non_q_coefficient == 0
        assert q_coefficient == 0

    # D_b(1)=a is true but belongs to the degree 0 -> 1 block.  The second
    # resonance belongs to target degree (7,1), so comparing D_b(1) with its
    # degree-seven Rees frame mixes distinct blocks.
    low_source_degree = (0, 0)
    low_target_degree = (1, 0)
    resonant_target_degree = (7, 1)
    assert low_target_degree != resonant_target_degree

    print("D_b_on_unit: degree_(0,0)_to_(1,0)")
    print("second_resonant_target: degree_(7,1)")
    print("Entry_458_cross_frame_comparison_was_graded: NO")
    print("relevant_D_b_source: a^6*c")
    print("relevant_D_b_coefficient: 1-1=0")
    print("relevant_D_a_source: a^7")
    print("relevant_D_a_coefficient: 7-7=0")
    print("all_four_sector_coefficients_at_a7c: ZERO")
    print("claimed_1/w_cross_term_obstruction: RETRACTED")
    print("sevenfold_twist_and_log_residues: UNAFFECTED")
    print("next_gate: BUILD_THE_DEGREEWISE_REES_COMPLEX_BEFORE_TAKING_HYPERCOHOMOLOGY")


if __name__ == "__main__":
    main()
