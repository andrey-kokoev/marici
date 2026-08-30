#!/usr/bin/env python3
"""Certify the CM coefficient-level second-total-energy adapter."""

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
        CM_TOTAL_ENERGY_SECOND="1",
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
    if not summary:
        raise RuntimeError("missing rank summary")
    labels = ast.literal_eval(
        re.search(r"NORMAL_TOWER_LABELS=(.*)", completed.stdout).group(1)
    )
    kernel = ast.literal_eval(
        re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1)
    )
    adapter_relations = []
    for adapter_column in (10, 11):
        matches = [
            row
            for row in kernel
            if row[adapter_column] != 0
            and all(row[other] == 0 for other in (10, 11) if other != adapter_column)
        ]
        if len(matches) != 1:
            raise RuntimeError(f"adapter column {adapter_column} lacks one echelon relation")
        relation = matches[0]
        inverse_pivot = pow(relation[adapter_column], -1, int(prime))
        normalized = [(value * inverse_pivot) % int(prime) for value in relation]
        adapter_relations.append(
            [
                value if value <= int(prime) // 2 else value - int(prime)
                for value in normalized
            ]
        )
    return {
        "point": point,
        "prime": int(prime),
        "cohomology_rank": int(summary.group(1)),
        "labelled_class_rank": int(summary.group(2)),
        "label_count": int(summary.group(3)),
        "labels": labels,
        "kernel_dimension": len(kernel),
        "adapter_relations": adapter_relations,
        "quadratic_quotient_coordinates": [
            -relation[3] for relation in adapter_relations
        ],
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = [run_case(*case) for case in CASES]
    checks = {
        "all_cm_cohomology_rank_7": all(run["cohomology_rank"] == 7 for run in runs),
        "adapter_adds_no_fifth_direction": all(
            run["labelled_class_rank"] == 4 for run in runs
        ),
        "twelve_classes_have_eight_relations": all(
            run["label_count"] == 12 and run["kernel_dimension"] == 8 for run in runs
        ),
        "both_adapters_reduce_in_first_four_basis": all(
            all(all(value == 0 for value in relation[4:10]) for relation in run["adapter_relations"])
            for run in runs
        ),
        "both_quadratic_quotient_components_are_nonzero": all(
            all(value != 0 for value in run["quadratic_quotient_coordinates"])
            for run in runs
        ),
        "all_groebner_runs_completed": all(run["gb_complete"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_total_energy_second_period_adapter.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_binary": "research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs",
        "source_formulas": {
            "algebraic_K^-5": "-5*L3/K + 60*P3^2*L3^2/K^2",
            "physical_K^-1/2": "-1/2*L3/K + 3/2*P3^2*L3^2/K^2",
        },
        "runs": runs,
        "checks": checks,
        "conclusion": (
            "Both the algebraic K^-5 audit twist and the physical K^-1/2 "
            "coefficient twist select the unique quadratic quotient line "
            "projectively at every tested background and at two primes, without "
            "adding a fifth class."
        ),
        "scope_warning": (
            "The affine quotient coordinate depends on kinematics. This certifies "
            "a projective CM coefficient direction, not a physical marked-wall "
            "class or a source-normalized affine trivialization of that line."
        ),
    }
    output = ROOT / "results" / "cm-total-energy-second-period-adapter.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
