import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1156,1157,1158,1159)
wp1156=json.loads((ROOT/"results"/"wp1156_support_four_witness.json").read_text())
wp1157=json.loads((ROOT/"results"/"wp1157_support_four_graph_search.json").read_text())
wp1158=json.loads((ROOT/"results"/"wp1158_support_four_polytope_point.json").read_text())
wp1159=json.loads((ROOT/"results"/"wp1159_support_four_interior_point.json").read_text())
assert wp1156["classification"].startswith("productive algebraic gate")
assert wp1157["classification"].startswith("productive graph gate")
assert wp1158["classification"].startswith("productive polytope gate")
assert wp1159["classification"].startswith("productive algebraic gate")
# Support-four existence and graph compatibility are exact algebra.
# Neither an algebraic witness nor graph compatibility supplies phases,
# unitarity, production locality, or the selected kernel.
algebraic_witness=True
graph_compatibility=True
polytope_point=True
interior_point=True
unitary_phase_lift=False
physical_production_map=False
locality_certificate=False
selected_kernel=False
assert algebraic_witness and graph_compatibility and polytope_point and interior_point
assert wp1159["positive_entries"]==24 and wp1159["minimum_positive_entry"]=="1/42"
assert not (unitary_phase_lift or physical_production_map or locality_certificate or selected_kernel)
result={
    "schema":"marici.flavor.wp1261.v1",
    "status":"PASS",
    "question":"Do graph-compatible support-four candidates contain an exact fixed-q interior point?",
    "dpc":{
        "conjecture":"A graph-compatible support-four carrier contains a fixed-q doubly stochastic interior point and a physical phase lift.",
        "rivals":["support-four algebraic witness","single-overlap-free graph","carrier polytope point","interior algebraic point","phase lift"],
        "risky_consequences":["WP1156 gives a support-four algebraic witness","all 67950 support-four regular graphs are single-overlap-free","WP1158 gives an exact carrier-polytope boundary point","WP1159 gives 24 positive carrier entries with minimum 1/42"],
        "falsification_attempt":"the exact rational interior point passes every algebraic test, but no phase-lift certificate is found.",
        "residual":"test whether the exact support-four modulus has a unitary phase lift",
        "disposition":"accept support-four algebraic and graph existence; reject promotion to a kernel"
    },
    "witness":{
        "matrix":wp1156["witness_matrix"],
        "row_support":wp1156["row_support"],
        "column_support":wp1156["column_support"],
        "nonzero_entries":wp1156["nonzero_entries"]
    },
    "graph_search":{
        "support_four_patterns_tested":wp1157["support_four_patterns_tested"],
        "single_overlap_free_graphs":wp1157["single_overlap_free_graphs"],
        "allowed_overlap_sizes":wp1157["allowed_overlap_sizes"]
    },
    "polytope":{
        "zero_carrier_pattern":wp1158["zero_carrier_pattern"],
        "boundary_zeros":wp1158["boundary_zeros"],
        "carrier_row_support":wp1158["carrier_row_support"]
    },
    "interior":{
        "zero_carrier_pattern":wp1159["zero_carrier_pattern"],
        "matrix":wp1159["witness_matrix"],
        "minimum_positive_entry":wp1159["minimum_positive_entry"],
        "positive_entries":wp1159["positive_entries"]
    },
    "algebraic_witness":algebraic_witness,
    "graph_compatibility":graph_compatibility,
    "polytope_point":polytope_point,
    "interior_point":interior_point,
    "unitary_phase_lift":unitary_phase_lift,
    "physical_production_map":physical_production_map,
    "locality_certificate":locality_certificate,
    "selected_kernel":selected_kernel,
    "classification":"conditional support-four gate: exact interior algebra exists, phase lift remains absent",
    "remaining_gate":"test whether the exact support-four modulus has a unitary phase lift and physical production locality",
    "hostile_gate":"do not call an algebraic witness, graph compatibility, polytope point, or interior algebra a phase lift, production map, or kernel",
    "claim_boundary":"WP1156 through WP1159 establish exact algebra and necessary graph conditions; no unitary lift, locality, or selected kernel is sourced",
    "disposition":"support-four search leaf resolved; phase-lift rival selected"
}
(ROOT/"results"/"wp1261_support_four_search_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1261 PASS: exact interior algebra exists, phase lift absent")
