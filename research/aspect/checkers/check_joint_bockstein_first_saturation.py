#!/usr/bin/env python3
"""Independently audit the joint x/y first saturation of the Bockstein line."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "aspect" / "results" / "joint_bockstein_first_saturation.json"


def rank(vectors, prime):
    pivots = {}
    for source in vectors:
        row = {int(k): int(v) % prime for k, v in source.items() if int(v) % prime}
        while row:
            column = max(row)
            coefficient = row[column]
            if column not in pivots:
                inverse = pow(coefficient, -1, prime)
                pivots[column] = {k: v * inverse % prime for k, v in row.items()}
                break
            for k, v in pivots[column].items():
                residual = (row.get(k, 0) - coefficient * v) % prime
                if residual:
                    row[k] = residual
                else:
                    row.pop(k, None)
    return len(pivots)


def nonzero(rows):
    return [row for row in rows if any(int(value) for value in row.values())]


reports = []
for prime in (32009, 32003):
    suffix = "" if prime == 32009 else f"-p{prime}"
    packets = {}
    for axis in ("x", "y"):
        path = ROOT / "research" / "benincasa" / "results" / f"rank26-bidual-quotient-horizontality{suffix}-{axis}.json"
        packets[axis] = json.loads(path.read_text(encoding="utf-8"))
    bx = nonzero(packets["x"]["bockstein_vectors"])
    by = nonzero(packets["y"]["bockstein_vectors"])
    mx = nonzero(packets["x"]["mixed_vectors"])
    my = nonzero(packets["y"]["mixed_vectors"])
    line_rank = rank(bx + by, prime)
    x_rank = rank(bx + by + mx, prime)
    y_rank = rank(bx + by + my, prime)
    joint_rank = rank(bx + by + mx + my, prime)
    # Any invertible change of the two source directions preserves their joint span.
    axis_basis_invariant = True
    if len(mx) == len(my) == 1:
        keys = set(mx[0]) | set(my[0])
        for matrix in (((1, 1), (1, 2)), ((2, 3), (5, 7)), ((1, 0), (9, 1))):
            determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % prime
            if not determinant:
                continue
            changed = [
                {k: (a * mx[0].get(k, 0) + b * my[0].get(k, 0)) % prime for k in keys}
                for a, b in matrix
            ]
            axis_basis_invariant &= rank(bx + by + changed, prime) == joint_rank
    else:
        axis_basis_invariant = False
    reports.append({
        "prime": prime,
        "packets_pass": packets["x"]["passed"] and packets["y"]["passed"],
        "ranks": {"common_line": line_rank, "line_plus_x": x_rank, "line_plus_y": y_rank, "joint": joint_rank},
        "axis_basis_invariant": axis_basis_invariant,
    })

checks = {
    "both_primes_replayed": len(reports) == 2,
    "all_source_packets_pass": all(report["packets_pass"] for report in reports),
    "x_and_y_share_one_bockstein_line": all(report["ranks"]["common_line"] == 1 for report in reports),
    "each_direction_adds_one_rank": all(report["ranks"]["line_plus_x"] == report["ranks"]["line_plus_y"] == 2 for report in reports),
    "directions_are_independent_modulo_the_line": all(report["ranks"]["joint"] == 3 for report in reports),
    "joint_rank_is_source_axis_basis_invariant": all(report["axis_basis_invariant"] for report in reports),
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.joint-bockstein-first-saturation.v1",
    "reports": reports,
    "checks": checks,
    "passed": passed,
    "classification": "rank_three_first_saturation" if passed else "joint_saturation_not_admitted",
    "admitted_scope": "the audited point (2,3,4), primes 32009 and 32003, and invertible changes of the two-dimensional source-axis basis" if passed else "none",
    "consequence": "The common Bockstein line has two independent first directional images. Its first saturation is rank three, not rank two, so no one-direction connection surrogate captures the local two-parameter deformation." if passed else "No joint source-direction conclusion is admitted.",
    "next_falsifier": "construct the mixed x-y second jet and test whether it closes inside the rank-three first saturation" if passed else "regenerate the four quotient-projected source packets",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)
