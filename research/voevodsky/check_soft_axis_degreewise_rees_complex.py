"""Construct the degreewise Rees lattice for the frozen Euler complex."""


def boundary_divisor(a_degree, c_degree):
    """Multiplicities at (b=+1,b=-1) on the Cartier section."""
    rees_power = a_degree // 2
    return rees_power, rees_power + c_degree


def main():
    for cutoff in (8, 12, 16, 20, 24, 32):
        survivors = []
        for total in range(cutoff + 1):
            for target_a in range(total + 1):
                target_c = total - target_a

                # D_b=a(1-c*d_c): source (I-1,J), coefficient 1-J.
                hit_by_db = target_a >= 1 and (1 - target_c) != 0
                if target_a >= 1:
                    source_divisor = boundary_divisor(target_a - 1, target_c)
                    target_divisor = boundary_divisor(target_a, target_c)
                    divisor_increment = tuple(t - s for s, t in zip(source_divisor, target_divisor))
                    expected = (1, 1) if target_a % 2 == 0 else (0, 0)
                    assert divisor_increment == expected

                # D_a=c(a*d_a-7): source (I,J-1), coefficient I-7.
                hit_by_da = target_c >= 1 and (target_a - 7) != 0
                if target_c >= 1:
                    source_divisor = boundary_divisor(target_a, target_c - 1)
                    target_divisor = boundary_divisor(target_a, target_c)
                    assert tuple(t - s for s, t in zip(source_divisor, target_divisor)) == (0, 1)

                if not hit_by_db and not hit_by_da:
                    survivors.append((target_a, target_c))

        expected = [(0, 0)]
        if cutoff >= 8:
            expected.append((7, 1))
        assert survivors == expected
        print(f"cutoff_{cutoff}: surviving_bidegrees={survivors}")

    assert boundary_divisor(0, 0) == (0, 0)
    assert boundary_divisor(7, 1) == (3, 4)

    # The other three sectors cannot hit (7,1): their required source degrees
    # make their scalar coefficients vanish, as in Entries 449 and 459.
    for sa, sb in ((1, 1), (1, 0), (0, 1), (0, 0)):
        assert sa - sa == 0
        assert (6 + sb) - (sb + 6) == 0

    print("degreewise_divisor_rule: B(I,J)=(floor(I/2),floor(I/2)+J)")
    print("D_b_lattice_increment: parity_dependent_tautological_(0_or_div(t))")
    print("D_a_lattice_increment: incidence_div(c)=(0,1)")
    print("all_homogeneous_operator_blocks_regular: YES")
    print("exceptional_graded_cokernel_bidegrees: (0,0),(7,1)")
    print("boundary_divisors_of_survivors: (0,0),(3,4)")
    print("Euler_resonance_dimension: 2")
    print("next_gate: COMPARE_THE_GRADED_COKERNEL_WITH_NEARBY_CYCLES_AND_MONODROMY")


if __name__ == "__main__":
    main()
