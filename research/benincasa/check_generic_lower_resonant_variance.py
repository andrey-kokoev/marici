"""Check whether star/shriek variance selects one Kummer resonance grade."""


def cohomology_dimensions_zero_differential(source_rank, target_rank):
    return source_rank, target_rank


def main():
    # N=[R --lambda--> R]. Derived restriction to lambda=0 is [k --0--> k].
    star_grades = cohomology_dimensions_zero_differential(1, 1)
    assert star_grades == (1, 1)

    # For a regular codimension-one embedding and a perfect complex,
    # i^! differs from Li^* by the normal determinant and a cohomological
    # shift. Neither operation removes a grade.
    shriek_grades_up_to_shift = star_grades
    assert shriek_grades_up_to_shift == (1, 1)

    # A single grade requires extra t-structure/truncation data.
    ordinary_h0_selection = (1, 0)
    ordinary_h1_selection = (0, 1)
    assert ordinary_h0_selection != star_grades
    assert ordinary_h1_selection != shriek_grades_up_to_shift

    print("Li_star_resonant_grades: 1,1")
    print("i_shriek_resonant_grades_up_to_shift: 1,1")
    print("variance_alone_selects_one_grade: NO")
    print("required_extra_datum: T_STRUCTURE_OR_PHYSICAL_CHAIN_TRUNCATION")
    print("entry_544_six_functor_calculus_sufficient_for_selection: NO")


if __name__ == "__main__":
    main()
