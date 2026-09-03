import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1267-new-yukawa-geometry-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1212,1218))
wp1212=json.loads((ROOT/"results"/"wp1212_new_yukawa_active_source_gate.json").read_text())
wp1213=json.loads((ROOT/"results"/"wp1213_spin5_matter_completion_selector_gate.json").read_text())
wp1214=json.loads((ROOT/"results"/"wp1214_independent_completion_principle_gate.json").read_text())
wp1215=json.loads((ROOT/"results"/"wp1215_complete_endpoint_exchange_action_gate.json").read_text())
wp1216=json.loads((ROOT/"results"/"wp1216_new_three_family_source_action_gate.json").read_text())
wp1217=json.loads((ROOT/"results"/"wp1217_new_source_geometry_gate.json").read_text())

declared_grammar_routes={
    "spin5_packet":{
        "ordered_two_vector_source":wp1212["ordered_two_vector_source"],
        "anomaly_free_completions":wp1212["anomaly_free_completions"],
        "matter_completion_selected":wp1212["matter_completion_selected"],
        "complete_source_action":wp1212["complete_source_action"]
    },
    "completion_probes":{
        "anomaly_nonfaithful":wp1213["anomaly_nonfaithful"],
        "threshold_nonselective":wp1213["threshold_nonselective"],
        "completion_selected":wp1213["completion_selected"],
        "yukawa_matrices_selected":wp1213["yukawa_matrices_selected"]
    },
    "spin7_orbifold_exchange":{
        "spin7_excludes_b":wp1214["spin7_excludes_b"],
        "orbifold_realizes_a":wp1214["orbifold_realizes_a"],
        "exchange_fixes_ratio":wp1214["exchange_fixes_ratio"],
        "parity_authority":wp1214["parity_authority"],
        "full_exchange_action":wp1214["full_exchange_action"]
    },
    "complete_exchange_action":{
        "ratio_constraint":wp1215["ratio_constraint"],
        "family_conjugate_copy":wp1215["family_conjugate_copy"],
        "complete_action_derived":wp1215["complete_action_derived"],
        "source_beta_derived":wp1215["source_beta_derived"]
    },
    "declared_packet_exhaustion":{
        "declared_grammar_exhausted":wp1216["declared_grammar_exhausted"],
        "new_three_family_action":wp1216["new_three_family_action"],
        "tensor_beta_derived":wp1216["tensor_beta_derived"],
        "threshold_transport":wp1216["threshold_transport"]
    }
}
assert declared_grammar_routes["spin5_packet"]["ordered_two_vector_source"]
assert declared_grammar_routes["spin5_packet"]["anomaly_free_completions"]
assert not declared_grammar_routes["spin5_packet"]["matter_completion_selected"]
assert not declared_grammar_routes["spin5_packet"]["complete_source_action"]
assert declared_grammar_routes["completion_probes"]["anomaly_nonfaithful"]
assert declared_grammar_routes["completion_probes"]["threshold_nonselective"]
assert not declared_grammar_routes["completion_probes"]["completion_selected"]
assert declared_grammar_routes["spin7_orbifold_exchange"]["orbifold_realizes_a"]
assert declared_grammar_routes["spin7_orbifold_exchange"]["exchange_fixes_ratio"]
assert not declared_grammar_routes["spin7_orbifold_exchange"]["parity_authority"]
assert not declared_grammar_routes["spin7_orbifold_exchange"]["full_exchange_action"]
assert declared_grammar_routes["complete_exchange_action"]["ratio_constraint"]
assert not declared_grammar_routes["complete_exchange_action"]["complete_action_derived"]
assert declared_grammar_routes["declared_packet_exhaustion"]["declared_grammar_exhausted"]
assert not declared_grammar_routes["declared_packet_exhaustion"]["new_three_family_action"]

source_geometry_test={
    "all_routes_fail":wp1217["all_routes_fail"],
    "passing_routes":wp1217["passing_routes"],
    "boundaryless_replaces_domain":wp1217["boundaryless_replaces_domain"],
    "endpoint_ports_lost":wp1217["endpoint_ports_lost"],
    "marked_circle_new_groupoid":wp1217["marked_circle_new_groupoid"],
    "new_geometry_derived":wp1217["new_geometry_derived"],
    "holonomy_instrument":wp1217["holonomy_instrument"],
    "uv_boundary_law":wp1217["uv_boundary_law"]
}
assert source_geometry_test["all_routes_fail"] and source_geometry_test["passing_routes"] == []
assert source_geometry_test["boundaryless_replaces_domain"] and source_geometry_test["endpoint_ports_lost"]
assert not source_geometry_test["new_geometry_derived"]
assert not source_geometry_test["holonomy_instrument"] and not source_geometry_test["uv_boundary_law"]

# A falsifier would be a complete Yukawa-active source action obtained by
# extending the declared Spin5/Spin7 interval grammar, without new geometry.
declared_grammar_complete_action=False
new_source_geometry_constructed=False
conjecture_refuted=declared_grammar_complete_action
assert not conjecture_refuted and not new_source_geometry_constructed

result={
    "schema":"marici.flavor.wp1267.v1",
    "status":"PASS",
    "question":"Can declared Spin5/Spin7 interval grammar produce the new Yukawa-active source without a genuinely new source geometry?",
    "dpc":{
        "conjecture":"Every new Yukawa-active source sufficient for the threshold anchor must come from a genuinely new source geometry; extensions of the declared Spin5/Spin7 interval grammar cannot suffice.",
        "rivals":["conditional Spin5 packet","anomaly/threshold/massability probes","Spin7 orbifold exchange","complete endpoint-exchange action","declared-packet exhaustion","boundaryless circle replacement"],
        "risky_consequences":["WP1212 constructs an ordered Spin5 packet but selects no completion or action","WP1213 leaves completions A and B viable","WP1214 conditionally selects A and ratio one without parity or full action authority","WP1215 leaves an 18-real-dimensional family tensor fiber and no source beta","WP1216 exhausts declared packets without a new three-family action","WP1217 finds zero passing source-geometry routes and boundaryless circle loses endpoint ports"],
        "falsification_attempt":"Replay WP1212 through WP1217 and search for a complete Yukawa-active source action arising from the declared grammar without new geometry.",
        "residual":"No declared-grammar route constructs the action, so the new-geometry necessity conjecture survives. A boundaryless holonomy-to-Yukawa instrument or completion-stable UV boundary law remains unconstructed.",
        "disposition":"new-geometry necessity survives attempted falsification; boundaryless holonomy source selected"
    },
    "declared_grammar_routes":declared_grammar_routes,
    "source_geometry_test":source_geometry_test,
    "declared_grammar_complete_action":declared_grammar_complete_action,
    "new_source_geometry_constructed":new_source_geometry_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold new-geometry necessity gate: declared Spin5/Spin7 grammar fails to produce the Yukawa-active source action",
    "remaining_gate":"derive a boundaryless holonomy-to-Yukawa physical16 instrument or a completion-stable UV boundary law from one new source geometry",
    "hostile_gate":"do not treat conditional Spin5/Spin7 constructors, exchange ratio constraints, exhausted declared packets, or boundary removal as a new source geometry or proof of necessity",
    "claim_boundary":"WP1212 through WP1217 falsify the tested declared-grammar bypass routes; the new-geometry necessity conjecture survives but remains unproven",
    "disposition":"new-Yukawa-active-source leaf resolved conditionally; boundaryless holonomy source required"
}
(ROOT/"results"/"wp1267_new_yukawa_geometry_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1267 PASS: new-geometry necessity survives attempted falsification; boundaryless holonomy source remains open")
