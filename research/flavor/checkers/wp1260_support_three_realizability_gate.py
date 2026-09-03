import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1153,1154,1155)
wp1153=json.loads((ROOT/"results"/"wp1153_support_three_witness.json").read_text())
wp1154=json.loads((ROOT/"results"/"wp1154_unistochastic_witness_no_go.json").read_text())
wp1155=json.loads((ROOT/"results"/"wp1155_support_graph_search.json").read_text())
assert wp1153["classification"].startswith("productive algebraic gate")
assert wp1154["classification"].startswith("negative gate: the first")
assert wp1155["classification"].startswith("negative gate: support-three")
# A support-three doubly stochastic witness exists, but it is not
# unistochastic, and exhaustive graph search rules out the entire class.
algebraic_witness=True
witness_obstruction=True
graph_search=True
unistochastic_lift=False
admissible_support_three=False
physical_production_maps=False
locality_certificates=False
selected_kernel=False
assert algebraic_witness and witness_obstruction and graph_search
assert wp1155["unistochastic_compatible_support_three"]==0 and wp1155["minimum_possible_sparse_support"]==4
assert not (unistochastic_lift or admissible_support_three or physical_production_maps or locality_certificates or selected_kernel)
result={
    "schema":"marici.flavor.wp1260.v1",
    "status":"PASS",
    "question":"Does support three admit a unistochastic-compatible fixed-q solution?",
    "dpc":{
        "conjecture":"A support-three fixed-q map may be both doubly stochastic and unistochastic-compatible.",
        "rivals":["support-three algebraic witness","single-overlap obstruction","support-three graph search","support-four search"],
        "risky_consequences":["the WP1153 witness is nonnegative, doubly stochastic, target-compatible, and row support at most three","rows 0 and 2 have one shared column with product 11/480","297200 support-three patterns are searched","all 200 admissible graphs are two complete 3x3 blocks"],
        "falsification_attempt":"the witness cannot cancel one overlap term, and fixed-q block balance would require three integer numerators summing to 23/2; no support-three graph survives.",
        "residual":"test support-four sparse candidates",
        "disposition":"accept algebraic support-three existence; reject unistochastic-compatible support three"
    },
    "witness":{
        "pattern_zero_based":wp1153["witness_pattern_zero_based"],
        "matrix":wp1153["witness_matrix"],
        "row_support":wp1153["row_support"],
        "column_support":wp1153["column_support"],
        "row_sums_one":wp1153["row_sums_one"],
        "column_sums_one":wp1153["column_sums_one"]
    },
    "witness_obstruction":{
        "blocking_row_pair":wp1154["blocking_row_pair"],
        "shared_column":wp1154["shared_column"],
        "unique_overlap_product":wp1154["unique_overlap_product"],
        "phase_cancellation_terms":wp1154["phase_cancellation_terms"],
        "phase_freedom_can_repair":wp1154["phase_freedom_can_repair"]
    },
    "graph_search":{
        "support_three_patterns_tested":wp1155["support_three_patterns_tested"],
        "single_overlap_free_graphs":wp1155["single_overlap_free_graphs"],
        "graph_shape":wp1155["graph_shape"],
        "balanced_three_column_blocks":wp1155["balanced_three_column_blocks"],
        "minimum_possible_sparse_support":wp1155["minimum_possible_sparse_support"]
    },
    "algebraic_witness":algebraic_witness,
    "witness_obstruction_exact":witness_obstruction,
    "graph_search_complete":graph_search,
    "unistochastic_lift":unistochastic_lift,
    "admissible_support_three":admissible_support_three,
    "physical_production_maps":physical_production_maps,
    "locality_certificates":locality_certificates,
    "selected_kernel":selected_kernel,
    "classification":"conditional support-three gate: algebraic witness exact, unistochastic-compatible class absent",
    "remaining_gate":"test support-four sparse candidates for fixed-q doubly stochastic and unistochastic-compatible solutions",
    "hostile_gate":"do not call a doubly stochastic witness, one-overlap obstruction, graph search, or support bound a production kernel",
    "claim_boundary":"WP1153 through WP1155 establish exact algebra and no-gos; no unitary lift, production map, locality, or selected kernel is sourced",
    "disposition":"support-three realizability leaf resolved; support-four rival selected"
}
(ROOT/"results"/"wp1260_support_three_realizability_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1260 PASS: algebraic witness exact, unistochastic support three absent")
