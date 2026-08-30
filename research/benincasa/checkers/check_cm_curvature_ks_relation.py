#!/usr/bin/env python3
"""Test whether CM curvature can factor through the KS pair-wedge packet."""

import json
from pathlib import Path

from check_cm_conormal_kodaira_spencer import normalized_relation


ROOT = Path(__file__).resolve().parent.parent


def flatten(matrix):
    return [value for row in matrix for value in row]


def main():
    ks = json.loads((ROOT / "results" / "cm-conormal-kodaira-spencer.json").read_text())
    curvature = json.loads((ROOT / "results" / "cm-rank-seven-dual-flatness.json").read_text())
    ks_runs = {(run["point"], run["prime"]): run for run in ks["runs"]}
    runs = []
    for run in curvature["runs"]:
        key = (run["point"], run["prime"])
        ks_run = ks_runs[key]
        result = {
            "point": run["point"],
            "prime": run["prime"],
            "ks_pair_relation": ks_run["pair_wedge_relation"],
        }
        for convention, field in (
            ("minus", "minus_sign_curvatures"),
            ("plus", "plus_sign_curvatures"),
        ):
            columns = [flatten(run[field][name]) for name in ("F_12", "F_13", "F_23")]
            try:
                relation = normalized_relation(columns, run["prime"])
                rank = 2
            except RuntimeError:
                relation = None
                rank = 3
            result[f"{convention}_curvature_rank"] = rank
            result[f"{convention}_curvature_relation"] = relation
            result[f"{convention}_matches_ks_relation"] = relation == ks_run["pair_wedge_relation"]
        runs.append(result)

    checks = {
        "all_ks_pair_packets_have_rank_two": all(run["ks_pair_relation"] is not None for run in runs),
        "minus_curvature_has_matching_relation": all(run["minus_matches_ks_relation"] for run in runs),
        "plus_curvature_has_matching_relation": all(run["plus_matches_ks_relation"] for run in runs),
    }
    at_least_one = checks["minus_curvature_has_matching_relation"] or checks["plus_curvature_has_matching_relation"]
    packet = {
        "schema": "marici.cm_curvature_ks_relation.v1",
        "status": "pass" if checks["all_ks_pair_packets_have_rank_two"] else "fail",
        "factorization_survives_necessary_relation_test": at_least_one,
        "runs": runs,
        "checks": checks,
        "scope": (
            "Matching relation kernels is necessary but not sufficient for a source-derived Koszul factorization. "
            "A mismatch rules out a base-linear factorization through the KS pair-wedge packet."
        ),
    }
    output = ROOT / "results" / "cm-curvature-ks-relation.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
