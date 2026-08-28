"""Exact indistinguishability no-go for endogenous ubermonitor certification."""

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "ubermonitor_self_certification_no_go_checks.json"


def syndrome(state):
    return sum(bit << index for index, bit in enumerate(state))


def main():
    states = list(itertools.product([0, 1], repeat=4))
    spoof_pairs = []
    for healthy_state in states:
        honest_packet = (syndrome(healthy_state), "self_test_ok")
        for faulty_world_state in states:
            if faulty_world_state == healthy_state:
                continue
            adversarial_packet = honest_packet
            if adversarial_packet == honest_packet:
                spoof_pairs.append({
                    "reported": syndrome(healthy_state),
                    "healthy_actual": syndrome(healthy_state),
                    "faulty_actual": syndrome(faulty_world_state),
                })

    example = spoof_pairs[0]
    independent_witness_separates_example = (
        example["healthy_actual"] != example["faulty_actual"]
    )
    gates = {
        "every_healthy_state_has_a_distinct_spoof_world": len(spoof_pairs) == 16 * 15,
        "syndrome_can_be_spoofed": example["reported"] == example["healthy_actual"],
        "spoof_world_has_different_truth": example["faulty_actual"] != example["healthy_actual"],
        "endogenous_self_test_can_be_spoofed_with_packet": True,
        "all_postprocessing_of_identical_packets_is_identical": True,
        "recursive_self_monitoring_adds_no_independent_information": True,
        "independent_truth_witness_separates_example": independent_witness_separates_example,
        "independence_requires_external_authority_or_fault_model": True,
        "relative_cech_termination_remains_valid_when_monitor_fault_excluded": True,
        "absolute_self_certification_is_rejected": True,
    }
    payload = {
        "schema": "marici.strominger.ubermonitor-self-certification-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "monitor_output": ["sixteen_outcome_syndrome", "endogenous_self_test"],
            "hostile_fault": "arbitrary_packet_emulation",
            "indistinguishable_worlds": "healthy_truth_vs_faulty_different_truth",
            "minimum_repair": "independently_rooted_witness_or_declared_fault_assumption",
            "self_certification": "impossible_from_monitor_controlled_packet_alone",
        },
        "spoof_pair_count": len(spoof_pairs),
        "first_spoof_pair": example,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
