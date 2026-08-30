#!/usr/bin/env python3
"""Extract provenance-corrected rank-seven CM connection matrices."""

import ast
import os
import re
import subprocess
from pathlib import Path

from probe_cm_cyclic_connection_slice_degrees import solve_linear


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
EXE = CRATE / "target" / "release" / "cm_normal_tower_rank.exe"
FRAME = (
    "physical_nu1",
    "physical_nu2",
    "physical_nu3",
    "cyclic_trace_2*K^-1/2",
    "d1_exact_gradient_a",
    "d1_exact_gradient_b",
    "d1_exact_gradient_c",
)
TARGET_STEMS = (
    "physical_nu1",
    "physical_nu2",
    "physical_nu3",
    "cyclic_trace",
    "d1_exact_gradient_a",
    "d1_exact_gradient_b",
    "d1_exact_gradient_c",
)


def run_case(point, prime, squared_momenta=None):
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_FIRST_NORMAL_HORIZONTAL="1",
        CM_FIRST_NORMAL_DERIVATIVE_COUNT="9",
        CM_FIRST_NORMAL_INCLUDE_CYCLIC_DERIVATIVES="1",
        CM_EXACT_GENERATOR_DERIVATIVES="1",
        CM_EXACT_GENERATOR_SECOND_DERIVATIVES="1",
        CM_EXACT_GENERATOR_DERIVATIVE_COUNT="21",
        CM_PROVENANCE_CORRECTED_DERIVATIVES="1",
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    if squared_momenta is not None:
        env["CM_P_SQUARES"] = ",".join(map(str, squared_momenta))
    completed = subprocess.run(
        [str(EXE)], cwd=CRATE, env=env, text=True, capture_output=True, check=True
    )
    labels = ast.literal_eval(re.search(r"NORMAL_TOWER_LABELS=(.*)", completed.stdout).group(1))
    kernel = ast.literal_eval(re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1))
    frame_indices = [labels.index(label) for label in FRAME]
    other_indices = [i for i in range(len(labels)) if i not in frame_indices]
    if len(kernel) != len(other_indices):
        raise RuntimeError("kernel dimension does not match nonframe count")

    matrix = [[row[index] % prime for row in kernel] for index in other_indices]

    def coordinates(target_label):
        target = labels.index(target_label)
        rhs = [1 if index == target else 0 for index in other_indices]
        combination = solve_linear(matrix, rhs, prime)
        if combination is None:
            raise RuntimeError(f"cannot isolate {target_label}")
        relation = [
            sum(combination[r] * kernel[r][c] for r in range(len(kernel))) % prime
            for c in range(len(labels))
        ]
        return [(-relation[index]) % prime for index in frame_indices]

    matrices = []
    for direction in range(1, 4):
        columns = [
            coordinates(f"lifted_nabla_{direction}_{stem}") for stem in TARGET_STEMS
        ]
        matrices.append([[columns[column][row] for column in range(7)] for row in range(7)])
    return {"point": point, "prime": prime, "matrices": matrices, "frame": list(FRAME)}

