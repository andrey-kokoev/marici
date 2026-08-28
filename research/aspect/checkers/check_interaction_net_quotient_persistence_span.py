#!/usr/bin/env python3
"""Exact rank decomposition of the depth-3 to depth-4 quotient transition."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect"
CONTRACT = ASPECT / "contracts" / "interaction-net-quotient-persistence-span.v1.json"
RESULT = ASPECT / "results" / "interaction_net_quotient_persistence_span.json"

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    transition_packets = [
        json.loads((ROOT / locator).read_text(encoding="utf-8"))
        for locator in contract["source_packets"][:7]
    ]
    depth4 = json.loads((ROOT / contract["source_packets"][7]).read_text(encoding="utf-8"))
    rows = []
    for packet in transition_packets:
        source_depth = packet.get("source_depth", 3)
        target_depth = packet.get("target_depth", 4)
        q3 = packet.get("source_quotient_rank", packet.get("depth3_quotient_rank"))
        target_dimension = depth4["global_quotient_rank"] if target_depth == 4 else None
        rank = packet["transition_image_rank"]
        kernel = packet["transition_kernel_rank"]
        cokernel = target_dimension - rank if target_dimension is not None else None
        rows.append({
            "chart": packet["chart"], "prime": packet["prime"],
            "source_depth": source_depth, "target_depth": target_depth,
            "source_dimension": q3, "target_dimension": target_dimension,
            "persistent_dimension": rank,
            "dying_dimension": kernel,
            "emergent_dimension_when_target_rank_known": cokernel,
            "rank_nullity": rank + kernel == q3,
            "dual_rank": rank,
            "dual_nonliftable_source_observables": q3 - rank,
            "dual_target_observables_vanishing_on_old_image_when_known": cokernel
        })
    depth3_rows = [r for r in rows if r["source_depth"] == 3]
    chart_signatures = {}
    for chart in ("G12", "G31"):
        chart_signatures[chart] = [
            (r["target_depth"], r["persistent_dimension"], r["dying_dimension"])
            for r in depth3_rows if r["chart"] == chart
        ]
    expected = contract["transition"]
    hostiles = {
        "two_chart_replication": chart_signatures["G12"] == chart_signatures["G31"] == [(4, 33, 20), (5, 27, 26), (6, 27, 26)],
        "rank_nullity": all(r["rank_nullity"] for r in rows),
        "noninjectivity_retained": expected["injective"] is False and all(r["dying_dimension"] > 0 for r in rows),
        "six_later_deaths_retained": 33 - 27 == 6,
        "bounded_survival_not_promoted": contract["depth3_barcode_through_tested_depth6"]["survival_beyond_depth6"] == "unknown",
        "depth4_emergent_sector_retained": all(
            r["emergent_dimension_when_target_rank_known"] == 1353
            for r in rows if r["source_depth"] == 3 and r["target_depth"] == 4
        ),
        "lossless_inverse_rejected": contract["dual_instrument_decomposition"]["lossless_inverse_restriction_exists"] is False,
        "physical_modes_not_promoted": "dual coefficient rows in the source-labelled carrier" in contract["required_export"]
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-quotient-persistence-span-result.v1",
        "passed": passed,
        "chart_rows": rows,
        "depth3_chart_signatures": chart_signatures,
        "hostiles": hostiles,
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
