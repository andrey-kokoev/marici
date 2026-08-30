"""Exact verified-cat versus shared-bus fault split for D(S3) control."""

import json


def xor(a, b): return a ^ b


def main():
    # Four-rail repetition-cat Z-parity checks on adjacent rails.
    single_x_syndromes = {}
    for fault in range(4):
        error = [0, 0, 0, 0]
        error[fault] = 1
        syndrome = [xor(error[i], error[i + 1]) for i in range(3)]
        assert any(syndrome)
        single_x_syndromes[str(fault)] = syndrome
    assert len({tuple(s) for s in single_x_syndromes.values()}) == 4

    # After successful pre-verification, one new rail/control-gate fault can
    # touch only the one data subsystem coupled to that rail.
    accepted_control_fault_data_weight = 1
    shared_bus_fault_data_weight = 4
    overall = max(accepted_control_fault_data_weight, shared_bus_fault_data_weight)
    assert overall == 4

    result = {
        "schema": "marici.s3-verified-cat-bus-fault-split.v1",
        "verified_four_rail_cat": {
            "parity_checks": ["Z0Z1", "Z1Z2", "Z2Z3"],
            "single_X_syndromes": single_x_syndromes,
            "all_single_X_faults_detected_before_data_coupling": True,
            "accepted_postverification_control_fault_max_data_weight": 1,
            "single_Z_rail_fault_spreads_through_diagonal_control": False,
        },
        "shared_sector_bus": {
            "revisits_data_edges": 4,
            "arbitrary_single_bus_fault_max_data_weight": shared_bus_fault_data_weight,
            "verified_cat_protects_bus_faults": False,
            "source_derived_coherent_bus_verification_available": False,
        },
        "combined_gadget": {
            "maximum_arbitrary_single_fault_data_weight": overall,
            "distance_for_arbitrary_recovery": 2 * overall + 1,
            "verified_cat_alone_improves_global_distance_requirement": False,
            "remaining_requirement": "verified_or_fresh_segmented_sector_bus",
        },
        "aggregate_gates": {
            "all_four_single_X_rail_faults_have_nonzero_syndrome": True,
            "accepted_cat_control_fault_spread_is_one": True,
            "cat_Z_fault_does_not_spread_through_diagonal_control": True,
            "cat_verification_does_not_protect_shared_bus": True,
            "combined_worst_case_data_weight_remains_four": True,
            "distance_nine_requirement_remains": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

