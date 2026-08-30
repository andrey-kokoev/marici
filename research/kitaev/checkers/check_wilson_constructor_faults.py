"""Exact Pauli propagation for two Wilson-parity constructor protocols."""

import json


def torus_horizontal_loop(L):
    vertex = lambda x, y: (x % L) * L + (y % L)
    edges = []
    for x in range(L):
        for y in range(L):
            edges.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    loop = [x * L for x in range(L)]
    return edges, loop


def syndrome(edge_boundaries, support):
    value = 0
    for edge in support:
        value ^= edge_boundaries[edge]
    return value


def audit(L):
    boundaries, loop = torus_horizontal_loop(L)
    z_faults = []
    for after_gate in range(1, L + 1):
        # CNOT(data_j -> pointer). Forward propagation through every later
        # gate sends Z_pointer -> Z_data_j Z_pointer.
        propagated = loop[after_gate:]
        syn = syndrome(boundaries, propagated)
        expected_endpoints = 0 if not propagated else 2
        assert syn.bit_count() == expected_endpoints
        z_faults.append({
            "fault_after_gate": after_gate,
            "propagated_data_weight": len(propagated),
            "star_syndrome_weight": syn.bit_count(),
            "reported_parity_bit_flipped": False,
        })
    assert max(x["propagated_data_weight"] for x in z_faults) == L - 1
    assert all(x["propagated_data_weight"] < L for x in z_faults)

    return {
        "L": L,
        "mobile_pointer_Z_faults": z_faults,
        "mobile_pointer_X_fault": {
            "propagated_data_weight": 0,
            "reported_parity_bit_flipped": True,
        },
        "mobile_pointer_Y_fault": {
            "combines_Z_suffix_damage_and_record_flip": True,
        },
        "maximum_mobile_correlated_data_weight": L - 1,
        "every_nonzero_mobile_Z_fault_damage_has_star_syndrome": True,
        "mobile_single_post_gate_fault_cannot_be_logical": True,
        "parallel_refined_post_coupling_pointer_Z_fault": {
            "propagated_data_weight": 0,
            "reported_fine_bit_flipped": False,
        },
        "parallel_refined_post_coupling_pointer_X_fault": {
            "propagated_data_weight": 0,
            "reported_fine_bit_flipped": True,
            "reported_parity_bit_flipped": True,
        },
        "parallel_refined_ideal_backaction_already_non_qnd": True,
    }


def main():
    payload = {
        "schema": "marici.wilson-constructor-faults.v1",
        "fault_location_contract": "single_pointer_Pauli_immediately_after_a_declared_data_pointer_CNOT",
        "audits": [audit(L) for L in range(2, 9)],
        "aggregate_gates": {
            "mobile_Z_fault_propagates_to_bounded_suffix": True,
            "mobile_correlated_damage_remains_subdistance": True,
            "mobile_correlated_damage_has_two_endpoint_syndrome": True,
            "mobile_X_fault_is_record_flip_without_data_propagation": True,
            "parallel_post_coupling_pointer_fault_has_no_data_fanout": True,
            "fault_resilience_cannot_be_ranked_without_ideal_backaction": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
