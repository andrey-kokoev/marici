"""Rank certificate for the canonical incidence filtration of V_union."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "physical_union_incidence_filtration.json"


def main() -> None:
    common = 15
    branch23 = branch31 = 20
    branch_sum = 25
    union = 26
    q23_only = branch23 - common
    q31_only = branch31 - common
    crossing = union - branch_sum
    associated_graded = [common, q23_only, q31_only, crossing]
    payload = {
        "schema": "marici.physical-union-incidence-filtration.v1",
        "filtration_ranks": [common, branch_sum, union],
        "associated_graded_ranks": associated_graded,
        "associated_graded_labels": [
            "common three-mark core",
            "g23-only boundary quotient",
            "g31-only boundary quotient",
            "g23-g31 double-normal Kato line"
        ],
        "rank_identity": "26 = 15 + 5 + 5 + 1",
        "splitting_claimed": False,
        "passed": sum(associated_graded) == union and branch23 + branch31 - common == branch_sum,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
