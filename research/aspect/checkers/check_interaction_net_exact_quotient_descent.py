#!/usr/bin/env python3
"""Transfer checker for Benincasa's exact source-reachable quotient packets."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect"
CONTRACT = ASPECT / "contracts" / "interaction-net-exact-quotient-descent.v1.json"
RESULT = ASPECT / "results" / "interaction_net_exact_quotient_descent.json"

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    packets = []
    for locator in contract["source_packets"]:
        packet = json.loads((ROOT / locator).read_text(encoding="utf-8"))
        packets.append({
            "locator": locator,
            "prime": packet["prime"],
            "chart": packet["chart"],
            "k_depth": packet["k_depth"],
            "generated_rank": packet["generated_rank"],
            "quotient_rank": packet["global_quotient_rank"],
            "relation_kernel_rank": packet["global_relation_kernel_rank"],
            "cross_grade_reduction_count": packet["cross_grade_reduction_count"],
            "associated_rees_nonnegative": packet["associated_rees_nonnegative"],
            "rank_nullity": packet["checks"]["rank_nullity"],
            "grade_preserved": packet["checks"]["relation_reduction_preserves_k_occurrence_grade"]
        })

    depth_three = [p for p in packets if p["k_depth"] == 3]
    replicated_signature = {
        (p["generated_rank"], p["quotient_rank"], p["relation_kernel_rank"],
         p["cross_grade_reduction_count"], p["associated_rees_nonnegative"])
        for p in depth_three
    }
    depth_four = next(p for p in packets if p["k_depth"] == 4)
    hostiles = {
        "depth_three_two_prime_two_chart_replication": len(depth_three) == 4 and len(replicated_signature) == 1,
        "rank_nullity_all_packets": all(p["rank_nullity"] for p in packets),
        "cross_grade_nondescent_detected": all(p["cross_grade_reduction_count"] > 0 for p in packets),
        "negative_associated_multiplicity_retained": any(not p["associated_rees_nonnegative"] for p in packets),
        "depth_extension_not_falsely_stabilized": depth_four["quotient_rank"] != depth_three[0]["quotient_rank"],
        "categorical_promotion_rejected": not contract["claims"]["complete_categorical_relation_module_available"],
        "prequotient_promotion_rejected": not contract["claims"]["prequotient_coordinate_tower_descends"]
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-exact-quotient-descent-result.v1",
        "passed": passed,
        "packets": packets,
        "depth_three_replicated_signature": list(next(iter(replicated_signature))),
        "hostiles": hostiles,
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
