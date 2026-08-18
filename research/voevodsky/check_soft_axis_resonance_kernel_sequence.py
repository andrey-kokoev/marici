"""Verify the canonical carrier-reduction sequence at the frozen soft fiber."""


def monomial_count(cutoff):
    return (cutoff + 1) * (cutoff + 2) // 2


def quartic_carrier_count(cutoff):
    return sum(cutoff - a_degree + 1 for a_degree in range(4))


def divided_survivors(cutoff):
    survivors = []
    for total in range(cutoff + 1):
        for a_degree in range(total + 1):
            c_degree = total - a_degree
            hit_by_db = a_degree >= 1 and (1 - c_degree) != 0
            hit_by_da = c_degree >= 1 and (a_degree - 7) != 0
            if not hit_by_db and not hit_by_da:
                survivors.append((a_degree, c_degree))
    return survivors


def main():
    for cutoff in (12, 16, 20, 24, 28, 32):
        divided_cutoff = cutoff - 4
        survivors = divided_survivors(divided_cutoff)
        assert survivors == [(0, 0), (7, 1)]

        divided_dimension = monomial_count(divided_cutoff)
        exact_rank = divided_dimension - len(survivors)
        full_cokernel = monomial_count(cutoff) - exact_rank
        carrier = quartic_carrier_count(cutoff)
        relative_kernel = full_cokernel - carrier

        assert carrier == 4 * cutoff - 2
        assert full_cokernel == 4 * cutoff
        assert relative_kernel == 2
        print(
            f"cutoff_{cutoff}: full={full_cokernel},carrier={carrier},"
            f"kernel={relative_kernel}"
        )

    # Restoring the universal a^4 shifts the divided representatives.
    restored = [(a_degree + 4, c_degree) for a_degree, c_degree in divided_survivors(12)]
    assert restored == [(4, 0), (11, 1)]

    print("canonical_map: full_exact_cokernel -> quartic_carrier_quotient")
    print("canonical_kernel_representatives: a^4,a^11*(b+1)")
    print("kernel_dimension: 2")
    print("canonical_projection_full_to_resonance: NONE_DERIVED")
    print("correct_relative_object: FIBER_OF_CARRIER_REDUCTION")
    print("next_gate: LIFT_THE_CARRIER_REDUCTION_SEQUENCE_TO_THE_WEIGHTED_REES_FAMILY")


if __name__ == "__main__":
    main()
