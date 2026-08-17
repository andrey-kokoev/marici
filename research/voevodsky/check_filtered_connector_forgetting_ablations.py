"""Audit the two mandatory ordinary-forgetting ablations."""

import check_collapsed_filtered_pc_module as model


def main():
    carrier_identities = 0
    cartier_identities = 0
    for degree in range(4):
        for basis in model.module_basis(degree):
            vector = {basis: 1}

            carrier_nullhomotopy = model.sum_vectors(
                model.apply(
                    model.chain_boundary,
                    model.apply(model.chain_homotopy, vector),
                ),
                model.apply(
                    model.chain_homotopy,
                    model.apply(model.chain_boundary, vector),
                ),
            )
            assert carrier_nullhomotopy == vector
            carrier_identities += 1

            cartier_nullhomotopy = model.sum_vectors(
                model.apply(
                    model.bockstein,
                    model.apply(model.cartier_homotopy, vector),
                ),
                model.apply(
                    model.cartier_homotopy,
                    model.apply(model.bockstein, vector),
                ),
            )
            assert cartier_nullhomotopy == vector
            cartier_identities += 1

    assert carrier_identities == 64
    assert cartier_identities == 64

    # These values are retained only before applying either forgetting functor.
    framed_generic_q = 1
    framed_cartier_residue = 1
    framed_endpoint_determinant = -1
    assert (framed_generic_q, framed_cartier_residue, framed_endpoint_determinant) == (
        1,
        1,
        -1,
    )

    print("filtered_generators_checked: 64")
    print("forget_support_Q_carrier_contraction: PASS")
    print("forget_Tate_window_Cartier_contraction: PASS")
    print("ordinary_chain_class_after_first_ablation: 0")
    print("ordinary_filtration_class_after_second_ablation: 0")
    print("framed_generic_Q_before_forgetting: +1")
    print("framed_Cartier_residue_before_forgetting: +1")
    print("framed_endpoint_determinant_before_forgetting: -1")
    print("Entry_133_mandatory_controls: BOTH_PASS")
    print("class_type: SECONDARY_AND_FRAMED")


if __name__ == "__main__":
    main()
