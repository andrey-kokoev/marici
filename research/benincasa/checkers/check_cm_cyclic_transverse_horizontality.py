#!/usr/bin/env python3
"""Test quotient horizontality of the cyclic CM transverse-curvature port."""

import ast
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
CASES = (
    ("A", "32003"),
    ("A", "65521"),
    ("B", "65521"),
    ("HOMA", "32003"),
    ("SOFT1", "32003"),
)


def run_case(point, prime):
    environment = os.environ.copy()
    environment.update(
        NORMAL_TOWER="1",
        CM_CYCLIC_SECOND="horizontal",
        KINEMATIC_POINT=point,
        PRIME=prime,
    )
    completed = subprocess.run(
        ["cargo", "run", "--quiet", "--bin", "cm_normal_tower_rank"],
        cwd=CRATE,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    )
    summary = re.search(
        r"cohomology_rank=(\d+) labelled_class_rank=(\d+) label_count=(\d+)",
        completed.stdout,
    )
    labels = ast.literal_eval(
        re.search(r"NORMAL_TOWER_LABELS=(.*)", completed.stdout).group(1)
    )
    kernel = ast.literal_eval(
        re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1)
    )
    modulus = int(prime)
    relations = []
    for column in range(10, 14):
        matches = [row for row in kernel if row[column] != 0]
        if len(matches) != 1:
            raise RuntimeError(f"column {column} lacks a unique echelon relation")
        relation = matches[0]
        inverse_pivot = pow(relation[column], -1, modulus)
        normalized = [(value * inverse_pivot) % modulus for value in relation]
        signed = [
            value if value <= modulus // 2 else value - modulus
            for value in normalized
        ]
        relations.append(signed)
    quotient_coordinates = [-relation[3] for relation in relations]
    trace_coordinate = quotient_coordinates[0] % modulus
    connection_scalars = [
        (coordinate % modulus) * pow(trace_coordinate, -1, modulus) % modulus
        for coordinate in quotient_coordinates[1:]
    ]
    return {
        "point": point,
        "prime": modulus,
        "cohomology_rank": int(summary.group(1)),
        "labelled_class_rank": int(summary.group(2)),
        "label_count": int(summary.group(3)),
        "labels": labels,
        "kernel_dimension": len(kernel),
        "relations": relations,
        "quadratic_quotient_coordinates": quotient_coordinates,
        "quotient_connection_scalars_mod_prime": connection_scalars,
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = [run_case(*case) for case in CASES]
    checks = {
        "all_cm_cohomology_rank_7": all(run["cohomology_rank"] == 7 for run in runs),
        "derivatives_add_no_fifth_direction": all(
            run["labelled_class_rank"] == 4 for run in runs
        ),
        "fourteen_classes_have_ten_relations": all(
            run["label_count"] == 14 and run["kernel_dimension"] == 10
            for run in runs
        ),
        "all_new_classes_reduce_in_normal_rank_four_image": all(
            all(all(value == 0 for value in relation[4:10])
                for relation in run["relations"])
            for run in runs
        ),
        "trace_has_nonzero_quotient_coordinate": all(
            run["quadratic_quotient_coordinates"][0] != 0 for run in runs
        ),
        "all_groebner_runs_completed": all(run["gb_complete"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_cyclic_transverse_horizontality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "directions": ["d/d(P1^2)", "d/d(P2^2)", "d/d(P3^2)"],
        "connection_convention": (
            "nabla_D(A*K^-1/2)=(D A - (1/2) A (D K)/K)*K^-1/2"
        ),
        "runs": runs,
        "checks": checks,
        "conclusion": (
            "The cyclic transverse-curvature port is horizontal in the unique "
            "quadratic quotient by the three first-normal classes."
        ),
        "scope_warning": (
            "A lift in the full seven-dimensional CM cohomology may mix with "
            "first-normal classes. This does not certify a marked-relative "
            "subconnection or physical activation."
        ),
    }
    output = ROOT / "results" / "cm-cyclic-transverse-horizontality.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
