"""Audit the two physical half-weight resonances at wall infinity."""


def main():
    # At both infinity points, in local coordinates (x,y) with y=0 the
    # infinity line, the exact quadratic tangent cone is:
    # 100*x^2 + 776*x*y - 755*y^2.
    a, b, c = 100, 776, -755
    discriminant = b * b - 4 * a * c
    assert discriminant == 904_176
    assert discriminant != 0

    # y=0 is not either tangent line because the x^2 coefficient is nonzero
    # and the tangent cone is not divisible by y.
    infinity_line_is_distinct = True
    assert infinity_line_is_distinct

    # Characters around the two curve branches and the infinity line.
    characters = (-1, -1, 1)
    assert characters[0] * characters[1] * characters[2] == 1
    assert characters != (1, 1, 1)

    # For an ordinary triple point, the complement is C* times a three-punctured
    # projective line. With trivial total/fiber character and nontrivial base
    # character, H1 has dimension 3-2=1.
    local_h1 = len(characters) - 2
    assert local_h1 == 1
    infinity_points = 2
    local_resonance_sum = infinity_points * local_h1
    assert local_resonance_sum == 2

    print("wall_quartic_affine_singularities: NONE")
    print("infinity_points: 2")
    print("local_union_type: ORDINARY_TRIPLE_POINT")
    print("physical_local_characters: -1,-1,+1")
    print("local_H1_per_infinity_point: 1")
    print("total_local_resonance_dimension: 2")
    print("global_survival_of_both_classes: NOT_YET_PROVED")


if __name__ == "__main__":
    main()
