#!/usr/bin/env python3
"""Compile the C3 packet and require hostile mistypings to fail."""

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))
from data_descent_kernel import compile_packet  # noqa: E402

CONTRACT = ROOT / "research" / "nima" / "contracts" / "cosmology-c3-data-descent.v1.json"
OUT = ROOT / "research" / "nima" / "results" / "data_descent_kernel.json"


def codes(result):
    return {e["code"] for e in result["errors"]}


def main():
    packet = json.loads(CONTRACT.read_text())
    positive = compile_packet(packet)
    assert positive["valid"]

    hostile = {}
    p = copy.deepcopy(packet)
    p["arrows"][0]["kind"] = "open_restriction"
    hostile["groupoid_as_open_overlap"] = compile_packet(p)
    assert "missing_open_overlap" in codes(hostile["groupoid_as_open_overlap"])

    p = copy.deepcopy(packet)
    p["local_objects"][1]["rank"] = 25
    hostile["rank_changing_groupoid_arrow"] = compile_packet(p)
    assert "groupoid_fiber_mismatch" in codes(hostile["rank_changing_groupoid_arrow"])

    p = copy.deepcopy(packet)
    p["coherence_cells"][0]["paths"][0] = ["T12_23", "T31_12"]
    hostile["noncomposable_cycle"] = compile_packet(p)
    assert "noncomposable_path" in codes(hostile["noncomposable_cycle"])

    p = copy.deepcopy(packet)
    p["coherence_cells"][0]["identity_defect"] = 1
    hostile["failed_cocycle"] = compile_packet(p)
    assert "nonzero_identity_defect" in codes(hostile["failed_cocycle"])

    result = {
        "schema": "marici.data-descent-kernel-result.v1",
        "positive_compile": positive,
        "hostile_cases": {k: {"valid": v["valid"], "error_codes": sorted(codes(v))}
                          for k, v in hostile.items()},
        "all_hostile_cases_rejected": all(not v["valid"] for v in hostile.values()),
        "verdict": "The C3 cosmology packet compiles as groupoid-equivariant descent; four representative type erasures are rejected.",
    }
    assert result["all_hostile_cases_rejected"]
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
