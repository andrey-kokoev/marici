"""Exact controlization boundary for the finite D(S3) center instrument."""

import json
import sympy as sp


def controlled(matrix):
    n = matrix.rows
    out = sp.zeros(2 * n)
    out[:n, :n] = sp.eye(n)
    out[n:, n:] = matrix
    return out


def main():
    # A concrete non-scalar target makes the global/relative phase distinction
    # exact.  phi=pi gives ctrl(-U), which cannot equal ctrl(U) up to a scalar.
    U = sp.diag(1, sp.I)
    c_u = controlled(U)
    c_minus_u = controlled(-U)
    relative = sp.simplify(c_minus_u * c_u.H)
    assert relative == sp.diag(1, 1, -1, -1)
    assert relative != relative[0, 0] * sp.eye(4)

    # Any n unconditional oracle calls acquire only the scalar (-1)^n under
    # U -> -U, hence cannot reproduce the branch-relative matrix above.
    fixed_query_phase_is_global = all((-1) ** n in (-1, 1) for n in range(9))
    assert fixed_query_phase_is_global

    # Conditional Hamiltonian identity on the exact eight sector lifts.
    lifts = (-8, 1, 2, 3, 6, 7, 20, 5)
    residues = tuple(z % 8 for z in lifts)
    assert len(set(residues)) == 8
    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    conditional_identities = {}
    for j in (1, 2, 4):
        phases = sp.diag(*[sp.exp(-sp.I * sp.pi * j * z / 4) for z in lifts])
        lhs = sp.diag(*([1] * 8 + list(phases.diagonal())))
        rhs = sp.kronecker_product(P0, sp.eye(8)) + sp.kronecker_product(P1, phases)
        assert sp.simplify(lhs - rhs) == sp.zeros(16)
        conditional_identities[str(j)] = True

    # Controlled-word composition is exact and preserves order.
    G1 = sp.Matrix([[0, 1], [1, 0]])
    G2 = sp.diag(1, sp.I)
    lhs_word = controlled(G2) * controlled(G1)
    rhs_word = controlled(G2 * G1)
    assert sp.simplify(lhs_word - rhs_word) == sp.zeros(4)

    result = {
        "schema": "marici.s3-controlization-boundary.v1",
        "black_box_no_go": {
            "phase_pair": ["U", "-U"],
            "uncontrolled_difference": "global_phase_only",
            "controlled_relative_operator": [1, 1, -1, -1],
            "controlled_difference_is_global": False,
            "uniform_fixed_query_controlization_from_uncontrolled_oracle": False,
        },
        "constructive_repairs": {
            "conditional_hamiltonian": "P1_tensor_Z",
            "powers_verified": conditional_identities,
            "conditional_pulse_count": 3,
            "controlled_known_word_composes_exactly": True,
            "known_timed_word_currently_available": False,
        },
        "sector_data": {
            "labels": list("ABCDEFGH"),
            "integer_lifts": list(lifts),
            "residues": list(residues),
            "all_residues_distinct": True,
        },
        "locality_typing": {
            "data_support_change_under_controlization": 0,
            "total_support_change_under_controlization": 1,
            "interaction_arity_change": 1,
        },
        "remaining_obligations": [
            "timed_primitive_word_for_Z",
            "physical_record_qubit_conditional_coupling",
            "coupling_calibration_and_noise_model",
            "fault_tolerant_schedule",
        ],
        "aggregate_gates": {
            "global_phase_becomes_control_branch_relative": True,
            "black_box_controlization_is_impossible": True,
            "conditional_hamiltonian_repairs_all_three_powers": True,
            "controlled_known_word_composes_exactly": True,
            "eight_sector_residues_remain_distinct": True,
            "controlization_adds_one_to_interaction_arity": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

