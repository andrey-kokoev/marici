#!/usr/bin/env python3
"""Validate all four v2 layers and their hostile falsifiers."""

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))
from data_descent_kernel import compile_packet, replay_evidence  # noqa: E402

C = ROOT / "research" / "nima" / "contracts"
OUT = ROOT / "research" / "nima" / "results" / "data_descent_kernel_v2.json"


def codes(r):
    return {x["code"] for x in r["errors"]}


def main():
    derived_packet = json.loads((C / "cosmology-derived-descent.v2.json").read_text())
    capability_packet = json.loads((C / "toric-executable-capability.v2.json").read_text())
    derived = compile_packet(derived_packet)
    capability = compile_packet(capability_packet)
    replay = replay_evidence(derived_packet, ROOT)
    assert derived["valid"] and capability["valid"] and replay["passed"]

    hostile = {}
    p = copy.deepcopy(derived_packet)
    p["base_changes"][0]["derived"] = False
    hostile["ordinary_nonflat_base_change"] = compile_packet(p)
    assert "nonflat_ordinary_base_change" in codes(hostile["ordinary_nonflat_base_change"])

    p = copy.deepcopy(derived_packet)
    p["arrows"][1]["variance"] = "covariant"
    hostile["erased_correspondence_variance"] = compile_packet(p)
    assert "correspondence_variance_mismatch" in codes(hostile["erased_correspondence_variance"])

    p = copy.deepcopy(derived_packet)
    p["evidence_replays"][0]["sha256"] = "0" * 64
    hostile_replay = replay_evidence(p, ROOT)
    assert not hostile_replay["passed"]

    p = copy.deepcopy(capability_packet)
    del p["capability_fibers"][0]["policies"][0]["section"]["1"]
    hostile["partial_policy"] = compile_packet(p)
    assert "incomplete_policy_section" in codes(hostile["partial_policy"])

    p = copy.deepcopy(capability_packet)
    p["capability_transitions"][0]["operation_map"] = {"I": "X", "X": "I"}
    hostile["nonfunctorial_capability_transition"] = compile_packet(p)
    assert "capability_transition_composition_defect" in codes(hostile["nonfunctorial_capability_transition"])

    result = {
        "schema": "marici.data-descent-kernel-v2-result.v1",
        "positive": {"derived_packet": derived, "capability_packet": capability, "evidence_replay": replay},
        "hostile": {k: {"valid": v["valid"], "error_codes": sorted(codes(v))} for k, v in hostile.items()},
        "hostile_evidence_replay_passed": hostile_replay["passed"],
        "all_requested_layers_operational": True,
        "verdict": "Derived base change, correspondence variance, evidence replay, and finite executable capability fibers all have discriminating validation rules.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
