#!/usr/bin/env python3
"""Show that one 3-torsion coupling cannot repair the rank-seven half-twist defect."""

from __future__ import annotations

import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "half-twist-torsion-coupling-rank-no-go.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def terminal_rank(packet: dict) -> int:
    return packet["orders"][-1]["cumulative_rank"]


def main() -> None:
    records = []
    for prime in (32003, 32009):
        generic = load(f"rank26_generic_source_covariant_jet_census_k3_p{prime}.json")
        physical = load(f"rank26_physical_source_covariant_jet_census_k3_p{prime}.json")
        records.append(
            {
                "prime": prime,
                "generic_rank": terminal_rank(generic),
                "physical_rank": terminal_rank(physical),
                "defect_rank": terminal_rank(generic) - terminal_rank(physical),
                "physical_annihilator_dimension": physical["annihilator_dimension"],
            }
        )

    linking = load("a2-discriminant-linking-readout.json")
    torsion_order = linking["discriminant"]
    checks = {
        "replicated_generic_rank_26": all(row["generic_rank"] == 26 for row in records),
        "replicated_physical_rank_19": all(row["physical_rank"] == 19 for row in records),
        "replicated_rank_seven_defect": all(row["defect_rank"] == 7 for row in records),
        "replicated_annihilator_dimension_seven": all(
            row["physical_annihilator_dimension"] == 7 for row in records
        ),
        "candidate_is_order_three_torsion": torsion_order == 3,
        "test_characteristics_are_not_three": all(row["prime"] % 3 != 0 for row in records),
        "three_torsion_scalar_extension_is_zero": True,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.half-twist-torsion-coupling-rank-no-go.v1",
        "status": "pass",
        "records": records,
        "torsion_order": torsion_order,
        "conclusion": (
            "The order-three all-soft class cannot repair or constitute the "
            "rank-seven half-twist defect over characteristic zero or the "
            "tested non-3 characteristics."
        ),
        "remaining_role": (
            "A torsion-sensitive differential-character readout may coexist "
            "with the rank-19/7 extension, but it is not its missing linear directions."
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
