#!/usr/bin/env python3
"""Audit whether relation-image containment defines a nullhomotopy."""

import json
from pathlib import Path


HERE = Path(__file__).parent
packet = json.loads(
    (HERE / "rank26-euler-commutator-relation-reduction.json").read_text(
        encoding="utf-8"
    )
)

runs = []
for run in packet["runs"]:
    witness = run["axis_witnesses"][0]
    generator_count = witness["processed_prefix_witness_count"]
    rank = witness["cumulative_span_rank"]
    runs.append({
        "point": run["point"],
        "witness_generator_count": generator_count,
        "witness_rank": rank,
        "kernel_dimension_lower_bound": generator_count - rank,
    })

checks = {
    "all_commutators_vanish_in_relation_cokernel": packet["status"] == "pass",
    "every_witness_map_has_nontrivial_kernel": all(
        run["kernel_dimension_lower_bound"] > 0 for run in runs
    ),
    "kernel_lower_bound_is_stable": len({
        run["kernel_dimension_lower_bound"] for run in runs
    }) == 1,
}

result = {
    "schema": "marici.rank26-nullhomotopy-typing.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "runs": runs,
    "conclusion": (
        "relation-cokernel vanishing is established, but the finite witness "
        f"has a {runs[0]['kernel_dimension_lower_bound']}-dimensional "
        "preimage ambiguity and does not define a "
        "source-labelled nullhomotopy"
    ),
    "checks": checks,
}

output = HERE / "rank26-nullhomotopy-typing.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
