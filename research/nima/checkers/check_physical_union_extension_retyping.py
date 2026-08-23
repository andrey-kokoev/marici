"""Certify withdrawal of the untyped rank-41 localization proposal."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "physical_union_extension_retyping.json"


def main() -> None:
    represented_relations = 5_780
    nonzero_target_remainders = 852
    established_union_rank = 26
    missing_target_terms = 0

    descent_holds = nonzero_target_remainders == 0
    payload = {
        "schema": "marici.physical-union-extension-retyping.v2",
        "status": "superseded",
        "relation_descent_audit": {
            "fully_represented_domain_relations": represented_relations,
            "nonzero_target_remainders": nonzero_target_remainders,
            "missing_target_terms": missing_target_terms,
            "descent_holds": descent_holds,
        },
        "surviving_intrinsic_union_rank": established_union_rank,
        "withdrawn": [
            "rank-15 branch intersection",
            "rank-41 middle object",
            "15x26 off-diagonal block",
            "Q-support gate derived from that block",
        ],
        "subsequent_typed_repair": (
            "the common five-mark localization complex recovers 15<25<26; "
            "its valid extension target is 0->F25->H26->T_top->0"
        ),
        "passed": (
            represented_relations > 0
            and nonzero_target_remainders > 0
            and missing_target_terms == 0
            and established_union_rank == 26
            and not descent_holds
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
