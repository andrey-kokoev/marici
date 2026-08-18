"""Audit whether deletion-rank differences define an actual residue cokernel."""

from fractions import Fraction


def wedge(left, right):
    """Exterior product of one-forms in the ordered basis dc,da,db."""
    return (
        left[0] * right[1] - left[1] * right[0],
        left[0] * right[2] - left[2] * right[0],
        left[1] * right[2] - left[2] * right[1],
    )


def main():
    # q_g1=c+b+X1, so dlog(q_g1)=q_g1^{-1}(dc+db).
    dlog_qg1 = (Fraction(1, 2), Fraction(0), Fraction(1, 2))
    connection_jump = tuple(17 * value for value in dlog_qg1)
    assert connection_jump != (0, 0, 0)

    # The identity intertwines the twisted differentials only if the added
    # one-form wedges to zero with every test form.
    test_form = (Fraction(0), Fraction(1), Fraction(0))
    commutator = wedge(connection_jump, test_form)
    assert commutator != (0, 0, 0)

    # The auxiliary inverse variable also presents two distinct localizations.
    saturation_empty = "u*K-1"
    saturation_single = "u*K*q_g1-1"
    assert saturation_empty != saturation_single

    mobius_increment = 12 - 7
    assert mobius_increment == 5

    print("empty_twist: d+5*dlog(K)")
    print("single_twist: d+5*dlog(K)+17*dlog(q_g1)")
    print("identity_chain_map: FAIL_NONZERO_CONNECTION_JUMP")
    print("shared_auxiliary_localization: FAIL_DIFFERENT_SATURATION_EQUATIONS")
    print("rank_difference_12_minus_7: 5")
    print("constructed_rank_five_cokernel: NO")
    print("required_next_object: CHAIN_LEVEL_CARTIER_LOCALIZATION_MAP")


if __name__ == "__main__":
    main()
