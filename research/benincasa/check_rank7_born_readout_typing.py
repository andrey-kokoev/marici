#!/usr/bin/env python3
"""Audit that the rank-seven score packet is already post-Born readout."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).parent
source = json.loads((ROOT / "fixed-loop-physical-score-rank.json").read_text(encoding="utf-8"))

checks = {
    "fixed_score_packet_passed": source["status"] == "passed",
    "observer_is_density_based": source["density"] == "1/(q_g1*q_g2*q_g3*q_g23)",
    "observer_is_normalized_score_tower": source["generic_response_rank"] == 10,
    "source_interaction_quotient_is_rank7": source["source_interaction_quotient_rank"] == 7,
    "post_born_observer_is_faithful_on_rank7": (
        source["regulated_physical_score_kernel_on_source_quotient"] == 0
    ),
}

packet = {
    "schema": "marici.benincasa.rank7-born-readout-typing.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "source_packet": "fixed-loop-physical-score-rank.json",
    "typed_factorization": (
        "wavefunction -> modulus-square/positive density -> normalized density-score tower "
        "-> rank-seven interaction quotient"
    ),
    "phase_kernel": (
        "Global state-line phase is killed at modulus-square gluing, before the fixed-loop "
        "score observer is formed (Ledger 2110)."
    ),
    "rank_result": 7,
    "conclusion": (
        "The rank-seven packet is already a post-Born density-response object. Applying a "
        "second phase-forgetting quotient is mistyped and cannot be used to lower its rank."
    ),
    "next_falsifier": (
        "Test the source-derived physical momentum-identification map and the accessibility "
        "of the ten labelled score channels; these are downstream maps not already included "
        "in modulus-square gluing."
    ),
    "new_carrier_support": False,
}

output = ROOT / "rank7-born-readout-typing.json"
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
