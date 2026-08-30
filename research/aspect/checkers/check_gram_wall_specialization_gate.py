#!/usr/bin/env python3
"""Audit the Gram-wall rank jump and type its next acceptance gate."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "aspect" / "results" / "gram_wall_specialization_gate.json"


def rank(vectors, prime):
    pivots = {}
    for source in vectors:
        row = {int(k): int(v) % prime for k, v in source.items() if int(v) % prime}
        while row:
            column = max(row)
            coefficient = row[column]
            if column not in pivots:
                inverse = pow(coefficient, -1, prime)
                pivots[column] = {k: value * inverse % prime for k, value in row.items()}
                break
            for k, value in pivots[column].items():
                residual = (row.get(k, 0) - coefficient * value) % prime
                if residual:
                    row[k] = residual
                else:
                    row.pop(k, None)
    return len(pivots)


point = (3, 4, 5)
reports = []
for prime in (32009, 32003):
    suffix = "" if prime == 32009 else f"-p{prime}"
    packets = []
    for axis in ("x", "y"):
        path = ROOT / "research" / "benincasa" / "results" / f"rank26-bidual-quotient-horizontality{suffix}-{axis}-at-3-4-5.json"
        packet = json.loads(path.read_text(encoding="utf-8"))
        packets.append(packet)
    obstructions = [row for packet in packets for row in packet["obstruction_classes"]]
    obstruction_x = packets[0]["obstruction_classes"]
    obstruction_y = packets[1]["obstruction_classes"]
    mixed = [row for packet in packets for row in packet["mixed_vectors"] if any(int(value) for value in row.values())]
    mixed_x, mixed_y = mixed
    mixed_keys = set(mixed_x) | set(mixed_y)
    tangent = {key: (4 * int(mixed_x.get(key, 0)) - 3 * int(mixed_y.get(key, 0))) % prime for key in mixed_keys}
    normal = {key: (3 * int(mixed_x.get(key, 0)) + 4 * int(mixed_y.get(key, 0))) % prime for key in mixed_keys}
    obstruction_tangent_ranks = []
    obstruction_normal_ranks = []
    for row_x, row_y in zip(obstruction_x, obstruction_y):
        keys = set(row_x) | set(row_y)
        obstruction_tangent = {key: (4 * int(row_x.get(key, 0)) - 3 * int(row_y.get(key, 0))) % prime for key in keys}
        obstruction_normal = {key: (3 * int(row_x.get(key, 0)) + 4 * int(row_y.get(key, 0))) % prime for key in keys}
        obstruction_tangent_ranks.append(rank([obstruction_tangent], prime))
        obstruction_normal_ranks.append(rank([obstruction_normal], prime))
    reports.append({
        "prime": prime,
        "patterns": [
            [packet["base_relation_dimension"], packet["lifted_relation_dimension"], packet["obstructed_relation_dimension"], packet["bockstein_rank"], packet["bockstein_plus_mixed_rank"]]
            for packet in packets
        ],
        "obstruction_supports": [sorted(int(k) for k, value in row.items() if int(value) % prime) for row in obstructions],
        "obstruction_costalk_rank": rank(obstructions, prime),
        "joint_mixed_rank": rank(mixed, prime),
        "gram_tangent_image_rank": rank([tangent], prime),
        "gram_normal_image_rank": rank([normal], prime),
        "obstruction_tangent_ranks": obstruction_tangent_ranks,
        "obstruction_normal_ranks": obstruction_normal_ranks,
    })

checks = {
    "point_lies_on_frozen_gram_wall": point[0] ** 2 + point[1] ** 2 - point[2] ** 2 == 0,
    "four_runs_have_wall_pattern_3_1_2_0_1": all(pattern == [3, 1, 2, 0, 1] for report in reports for pattern in report["patterns"]),
    "all_obstructions_have_common_single_coordinate_support": all(support == [7] for report in reports for support in report["obstruction_supports"]),
    "two_obstructed_relations_collapse_to_one_costalk_line": all(report["obstruction_costalk_rank"] == 1 for report in reports),
    "two_directional_mixed_images_collapse_to_one_line": all(report["joint_mixed_rank"] == 1 for report in reports),
    "gram_tangent_direction_is_killed": all(report["gram_tangent_image_rank"] == 0 for report in reports),
    "gram_normal_direction_generates_mixed_line": all(report["gram_normal_image_rank"] == 1 for report in reports),
    "gram_tangent_kills_every_lift_obstruction": all(rank_value == 0 for report in reports for rank_value in report["obstruction_tangent_ranks"]),
    "gram_normal_generates_every_lift_obstruction": all(rank_value == 1 for report in reports for rank_value in report["obstruction_normal_ranks"]),
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.gram-wall-specialization-gate.v1",
    "reports": reports,
    "checks": checks,
    "passed": passed,
    "classification": "first_order_defect_factors_through_gram_conormal" if passed else "gram_wall_typing_not_admitted",
    "admitted_scope": "the point (3,4,5) on h=0, directions x and y, and primes 32009 and 32003" if passed else "none",
    "consequence": "Every first-order defect factors through the Gram conormal. For both lift obstructions and the mixed image, the tangent combination 4 dx-3 dy vanishes and the normal combination 3 dx+4 dy is nonzero. The obstruction and transport targets are distinct lines, so their cohomological comparison still requires the shifted connecting morphism." if passed else "No support-factorization claim is admitted.",
    "missing_constructors": ["source-derived h=0 specialization/Gysin costalk map"] if passed else ["repaired Gram-wall packets"],
    "next_falsifier": "derive the existing h=0 specialization/Gysin costalk map and test whether its normal image simultaneously accounts for quotient coordinate 7 and the common mixed line while annihilating the Gram tangent" if passed else "regenerate the four Gram-wall packets",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)
