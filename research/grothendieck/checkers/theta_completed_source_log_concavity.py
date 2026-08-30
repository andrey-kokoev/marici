"""Hostile log-curvature scan of the completed theta source Phi."""

import json
import math
from pathlib import Path


def log_phi(u, max_label=12):
    scale = math.exp(2.0 * u)
    logs = []
    for label in range(1, max_label + 1):
        a = math.pi * label * label
        logs.append(
            math.log(2.0 * a)
            + 2.5 * u
            + math.log(2.0 * a * scale - 3.0)
            - a * scale
        )
    largest = max(logs)
    return largest + math.log(math.fsum(math.exp(value - largest) for value in logs))


def row(u, step=1.0e-4):
    center = log_phi(u)
    left = log_phi(u - step)
    right = log_phi(u + step)
    curvature = (right - 2.0 * center + left) / step**2
    third_step = 1.0e-3
    log_third = (
        log_phi(u + 2.0 * third_step)
        - 2.0 * log_phi(u + third_step)
        + 2.0 * log_phi(u - third_step)
        - log_phi(u - 2.0 * third_step)
    ) / (2.0 * third_step**3)
    half_step = third_step / 2.0
    log_third_half_step = (
        log_phi(u + 2.0 * half_step)
        - 2.0 * log_phi(u + half_step)
        + 2.0 * log_phi(u - half_step)
        - log_phi(u - 2.0 * half_step)
    ) / (2.0 * half_step**3)
    return {
        "u": u,
        "log_Phi": center,
        "log_curvature": curvature,
        "log_concave_at_sample": curvature <= 0.0,
        "potential_curvature_derivative": -log_third,
        "potential_curvature_derivative_half_step": -log_third_half_step,
        "third_derivative_step_discrepancy": abs(log_third - log_third_half_step),
        "potential_curvature_increasing_at_both_steps": (
            -log_third >= 0.0 and -log_third_half_step >= 0.0
        ),
    }


u_values = [index / 100.0 for index in range(0, 401)]
rows = [row(u) for u in u_values]
violations = [item for item in rows if not item["log_concave_at_sample"]]
curvature_monotonicity_violations = [
    item
    for item in rows[1:]
    if not item["potential_curvature_increasing_at_both_steps"]
]
result = {
    "source": "Phi(u)=sum_n (4(pi n^2)^2 e^(9u/2)-6 pi n^2 e^(5u/2)) exp(-pi n^2 e^(2u))",
    "sample_interval": [u_values[0], u_values[-1]],
    "sample_step": 0.01,
    "finite_difference_step": 1.0e-4,
    "all_samples_log_concave": not violations,
    "first_violation": violations[0] if violations else None,
    "least_negative_curvature_row": max(rows, key=lambda item: item["log_curvature"]),
    "most_negative_curvature_row": min(rows, key=lambda item: item["log_curvature"]),
    "all_positive_samples_have_increasing_potential_curvature_at_both_steps": (
        not curvature_monotonicity_violations
    ),
    "first_curvature_monotonicity_violation": (
        curvature_monotonicity_violations[0]
        if curvature_monotonicity_violations
        else None
    ),
    "smallest_potential_curvature_derivative_row": min(
        rows[1:], key=lambda item: item["potential_curvature_derivative"]
    ),
    "largest_third_derivative_step_discrepancy_row": max(
        rows[1:], key=lambda item: item["third_derivative_step_discrepancy"]
    ),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-completed-source-log-concavity.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
