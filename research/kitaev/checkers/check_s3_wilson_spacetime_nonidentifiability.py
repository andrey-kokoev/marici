#!/usr/bin/env python3
"""Typed non-identifiability of Wilson fault-tolerant spacetime scheduling."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
CONTRACT = K / "contracts" / "d-s3-resource-relative-capability.v2.json"
COMPRESSION = K / "results" / "s3-wilson-phase-native-compression.json"
OUT = K / "results" / "s3-wilson-spacetime-nonidentifiability.json"


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    compression = json.loads(COMPRESSION.read_text(encoding="utf-8"))
    future = next(item for item in contract["capabilities"]
                  if item["id"] == "complete_compiler_future_magic")
    theory = next(item for item in contract["resource_theories"]
                  if item["id"] == "d_s3_future_magic_envelope")
    magic = next(item for item in theory["resources"] if item["id"] == "verified_magic_source")
    assert theory["admission"] == "proposed"
    assert magic["admitted"] is False
    assert future["status"]["cost"]["depth"]["kind"] == "undefined"
    assert future["status"]["cost"]["magic_ancilla_count"]["kind"] == "undefined"

    # H is the worst controlled target in the phase-native compiler.
    target = compression["controlled"]["H"]
    active = [term for term in target["terms"] if term["T_count_upper_bound"]]
    total_t = sum(term["T_count_upper_bound"] for term in active)
    serial_peak_work = max(term["clean_ancillas"] for term in active)
    parallel_peak_work = sum(term["clean_ancillas"] for term in active)
    ideal_parallel_rounds = max(term["T_count_upper_bound"] for term in active)
    assert total_t == 85 and serial_peak_work == 2 and parallel_peak_work == 5

    # Two completions of the missing factory data, both compatible with the
    # present contract, reverse the schedule preference.
    completions = {
        "single_lane_factory": {
            "factory_T_states_per_round": 1,
            "serial_rounds_lower_bound": total_t,
            "parallel_rounds_lower_bound": total_t,
            "preferred": "serial_reuse",
            "reason": "parallel term execution cannot increase one-lane magic throughput and uses more work blocks",
        },
        "unbounded_parallel_factory": {
            "factory_T_states_per_round": "at_least_85",
            "serial_rounds_in_abstract_module_model": total_t,
            "parallel_rounds_in_abstract_module_model": ideal_parallel_rounds,
            "preferred": "parallel_terms",
            "reason": "parallel term modules reduce abstract injection rounds from 85 to 31 when throughput and layout are free",
        },
    }
    assert completions["single_lane_factory"]["preferred"] != completions["unbounded_parallel_factory"]["preferred"]
    result = {
        "schema": "marici.kitaev.s3-wilson-spacetime-nonidentifiability.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (CONTRACT, COMPRESSION)
        },
        "frozen_contract_readback": {
            "future_magic_envelope": "proposed",
            "verified_magic_source_admitted": False,
            "physical_depth": "undefined",
            "magic_ancilla_count": "undefined",
        },
        "controlled_H_abstract_demand": {
            "T_state_upper_bound": total_t,
            "serial_reuse_peak_clean_work_blocks": serial_peak_work,
            "fully_parallel_peak_clean_work_blocks": parallel_peak_work,
            "idealized_parallel_term_rounds": ideal_parallel_rounds,
        },
        "compatible_completions_with_reversed_preference": completions,
        "minimum_reopening_data": [
            "admitted verified magic source or code-switching surface",
            "factory acceptance probability and output-error contract",
            "T-state throughput and latency",
            "encoded CS, CCZ, and Toffoli exRec latency and fault-spread contracts",
            "clean-work-block preparation, verification, reset, and reuse latency",
            "layout concurrency and routing constraints",
            "objective ordering or weights for depth, footprint, and failure probability",
        ],
        "verdict": "Fault-tolerant spacetime optimization is not identifiable from the frozen data. Exact algebraic T upper bounds do not type physical depth: two resource completions consistent with the current proposed envelope prefer opposite schedules. The correct current values remain undefined, not estimated from T count.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
