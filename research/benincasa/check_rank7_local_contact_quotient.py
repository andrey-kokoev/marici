#!/usr/bin/env python3
"""Prove that local contact shifts do not intersect the physical score image."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
with (ROOT / "fixed-loop-physical-score-rank.json").open(encoding="utf-8") as stream:
    physical = json.load(stream)

runs = physical["runs"]
intersections = []
for run in runs:
    response_rank = run["response_rank"]
    contact_rank = 1
    augmented_rank = run["rank_with_constant"]
    intersection_rank = response_rank + contact_rank - augmented_rank
    intersections.append(
        {
            "prime": run["prime"],
            "energies": run["energies"],
            "response_rank": response_rank,
            "loop_independent_contact_rank": contact_rank,
            "augmented_rank": augmented_rank,
            "intersection_rank": intersection_rank,
        }
    )

checks = {
    "two_independent_generic_runs": len(runs) >= 2,
    "all_response_ranks_are_ten": all(item["response_rank"] == 10 for item in runs),
    "constant_contact_port_raises_rank": all(
        item["rank_with_constant"] == item["response_rank"] + 1 for item in runs
    ),
    "response_contact_intersection_is_zero": all(
        item["intersection_rank"] == 0 for item in intersections
    ),
    "rank7_source_quotient_was_already_injective": (
        physical["regulated_physical_score_kernel_on_source_quotient"] == 0
    ),
}

packet = {
    "schema": "marici.benincasa.rank7-local-contact-quotient.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "runs": intersections,
    "locality_typing": (
        "At fixed external kinematics, every spacetime-local counterterm is "
        "independent of the loop point. Its fixed-cycle evaluation therefore lies "
        "in the predeclared constant contact port."
    ),
    "intersection": "image(score responses) intersect contact port = 0",
    "rank7_contact_quotient_rank": 7,
    "retracted_candidate": (
        "The cyclic polynomials L1+L2+L3 and D1+D2+D3 depend on loop coordinates "
        "and are not local counterterms. They cannot define scheme quotients."
    ),
    "consequence": (
        "Arbitrary source-authorized local finite counterterms may translate the "
        "contact readout but cannot identify two rank-seven interaction classes."
    ),
    "new_carrier_support": False,
}

output = ROOT / "rank7-local-contact-quotient.json"
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
