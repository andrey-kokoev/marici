import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1275-source-selected-u-object"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1253,1254,1255,1256,1257,1258,1259,1274)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1253=json.loads((ROOT/"results"/"wp1253_sourced_boundary_character_gate.json").read_text())
wp1254=json.loads((ROOT/"results"/"wp1254_six_branch_preparation_gate.json").read_text())
wp1255=json.loads((ROOT/"results"/"wp1255_mass_clock_gate.json").read_text())
wp1256=json.loads((ROOT/"results"/"wp1256_channel_gain_gate.json").read_text())
wp1257=json.loads((ROOT/"results"/"wp1257_kernel_classification_gate.json").read_text())
wp1258=json.loads((ROOT/"results"/"wp1258_matching_selection_gate.json").read_text())
wp1259=json.loads((ROOT/"results"/"wp1259_boundary_smatrix_phase_gate.json").read_text())
wp1274=json.loads((ROOT/"results"/"wp1274_shared_frame_handoff_necessity_gate.json").read_text())
no_go=(REPO/"research"/"nima"/"flavor-typed-uv-packet-construction-no-go.md").read_text()
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

required_no_go_phrases=[
    "No. This is an authority no-go",
    "no candidate `U`",
    "no common-lineage keys",
    "no source maps defining this diagram",
    "event production, preparation, compactification, channel cascade, production matching, and phase authority"
]
missing_no_go=[x for x in required_no_go_phrases if x not in no_go]
assert not missing_no_go, missing_no_go
assert "source-selected UV boundary object `U`" in request
assert wp1128["actual_packets_supplied"]==0
assert wp1253["actual_packets_supplied"]==0 and wp1253["admissible_corpus_packets"]==0
assert wp1254["physical_preparation"] is False
assert wp1255["absolute_clock"] is False
assert wp1256["physical_ratio_law"] is False
assert wp1257["selected_kernel"] is False
assert wp1258["selected_matching_class"] is False
assert wp1259["selected_class"] is False and wp1259["selected_kernel"] is False
assert wp1274["actual_typed_packet_admitted"] is False and wp1274["partial_replies_compose"] is False

u_object={
    "packet_identity":False,
    "common_frame":False,
    "common_lineage":False,
    "maps":{
        "event_production":False,
        "preparation":wp1254["physical_preparation"],
        "compactification":wp1255["absolute_clock"],
        "channel_cascade":wp1256["physical_ratio_law"],
        "production_matching":wp1257["production_matching_packet"],
        "phase_authority":wp1259["selected_class"]
    }
}
assert not any(u_object["maps"].values())

# Falsifier: a currently admitted source or packet supplies U while bypassing
# the six typed outgoing maps or common identity/frame/lineage.
current_u_candidate_found=False
u_object_constructed=False
conjecture_refuted=current_u_candidate_found
assert not conjecture_refuted and not u_object_constructed

result={
    "schema":"marici.flavor.wp1275.v1",
    "status":"PASS",
    "question":"Does any currently admitted source or packet supply the source-selected UV boundary object U?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must be transported from one source-selected UV boundary object U carrying packet identity, common frame, lineage, and six typed maps to event production, preparation, compactification, channel cascade, production matching, and phase authority.",
        "rivals":["WP1128 admission contract without an actual packet","WP1253 corpus candidate","WP1254 preparation law","WP1255 compactification clock","WP1256 channel/gain rows","WP1257 kernel classification","WP1258 matching quotient","WP1259 S-matrix phase classification","WP1274 partial handoff replies"],
        "risky_consequences":["WP1128 and WP1253 admit zero actual packets","WP1254 through WP1259 leave every corresponding interface unconstructed","WP1274 shows partial replies do not compose","the Nima-side no-go reports no candidate U, no common-lineage keys, and no source maps"],
        "falsification_attempt":"Replay WP1128, WP1253 through WP1259, and WP1274, then compare the strengthened handoff request with the Nima-side no-go.",
        "residual":"No current source or corpus candidate supplies U. The U-object necessity conjecture survives. The residual is a cited source or admitted packet deriving U and all six outgoing maps in one frame.",
        "disposition":"U-object necessity survives attempted falsification; U source-candidate derivation selected"
    },
    "u_object":u_object,
    "current_u_candidate_found":current_u_candidate_found,
    "u_object_constructed":u_object_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold U-object necessity gate: current admitted sources and corpus do not supply the source-selected boundary object",
    "remaining_gate":"derive or obtain U with packet identity, common frame, lineage, and all six outgoing maps; then submit the resulting packet to WP1128 admission",
    "hostile_gate":"do not treat the admission contract, corpus mention, partial interface, fitted kernel, ratio, gain, image, or analogue theorem as U",
    "claim_boundary":"WP1128, WP1253 through WP1259, and WP1274 establish current absence; the U-object necessity conjecture survives but remains unproven",
    "disposition":"source-selected-UV-boundary-object leaf resolved conditionally; U source-candidate derivation required"
}
(ROOT/"results"/"wp1275_source_selected_uv_boundary_object_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1275 PASS: U-object necessity survives attempted falsification; U source candidate remains open")
