from __future__ import annotations

import json
from pathlib import Path


def relative(left, right):
    return (left - right) % 4


def edge_record(frames):
    return {
        "S-A": relative(frames["S"], frames["A"]),
        "S-B": relative(frames["S"], frames["B"]),
        "A-B": relative(frames["A"], frames["B"]),
    }


def closes(record):
    return (record["S-A"] + record["A-B"]) % 4 == record["S-B"]


def main() -> None:
    baseline = {"S": 0, "A": 0, "B": 0}
    science_drift = {"S": 1, "A": 0, "B": 0}
    anchor_a_drift = {"S": 0, "A": 3, "B": 0}

    baseline_record = edge_record(baseline)
    science_record = edge_record(science_drift)
    anchor_record = edge_record(anchor_a_drift)

    assert baseline_record == {"S-A": 0, "S-B": 0, "A-B": 0}
    assert science_record == {"S-A": 1, "S-B": 1, "A-B": 0}
    assert anchor_record == {"S-A": 1, "S-B": 0, "A-B": 3}
    assert science_record["S-A"] == anchor_record["S-A"]
    assert science_record != anchor_record
    assert closes(science_record)
    assert closes(anchor_record)

    single_anchor_attribution_unique = science_record["S-A"] != anchor_record["S-A"]
    triangle_attribution_unique_under_single_locus_model = science_record != anchor_record
    assert not single_anchor_attribution_unique
    assert triangle_attribution_unique_under_single_locus_model

    result = {
        "schema": "marici.aspect.single-anchor-detects-but-does-not-attribute-drift.v1",
        "status": "pass",
        "baseline_edges": baseline_record,
        "science_drift_edges": science_record,
        "anchor_a_drift_edges": anchor_record,
        "single_anchor_SA_records_identical": science_record["S-A"] == anchor_record["S-A"],
        "single_anchor_attribution_unique": single_anchor_attribution_unique,
        "science_drift_triangle_closes": closes(science_record),
        "anchor_drift_triangle_closes": closes(anchor_record),
        "triangle_patterns_distinct": science_record != anchor_record,
        "triangle_attribution_unique_under_single_locus_model": triangle_attribution_unique_under_single_locus_model,
        "verdict": "One perfect cross-locus edge detects the same quarter-turn mismatch whether the science frame or anchor moved. A second anchor produces distinct triangle patterns under stable-link and single-moving-locus assumptions. Loop closure certifies consistency, not causal attribution by itself.",
        "claim_boundary": "exact quarter-turn frames, noiseless pairwise differences, stable links, and single-moving-locus attribution; no simultaneous drift, link bias, nonreciprocity, or statistical thresholds",
    }
    output = Path(__file__).parents[1] / "results" / "single_anchor_detects_but_does_not_attribute_drift.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
