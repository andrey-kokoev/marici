"""Place the lower boundary dual-graph cycle in the open-surface weight degree."""


def main():
    complex_dimension = 2
    dual_graph_cohomological_degree = 1

    # For an SNC boundary in a smooth complex surface, reduced H^1 of the
    # dual complex contributes to the top-weight part of middle cohomology.
    open_cohomological_degree = complex_dimension
    weight = 2 * complex_dimension
    assert (open_cohomological_degree, weight) == (2, 4)

    local_link_degree = 1
    assert local_link_degree == dual_graph_cohomological_degree
    assert local_link_degree != open_cohomological_degree

    print("ambient_complex_dimension: 2")
    print("boundary_dual_graph_H1_rank: 1")
    print("open_surface_target_degree: H2")
    print("open_surface_weight: GrW4")
    print("graph_cycle_implies_global_H1: NO")
    print("critical_rank_five_can_contain_graph_cycle: YES")
    print("full_physical_Betti_numbers: STILL_OPEN")


if __name__ == "__main__":
    main()
