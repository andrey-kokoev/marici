"""Type the resolved lower boundary packet as an integral C2-module."""


def main():
    # A C2-equivariant section of augmentation Z[C2] -> Z_triv must send 1
    # to an invariant pair (a,a). Augmentation then equals 2a.
    integral_solutions = [
        a for a in range(-10, 11) if 2 * a == 1
    ]
    assert integral_solutions == []

    # After inverting two, a=1/2 gives the usual character projector.
    rational_section = (1 / 2, 1 / 2)
    assert sum(rational_section) == 1

    # Boundary packet:
    # sheet pair = regular module; E+,E- = trivial; gamma = sign.
    total_rank = 2 + 1 + 1 + 1
    invariant_quotient_rank = 1 + 1 + 1
    sign_submodule_rank = 1 + 1
    assert (total_rank, invariant_quotient_rank, sign_submodule_rank) == (5, 3, 2)

    print("sheet_module: Z[C2]")
    print("sheet_exact_sequence: 0->Z_sign->Z[C2]->Z_triv->0")
    print("integral_C2_equivariant_split: NO")
    print("split_after_inverting_2: YES")
    print("boundary_C2_module: Z[C2]+Z_triv^2+Z_sign")
    print("boundary_extension: 0->Z_sign^2->B->Z_triv^3->0")
    print("nontrivial_extension_support: SHEET_REGULAR_SUMMAND")
    print("extension_order: 2")


if __name__ == "__main__":
    main()
