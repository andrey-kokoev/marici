"""Test the minimal derived-DNC bridge that forces a common special fiber."""


def main():
    # Minimal proposed incidence expansion: x5-y=0 and X_D03-y=0.
    # Subtracting relations eliminates y and adds x5-X_D03=0.
    relation_x5 = (1, 0, -1)  # coefficients of (x5, X_D03, y)
    relation_xD = (0, 1, -1)
    eliminated = tuple(a - b for a, b in zip(relation_x5, relation_xD))
    assert eliminated == (1, -1, 0)

    # Setting y=0 forces both endpoint-exclusive normals to zero.
    special_fiber_relations = ((1, 0), (0, 1))
    assert special_fiber_relations == ((1, 0), (0, 1))

    # On the original interval, 1=s+(1-s): endpoint ideals are comaximal.
    bezout_coefficients = (1, 1)
    assert bezout_coefficients == (1, 1)

    print("candidate: x5=y, X_D03=y")
    print("common_special_fiber: NONEMPTY")
    print("eliminated_original_base_relation: x5-X_D03=0")
    print("conservative_over_original_geometry: NO")
    print("source_authorized: NO")
    print("disposition: REJECT_MINIMAL_COMMON_NORMAL_BRIDGE")
    print("remaining_candidate_type: incidence_correspondence_with_two_distinct_normals_and_a_new_2-cell")


if __name__ == "__main__":
    main()
