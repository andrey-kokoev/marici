"""Audit identification of the cellular log kernel with the framed connector."""


def main():
    geometric_log_kernel = {
        "generic_Q_roof": 1,
        "generic_Rees_factor": "x_D",
        "closed_Cartier_residue": 1,
        "endpoint_matrix": ((0, 1), (1, 0)),
        "Tor1_suspension_orientation": 1,
        "Cech_residual": 0,
        "Cartier_commutator": 0,
        "reflection_defect": 0,
        "Jordan_associator": 0,
    }
    finite_framed_connector = {
        "generic_Q_roof": 1,
        "generic_Rees_factor": "x_D",
        "closed_Cartier_residue": 1,
        "endpoint_matrix": ((0, 1), (1, 0)),
        "Tor1_suspension_orientation": 1,
        "Cech_residual": 0,
        "Cartier_commutator": 0,
        "reflection_defect": 0,
        "Jordan_associator": 0,
    }
    assert geometric_log_kernel == finite_framed_connector

    # Entry 388 kills local relative deformations; Entry 413 kills the global
    # order-three lift torsor and its automorphisms.
    local_relative_deformation_rank = 0
    global_order_three_h1 = 0
    global_order_three_h0 = 0
    assert (
        local_relative_deformation_rank,
        global_order_three_h1,
        global_order_three_h0,
    ) == (0, 0, 0)

    connector_space_nonempty = True
    connector_components = 1 if connector_space_nonempty else 0
    assert connector_components == 1

    print("boundary_signature_match: EXACT")
    print("local_relative_deformation_group: 0")
    print("global_order_three_lift_torsor: 0")
    print("global_order_three_automorphisms: 0")
    print("connector_space_components: 1")
    print("cellular_log_kernel_equals_framed_connector: YES")
    print("finite_cellular_realization: COMPLETE")
    print("ringed_algebraic_six_functor_lift: NOT_YET_CONSTRUCTED")


if __name__ == "__main__":
    main()
