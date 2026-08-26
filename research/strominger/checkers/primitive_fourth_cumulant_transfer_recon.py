"""Floating-point reconnaissance for the theta adjacent-bias transfer margin."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = (
    ROOT
    / "research"
    / "strominger"
    / "primitive-fourth-cumulant-transfer-normal-form.md"
)
RESULT = (
    ROOT
    / "research"
    / "strominger"
    / "results"
    / "primitive_fourth_cumulant_transfer_recon.json"
)


def moments(c: float, q: float, panels: int) -> tuple[tuple[float, ...], tuple[float, ...]]:
    """Return raw log-moments through order three for Q_q and Q_(q-1)."""
    upper = 60.0
    step = upper / panels
    sums_q = [0.0, 0.0, 0.0, 0.0]
    sums_minus = [0.0, 0.0, 0.0, 0.0]
    for index in range(1, panels):
        x = index * step
        coefficient = 4.0 if index % 2 else 2.0
        exp_scaled = math.exp(x / c)
        carrier = (
            math.exp(5.0 * x / (4.0 * c) + c - c * exp_scaled)
            * (2.0 * c * exp_scaled - 3.0)
        )
        base_minus = x ** (q - 1.0) * carrier
        base_q = x * base_minus
        log_x = math.log(x)
        log_power = 1.0
        for order in range(4):
            sums_q[order] += coefficient * base_q * log_power
            sums_minus[order] += coefficient * base_minus * log_power
            log_power *= log_x
    scale = step / 3.0
    raw_q = tuple(value * scale for value in sums_q)
    raw_minus = tuple(value * scale for value in sums_minus)
    return raw_q, raw_minus


def cumulants(raw: tuple[float, ...]) -> tuple[float, float, float]:
    mean = raw[1] / raw[0]
    second = raw[2] / raw[0]
    third = raw[3] / raw[0]
    variance = second - mean * mean
    third_central = third - 3.0 * mean * second + 2.0 * mean**3
    return mean, variance, third_central


def state(c_wall: float, q: float, panels: int) -> dict[str, float]:
    raw_q, raw_minus = moments(c_wall, q, panels)
    mean_q, variance_q, skew_q = cumulants(raw_q)
    mean_minus, variance_minus, skew_minus = cumulants(raw_minus)
    d = mean_q - mean_minus
    variance_step = variance_minus - variance_q
    skew_step = skew_q - skew_minus
    A = 1.0 - q * d
    b = variance_step / (d * d)
    c = skew_step / (d * d * d)
    margin = 2.0 + A + 3.0 * A * b - (1.0 - A) * c
    return {
        "wall_c": c_wall,
        "q": q,
        "A": A,
        "b": b,
        "c": c,
        "margin": margin,
        "d": d,
        "variance_step": variance_step,
        "skew_step": skew_step,
    }


wall_values = (
    1.500001,
    1.55,
    1.6,
    1.65,
    1.7,
    1.75,
    1.8,
    1.9,
    2.0,
    3.0,
    5.0,
    10.0,
    20.0,
    50.0,
    100.0,
    200.0,
)
q_values = tuple(4.0 + index / 10.0 for index in range(61))
panel_count = 6000
states = [
    state(c_wall, q, panel_count)
    for c_wall in wall_values
    for q in q_values
]
minimum = min(states, key=lambda item: item["margin"])
refined = state(minimum["wall_c"], minimum["q"], 12000)
refinement_delta = abs(refined["margin"] - minimum["margin"])
far_wall_q4 = [
    {
        "wall_c": item["wall_c"],
        "margin": item["margin"],
        "c2_margin": item["wall_c"] ** 2 * item["margin"],
        "c3_margin": item["wall_c"] ** 3 * item["margin"],
    }
    for item in states
    if item["q"] == 4.0 and item["wall_c"] >= 20.0
]
grade_monotonicity = all(
    all(
        row[index + 1]["margin"] > row[index]["margin"]
        for index in range(len(row) - 1)
    )
    for c_wall in wall_values
    for row in [[item for item in states if item["wall_c"] == c_wall]]
)
grade_steps = [
    {
        "wall_c": c_wall,
        "q_left": row[index]["q"],
        "q_right": row[index + 1]["q"],
        "margin_delta": row[index + 1]["margin"] - row[index]["margin"],
    }
    for c_wall in wall_values
    for row in [[item for item in states if item["wall_c"] == c_wall]]
    for index in range(len(row) - 1)
]
smallest_grade_step = min(grade_steps, key=lambda item: item["margin_delta"])
grade_minimum_by_wall = [
    min(
        (item for item in states if item["wall_c"] == c_wall),
        key=lambda item: item["margin"],
    )
    for c_wall in wall_values
]
wall_monotonicity = all(
    all(
        row[index + 1]["margin"] < row[index]["margin"]
        for index in range(len(row) - 1)
    )
    for q in q_values
    for row in [[item for item in states if item["q"] == q]]
)

checks = {
    "all_sampled_d_are_positive": all(item["d"] > 0.0 for item in states),
    "all_sampled_A_are_nonnegative": all(item["A"] >= -1e-9 for item in states),
    "all_sampled_variance_steps_are_positive": all(
        item["variance_step"] > 0.0 for item in states
    ),
    "all_sampled_skew_steps_are_positive": all(
        item["skew_step"] > 0.0 for item in states
    ),
    "all_sampled_normalized_margins_are_positive": all(
        item["margin"] > 0.0 for item in states
    ),
    "minimum_margin_is_stable_under_panel_doubling": refinement_delta < 2e-6,
    "sampled_margin_is_not_globally_monotone_in_q": not grade_monotonicity,
    "sampled_margin_decreases_with_wall_at_fixed_q": wall_monotonicity,
    "reconnaissance_is_not_reported_as_proof": True,
}

payload = {
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "wall_values": wall_values,
        "q_grid": {"minimum": 4.0, "maximum": 10.0, "step": 0.1},
        "panels": panel_count,
        "minimum_state": minimum,
        "refined_minimum_state": refined,
        "refinement_delta": refinement_delta,
        "far_wall_q4_scaling": far_wall_q4,
        "smallest_grade_step": smallest_grade_step,
        "grade_minimum_by_wall": grade_minimum_by_wall,
        "status": "floating_point_reconnaissance_only",
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Composite-Simpson reconnaissance can falsify a proposed pointwise "
        "margin on this grid. Positivity on the grid is not an analytic proof."
    ),
}

RESULT.write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(payload, indent=2, sort_keys=True))
