#!/usr/bin/env python3
"""Aggregate the global two-soft polynomial-module selection tests."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
INPUTS = [
    RESULTS / "global_two_soft_polynomial_module_degree4.json",
    RESULTS / "global_two_soft_polynomial_module_degree6.json",
    RESULTS / "global_two_soft_polynomial_module_degree8.json",
    RESULTS / "global_two_soft_polynomial_module_degree8_replication.json",
]
OUTPUT = RESULTS / "global_two_soft_selection_closure.json"


packets = [json.loads(path.read_text(encoding="utf-8")) for path in INPUTS]
checks = {
    "degrees_4_6_8": {packet["numerator_degree"] for packet in packets} == {4, 6, 8},
    "degree8_two_primes": len({
        packet["prime"] for packet in packets if packet["numerator_degree"] == 8
    }) == 2,
    "common_denominator": all(packet["denominator"] == "v*(v-2)" for packet in packets),
    "u_zero_v_derivative": all(
        packet["u"] == 0 and packet["derivative_axis"] == "v" for packet in packets
    ),
    "held_out_identities": all(packet["held_out_polynomial_identity"] for packet in packets),
    "all_consistent": all(packet["consistent"] for packet in packets),
    "target_never_pivot": all(not packet["target_is_pivot"] for packet in packets),
    "target_never_fixed": all(not packet["target_fixed"] for packet in packets),
    "degree8_rank_replication": len({
        packet["rank"] for packet in packets if packet["numerator_degree"] == 8
    }) == 1,
}

packet = {
    "schema": "marici.benincasa.global_two_soft_selection_closure.v1",
    "denominator": "v*(v-2)",
    "target": "constant numerator of (B_v)_e6,q0",
    "candidate": "1/4",
    "runs": [
        {
            "prime": item["prime"],
            "degree": item["numerator_degree"],
            "equations": item["equations"],
            "variables": item["variables"],
            "rank": item["rank"],
            "consistent": item["consistent"],
            "target_is_pivot": item["target_is_pivot"],
        }
        for item in packets
    ],
    "checks": checks,
    "verdict": (
        "The global no-infinity polynomial module does not select the candidate "
        "e6 logarithmic amplitude: its constant numerator remains a free variable."
    ),
    "interpretation": (
        "The class, support, primitive residue vector, and C2-matched candidate "
        "are canonical data, but the rank-twelve source reduction admits the zero "
        "class and arbitrary scalar multiples at the tested global module bounds."
    ),
    "scope": (
        "Replicated exact finite-field polynomial-module result through numerator "
        "degree eight; no characteristic-zero primitive witness was reconstructed."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

OUTPUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
