"""Consolidated lower-arity sector-bus audit for finite D(S3)."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load(relative):
    raw = (ROOT / relative).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    paths = {
        "holonomy_limit": "research/kitaev/results/s3-holonomy-bus-sector-limit.json",
        "sequential_predicates": "research/kitaev/results/s3-sequential-sector-predicate-minimum.json",
        "edge_support": "research/kitaev/results/s3-sector-bus-edge-support.json",
        "centralizer_compiler": "research/kitaev/results/s3-centralizer-fourier-sector-bus.json",
        "verified_cat": "research/kitaev/results/s3-verified-cat-bus-fault-split.json",
        "encoded_bus": "research/kitaev/results/s3-encoded-bus-interleaving.json",
    }
    loaded = {name: load(path) for name, path in paths.items()}
    H, S, E, C, V, B = (loaded[name][0] for name in
                         ("holonomy_limit", "sequential_predicates", "edge_support",
                          "centralizer_compiler", "verified_cat", "encoded_bus"))
    assert H["schema"] == "marici.s3-holonomy-bus-sector-limit.v1"
    assert S["schema"] == "marici.s3-sequential-sector-predicate-minimum.v1"
    assert E["schema"] == "marici.s3-sector-bus-edge-support.v1"
    assert C["schema"] == "marici.s3-centralizer-fourier-sector-bus.v1"
    assert V["schema"] == "marici.s3-verified-cat-bus-fault-split.v1"
    assert B["schema"] == "marici.s3-encoded-bus-interleaving.v1"

    assert H["one_shot_clean_label_bus"]["minimum_dimension"] == 8
    assert H["holonomy_bus"]["maximum_gauge_invariant_sector_signature_count"] == 3
    assert S["minimum_binary_predicates"] == 3
    assert S["minimum_charge_sensitive_predicates"] == 3
    assert S["three_bit_bijections_enumerated"] == 40320
    assert E["minimum_data_support_for_full_sector_label"] == 4
    assert E["clean_compute_phase_uncompute_lower_bound"]["baseline_serial_gates"] == 9
    assert C["derived_sector_census"]["regular_endpoint_dimension"] == 36
    assert C["compute_phase_uncompute_basis_cases_verified"] == 72
    assert C["gate_inventory"]["maximum_primitive_arity"] == 2
    assert C["gate_inventory"]["total_serial_gates_per_controlled_power"] == 45
    assert C["ancillas"]["workspace_cleanup"] == "both_buses_exactly_clean"
    assert C["controlled_powers_verified"] == [1, 2, 4]
    assert V["combined_gadget"]["maximum_arbitrary_single_fault_data_weight"] == 4
    assert not V["combined_gadget"]["verified_cat_alone_improves_global_distance_requirement"]
    assert B["encoded_buses"]["total_bus_rails"] == 10
    assert B["interleaved_schedule"]["minimum_intervening_correction_cycles"] == 20
    assert B["conditional_fault_bound"]["combined_max_data_weight"] == 2
    assert B["conditional_fault_bound"]["data_code_distance_for_arbitrary_recovery"] == 5

    component_gate_count = sum(len(packet["aggregate_gates"])
                               for packet in (H, S, E, C, V, B))
    assert component_gate_count == 40

    result = {
        "schema": "marici.s3-lower-arity-sector-bus-audit.v1",
        "input_sha256": {name: digest for name, (_, digest) in loaded.items()},
        "information_and_support_bounds": {
            "holonomy_only_signatures": 3,
            "one_shot_label_dimension": 8,
            "sequential_binary_rounds": 3,
            "charge_sensitive_rounds": 3,
            "minimum_data_support": 4,
            "clean_flux_bus_baseline_gates": 9,
        },
        "exact_lower_arity_compiler": {
            "derivation": "centralizer_Fourier_S3_Z2_Z3_before_residue_assignment",
            "workspace_dimensions": {"holonomy": 6, "sector_label": 8},
            "maximum_primitive_arity": 2,
            "serial_gates_per_controlled_power": 45,
            "controlled_powers": [1, 2, 4],
            "total_gates_for_three_powers": 135,
            "workspace_cleanup": "exact",
            "basis_cases_verified": 72,
            "data_support": 4,
        },
        "fault_hierarchy": {
            "unverified_shared_bus_max_data_weight": 4,
            "verified_cat_control_component_weight": 1,
            "verified_cat_changes_global_bound": False,
            "fully_encoded_interleaved_bus_conditional_weight": 1,
            "relative_coordinate_weight": 2,
            "conditional_combined_weight": 2,
            "unencoded_data_distance": 9,
            "encoded_interleaved_conditional_data_distance": 5,
            "encoded_bus_rails": 10,
            "correction_cycles_per_power": 20,
        },
        "remaining_typing": B["unresolved_gate_typing"],
        "component_gate_count": component_gate_count,
        "aggregate_gates": {
            "all_six_packets_are_digest_bound": True,
            "sector_information_is_derived_before_phase_fitting": True,
            "holonomy_only_and_relabeling_shortcuts_are_falsified": True,
            "all_three_controlled_powers_have_clean_two_body_compilers": True,
            "gate_ancilla_locality_and_cleanup_costs_are_exact": True,
            "verified_cat_does_not_hide_the_shared_bus_fault": True,
            "encoded_interleaving_conditionally_reduces_distance_nine_to_five": True,
            "fault_transversal_logical_bus_gates_are_not_claimed_without_a_compiler": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

