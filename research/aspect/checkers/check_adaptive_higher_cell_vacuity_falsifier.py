import json
from pathlib import Path

import sympy as sp


samples = [
    (
        sp.Matrix([[1, 0], [0, 1]]),
        sp.Matrix([[1, 0], [0, 1]]),
        sp.Matrix([[1, 0], [0, 1]]),
        sp.Matrix([[1, 0], [0, 1]]),
    ),
    (
        sp.Matrix([[1, 2], [0, 1]]),
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[2, 0], [1, 1]]),
        sp.Matrix([[1, 0], [3, 1]]),
    ),
    (
        sp.Matrix([[2, 0], [0, 3]]),
        sp.Matrix([[1, 1], [0, 1]]),
        sp.Matrix([[0, 1], [-1, 0]]),
        sp.Matrix([[4, 0], [2, 1]]),
    ),
]

residuals = []
absorbed = []
for A, B, C, D in samples:
    upper_path = D * A
    lower_path = C * B
    alpha = upper_path - lower_path
    residuals.append(alpha)
    absorbed.append(upper_path == lower_path + alpha)

checks = {
    "strict_control_square_closes": residuals[0] == sp.zeros(2),
    "first_hostile_square_fails_strictly": residuals[1] != sp.zeros(2),
    "second_hostile_square_fails_strictly": residuals[2] != sp.zeros(2),
    "adjoined_cell_absorbs_every_sample": all(absorbed),
    "distinct_hostiles_get_distinct_cells": residuals[1] != residuals[2],
    "acceptance_rate_after_adaptive_completion": sum(absorbed) == len(samples),
}

result = {
    "schema": "marici.aspect.adaptive-higher-cell-vacuity-falsifier.v1",
    "status": "falsified_as_deutschian_conjecture" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "falsified_clause": "Whenever a constructor fails to descend, adjoin a typed cell at the next depth.",
    "reason": "Unrestricted adaptive cell adjunction accepts every finite residual and therefore excludes no hostile packet.",
    "repair": "Preregister a finite signature, admitted cell types, equations, depth bound, and forbidden residuals before testing.",
}

out = Path(__file__).parents[1] / "results" / "adaptive_higher_cell_vacuity_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "falsified_as_deutschian_conjecture" else 1)
