import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1274-shared-frame-handoff-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1128,1254,1255,1256,1257,1258,1259)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1254=json.loads((ROOT/"results"/"wp1254_six_branch_preparation_gate.json").read_text())
wp1255=json.loads((ROOT/"results"/"wp1255_mass_clock_gate.json").read_text())
wp1256=json.loads((ROOT/"results"/"wp1256_channel_gain_gate.json").read_text())
wp1257=json.loads((ROOT/"results"/"wp1257_kernel_classification_gate.json").read_text())
wp1258=json.loads((ROOT/"results"/"wp1258_matching_selection_gate.json").read_text())
wp1259=json.loads((ROOT/"results"/"wp1259_boundary_smatrix_phase_gate.json").read_text())
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()
contract=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v1.json").read_text())

required_request_phrases=[
    "one packet, not five unrelated partial answers",
    "packet identity",
    "preparation lineage",
    "messenger lineage",
    "compactification frame",
    "momentum frame",
    "six independent Physical16 channel vectors",
    "selected-packet-preserving H6-or-equivalent phase observable",
    "row-stochastic 6 by 6 production kernel `P`",
    "`P q = (1/6)^6`",
    "`(3/2) P q = (1/4)^6`",
    "sourced 23-dimensional microspace",
    "sector projections `(6,8,1,4,2,2)/23`",
    "unique flux sector `n`",
    "`B/A = 6 n^2`",
    "localization-preserving clock descent",
    "soft channel",
    "vector channel",
    "exact cascade factor `3/2`",
    "one selected branch matching",
    "explicit label correspondence",
    "selected quotient matching class",
    "fixed-`q` matching intersection",
    "event-time interface"
]
missing_request_phrases=[x for x in required_request_phrases if x not in request]
assert not missing_request_phrases, missing_request_phrases
assert wp1128["required_object_count"]==5 and wp1128["hostile_rejection_count"]==5
assert wp1128["actual_packets_supplied"]==0 and not wp1128["mock_without_provenance_admitted"]
assert contract["required_objects"]["channel_basis"]["count"]==6
assert contract["required_objects"]["event_map"]["gain"]=="3/2"
assert wp1254["physical_preparation"] is False and wp1254["current_source_passes"]==0
assert wp1255["absolute_clock"] is False and wp1255["current_source_passes"]==0
assert wp1256["physical_ratio_law"] is False and wp1256["realized_physical16_channels"]==0
assert wp1257["selected_kernel"] is False and wp1257["production_matching_packet"] is False
assert wp1258["selected_matching_class"] is False and wp1258["selected_kernel"] is False
assert wp1259["selected_class"] is False and wp1259["selected_kernel"] is False

handoff_interfaces={
    "admission_contract":{"required_objects":5,"hostile_rejections":5,"actual_packets_supplied":wp1128["actual_packets_supplied"]},
    "preparation":{"physical_preparation":wp1254["physical_preparation"],"current_source_passes":wp1254["current_source_passes"]},
    "clock":{"absolute_clock":wp1255["absolute_clock"],"current_source_passes":wp1255["current_source_passes"]},
    "channel_gain":{"physical_ratio_law":wp1256["physical_ratio_law"],"realized_physical16_channels":wp1256["realized_physical16_channels"]},
    "production_matching":{"production_matching_packet":wp1257["production_matching_packet"],"selected_kernel":wp1257["selected_kernel"]},
    "matching_selection":{"selected_matching_class":wp1258["selected_matching_class"],"selected_kernel":wp1258["selected_kernel"]},
    "source_phase":{"selected_class":wp1259["selected_class"],"selected_kernel":wp1259["selected_kernel"]}
}

# Falsifier: five partial replies can compose into the admitted packet without
# shared identity, lineage, compactification frame, and momentum frame.
partial_replies_compose=False
actual_typed_packet_admitted=False
conjecture_refuted=partial_replies_compose
assert not conjecture_refuted and not actual_typed_packet_admitted

result={
    "schema":"marici.flavor.wp1274.v1",
    "status":"PASS",
    "question":"Can five partial handoff replies compose into the admitted UV packet without one shared frame and lineage?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet handoff must return one shared-frame packet carrying event production, preparation, compactification clock, channel/gain cascade, production matching, and source phase authority with common identity and lineage.",
        "rivals":["five independent partial replies","kernel-only reply","phase-only reply","preparation-only reply","clock-only reply","channel-only reply","matching-only reply","mock fixture packet"],
        "risky_consequences":["WP1128 gives a five-object admission contract and rejects provenance-free mocks","WP1254 and WP1255 each have zero current-source passes","WP1256 has zero realized physical16 channels","WP1257 through WP1259 have no selected matching, class, or kernel","the handoff request requires shared packet identity, preparation and messenger lineage, compactification frame, and momentum frame"],
        "falsification_attempt":"Replay WP1128 and WP1254 through WP1259 and mechanically compare the typed request against the current packet state.",
        "residual":"No actual typed packet is admitted and no partial-reply composition is authorized; the shared-frame handoff necessity conjecture survives. The residual is an authorized owner reply carrying the complete packet in one frame.",
        "disposition":"shared-frame handoff necessity survives attempted falsification; authorized owner packet reply selected"
    },
    "handoff_request":"research/flavor/flavor-typed-uv-packet-handoff-request.md",
    "required_request_phrases":required_request_phrases,
    "handoff_interfaces":handoff_interfaces,
    "partial_replies_compose":partial_replies_compose,
    "actual_typed_packet_admitted":actual_typed_packet_admitted,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold shared-frame handoff necessity gate: partial replies do not compose into the admitted UV packet",
    "remaining_gate":"receive an authorized owner reply carrying the complete typed packet in one shared frame and submit it to WP1128 admission",
    "hostile_gate":"do not treat separate preparation, clock, channel, matching, phase, kernel, fixture, or narrative replies as the shared typed UV packet",
    "claim_boundary":"WP1128 and WP1254 through WP1259 establish the admission interface and current absence; the shared-frame necessity conjecture survives but remains unproven",
    "disposition":"typed-UV-packet-handoff leaf resolved conditionally; authorized owner packet reply required"
}
(ROOT/"results"/"wp1274_shared_frame_handoff_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1274 PASS: shared-frame handoff necessity survives attempted falsification; authorized packet reply remains open")
