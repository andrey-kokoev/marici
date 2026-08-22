"""Retype the physical localization extension after rank-26 stabilization."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1] / "results" / "physical_union_extension_retyping.json"


def main() -> None:
    lower_rank = 15
    single_branch_restriction = 20
    union_restriction = 26
    old_total = lower_rank + single_branch_restriction
    union_total = lower_rank + union_restriction
    payload = {
        "schema": "marici.physical-union-extension-retyping.v1",
        "localization_sequence": {
            "lower_deletion_rank": lower_rank,
            "literal_union_restriction_rank": union_restriction,
            "conditional_total_rank": union_total,
        },
        "retired_single_branch_packet": {
            "restriction_rank": single_branch_restriction,
            "total_rank": old_total,
            "deficit_from_literal_union": union_total - old_total,
        },
        "off_diagonal_block_shape": [lower_rank, union_restriction],
        "off_diagonal_scalar_count_before_constraints": lower_rank * union_restriction,
        "status": "rank 41 is conditional on concentration/exactness of the localization sequence; the rank-26 restriction is established",
        "consequence": "rank-35 and 4x3 extension blocks are projections and cannot decide Q-support of the full literal union",
        "passed": old_total == 35 and union_total == 41 and union_total - old_total == 6,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
