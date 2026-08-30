#!/usr/bin/env python3
"""Certify the cyclic trace of labelled CM transverse period curvatures."""

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
        CM_CYCLIC_SECOND="1",
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
    matches = [row for row in kernel if row[10] != 0]
    if len(matches) != 1:
        raise RuntimeError("cyclic trace lacks a unique echelon relation")
    relation = matches[0]
    modulus = int(prime)
    inverse_pivot = pow(relation[10], -1, modulus)
    normalized = [(value * inverse_pivot) % modulus for value in relation]
    signed = [value if value <= modulus // 2 else value - modulus for value in normalized]
    return {
        "point": point,
        "prime": modulus,
        "cohomology_rank": int(summary.group(1)),
        "labelled_class_rank": int(summary.group(2)),
        "label_count": int(summary.group(3)),
        "labels": labels,
        "kernel_dimension": len(kernel),
        "cyclic_trace_relation": signed,
        "quadratic_quotient_coordinate": -signed[3],
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = [run_case(*case) for case in CASES]
    checks = {
        "all_cm_cohomology_rank_7": all(run["cohomology_rank"] == 7 for run in runs),
        "cyclic_trace_adds_no_fifth_direction": all(
            run["labelled_class_rank"] == 4 for run in runs
        ),
        "eleven_classes_have_seven_relations": all(
            run["label_count"] == 11 and run["kernel_dimension"] == 7 for run in runs
        ),
        "trace_reduces_in_first_four_basis": all(
            all(value == 0 for value in run["cyclic_trace_relation"][4:10])
            for run in runs
        ),
        "quadratic_quotient_coordinate_is_nonzero": all(
            run["quadratic_quotient_coordinate"] != 0 for run in runs
        ),
        "all_groebner_runs_completed": all(run["gb_complete"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_cyclic_transverse_curvature.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_operation": (
            "sum_i twice the K^(-1/2) second coefficient under the labelled "
            "normal path P_i -> P_i + tau_i"
        ),
        "runs": runs,
        "checks": checks,
        "scope_warning": (
            "The cyclic trace is a canonical transverse coefficient operation. "
            "It is not a map from the scalar total-energy conormal."
        ),
    }
    output = ROOT / "results" / "cm-cyclic-transverse-curvature.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
