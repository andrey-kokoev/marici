#!/usr/bin/env python3
"""Test whether the three physical first-normal CM classes form a subconnection."""

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))


def run_case(
    point,
    prime,
    derivative_count,
    include_cyclic=False,
    include_cyclic_derivatives=False,
):
    environment = os.environ.copy()
    environment.update(
        NORMAL_TOWER="1",
        CM_FIRST_NORMAL_HORIZONTAL="1",
        CM_FIRST_NORMAL_DERIVATIVE_COUNT=str(derivative_count),
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    if include_cyclic:
        environment["CM_FIRST_NORMAL_INCLUDE_CYCLIC"] = "1"
    if include_cyclic_derivatives:
        environment["CM_FIRST_NORMAL_INCLUDE_CYCLIC_DERIVATIVES"] = "1"
    completed = subprocess.run(
        ["cargo", "run", "--quiet", "--bin", "cm_normal_tower_rank"],
        cwd=CRATE,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    )
    match = re.search(
        r"cohomology_rank=(\d+) labelled_class_rank=(\d+) label_count=(\d+)",
        completed.stdout,
    )
    return {
        "derivative_count": derivative_count,
        "include_cyclic": include_cyclic,
        "include_cyclic_derivatives": include_cyclic_derivatives,
        "cohomology_rank": int(match.group(1)),
        "class_rank": int(match.group(2)),
        "label_count": int(match.group(3)),
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = []
    for point, prime in CASES:
        prefixes = [run_case(point, prime, count) for count in range(10)]
        cyclic_without_escape = run_case(point, prime, 0, include_cyclic=True)
        cyclic_with_escape = run_case(point, prime, 1, include_cyclic=True)
        complete_rank_four_closure = run_case(
            point,
            prime,
            9,
            include_cyclic_derivatives=True,
        )
        first_escape = next(
            (item["derivative_count"] for item in prefixes if item["class_rank"] > prefixes[0]["class_rank"]),
            None,
        )
        runs.append({
            "point": point,
            "prime": prime,
            "prefixes": prefixes,
            "first_escape": first_escape,
            "cyclic_without_escape": cyclic_without_escape,
            "cyclic_with_escape": cyclic_with_escape,
            "complete_rank_four_closure": complete_rank_four_closure,
        })
    checks = {
        "physical_first_normal_span_has_rank_three": all(run["prefixes"][0]["class_rank"] == 3 for run in runs),
        "a_derivative_escapes_at_every_case": all(run["first_escape"] is not None for run in runs),
        "smallest_escape_is_stable": len({run["first_escape"] for run in runs}) == 1,
        "cyclic_class_is_the_same_unique_escape_direction": all(
            run["cyclic_without_escape"]["class_rank"] == 4
            and run["cyclic_with_escape"]["class_rank"] == 4
            for run in runs
        ),
        "rank_four_transport_closure_is_preserved": all(
            run["complete_rank_four_closure"]["class_rank"] == 4
            and run["complete_rank_four_closure"]["label_count"] == 16
            for run in runs
        ),
        "all_groebner_runs_complete": all(
            prefix["gb_complete"] for run in runs for prefix in (
                run["prefixes"]
                + [
                    run["cyclic_without_escape"],
                    run["cyclic_with_escape"],
                    run["complete_rank_four_closure"],
                ]
            )
        ),
    }
    packet = {
        "schema": "marici.cm_first_normal_subconnection.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "derivative_order": [
            "nabla_1_nu1", "nabla_1_nu2", "nabla_1_nu3",
            "nabla_2_nu1", "nabla_2_nu2", "nabla_2_nu3",
            "nabla_3_nu1", "nabla_3_nu2", "nabla_3_nu3",
        ],
        "runs": runs,
        "checks": checks,
        "conclusion": (
            "The physical first-normal rank-three span is not a subconnection; "
            "the first prefix rank increase is the smallest off-span witness."
        ),
    }
    output = ROOT / "results" / "cm-first-normal-subconnection.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": packet["status"],
        "first_escapes": [run["first_escape"] for run in runs],
        "ranks": [[prefix["class_rank"] for prefix in run["prefixes"]] for run in runs],
        "checks": checks,
    }, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
