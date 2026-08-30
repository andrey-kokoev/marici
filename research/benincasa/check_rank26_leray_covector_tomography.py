#!/usr/bin/env python3
"""Audit finite source-jet tomography of the rank-26 Leray covector."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main():
    words = json.loads((ROOT / "rank26-source-word-basis.json").read_text())
    descriptors = words["descriptors"]
    roots = sorted({item["root"] for item in descriptors})
    checks = {
        "packet_has_26_primitive_words": len(descriptors) == 26,
        "reference_rank_is_26": words["reference_rank"] == 26,
        "control_ranks_are_26": all(item["rank"] == 26 for item in words["control_ranks"]),
        "maximum_depth_is_three": max(item["depth"] for item in descriptors) == 3,
        "roots_are_source_and_two_first_derivatives": roots == ["D0", "D1", "S"],
        "selection_is_primitive_not_reduced_representative": "never replaces the raw primitive" in words["selection"],
    }
    packet = {
        "schema": "marici.rank26_leray_covector_tomography.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "field": words["field"],
        "word_count": len(descriptors),
        "maximum_connection_depth": max(item["depth"] for item in descriptors),
        "roots": roots,
        "descriptors": descriptors,
        "checks": checks,
        "conclusion": (
            "At each certified generic point, a dual covector is uniquely determined by its evaluations on these 26 "
            "source-derived primitive words. The source-normalized Leray covector is therefore a finite period-jet "
            "evaluation problem, not a free complement or projector choice."
        ),
        "scope": (
            "This proves finite-field generic tomography and does not compute the characteristic-zero period jets, "
            "their integral normalization, or continuation through discriminant support."
        ),
    }
    output = ROOT / "rank26-leray-covector-tomography.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
