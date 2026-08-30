#!/usr/bin/env python3
"""Test whether visible curvature is a chain map of the CM transitivity complex."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def block_diagonal(matrix, copies):
    n = len(matrix)
    return [
        [matrix[i % n][j % n] if i // n == j // n else 0 for j in range(copies * n)]
        for i in range(copies * n)
    ]


def multiply(left, right, prime):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) % prime for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def subtract(left, right, prime):
    return [[(a - b) % prime for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


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
            work[row] = [(work[row][j] - factor * work[rank][j]) % prime for j in range(len(work[row]))]
        rank += 1
    return rank


def main():
    transitivity = json.loads((ROOT / "results" / "cm-conormal-kodaira-spencer.json").read_text())
    curvature = json.loads((ROOT / "results" / "cm-rank-seven-dual-flatness.json").read_text())
    trans_runs = {(run["point"], run["prime"]): run for run in transitivity["runs"]}
    runs = []
    for run in curvature["runs"]:
        key = (run["point"], run["prime"])
        kappa = trans_runs[key]["transitivity_matrix"]
        item = {"point": run["point"], "prime": run["prime"]}
        for convention, field in (("minus", "minus_sign_curvatures"), ("plus", "plus_sign_curvatures")):
            ranks = {}
            for name in ("F_12", "F_13", "F_23"):
                visible = run[field][name]
                target = block_diagonal(visible, 4)
                source = block_diagonal(visible, 3)
                defect = subtract(multiply(target, kappa, run["prime"]), multiply(kappa, source, run["prime"]), run["prime"])
                ranks[name] = rank_mod(defect, run["prime"])
            item[f"{convention}_chain_map_defect_ranks"] = ranks
            item[f"{convention}_all_descend"] = all(rank == 0 for rank in ranks.values())
        runs.append(item)

    checks = {
        "all_input_packets_matched": len(runs) == len(curvature["runs"]),
        "minus_curvature_descends": all(run["minus_all_descend"] for run in runs),
        "plus_curvature_descends": all(run["plus_all_descend"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_curvature_transitivity_descent.v1",
        "status": "pass" if checks["all_input_packets_matched"] else "fail",
        "curvature_descends_for_at_least_one_convention": checks["minus_curvature_descends"] or checks["plus_curvature_descends"],
        "runs": runs,
        "checks": checks,
        "scope": (
            "The diagonal action is the unique untwisted action of the visible quotient curvature on the four target and "
            "three source occurrence blocks. A nonzero defect rejects descent under that frozen action but does not exclude "
            "a source-derived off-diagonal coherence action."
        ),
    }
    output = ROOT / "results" / "cm-curvature-transitivity-descent.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
