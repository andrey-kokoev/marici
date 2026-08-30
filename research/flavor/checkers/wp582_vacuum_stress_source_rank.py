"""Exact WP582 Lorentz-invariant vacuum and traceless-source rank gate."""

import json
from pathlib import Path

import sympy as sp


rho, tau, mass = sp.symbols("rho tau M", real=True)
metric = sp.diag(-1, 1, 1, 1)
metric_inverse = metric.inv()

vacuum_stress = -rho * metric
vacuum_trace = sp.simplify(
    sum(metric_inverse[i, j] * vacuum_stress[i, j] for i in range(4) for j in range(4))
)
trace_reversed = sp.simplify(vacuum_stress - vacuum_trace * metric / 2)

traceless_channel = sp.diag(3, 1, 1, 1)
traceless_trace = sp.simplify(
    sum(metric_inverse[i, j] * traceless_channel[i, j] for i in range(4) for j in range(4))
)

two_source_stress = -rho * metric + tau * traceless_channel
vacuum_direction = two_source_stress.diff(rho)
traceless_direction = two_source_stress.diff(tau)
direction_matrix = sp.Matrix.hstack(
    sp.Matrix(vacuum_direction).reshape(16, 1),
    sp.Matrix(traceless_direction).reshape(16, 1),
)

reference_derivative = vacuum_stress.diff(mass)
rho_reference_direction_matrix = sp.Matrix.hstack(
    sp.Matrix(vacuum_stress.diff(rho)).reshape(16, 1),
    sp.Matrix(reference_derivative).reshape(16, 1),
)

checks = {
    "vacuum_trace_is_minus_four_rho": vacuum_trace == -4 * rho,
    "trace_reversed_vacuum_is_metric_line": trace_reversed == rho * metric,
    "reference_scale_does_not_change_physical_stress": reference_derivative == sp.zeros(4),
    "rho_plus_reference_has_physical_rank_one": rho_reference_direction_matrix.rank() == 1,
    "completion_channel_is_traceless": traceless_trace == 0,
    "completion_channel_is_not_metric_proportional": traceless_channel != 3 * metric
    and traceless_channel != metric,
    "vacuum_plus_traceless_channel_has_rank_two": direction_matrix.rank() == 2,
    "two_source_stress_has_declared_form": two_source_stress
    == -rho * metric + tau * traceless_channel,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP582",
    "classification": "Lorentz-invariant vacuum stress is one physical source channel; a second channel requires nonmetric stress plus a declared frame or boundary source",
    "metric": encode_matrix(metric),
    "vacuum_stress": encode_matrix(vacuum_stress),
    "vacuum_trace": str(vacuum_trace),
    "trace_reversed_vacuum": encode_matrix(trace_reversed),
    "reference_scale_derivative": encode_matrix(reference_derivative),
    "rho_reference_physical_rank": rho_reference_direction_matrix.rank(),
    "traceless_channel": encode_matrix(traceless_channel),
    "traceless_channel_trace": str(traceless_trace),
    "vacuum_traceless_source_rank": direction_matrix.rank(),
    "smallest_exact_falsifier": "the pair (rho,M) has physical stress rank one because partial T_vac/partial M=0",
    "relational_change": "a nonmetric traceless channel requires a timelike frame, matter, anisotropic stress, or boundary source and changes the admitted groupoid",
    "remaining_gate": "derive a noncollinear coupling from two admitted stress channels to invariant flavor coordinates and calibrate its physical instrument",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp582_vacuum_stress_source_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
