#!/usr/bin/env python3
"""Exact finite audit of Coherent Resolution as a static linear realization."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as s


def characteristic_transform(m: int) -> tuple[list[tuple[int, int]], s.Matrix, int]:
    events = [(i, j) for i in range(1, m + 1) for j in range(i, m + 1)]
    position = {event: k for k, event in enumerate(events)}
    lower = [(1, j) for j in range(1, m + 1)]
    upper = [(i, m) for i in range(2, m + 1)]
    plaquettes = [(i, j) for i in range(2, m + 1) for j in range(i, m)]
    rows = lower + upper + plaquettes
    transform = s.zeros(len(rows), len(events))
    for r, event in enumerate(lower + upper):
        transform[r, position[event]] = 1
    for r, (i, j) in enumerate(plaquettes, start=len(lower) + len(upper)):
        for event, coefficient in (
            ((i, j), 1),
            ((i - 1, j), -1),
            ((i, j + 1), -1),
            ((i - 1, j + 1), 1),
        ):
            transform[r, position[event]] = coefficient
    return events, transform, len(lower) + len(upper)


rows = []
for m in range(2, 11):
    events, transform, boundary_rows = characteristic_transform(m)
    boundary = transform[:boundary_rows, :]
    rows.append(
        {
            "m": m,
            "field_dimension": len(events),
            "determinant": str(s.factor(transform.det())),
            "rank": transform.rank(),
            "boundary_rank": boundary.rank(),
            "boundary_kernel_dimension": len(events) - boundary.rank(),
            "bulk_coordinate_count": len(events) - boundary_rows,
        }
    )

# Deliberate hostile: at m=3 the field supported only at (2,2) has zero
# characteristic boundary but nonzero mixed curvature.
events3, transform3, boundary_rows3 = characteristic_transform(3)
hostile_field = s.zeros(len(events3), 1)
hostile_field[events3.index((2, 2)), 0] = 1
hostile_descriptor = transform3 * hostile_field
hostile_boundary = hostile_descriptor[:boundary_rows3, :]
hostile_bulk = hostile_descriptor[boundary_rows3:, :]

source = json.loads(
    (ROOT / "research/nima/results/nnmhv-kernel-wall-tail-boundary.json").read_text()
)
K = s.Matrix([[s.sympify(x) for x in row] for row in source["kernel_matrix"]])
K0 = s.Matrix(
    [[s.sympify(x) for x in row] for row in source["kernel_without_upper_boundary_transport"]]
)
t = s.symbols("t", real=True)
Kt = K0 + t * (K - K0)
effective = s.factor(Kt[2, 0] - Kt[2, 1] * Kt[1, 0] / Kt[1, 1])
critical = [root for root in s.solve(s.together(effective).as_numer_denom()[0], t) if root.is_real][0]
determinant_at_critical = s.factor(Kt.det().subs(t, critical))

checks = {
    "characteristic_transform_unimodular_m2_to_m10": all(
        abs(s.sympify(row["determinant"])) == 1 for row in rows
    ),
    "characteristic_transform_full_rank_m2_to_m10": all(
        row["rank"] == row["field_dimension"] for row in rows
    ),
    "boundary_kernel_equals_bulk_count_m2_to_m10": all(
        row["boundary_kernel_dimension"] == row["bulk_coordinate_count"] for row in rows
    ),
    "hostile_boundary_is_zero": hostile_boundary == s.zeros(boundary_rows3, 1),
    "hostile_bulk_is_nonzero": hostile_bulk != s.zeros(hostile_bulk.rows, 1),
    "schur_effective_sign_changes": bool(
        effective.subs(t, 0) < 0 and effective.subs(t, 1) > 0
    ),
    "schur_crossing_is_nonsingular": bool(determinant_at_critical != 0),
    "kernel_rank_stays_full_at_crossing": Kt.subs(t, critical).rank() == 3,
}

out = {
    "schema": "marici.sontag.coherent-resolution-control-audit.v1",
    "result_strength": "finite-cutoff theorem",
    "characteristic_rows": rows,
    "boundary_only_hostile": {
        "m": 3,
        "field_support": {"(2,2)": "1"},
        "boundary_descriptor": [str(x) for x in hostile_boundary],
        "bulk_descriptor": [str(x) for x in hostile_bulk],
        "predicted_nonzero_obstruction": "boundary-only reconstruction omits one bulk-curvature coordinate",
    },
    "schur_crossover": {
        "deformation_coordinate": "t",
        "critical_parameter": str(s.factor(critical)),
        "effective_coupling": str(effective),
        "determinant_at_critical_parameter": str(determinant_at_critical),
        "rank_at_critical_parameter": Kt.subs(t, critical).rank(),
        "classification": "readout-correlation sign crossover; not an invariant zero",
    },
    "control_typing": {
        "source_derived": [
            "finite configuration module",
            "boundary-plus-curvature coordinate isomorphism",
            "static physical kernel at the tested cutoff",
            "boundary-transport deformation coordinate",
        ],
        "absent": [
            "physical-time map",
            "state transition or vector field",
            "actuation map",
            "source-derived output family for a Rosenbrock pencil",
            "admissible feedback interconnection",
            "perturbation set and norm",
            "completion theorem",
        ],
        "verdict": "controllability, dynamic observability, invariant zeros, feedback stability, and robustness are undefined from the admitted data",
    },
    "checks": checks,
    "passed": all(checks.values()),
}

result_path = ROOT / "research/sontag/results/coherent_resolution_control_audit.json"
result_path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
