"""Hostile ordered-minor scan for TP2/TP3 of K(x-y)."""

import itertools
import json
import math
from pathlib import Path

def precursor(u, max_label=16):
    u = abs(float(u))
    x_scale = math.exp(2 * u)
    return math.exp(-u / 2) / 2 - math.fsum(
        math.exp(u / 2 - math.pi * n * n * x_scale)
        for n in range(1, max_label + 1)
    )


def minor(xs, ys):
    matrix = [[precursor(x - y) for y in ys] for x in xs]
    if len(xs) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(xs) == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    determinant = 0.0
    for permutation in itertools.permutations(range(len(xs))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(xs))
            for right in range(left + 1, len(xs))
        )
        term = math.prod(matrix[row][permutation[row]] for row in range(len(xs)))
        determinant += (-1.0 if inversions % 2 else 1.0) * term
    return determinant


grid = [index / 2 for index in range(-4, 5)]
rows = []
for order in (2, 3, 4):
    smallest = None
    negative = None
    count = 0
    for xs in itertools.combinations(grid, order):
        for ys in itertools.combinations(grid, order):
            determinant = minor(xs, ys)
            count += 1
            scale = max(abs(value) for row_values in [[precursor(x - y) for y in ys] for x in xs] for value in row_values)
            tolerance = 128 * math.ulp(1.0) * max(scale**order, 1e-300)
            record = {
                "x": list(xs),
                "y": list(ys),
                "determinant": determinant,
                "negative_tolerance": tolerance,
            }
            if smallest is None or determinant < smallest["determinant"]:
                smallest = record
            if determinant < -tolerance and negative is None:
                negative = record
    rows.append(
        {
            "order": order,
            "minor_count": count,
            "smallest_minor": smallest,
            "first_negative_minor": negative,
            "all_sampled_minors_nonnegative": negative is None,
        }
    )

result = {
    "kernel": "K(x-y), K(u)=cosh(u/2)-exp(u/2)*Theta(exp(2u))/2",
    "ordered_grid": grid,
    "arithmetic": "binary64 with scale-aware negative threshold",
    "max_theta_label": 16,
    "orders": rows,
    "all_sampled_tp4_conditions_pass": all(row["all_sampled_minors_nonnegative"] for row in rows),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-renormalized-precursor-tp3.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row)
    print(f"all_sampled_tp4_conditions_pass={result['all_sampled_tp4_conditions_pass']}")
