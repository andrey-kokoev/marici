"""Derivative-light chord scan for concavity of 1/sqrt(F')."""
import json
import math
from pathlib import Path

from reduced_source_pick_hostile_scan import reduced_F


def slope(x, depth, relative_height):
    h = relative_height * max(1.0, x)
    q1 = reduced_F(complex(x, h), depth).imag / h
    q2 = reduced_F(complex(x, h / 2), depth).imag / (h / 2)
    return (4 * q2 - q1) / 3


def reciprocal_sqrt_slope(x, depth, relative_height):
    value = slope(x, depth, relative_height)
    assert value > 0
    return 1 / math.sqrt(value)


xs = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
pairs = [(x, y) for i, x in enumerate(xs) for y in xs[i + 1 :]]


def scan(depth, height):
    rows = []
    for x, y in pairs:
        midpoint = (x + y) / 2
        gap = reciprocal_sqrt_slope(midpoint, depth, height) - (
            reciprocal_sqrt_slope(x, depth, height) + reciprocal_sqrt_slope(y, depth, height)
        ) / 2
        rows.append((gap, x, midpoint, y))
    return rows


baseline = scan(44, 1e-4)
control = scan(40, 5e-5)
minimum = min(baseline)
control_minimum = min(control)
maximum_discrepancy = max(abs(a[0] - b[0]) for a, b in zip(baseline, control))
robust_margin = min(minimum[0], control_minimum[0]) - maximum_discrepancy

result = {
    "endpoint_grid": xs,
    "chord_count": len(pairs),
    "minimum_baseline_midpoint_gap": minimum[0],
    "minimum_baseline_chord": minimum[1:],
    "minimum_control_midpoint_gap": control_minimum[0],
    "minimum_control_chord": control_minimum[1:],
    "maximum_baseline_control_discrepancy": maximum_discrepancy,
    "conservative_robust_margin": robust_margin,
    "all_sampled_chords_concave_in_both_runs": minimum[0] > 0 and control_minimum[0] > 0,
    "robust_positive_after_global_discrepancy": robust_margin > 0,
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-source-reciprocal-slope-concavity-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
