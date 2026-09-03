import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1127,1128,1129)
wp1127=json.loads((ROOT/"results"/"wp1127_production_constructor_closure_audit.json").read_text())
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1129=json.loads((ROOT/"results"/"wp1129_event_production_packet_corpus_search.json").read_text())
assert wp1127["classification"].startswith("closure audit")
assert wp1128["classification"].startswith("conditional gate: executable admission")
assert wp1129["classification"].startswith("negative corpus gate")
# The required boundary-character interface is now typed and auditable, but
# neither the tested source constructors nor the existing corpus admit a
# packet carrying it.
closure_audit=True
admission_contract=True
corpus_scan=True
current_source_passes=wp1127["current_source_passes"]
actual_packets=wp1128["actual_packets_supplied"]
admissible_corpus_packets=wp1129["admissible_packets"]
assert closure_audit and admission_contract and corpus_scan
assert current_source_passes==0 and actual_packets==0 and admissible_corpus_packets==0
sourced_character=False
six_channels=False
phase_observable=False
production_kernel=False
event_map=False
physical16_descent=False
assert not (sourced_character or six_channels or phase_observable or production_kernel or event_map or physical16_descent)
result={
    "schema":"marici.flavor.wp1253.v1",
    "status":"PASS",
    "question":"Can the current source or corpus derive a sourced boundary character?",
    "dpc":{
        "conjecture":"The tested constructors or existing corpus may contain a sourced boundary character carrying six channels, phases, production kernel, and readout map.",
        "rivals":["current-source production closure","typed packet admission","existing-corpus packet"],
        "risky_consequences":["the closure audit tests nine gates","the admission contract has five required objects and five hostile classes","the corpus scan covers 67 candidates and one typed JSON candidate"],
        "falsification_attempt":"zero current-source constructors pass, zero actual packets are supplied, and zero admissible corpus packets exist; the only typed candidate is the admission contract itself.",
        "residual":"obtain an external or newly derived UV packet carrying the four-part event-production interface and submit it to the admission contract",
        "disposition":"accept the admission contract conditionally; reject current source and existing corpus as boundary-character authorities"
    },
    "closure_audit":{
        "tested_gates":wp1127["tested_gates"],
        "constructor_candidates":wp1127["constructor_candidates"],
        "current_source_passes":current_source_passes,
        "current_source_capabilities":wp1127["current_source_capabilities"],
        "minimal_new_capability":wp1127["minimal_new_capability"]
    },
    "admission_contract":{
        "contract":wp1128["admission_contract"],
        "required_object_count":wp1128["required_object_count"],
        "hostile_rejection_count":wp1128["hostile_rejection_count"],
        "mock_without_provenance_admitted":wp1128["mock_without_provenance_admitted"]
    },
    "corpus_search":{
        "candidate_files_scanned":wp1129["candidate_files_scanned"],
        "typed_packet_candidates":wp1129["typed_packet_candidates"],
        "admission_contracts":wp1129["admission_contracts"],
        "admissible_packets":admissible_corpus_packets
    },
    "closure_audit_complete":closure_audit,
    "admission_contract_constructed":admission_contract,
    "corpus_scan_complete":corpus_scan,
    "current_source_passes":current_source_passes,
    "actual_packets_supplied":actual_packets,
    "admissible_corpus_packets":admissible_corpus_packets,
    "sourced_character":sourced_character,
    "six_channels":six_channels,
    "phase_observable":phase_observable,
    "production_kernel":production_kernel,
    "event_map":event_map,
    "physical16_descent":physical16_descent,
    "classification":"conditional sourced-character gate: admission contract exact, current source and corpus empty",
    "remaining_gate":"obtain an external or newly derived UV event-production packet and submit it to the WP1128 admission contract",
    "hostile_gate":"do not call closure audits, admission contracts, corpus mentions, or checker fixtures a sourced boundary character",
    "claim_boundary":"WP1127 through WP1129 specify and test the interface; no physical source packet or Physical16 descent is admitted",
    "disposition":"sourced-boundary-character leaf resolved conditionally; external/new UV packet rival selected"
}
(ROOT/"results"/"wp1253_sourced_boundary_character_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1253 PASS: admission contract exact, current source and corpus empty")
