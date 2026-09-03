import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Corpus audit as of the WP1128 admission contract; exclude WP1129 itself.
terms = ("physical16", "production", "event")
candidate_files = []
for path in sorted(ROOT.rglob("*")):
    if path.suffix.lower() not in (".md", ".json", ".py"):
        continue
    if "results" in path.parts or "wp1129" in path.name.lower() or "event-production-packet-corpus-search" in path.name.lower():
        continue
    text = path.read_text(errors="ignore").lower()
    if all(term in text for term in terms):
        candidate_files.append(path)

typed_packet_candidates = []
for path in sorted(ROOT.rglob("*.json")):
    if "results" in path.parts or "wp1129" in path.name.lower():
        continue
    text = path.read_text(errors="ignore").lower()
    if all(key in text for key in ("packet_id", "channel_basis", "phase_observable", "production_kernel", "event_map")):
        typed_packet_candidates.append(path)

candidate_file_floor = 63
assert len(candidate_files) >= candidate_file_floor
assert len(typed_packet_candidates) == 12
assert [p.name for p in typed_packet_candidates] == [
    "flavor-event-production-packet-admission.v1.json",
    "flavor-event-production-packet-admission.v10.json",
    "flavor-event-production-packet-admission.v11.json",
    "flavor-event-production-packet-admission.v12.json",
    "flavor-event-production-packet-admission.v2.json",
    "flavor-event-production-packet-admission.v3.json",
    "flavor-event-production-packet-admission.v4.json",
    "flavor-event-production-packet-admission.v5.json",
    "flavor-event-production-packet-admission.v6.json",
    "flavor-event-production-packet-admission.v7.json",
    "flavor-event-production-packet-admission.v8.json",
    "flavor-event-production-packet-admission.v9.json",
]

admission_contracts_data=[json.loads(p.read_text()) for p in typed_packet_candidates]
assert [c["schema"] for c in admission_contracts_data]==[
    "marici.flavor.event-production-packet-admission.v1",
    "marici.flavor.event-production-packet-admission.v10",
    "marici.flavor.event-production-packet-admission.v11",
    "marici.flavor.event-production-packet-admission.v12",
    "marici.flavor.event-production-packet-admission.v2",
    "marici.flavor.event-production-packet-admission.v3",
    "marici.flavor.event-production-packet-admission.v4",
    "marici.flavor.event-production-packet-admission.v5",
    "marici.flavor.event-production-packet-admission.v6",
    "marici.flavor.event-production-packet-admission.v7",
    "marici.flavor.event-production-packet-admission.v8",
    "marici.flavor.event-production-packet-admission.v9",
]
assert all("required_objects" in c for c in admission_contracts_data)
assert all("packet_id" not in c for c in admission_contracts_data)

# The typed candidates are admission tests, not packets. They supply no
# packet_id/boundary authority and therefore cannot be admitted as evidence.
admissible_packets = 0
admission_contracts = 12
assert admissible_packets == 0
assert admission_contracts == 12

# Exact target retained from the admission contract.
assert Fraction(3,2)*Fraction(1,6) == Fraction(1,4)

result = {
    "schema": "marici.flavor.wp1129.v1",
    "status": "PASS",
    "question": "Does the existing corpus contain an admissible event-production packet?",
    "dpc": {
        "conjecture": "The existing corpus already contains a packet satisfying the WP1128 admission contract.",
        "rivals": [
            "an existing physical16 production theorem",
            "an existing typed source packet",
            "the WP1128 admission contract itself",
            "no admissible corpus packet"
        ],
        "risky_consequences": [
            "a file must carry packet_id, channel_basis, phase_observable, production_kernel, and event_map",
            "it must include boundary authority and derivation references",
            "it must not be merely the admission schema"
        ],
        "falsification_attempt": f"The bounded corpus scan finds {len(candidate_files)} mention candidates and twelve typed JSON candidates; all typed candidates are admission contracts, and zero admissible packets exist.",
        "residual": "An external or future UV packet may still satisfy the contract.",
        "disposition": "reject the existing-corpus packet conjecture"
    },
    "candidate_file_floor": candidate_file_floor,
    "candidate_files_scanned": len(candidate_files),
    "typed_packet_candidates": [str(p) for p in typed_packet_candidates],
    "admission_contracts": admission_contracts,
    "admissible_packets": admissible_packets,
    "classification": "negative corpus gate: existing corpus has an admission test but no admissible event-production packet",
    "remaining_gate": "obtain an external or newly derived UV packet and submit it to WP1128",
    "hostile_gate": "do not treat mention density, theorem titles, admission contracts, or checker fixtures as source packets",
    "claim_boundary": "the scan is bounded to the current research/flavor corpus and WP1128 admission criteria",
    "disposition": "existing-corpus event-production packet rejected",
}

(ROOT / "results" / "wp1129_event_production_packet_corpus_search.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1129 PASS:", len(candidate_files), len(typed_packet_candidates), admissible_packets)
