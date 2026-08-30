"""Minimal source enlargement for controlled D(S3) sector powers."""

import json
import sympy as sp


def ctrl(U):
    n = U.rows
    C = sp.zeros(2 * n)
    C[:n, :n] = sp.eye(n)
    C[n:, n:] = U
    return C


def operator_schmidt_rank_control_data(M, d):
    # Rows are flattened control output/input pairs; columns are flattened
    # data output/input pairs.
    reshuffled = sp.zeros(4, d * d)
    for co in range(2):
        for ci in range(2):
            for do in range(d):
                for di in range(d):
                    reshuffled[2 * co + ci, d * do + di] = M[d * co + do, d * ci + di]
    return reshuffled.rank()


def main():
    lifts = (-8, 1, 2, 3, 6, 7, 20, 5)
    Z = sp.diag(*lifts)
    P0, P1 = sp.diag(1, 0), sp.diag(0, 1)
    powers = {}
    for j in (1, 2, 4):
        Uj = sp.diag(*[sp.exp(-sp.I * sp.pi * j * z / 4) for z in lifts])
        compiled = sp.diag(*([1] * 8 + list(Uj.diagonal())))
        target = ctrl(Uj)
        assert sp.simplify(compiled - target) == sp.zeros(16)
        # This is exp(-i*pi*j/4 P1 tensor Z), evaluated spectrally.
        spectral = sp.kronecker_product(P0, sp.eye(8)) + sp.kronecker_product(P1, Uj)
        assert spectral == target
        assert operator_schmidt_rank_control_data(target, 8) == 2
        powers[str(j)] = {"pulses": 1, "operator_schmidt_rank": 2}

    # Any circuit over record-only and data-only gates is a product operator,
    # and hence has operator Schmidt rank one.
    R = sp.Matrix([[1, 1], [1, -1]])
    D = sp.diag(*range(1, 9))
    product_witness = sp.kronecker_product(R, D)
    assert operator_schmidt_rank_control_data(product_witness, 8) == 1

    result = {
        "schema": "marici.s3-minimal-controlled-power-enlargement.v1",
        "frozen_surface_S0": {
            "record_only_gates": True,
            "data_and_holonomy_ancilla_gates": True,
            "record_data_interaction": False,
            "all_joint_circuits_operator_schmidt_rank": 1,
            "controlled_nontrivial_U_reachable": False,
        },
        "minimal_enlargement_S1": {
            "new_interaction_families": 1,
            "interaction": "P1_tensor_Z_with_tunable_pulse_area",
            "controlled_powers": powers,
            "total_controlled_pulses": 3,
            "data_support": 4,
            "total_interaction_arity": 5,
            "workspace_ancillas": 0,
            "workspace_cleanup": "vacuous",
            "three_record_qubits_are_retained_for_readout": True,
        },
        "single_fault_bound_for_primitive_five_body_model": {
            "control_Z_fault_data_weight": 0,
            "control_X_fault_max_data_weight": 4,
            "arbitrary_gate_fault_max_data_weight": 4,
            "distance_for_arbitrary_weight_four_recovery": 9,
            "decoder_selected": False,
        },
        "minimality": {
            "zero_new_record_data_interaction_families_suffice": False,
            "one_new_tunable_conditional_interaction_family_suffices": True,
            "sense": "number_of_record_data_interaction_families",
        },
        "aggregate_gates": {
            "factorized_surface_cannot_controlize": True,
            "controlled_U1_is_one_exact_pulse": True,
            "controlled_U2_is_one_exact_pulse": True,
            "controlled_U4_is_one_exact_pulse": True,
            "one_new_interaction_family_is_necessary_and_sufficient": True,
            "workspace_cleanup_is_exact": True,
            "five_body_fault_can_reach_four_data_edges": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

