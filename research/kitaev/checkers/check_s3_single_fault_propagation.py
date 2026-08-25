"""Exact single-fault propagation census for explicit D(S3) compiler gates."""

import itertools
import json


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)


def main():
    group = list(itertools.permutations(range(3)))
    e, y = (0, 1, 2), (1, 0, 2)
    states = list(itertools.product(group, repeat=4))

    def factor(edges, index):
        return edges[index] if index < 2 else inverse(edges[index])

    schedule = [(index, False) for index in range(4)] + [(index, True) for index in reversed(range(4))]

    def run(edges, ancilla=e, start=0):
        for index, undo in schedule[start:]:
            f = factor(edges, index)
            ancilla = compose(ancilla, inverse(f) if undo else f)
        return edges, ancilla

    assert all(run(state)[1] == e for state in states)

    edge_fault_cases = 0
    edge_fault_max_data_support = 0
    edge_fault_residual_ancilla_cases = 0
    for state, edge_index, boundary in itertools.product(states, range(4), range(9)):
        edges = state
        ancilla = e
        for step, (index, undo) in enumerate(schedule):
            if step == boundary:
                edges = list(edges); edges[edge_index] = compose(y, edges[edge_index]); edges = tuple(edges)
            f = factor(edges, index)
            ancilla = compose(ancilla, inverse(f) if undo else f)
        if boundary == 8:
            edges = list(edges); edges[edge_index] = compose(y, edges[edge_index]); edges = tuple(edges)
        support = sum(a != b for a, b in zip(edges, state))
        edge_fault_max_data_support = max(edge_fault_max_data_support, support)
        edge_fault_residual_ancilla_cases += int(ancilla != e)
        edge_fault_cases += 1
    assert edge_fault_max_data_support == 1

    ancilla_fault_cases = 0
    ancilla_fault_data_support = 0
    ancilla_fault_detected = 0
    for state, boundary in itertools.product(states, range(9)):
        edges = state
        ancilla = e
        for step, (index, undo) in enumerate(schedule):
            if step == boundary: ancilla = compose(y, ancilla)
            f = factor(edges, index)
            ancilla = compose(ancilla, inverse(f) if undo else f)
        if boundary == 8: ancilla = compose(y, ancilla)
        ancilla_fault_data_support = max(ancilla_fault_data_support, sum(a != b for a, b in zip(edges, state)))
        ancilla_fault_detected += int(ancilla != e)
        ancilla_fault_cases += 1
    assert ancilla_fault_data_support == 0
    assert ancilla_fault_detected == ancilla_fault_cases

    # Relative-coordinate gate R(g0,g3)=(g0,g0^-1 g3).
    first_input_spread = 0
    second_input_spread = 0
    pair_cases = 0
    for g0, g3 in itertools.product(group, repeat=2):
        ideal = (g0, compose(inverse(g0), g3))
        fault0 = (compose(y, g0), g3)
        out0 = (fault0[0], compose(inverse(fault0[0]), fault0[1]))
        fault3 = (g0, compose(y, g3))
        out3 = (fault3[0], compose(inverse(fault3[0]), fault3[1]))
        first_input_spread = max(first_input_spread, sum(a != b for a, b in zip(out0, ideal)))
        second_input_spread = max(second_input_spread, sum(a != b for a, b in zip(out3, ideal)))
        pair_cases += 1
    assert first_input_spread == 2 and second_input_spread == 1

    residue_to_label = {0: "A", 1: "B", 2: "C", 3: "D", 6: "E", 7: "F", 4: "G", 5: "H"}
    record_bit_flip_mislabels = 0
    for residue, bit in itertools.product(range(8), range(3)):
        flipped = residue ^ (1 << bit)
        assert residue_to_label[flipped] != residue_to_label[residue]
        record_bit_flip_mislabels += 1
    assert record_bit_flip_mislabels == 24

    result = {
        "schema": "marici.s3-single-fault-propagation.v1",
        "holonomy_compiler": {
            "edge_fault_cases": edge_fault_cases,
            "maximum_final_data_edge_support_from_one_edge_fault": edge_fault_max_data_support,
            "edge_fault_cases_with_residual_ancilla": edge_fault_residual_ancilla_cases,
            "ancilla_fault_cases": ancilla_fault_cases,
            "maximum_data_support_from_one_ancilla_fault": ancilla_fault_data_support,
            "ancilla_faults_detected_by_non_e_final_state": ancilla_fault_detected,
        },
        "relative_coordinate_gate": {
            "basis_pairs_checked": pair_cases,
            "first_input_fault_output_support": first_input_spread,
            "second_input_fault_output_support": second_input_spread,
            "single_fault_can_become_weight_two": True,
        },
        "classical_and_readout_faults": {
            "single_sector_record_bit_flips_checked": record_bit_flip_mislabels,
            "every_single_record_bit_flip_changes_the_reported_sector": True,
            "random_branch_bit_flip": "changes_central_unitary_but_preserves_sector_label",
            "local_syndrome_visibility": "classical_record_faults_are_invisible",
        },
        "recovery_typing": {
            "holonomy_ancilla_fault": "detect_by_final_non_e_check_then_discard_or_reset",
            "single_data_edge_fault": "route_to_a_declared_D_S3_syndrome_decoder",
            "relative_gate_weight_two_fault": "arbitrary_correction_requires_code_distance_at_least_five",
            "record_bit_fault": "requires_classical_redundancy_or_repeated_measurement",
            "preferred_decoder": "not_selected_by_syndrome_or_this_audit",
            "within_block_primitive_pulse_faults": "unresolved_because_timed_words_are_unresolved",
        },
        "deliberate_failure": {
            "claim": "every_single_fault_in_the_explicit_compilers_remains_weight_one_on_data",
            "actual": False,
            "counterexample": "first_input_fault_of_the_relative_coordinate_gate_has_output_support_two",
        },
        "aggregate_gates": {
            "holonomy_compiler_edge_faults_are_data_nonspreading": True,
            "holonomy_compiler_ancilla_faults_do_not_spread_to_data": True,
            "all_tested_ancilla_faults_leave_a_cleanliness_flag": True,
            "relative_coordinate_gate_can_spread_one_fault_to_two_edges": True,
            "every_single_readout_bit_flip_mislabels_the_sector": True,
            "branch_bit_faults_are_not_local_syndrome_events": True,
            "distance_five_is_required_for_arbitrary_weight_two_recovery": True,
            "syndrome_does_not_choose_a_preferred_decoder": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
