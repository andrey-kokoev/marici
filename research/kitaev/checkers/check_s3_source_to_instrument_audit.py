"""Requirement-by-requirement completion audit for the finite D(S3) programme."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUTS = {
    "local_source": "s3-local-source-model.json",
    "flux_compiler": "s3-ancilla-flux-port-compiler.json",
    "gh_compiler": "s3-gh-separator-compiler.json",
    "source_lie": "s3-source-generated-lie-closure.json",
    "within_twirl": "s3-within-block-twirl-protocol.json",
    "dephasing": "s3-eight-branch-dephasing-protocol.json",
    "leakage": "s3-control-leakage-energy.json",
    "errors": "s3-control-error-budget.json",
    "instrument": "s3-ancilla-measurement-instrument.json",
    "faults": "s3-single-fault-propagation.json",
    "readout_algebra": "s3-central-readout-algebra.json",
    "center_channel": "s3-center-conditional-expectation.json",
}


def main():
    data, digests = {}, {}
    for key, name in INPUTS.items():
        raw = (ROOT / "research/kitaev/results" / name).read_bytes()
        data[key] = json.loads(raw)
        digests[key] = hashlib.sha256(raw).hexdigest()

    schemas = {key: value["schema"] for key, value in data.items()}
    assert data["local_source"]["aggregate_gates"]["physical_pulse_availability_remains_a_source_assumption"]
    assert data["flux_compiler"]["ports"]["transposition"]["total_serial_gate_count"] == 9
    assert data["flux_compiler"]["ports"]["three_cycle"]["total_serial_gate_count"] == 9
    assert data["gh_compiler"]["serial_compiler"]["total"] == 13
    assert data["source_lie"]["compiled_source_lie_dimension"] == 34
    assert data["source_lie"]["remaining_central_phase_deficit"] == 2
    assert data["within_twirl"]["flattened_ensemble_size"] == 20736
    assert data["within_twirl"]["primitive_pulse_schedule"]["status"] == "unresolved"
    assert data["dephasing"]["minimum_branch_count"] == 8
    assert data["dephasing"]["ordered_cross_sector_units_checked"] == 56
    assert data["leakage"]["gauge_invariant_flux_excitation"]["maximum_at_theta_pi"]["three_cycle"] == "1"
    assert data["errors"]["branch_weight_error"]["all_nontrivial_mode_magnitudes"] == "8*Abs(eta)/7"
    assert data["instrument"]["sector_phase_estimation"]["controlled_power_source_status"].startswith("unresolved")
    assert data["faults"]["relative_coordinate_gate"]["single_fault_can_become_weight_two"]
    assert data["readout_algebra"]["central_readout_algebra_dimension"] == 8
    assert data["readout_algebra"]["full_block_diagonal_algebra_dimension"] == 36
    assert data["readout_algebra"]["full_hermitian_real_dimension"] == 256
    assert data["readout_algebra"]["invisible_real_operator_dimension"] == 248
    assert data["center_channel"]["center_expectation_image_dimension"] == 8
    assert data["center_channel"]["center_expectation_kernel_dimension"] == 248
    assert data["center_channel"]["kraus_rank"] == 36

    new_keys = ("local_source", "flux_compiler", "gh_compiler", "source_lie", "within_twirl",
                "dephasing", "leakage", "errors", "instrument", "faults")
    aggregate_gate_count = sum(len(data[key]["aggregate_gates"]) for key in new_keys)
    assert aggregate_gate_count == 82
    assert all(all(value is True for value in data[key]["aggregate_gates"].values()) for key in new_keys)

    result = {
        "schema": "marici.s3-source-to-instrument-audit.v1",
        "input_schemas": schemas,
        "input_sha256": digests,
        "new_aggregate_gates_passed": aggregate_gate_count,
        "move_dispositions": {
            "1_source_model": "complete_native_surface_frozen",
            "2_transposition_port": "complete_conditional_nine_gate_compiler",
            "3_three_cycle_port": "complete_conditional_nine_gate_compiler",
            "4_G_H_separator": "complete_conditional_thirteen_gate_compiler",
            "5_source_lie_closure": "complete_dimension_34_not_36",
            "6_within_block_twirl": "exact_target_protocol_primitive_timed_words_unresolved",
            "7_eight_branch_dephasing": "exact_three_bit_target_protocol_primitive_timed_words_unresolved",
            "8_leakage_energy": "complete_fixed_point_formulas",
            "9_control_errors": "complete_for_declared_coherent_and_weight_error_models",
            "10_instrument_typing": "exact_dilation_target_controlled_powers_unresolved",
            "11_single_faults": "bounded_explicit_gate_census_primitive_pulse_faults_unresolved",
            "12_final_verdict": "complete_not_physically_established_on_frozen_source",
        },
        "accessible_algebra_hierarchy": {
            "formal_central_readout_algebra_dimension": 8,
            "compiled_source_lie_dimension": 34,
            "endpoint_block_algebra_dimension": 36,
            "ambient_hermitian_dimension": 256,
            "center_expectation_kernel_dimension": 248,
            "frozen_native_source_full_center_record": "not_certified",
            "extended_controlized_apparatus_full_center_record": "exact_target_dimension_8",
        },
        "physical_verdict": {
            "frozen_native_D_S3_hamiltonian": "insufficient",
            "nonselective_center_expectation_channel": "conditionally_reachable_target_not_yet_timed_microscopic_implementation",
            "record_producing_center_instrument": "not_physically_established_controlled_powers_measurement_reset_and_fault_tolerance_missing",
            "global_impossibility_claim": False,
        },
        "unresolved_typing": [
            "named_finite_timed_words_for_block_Weyl_targets",
            "named_finite_timed_word_for_the_central_Z_generator",
            "physical_controlled_U1_U2_U4_interface",
            "hardware_ancilla_preparation_measurement_and_reset_error_models",
            "fault_tolerant_separator_coordinate_gate_and_declared_decoder",
        ],
        "assumptions": [
            "finite_oriented_square_and_fixed_point_D_S3_model",
            "clean_six_level_ancilla_and_exact_group_multiplication_gate_contract",
            "exact_C3_and_Z8_Fourier_targets",
            "fresh_independent_ideal_random_draws_for_exact_channels",
            "unit_fixed_point_vertex_and_plaquette_penalties",
        ],
        "decisive_falsifiers": [
            "failure_of_any_recorded_compiler_map_or_saved_result_digest",
            "direct_source_Lie_rank_other_than_34",
            "sector_collision_under_the_eight_branch_generator",
            "controlled_power_construction_from_the_frozen_source_without_added_interface",
            "fault_propagation_exceeding_the_bounded_census_or_a_valid_lower_distance_recovery_theorem",
        ],
        "aggregate_gates": {
            "all_twelve_moves_have_explicit_dispositions": True,
            "all_eighty_two_new_aggregate_gates_pass": True,
            "center_algebra_and_channel_dimensions_are_cross_checked": True,
            "native_source_insufficiency_is_preserved": True,
            "conditional_target_reachability_is_not_promoted_to_device_execution": True,
            "readout_channel_and_record_producing_instrument_are_separated": True,
            "fault_tolerance_is_not_claimed": True,
            "global_impossibility_is_not_claimed": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
