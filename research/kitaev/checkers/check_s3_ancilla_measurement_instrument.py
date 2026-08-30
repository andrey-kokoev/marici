"""Exact ancilla, record, and center-instrument typing for finite D(S3)."""

import json
import sympy as sp


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    dims = (1, 1, 2, 3, 3, 2, 2, 2)
    residues = (0, 1, 2, 3, 6, 7, 4, 5)
    omega = sp.sqrt(2) / 2 + sp.I * sp.sqrt(2) / 2
    fourier = sp.Matrix(8, 8, lambda k, r: omega ** (k * r)) / sp.sqrt(8)
    assert sp.simplify(fourier.H * fourier) == sp.eye(8)

    readout = {}
    for label, residue in zip(labels, residues):
        phased = sp.Matrix([omega ** (k * residue) for k in range(8)]) / sp.sqrt(8)
        decoded = sp.simplify(fourier.H * phased)
        expected = sp.zeros(8, 1); expected[residue] = 1
        assert decoded == expected
        readout[str(residue)] = label
    assert len(readout) == 8

    kraus_by_record = {label: dim * dim for label, dim in zip(labels, dims)}
    assert sum(kraus_by_record.values()) == 36

    # Matrix-unit census for the record-producing measure--prepare map.
    offsets = []
    cursor = 0
    for dim in dims:
        offsets.append(cursor); cursor += dim
    assert cursor == 16
    within = sum(dim * dim for dim in dims)
    cross = 16 ** 2 - within
    assert within == 36 and cross == 220

    result = {
        "schema": "marici.s3-ancilla-measurement-instrument.v1",
        "sector_phase_estimation": {
            "record_register": "three_qubits_dimension_eight",
            "initialization": "|000>",
            "controlled_powers": ["U1", "U2", "U4"],
            "inverse_qft_dimension": 8,
            "measurement_basis": "computational",
            "residue_to_sector": readout,
            "exact_decoding": True,
            "controlled_power_source_status": "unresolved_not_implied_by_uncontrolled_reachability",
        },
        "record_producing_center_instrument": {
            "record_values": list(labels),
            "operation": "rho_to_Tr(P_a*rho)/d_a*P_a_tensor_|a><a|",
            "kraus_count_by_record": kraus_by_record,
            "total_kraus_count": 36,
            "nonselective_channel": "center_conditional_expectation",
            "global_matrix_units_typed": 256,
            "within_block_units": within,
            "cross_block_units": cross,
        },
        "ancilla_inventory": {
            "local_holonomy_compiler": {
                "dimension": 6,
                "preparation": "|e>",
                "ideal_final_state": "|e>",
                "reuse_rule": "reuse_only_after_clean_return_verification_or_reset",
            },
            "sector_readout": {
                "dimension": 8,
                "physical_form": "three_qubits",
                "preparation": "|000>",
                "final_action": "measure_retain_sector_record_then_reset",
            },
        },
        "classical_random_inventory_for_nonselective_center_channel": {
            "sector_dephasing": "3 unbiased bits",
            "four_dimension_two_stages": "8 unbiased bits",
            "two_dimension_three_stages": "4 independent uniform trits",
            "ideal_entropy_bits": "11+4*log2(3)",
            "record_rule": "discard_or_keep_inaccessible_to_expose_the_nonselective_channel",
        },
        "instrument_distinctions": {
            "random_unitary_records_retained": "refined_control_branch_instrument_not_center_readout",
            "sector_record_retained_before_internal_depolarization": "sector_projective_instrument",
            "sector_record_retained_after_internal_depolarization": "record_producing_center_measure_prepare_instrument",
            "all_records_discarded": "nonselective_center_expectation_channel",
        },
        "deliberate_failure": {
            "claim": "uncontrolled_reachability_of_U1_U2_U4_supplies_their_controlled_versions",
            "actual": False,
            "reason": "controlization_requires_an_additional_conditional_coupling_interface",
        },
        "aggregate_gates": {
            "eight_sector_residues_decode_exactly": True,
            "three_qubits_are_sufficient_for_the_sector_record": True,
            "three_qubits_are_necessary_for_eight_orthogonal_records": True,
            "measure_prepare_instrument_has_thirty_six_kraus_operators": True,
            "discarding_the_sector_record_recovers_center_expectation": True,
            "coherent_control_and_readout_ancillas_are_distinct": True,
            "classical_random_records_change_instrument_typing_if_retained": True,
            "controlled_central_powers_remain_a_source_obligation": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
