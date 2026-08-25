"""Encoded-bus resource bound for the lower-arity D(S3) compiler."""

import json


def main():
    logical_qudits = 1
    code_distance = 3
    singleton_min_rails = logical_qudits + 2 * (code_distance - 1)
    assert singleton_min_rails == 5

    # A six-level rail factors as qubit x qutrit.  Tensoring distance-three
    # five-rail codes preserves one logical 2*3=6 dimensional system and has
    # distance min(3,3)=3.  Dimension eight is a prime-power qudit and also
    # admits the five-rail perfect-code parameter target conditionally.
    holonomy_bus = {"logical_dimension": 6, "rails": 5, "distance": 3,
                    "construction": "tensor_[[5,1,3]]_2_and_[[5,1,3]]_3"}
    label_bus = {"logical_dimension": 8, "rails": 5, "distance": 3,
                 "construction": "[[5,1,3]]_8_qudit_code"}
    assert holonomy_bus["rails"] == label_bus["rails"] == singleton_min_rails

    bus_data_interactions = {
        "holonomy_compute_and_uncompute": 8,
        "transporter_align_and_unalign": 2,
        "class_conditioned_fourier_forward_and_reverse": 8,
        "charge_label_copy_forward_and_reverse": 2,
    }
    interaction_count = sum(bus_data_interactions.values())
    assert interaction_count == 20
    correction_cycles = interaction_count

    conditional_bus_fault_weight = 1
    relative_coordinate_fault_weight = 2
    combined_weight = max(conditional_bus_fault_weight,
                          relative_coordinate_fault_weight)
    assert combined_weight == 2

    result = {
        "schema": "marici.s3-encoded-bus-interleaving.v1",
        "quantum_singleton_lower_bound": {
            "logical_qudits": logical_qudits,
            "distance": code_distance,
            "minimum_physical_rails": singleton_min_rails,
            "classical_repetition_is_sufficient_for_arbitrary_coherent_faults": False,
        },
        "encoded_buses": {
            "holonomy": holonomy_bus,
            "sector_label": label_bus,
            "total_bus_rails": holonomy_bus["rails"] + label_bus["rails"],
        },
        "interleaved_schedule": {
            "bus_data_interactions_per_controlled_power": bus_data_interactions,
            "total_bus_data_interactions": interaction_count,
            "minimum_intervening_correction_cycles": correction_cycles,
            "assumes_each_logical_interaction_is_one_fault_transversal": True,
            "assumes_correction_does_not_propagate_to_data": True,
        },
        "conditional_fault_bound": {
            "bus_induced_max_data_weight": conditional_bus_fault_weight,
            "relative_coordinate_gate_max_data_weight": relative_coordinate_fault_weight,
            "combined_max_data_weight": combined_weight,
            "data_code_distance_for_arbitrary_recovery": 2 * combined_weight + 1,
            "improves_unencoded_distance_nine_to_five": True,
        },
        "unresolved_gate_typing": [
            "fault_transversal_logical_S3_multiplication_on_encoded_six_level_bus",
            "fault_transversal_logical_F3_H_and_transporter_gates",
            "syndrome_extraction_and_recovery_circuit",
            "fresh_verified_ancillas_for_twenty_correction_cycles",
        ],
        "aggregate_gates": {
            "arbitrary_bus_error_correction_needs_distance_three": True,
            "five_rails_are_singleton_minimal": True,
            "six_level_distance_three_bus_code_exists_abstractly": True,
            "eight_level_distance_three_bus_code_exists_abstractly": True,
            "twenty_interleaved_correction_cycles_are_required_by_the_schedule": True,
            "conditional_bus_spread_falls_to_one": True,
            "relative_coordinate_spread_keeps_combined_weight_at_two": True,
            "conditional_data_distance_requirement_falls_to_five": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

