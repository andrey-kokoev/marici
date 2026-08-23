"""Hostile spectrum test of the canonical Phi ground-state transform.

Finite differences and Sturm bisection are reconnaissance, not a certified
operator computation.
"""

import json
import math
from pathlib import Path


def log_phi_positive(u, max_label=12):
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


def log_phi(u):
    return log_phi_positive(abs(u))


def potential(u, derivative_step=2.0e-4):
    center = log_phi(u)
    left = log_phi(u - derivative_step)
    right = log_phi(u + derivative_step)
    first = (right - left) / (2.0 * derivative_step)
    second = (right - 2.0 * center + left) / derivative_step**2
    return 0.25 + 0.25 * first * first + 0.5 * second


def sturm_count(diagonal, off_diagonal, value):
    count = 0
    pivot = diagonal[0] - value
    if pivot < 0.0:
        count += 1
    for index in range(1, len(diagonal)):
        if abs(pivot) < 1.0e-20:
            pivot = -1.0e-20 if pivot < 0.0 else 1.0e-20
        pivot = diagonal[index] - value - off_diagonal * off_diagonal / pivot
        if pivot < 0.0:
            count += 1
    return count


def eigenvalue(diagonal, off_diagonal, index, lower, upper):
    for _ in range(90):
        middle = 0.5 * (lower + upper)
        if sturm_count(diagonal, off_diagonal, middle) <= index:
            lower = middle
        else:
            upper = middle
    return 0.5 * (lower + upper)


def spectrum(cutoff, step, count=14):
    point_count = int(round(2.0 * cutoff / step)) - 1
    points = [-cutoff + (index + 1) * step for index in range(point_count)]
    inverse_step_squared = 1.0 / step**2
    diagonal = [2.0 * inverse_step_squared + potential(u) for u in points]
    off_diagonal = -inverse_step_squared
    lower = min(value - 2.0 * inverse_step_squared for value in diagonal)
    upper = max(value + 2.0 * inverse_step_squared for value in diagonal)
    values = [
        eigenvalue(diagonal, off_diagonal, index, lower, upper)
        for index in range(count)
    ]
    return {
        "cutoff": cutoff,
        "step": step,
        "eigenvalues": values,
        "first_excitation_above_ground": values[1] - values[0],
        "closest_to_first_reconstructed_rate": min(
            values, key=lambda value: abs(value - 200.04045599)
        ),
    }


rows = [spectrum(2.0, step) for step in [0.004, 0.002]]
result = {
    "operator": "A_Phi=1/4+Q_Phi^*Q_Phi, Q_Phi=d/du-(log Phi)'/2",
    "rows": rows,
    "expected_ground_eigenvalue": 0.25,
    "target_first_rate": 200.04045599,
    "matches_target_as_first_excitation": all(
        abs(row["eigenvalues"][1] - 200.04045599) < 1.0
        for row in rows
    ),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-ground-state-operator-spectrum.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
