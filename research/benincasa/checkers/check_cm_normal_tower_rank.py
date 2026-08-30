#!/usr/bin/env python3
"""Run and certify the bounded Cayley--Menger-only normal-tower census."""

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
    ("B", "65521"),
    ("HOMA", "32003"),
    ("SOFT1", "32003"),
)


def run_case(point, prime):
    environment = os.environ.copy()
    environment.update(NORMAL_TOWER="1", KINEMATIC_POINT=point, PRIME=prime)
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
    if not summary:
        raise RuntimeError("missing rank summary")
    labels = ast.literal_eval(
        re.search(r"NORMAL_TOWER_LABELS=(.*)", completed.stdout).group(1)
    )
    kernel = ast.literal_eval(
        re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1)
    )
    return {
        "point": point,
        "prime": int(prime),
        "cohomology_rank": int(summary.group(1)),
        "labelled_class_rank": int(summary.group(2)),
        "label_count": int(summary.group(3)),
        "labels": labels,
        "kernel": kernel,
        "kernel_dimension": len(kernel),
        "kernel_echelon_tail": [row[4:] for row in kernel],
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = [run_case(*case) for case in CASES]
    checks = {
        "all_cm_cohomology_rank_7": all(run["cohomology_rank"] == 7 for run in runs),
        "all_labelled_tower_rank_4": all(run["labelled_class_rank"] == 4 for run in runs),
        "all_kernel_dimension_6": all(run["kernel_dimension"] == 6 for run in runs),
        "first_four_columns_are_a_basis": all(
            run["kernel_echelon_tail"]
            == [[1 if row == column else 0 for column in range(6)] for row in range(6)]
            for run in runs
        ),
        "all_groebner_runs_completed": all(run["gb_complete"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_normal_tower_rank.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_binary": "research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs",
        "runs": runs,
        "checks": checks,
        "conclusion": (
            "The ten labelled normal coefficients span rank four in the generic "
            "Cayley-Menger-only rank-seven quotient. The first three normals and "
            "nu1^2 form a basis in every tested presentation."
        ),
        "scope_warning": (
            "This is generic coefficient compression on K != 0, not a computation "
            "of local cohomology supported on the Cayley-Menger discriminant."
        ),
    }
    output = ROOT / "results" / "cm-normal-tower-rank.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
