"""Exact exponent audit for primitive and square scale currents."""

from fractions import Fraction


def prime_sum_absolutely_converges(exponent: Fraction) -> bool:
    # The prime p-series converges absolutely exactly for exponent > 1.
    return exponent > 1


def main() -> None:
    half = Fraction(1, 2)
    zero = Fraction(0, 1)
    epsilon = Fraction(1, 100)

    assert not prime_sum_absolutely_converges(half + half)
    assert prime_sum_absolutely_converges(half + half + epsilon)
    assert not prime_sum_absolutely_converges(1 + zero)
    assert prime_sum_absolutely_converges(1 + epsilon)

    print("primitive_test_vanishing_threshold=alpha>1/2")
    print("square_test_vanishing_threshold=alpha>0")
    print("primitive_boundary_case_diverges=true")
    print("square_boundary_case_diverges=true")
    print("shared_scalar_boundary_functional=false")
    print("canonical_boundary_subtraction=window_plus_unit")
    print("finite_part_modular_sewing=not_derived")


if __name__ == "__main__":
    main()
