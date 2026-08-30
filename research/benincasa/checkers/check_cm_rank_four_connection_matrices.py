#!/usr/bin/env python3
"""Extract the source-labelled rank-four CM connection matrices."""

import ast
import json
import os
import re
import subprocess
from pathlib import Path

from probe_cm_cyclic_connection_slice_degrees import solve_linear


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))
FRAME = (
    "physical_nu1",
    "physical_nu2",
    "physical_nu3",
    "cyclic_trace_2*K^-1/2",
)


def run_case(point, prime, squared_momenta=None):
    environment = os.environ.copy()
    environment.update(
        NORMAL_TOWER="1",
        CM_FIRST_NORMAL_HORIZONTAL="1",
        CM_FIRST_NORMAL_DERIVATIVE_COUNT="9",
        CM_FIRST_NORMAL_INCLUDE_CYCLIC_DERIVATIVES="1",
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    if squared_momenta is not None:
        environment["CM_P_SQUARES"] = ",".join(map(str, squared_momenta))
    completed = subprocess.run(
        ["cargo", "run", "--quiet", "--bin", "cm_normal_tower_rank"],
        cwd=CRATE,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    )
    labels = ast.literal_eval(re.search(r"NORMAL_TOWER_LABELS=(.*)", completed.stdout).group(1))
    kernel = ast.literal_eval(re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1))
    frame_indices = [labels.index(label) for label in FRAME]
    other_indices = [index for index in range(len(labels)) if index not in frame_indices]
    if len(kernel) != len(other_indices):
        raise RuntimeError("kernel dimension does not match nonframe column count")

    def coordinates(target_label):
        target = labels.index(target_label)
        rhs = [1 if index == target else 0 for index in other_indices]
        matrix = [[row[index] % prime for row in kernel] for index in other_indices]
        combination = solve_linear(matrix, rhs, prime)
        if combination is None:
            raise RuntimeError(f"cannot isolate relation for {target_label}")
        relation = [
            sum(combination[row_index]*kernel[row_index][column] for row_index in range(len(kernel))) % prime
            for column in range(len(labels))
        ]
        if relation[target] != 1 or any(
            relation[index] != 0 for index in other_indices if index != target
        ):
            raise RuntimeError(f"invalid isolated relation for {target_label}")
        return [(-relation[index]) % prime for index in frame_indices]

    matrices = []
    for direction in range(1, 4):
        targets = [
            f"nabla_{direction}_physical_nu1",
            f"nabla_{direction}_physical_nu2",
            f"nabla_{direction}_physical_nu3",
            f"nabla_{direction}_cyclic_trace",
        ]
        columns = [coordinates(target) for target in targets]
        matrices.append([
            [columns[column][row] for column in range(4)]
            for row in range(4)
        ])
    return {
        "point": point,
        "squared_momenta_override": list(squared_momenta) if squared_momenta is not None else None,
        "prime": prime,
        "frame": list(FRAME),
        "matrices": matrices,
        "gb_complete": "GB_COMPLETE" in completed.stderr,
    }


def main():
    runs = [run_case(point, prime) for point, prime in CASES]
    checks = {
        "all_three_matrices_are_four_by_four": all(
            len(run["matrices"]) == 3
            and all(len(matrix) == 4 and all(len(row) == 4 for row in matrix) for matrix in run["matrices"])
            for run in runs
        ),
        "all_groebner_runs_complete": all(run["gb_complete"] for run in runs),
    }
    packet = {
        "schema": "marici.cm_rank_four_connection_matrices.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "connection_convention": "columns are covariant derivatives of the ordered source frame",
        "directions": ["d/d(P1^2)", "d/d(P2^2)", "d/d(P3^2)"],
        "runs": runs,
        "checks": checks,
    }
    output = ROOT / "results" / "cm-rank-four-connection-matrices.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": packet["status"],
        "checks": checks,
        "runs": [{"point": run["point"], "prime": run["prime"], "matrices": run["matrices"]} for run in runs],
    }, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
