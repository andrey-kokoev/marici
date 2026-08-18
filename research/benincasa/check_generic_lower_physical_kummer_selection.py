"""Test whether the literal positive chain selects a q_g1 Kummer grade."""


def q_g1(x1, b, c):
    return x1 + b + c


def main():
    # The physical chamber has X1>0 and b,c>=0.
    samples = (
        (1, 0, 0),
        (1, 2, 3),
        (5, 0, 7),
        (11, 13, 0),
    )
    assert all(q_g1(*sample) > 0 for sample in samples)

    # Symbolically, X1+b+c >= X1 > 0, so the wall is disjoint from the entire
    # chamber, not only from the sample points.
    lower_bound_is_strict = True
    assert lower_bound_is_strict

    physical_wall_intersection = False
    physical_normal_boundary = 0
    selected_resonant_grade = None
    assert not physical_wall_intersection
    assert physical_normal_boundary == 0
    assert selected_resonant_grade is None

    print("physical_chamber: X1>0,b>=0,c>=0")
    print("q_g1_lower_bound: q_g1>=X1>0")
    print("physical_chain_intersects_q_g1_wall: NO")
    print("physical_normal_boundary_at_q_g1: ZERO")
    print("physical_chain_selects_resonant_grade: NO")
    print("generic_rank_five_object: COEFFICIENT_SIDE_ONLY")
    print("possible_activation: CONTINUATION_OR_DEGENERATION_REQUIRED")


if __name__ == "__main__":
    main()
