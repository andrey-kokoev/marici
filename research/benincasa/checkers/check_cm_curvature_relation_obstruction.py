#!/usr/bin/env python3
"""Evaluate curvature on the unique KS pair-wedge relation."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def add_scaled(matrices, coefficients, prime):
    height = len(matrices[0])
    width = len(matrices[0][0])
    return [
        [
            sum(coefficients[k] * matrices[k][i][j] for k in range(3)) % prime
            for j in range(width)
        ]
        for i in range(height)
    ]


def rank_mod(matrix, prime):
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][j] - factor * work[rank][j]) % prime
                for j in range(len(work[row]))
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def main():
    ks = json.loads((ROOT / "results" / "cm-conormal-kodaira-spencer.json").read_text())
    curvature = json.loads((ROOT / "results" / "cm-rank-seven-dual-flatness.json").read_text())
    relations = {(run["point"], run["prime"]): run["pair_wedge_relation"] for run in ks["runs"]}
    runs = []
    for run in curvature["runs"]:
        key = (run["point"], run["prime"])
        relation = relations[key]
        item = {"point": run["point"], "prime": run["prime"], "relation": relation}
        for convention, field in (
            ("minus", "minus_sign_curvatures"),
            ("plus", "plus_sign_curvatures"),
        ):
            matrices = [run[field][name] for name in ("F_12", "F_13", "F_23")]
            obstruction = add_scaled(matrices, relation, run["prime"])
            item[f"{convention}_obstruction"] = obstruction
            item[f"{convention}_obstruction_rank"] = rank_mod(obstruction, run["prime"])
            item[f"{convention}_obstruction_nonzero"] = any(value for row in obstruction for value in row)
        runs.append(item)

    checks = {
        "relation_obstruction_is_nonzero_for_minus_sign": all(run["minus_obstruction_nonzero"] for run in runs),
        "relation_obstruction_is_nonzero_for_plus_sign": all(run["plus_obstruction_nonzero"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_curvature_relation_obstruction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "base_two_form_order": ["12", "13", "23"],
        "runs": runs,
        "checks": checks,
        "scope": (
            "The nonzero contraction is the canonical obstruction to descending curvature through the tested "
            "pair-wedge relation. It does not by itself construct a source-derived coherence cell."
        ),
    }
    output = ROOT / "results" / "cm-curvature-relation-obstruction.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
