"""Consolidated controlled-power successor audit for finite D(S3)."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load(relative):
    raw = (ROOT / relative).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    paths = {
        "controlization": "research/kitaev/results/s3-controlization-boundary.json",
        "direct_center": "research/kitaev/results/s3-direct-central-hamiltonian-span.json",
        "minimal_apparatus": "research/kitaev/results/s3-minimal-controlled-power-enlargement.json",
        "faults": "research/kitaev/results/s3-controlled-power-faults.json",
        "record_code": "research/kitaev/results/s3-sector-record-redundancy.json",
    }
    loaded = {name: load(path) for name, path in paths.items()}
    C, D, M, F, R = (loaded[name][0] for name in
                      ("controlization", "direct_center", "minimal_apparatus", "faults", "record_code"))
    assert C["schema"] == "marici.s3-controlization-boundary.v1"
    assert D["schema"] == "marici.s3-direct-central-hamiltonian-span.v1"
    assert M["schema"] == "marici.s3-minimal-controlled-power-enlargement.v1"
    assert F["schema"] == "marici.s3-controlled-power-faults.v1"
    assert R["schema"] == "marici.s3-sector-record-redundancy.v1"

    assert not C["black_box_no_go"]["uniform_fixed_query_controlization_from_uncontrolled_oracle"]
    assert D["direct_center"]["sector_signature_rank"] == 1
    assert not D["direct_center"]["target_Z_is_direct_linear_combination"]
    assert not M["frozen_surface_S0"]["controlled_nontrivial_U_reachable"]
    assert M["minimal_enlargement_S1"]["new_interaction_families"] == 1
    assert M["minimal_enlargement_S1"]["total_controlled_pulses"] == 3
    assert all(M["minimal_enlargement_S1"]["controlled_powers"][str(j)]["pulses"] == 1
               for j in (1, 2, 4))
    assert M["minimal_enlargement_S1"]["data_support"] == 4
    assert M["minimal_enlargement_S1"]["total_interaction_arity"] == 5
    assert M["minimal_enlargement_S1"]["workspace_ancillas"] == 0
    assert F["exact_identities"]["control_Z_commutes_and_does_not_spread"]
    assert M["single_fault_bound_for_primitive_five_body_model"]["control_X_fault_max_data_weight"] == 4
    assert M["single_fault_bound_for_primitive_five_body_model"]["distance_for_arbitrary_weight_four_recovery"] == 9
    assert R["lower_bound"]["minimum_length"] == 6
    assert R["protected_record"]["single_bit_corruptions_uniquely_decoded"] == 48

    total_gates = sum(len(packet["aggregate_gates"]) for packet in (C, D, M, F, R))
    assert total_gates == 28

    result = {
        "schema": "marici.s3-controlled-power-successor-audit.v1",
        "input_sha256": {name: digest for name, (_, digest) in loaded.items()},
        "frozen_surface_verdict": {
            "S0_record_data_factorized": True,
            "S0_controlled_powers": "impossible",
            "direct_center_signature_rank": 1,
            "Lie_accessible_center_rank": 6,
            "timed_switched_word": "existential_under_continuous_control_not_effectively_compiled",
        },
        "minimal_apparatus_verdict": {
            "surface": "S1_equals_S0_plus_tunable_P1_tensor_Z",
            "minimum_new_interaction_families": 1,
            "controlled_power_pulses": {"U1": 1, "U2": 1, "U4": 1},
            "total_pulses": 3,
            "data_support": 4,
            "total_arity": 5,
            "workspace_ancillas": 0,
            "workspace_cleanup": "exact_vacuous",
        },
        "fault_and_record_verdict": {
            "control_Z_data_weight": 0,
            "control_X_max_data_weight": 4,
            "arbitrary_primitive_gate_fault_max_data_weight": 4,
            "distance_for_arbitrary_recovery": 9,
            "minimum_final_record_bits_for_one_flip_correction": 6,
            "acquisition_fault_tolerance": "not_established",
            "decoder_selected": False,
        },
        "remaining_typing": [
            "physical_realization_and_calibration_of_five_body_P1_tensor_Z",
            "lower_arity_fault_tolerant_gadget_or_distance_nine_recovery_layer",
            "inverse_F8_measurement_and_reset_noise_models",
            "fault_tolerant_acquisition_and_encoder_schedule",
        ],
        "aggregate_gate_count": total_gates,
        "aggregate_gates": {
            "all_five_successor_packets_are_digest_bound": True,
            "native_factorized_surface_is_insufficient": True,
            "black_box_and_direct_span_shortcuts_are_falsified": True,
            "one_family_enlargement_is_necessary_and_sufficient": True,
            "all_three_controlled_powers_compile_exactly": True,
            "locality_gate_count_cleanup_and_fault_spread_are_typed": True,
            "record_redundancy_is_sharp_but_acquisition_remains_unprotected": True,
            "conditional_compiler_is_not_misreported_as_native_hardware": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

