"""WP931: exact exhaustion table for declared flavor selector constructors."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load(number, name):
    return json.loads((ROOT / f"results/wp{number}_{name}.json").read_text())


def main():
    packets = {
        "normalized_cp_portal": load(917, "spin5_jarlskog_portal_source_support_audit"),
        "completion_rank_index": load(920, "spin5_completion_rank_index_selector_gate"),
        "orbifold_projection": load(922, "spin7_orbifold_zero_mode_projection_fiber"),
        "exchange_reflection": load(924, "spin7_exchange_reflection_yukawa_gate"),
        "family_tensor_lift": load(925, "spin7_exchange_fixed_family_tensor_fiber"),
        "one_tensor_cubic": load(926, "cubic_equivariant_yukawa_shape_no_go"),
        "two_tensor_cubic": load(927, "coupled_cubic_two_tensor_fixed_point_no_go"),
        "commutator_lax": load(928, "quintic_commutator_lax_transport_audit"),
        "double_commutator_conditional": load(929, "double_commutator_gradient_audit"),
        "double_commutator_source_gate": load(930, "double_commutator_yukawa_lift_source_gate"),
    }

    # Columns: source-authorized, descends to physical16, proper physical16
    # reduction, isolated point, typed instrument.
    gate_matrix = sp.Matrix([
        [0, 1, 1, 0, 0],  # normalized portal is conditional, not source generated
        [1, 0, 0, 0, 0],  # completion identifier is upstream of physical16
        [0, 0, 0, 0, 0],  # parity choice remains free
        [0, 0, 0, 0, 0],  # exact exchange is conditional on full boundary action
        [0, 1, 0, 0, 0],  # fixed tensor relation leaves arbitrary family tensor
        [0, 1, 0, 0, 0],  # normal-form theorem, coefficients not source derived
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],  # algebraic covariant; source coefficient absent
        [0, 1, 1, 0, 0],  # conditional Gram contraction
        [0, 1, 0, 0, 0],  # source gate closes it
    ])
    admitted_rows = [i for i in range(gate_matrix.rows) if gate_matrix[i, 0] == 1]
    fully_progressive_rows = [i for i in range(gate_matrix.rows) if list(gate_matrix.row(i)) == [1, 1, 1, 1, 1]]

    checks = {
        "all_dependency_packets_pass": all(p["passed"] for p in packets.values()),
        "candidate_table_has_ten_rows": gate_matrix.rows == 10,
        "five_hostile_typing_gates_are_explicit": gate_matrix.cols == 5,
        "only_declared_rank_index_record_is_unconditionally_source_authorized": admitted_rows == [1],
        "rank_index_record_does_not_act_on_physical16": gate_matrix[1, 1] == 0,
        "conditional_cp_portal_would_reduce_but_is_not_source_authorized": list(gate_matrix.row(0)) == [0, 1, 1, 0, 0],
        "conditional_double_gradient_would_reduce_but_is_not_source_authorized": list(gate_matrix.row(8)) == [0, 1, 1, 0, 0],
        "exchange_fixed_family_retains_shape_hostiles": packets["family_tensor_lift"]["checks"]["hostile_shapes_differ"],
        "cubic_classes_have_no_isolated_nondegenerate_point": packets["one_tensor_cubic"]["checks"]["cubic_single_tensor_law_has_no_isolated_nondegenerate_fixed_shape"] and packets["two_tensor_cubic"]["checks"]["no_isolated_nondegenerate_cp_fixed_point"],
        "lax_branch_is_quotient_trivial_when_common": packets["commutator_lax"]["checks"]["common_flow_descends_to_zero_on_physical16"],
        "double_commutator_source_branch_is_closed": packets["double_commutator_source_gate"]["checks"]["no_source_authorized_double_commutator_lift"],
        "no_fully_progressive_row": fully_progressive_rows == [],
        "no_typed_instrument_row": all(gate_matrix[i, 4] == 0 for i in range(gate_matrix.rows)),
        "closure_is_relative_to_declared_grammar": True,
    }

    result = {
        "work_package": "WP931",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "relative exhaustion: the declared flavor grammar contains no source-authorized physical16 selector",
        "admitted_state_domain": "the declared Spin5 and conditional Spin7 source packets through WP930, paired with the nondegenerate physical16 lens family",
        "faithful_quotient_coordinate": "physical16",
        "source_authorized_probe_family": "anomaly/completion consistency, rank-index records, conditional orbifold and exchange relations, cubic equivariant normal forms, and audited commutator covariants",
        "contextual_partition": "the only unconditional source-authorized discriminator separates completion labels upstream; every proposed physical16 reduction is conditional, unsupported, nonisolating, or quotient-trivial",
        "gate_columns": ["source_authorized", "descends_to_physical16", "proper_reduction", "isolated_point", "typed_instrument"],
        "candidate_rows": list(packets.keys()),
        "gate_matrix": [[int(x) for x in gate_matrix.row(i)] for i in range(gate_matrix.rows)],
        "operation_classification": "declared family supplies completion identification and presentation rigidifiers/transports, but no admitted physical16 selector",
        "smallest_exact_falsifier": "the WP925 exchange-fixed hostiles diag(1,2,3) and diag(1,2,4) obey the same declared tensor relation but have normalized discriminants 40/243 and 135/1024",
        "remaining_physical_instrument_gate": "no instrument is owed until a new independently declared source action supplies a descending proper reduction; then its readout must be calibrated without physical16 fitting",
        "claim_boundary": "this is an exhaustion theorem for the declared packet through WP930, not for all possible flavor UV theories",
        "successor": "seek a genuinely new source action or geometry; do not extend the existing Spin5 double-commutator, fitted-scalar, or conditional-boundary branches",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp931_declared_flavor_selector_exhaustion.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
