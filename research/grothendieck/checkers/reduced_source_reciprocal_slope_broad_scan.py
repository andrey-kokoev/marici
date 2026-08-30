"""Broad hostile chord scan for concavity of the reciprocal source slope."""
import json
import math
from pathlib import Path

from reduced_source_pick_hostile_scan import reduced_F


def slope(x, depth, relative_height):
    h = relative_height * max(1.0, x)
    q1 = reduced_F(complex(x, h), depth).imag / h
    q2 = reduced_F(complex(x, h / 2), depth).imag / (h / 2)
    return (4 * q2 - q1) / 3


def height(x, depth, relative_height):
    derivative = slope(x, depth, relative_height)
    if derivative <= 0:
        return None
    return 1 / math.sqrt(derivative)


xs = [10.0**power for power in range(-6, 9)]
pairs = [(x, y) for i, x in enumerate(xs) for y in xs[i + 1 :]]


def scan(depth, relative_height):
    rows = []
    for x, y in pairs:
        midpoint = (x + y) / 2
        hx = height(x, depth, relative_height)
        hm = height(midpoint, depth, relative_height)
        hy = height(y, depth, relative_height)
        gap = None if None in (hx, hm, hy) else hm - (hx + hy) / 2
        rows.append((gap, x, midpoint, y))
    return rows


baseline = scan(48, 1e-4)
control = scan(44, 5e-5)
valid = [(a, b) for a, b in zip(baseline, control) if a[0] is not None and b[0] is not None]
invalid_count = len(pairs) - len(valid)
minimum = min((a for a, _ in valid), key=lambda row: row[0])
control_minimum = min((b for _, b in valid), key=lambda row: row[0])
negative_baseline = [row for row, _ in valid if row[0] < 0]
negative_control = [row for _, row in valid if row[0] < 0]
maximum_discrepancy = max(abs(a[0] - b[0]) for a, b in valid)
robust_negative = [
    (a[0], b[0], a[1], a[2], a[3])
    for a, b in valid
    if a[0] < -maximum_discrepancy and b[0] < -maximum_discrepancy
]
tail = [(a, b) for a, b in valid if a[1] >= 1]
tail_minimum = min((a for a, _ in tail), key=lambda row: row[0])
tail_control_minimum = min((b for _, b in tail), key=lambda row: row[0])

result = {
    "endpoint_range": [xs[0], xs[-1]],
    "endpoint_count": len(xs),
    "chord_count": len(pairs),
    "invalid_nonpositive_slope_count": invalid_count,
    "minimum_baseline_gap": minimum[0],
    "minimum_baseline_chord": minimum[1:],
    "minimum_control_gap": control_minimum[0],
    "minimum_control_chord": control_minimum[1:],
    "negative_baseline_count": len(negative_baseline),
    "negative_control_count": len(negative_control),
    "maximum_baseline_control_discrepancy": maximum_discrepancy,
    "robust_negative_count_after_global_discrepancy": len(robust_negative),
    "negative_rows_baseline": negative_baseline,
    "negative_rows_control": negative_control,
    "minimum_tail_gap_for_left_endpoint_at_least_one": tail_minimum[0],
    "minimum_tail_control_gap_for_left_endpoint_at_least_one": tail_control_minimum[0],
    "all_broad_chords_positive_in_both_runs": not negative_baseline and not negative_control and not invalid_count,
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-source-reciprocal-slope-broad-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
