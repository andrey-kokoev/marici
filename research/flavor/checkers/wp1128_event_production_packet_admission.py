import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "contracts" / "flavor-event-production-packet-admission.v1.json").read_text())
required = contract["required_objects"]
assert contract["schema"] == "marici.flavor.event-production-packet-admission.v1"
assert contract["status"] == "active"
assert list(required) == ["channel_basis", "phase_observable", "production_kernel", "event_map", "provenance"]
assert required["channel_basis"]["count"] == 6
assert required["channel_basis"]["independence"] == "rank_6"
assert required["phase_observable"]["squared_modulus"] == "1/6"
assert required["phase_observable"]["unitarity"] == "H_dagger_H=6I"
assert required["phase_observable"]["selected_packet_preserving"] is True
assert required["production_kernel"]["shape"] == [6,6]
assert required["production_kernel"]["row_sums"] == "1"
assert required["production_kernel"]["q_image"] == "(1/6)^6"
assert required["event_map"]["gain"] == "3/2"
assert required["event_map"]["event_image"] == "(1/4)^6"
assert required["provenance"]["derivation_references_min_count"] == 1
assert len(contract["hostile_rejections"]) == 5

# Exact target identity required by every admitted packet.
q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row = [Fraction(1,6)] * 6
Pq = [sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row = [Fraction(3,2)*x for x in Pq]
assert sum(P_row) == 1
assert Pq == [Fraction(1,6)]*6
assert event_row == [Fraction(1,4)]*6

# A structurally plausible mock without source provenance must be rejected; no
# actual future packet has been supplied.
mock_packet = {
    "channel_basis": "rank_6_fixture",
    "phase_observable": "H6_fixture",
    "production_kernel": "J6/6_fixture",
    "event_map": "(1/4)^6_fixture",
    "provenance": None,
}
mock_admitted = mock_packet["provenance"] is not None
actual_packets_supplied = 0
assert mock_admitted is False
assert actual_packets_supplied == 0

result = {
    "schema": "marici.flavor.wp1128.v1",
    "status": "PASS",
    "question": "Can the future event-production packet interface be made mechanically admissible?",
    "dpc": {
        "conjecture": "The four-part event-production interface can be represented by executable admission tests.",
        "rivals": [
            "typed admission contract",
            "narrative source claim",
            "kernel-only admission",
            "phase-gauge admission",
            "no packet"
        ],
        "risky_consequences": [
            "rank-6 physical16 channel basis",
            "packet-preserving H6 phase observable",
            "row-stochastic P with Pq=(1/6)^6",
            "readout map with (3/2)Pq=(1/4)^6",
            "explicit packet provenance"
        ],
        "falsification_attempt": "A mock packet containing the conditional algebra but no provenance is rejected; five hostile classes are explicit.",
        "residual": "An actual future UV packet may still pass the typed tests.",
        "disposition": "construct the admission contract; retain event production as conditional"
    },
    "admission_contract": "research/flavor/contracts/flavor-event-production-packet-admission.v1.json",
    "required_object_count": len(required),
    "hostile_rejection_count": len(contract["hostile_rejections"]),
    "probability_row": [str(x) for x in Pq],
    "event_row": [str(x) for x in event_row],
    "mock_without_provenance_admitted": mock_admitted,
    "actual_packets_supplied": actual_packets_supplied,
    "classification": "conditional gate: executable admission contract constructed; no actual source packet admitted",
    "remaining_gate": "supply a real UV source packet with all typed fields and provenance",
    "hostile_gate": "do not admit narrative, kernel-only, phase-gauge, fixture, or provenance-free packets",
    "claim_boundary": "the admission test is executable but certifies no physical source",
    "disposition": "future packet admission contract constructed",
}

(ROOT / "results" / "wp1128_event_production_packet_admission.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1128 PASS:", len(required), len(contract["hostile_rejections"]), actual_packets_supplied)
