"""Hostile scan of the first nontrivial diagonal Loewner contact density."""
import json
from pathlib import Path

from reduced_source_pick_hostile_scan import reduced_F


def extrapolate_zero(q1, q2, q4):
    """Fit q(h)=a+b*h^2+c*h^4 from values at h,h/2,h/4; return a,b."""
    # Put r=h^2 and absorb the unknown scale: nodes are 1, 1/4, 1/16.
    a = (q1 - 20 * q2 + 64 * q4) / 45
    b_scaled = (-4 * q1 + 68 * q2 - 64 * q4) / 9
    return a, b_scaled


def derivatives(x, depth=48, relative_step=0.01):
    h = relative_step * max(1.0, x)
    f0 = reduced_F(complex(x, 0), depth).real
    values = [reduced_F(complex(x, h / scale), depth) for scale in (1, 2, 4)]
    odd = [value.imag / (h / scale) for value, scale in zip(values, (1, 2, 4))]
    even = [2 * (f0 - value.real) / (h / scale) ** 2 for value, scale in zip(values, (1, 2, 4))]
    f1, odd_b = extrapolate_zero(*odd)
    f2, _ = extrapolate_zero(*even)
    # odd_b is the coefficient of (h/scale)^2 after normalization by h^2.
    f3 = -6 * odd_b / h**2
    return f1, f2, f3, h


xs = [10 ** (-2 + k / 8) for k in range(33)]  # 1e-2 through 1e2
rows = []
confirmation_rows = []
for x in xs:
    f1, f2, f3, h = derivatives(x)
    curvature = f1 * f3 / 6 - f2 * f2 / 4
    rows.append((curvature, x, h, f1, f2, f3))
    g1, g2, g3, gh = derivatives(x, depth=44, relative_step=0.005)
    confirmation_rows.append((g1 * g3 / 6 - g2 * g2 / 4, x, gh))

minimum = min(rows)
negative = [row for row in rows if row[0] < 0]
confirmation_minimum = min(confirmation_rows)
maximum_control_discrepancy = max(abs(row[0] - control[0]) for row, control in zip(rows, confirmation_rows))
quarter_row = min(rows, key=lambda row: abs(row[1] - 0.25))
certified_quarter_curvature = 3.1070157152602844e-8
quarter_relative_error = abs(quarter_row[0] - certified_quarter_curvature) / certified_quarter_curvature
result = {
    "x_range": [xs[0], xs[-1]],
    "sample_count": len(xs),
    "minimum_curvature": minimum[0],
    "minimum_location_x": minimum[1],
    "minimum_row": {
        "step": minimum[2],
        "F1": minimum[3],
        "F2": minimum[4],
        "F3": minimum[5],
    },
    "negative_sample_count": len(negative),
    "baseline_no_negative_curvature_found": not negative,
    "confirmation_minimum_curvature": confirmation_minimum[0],
    "confirmation_minimum_location_x": confirmation_minimum[1],
    "maximum_step_depth_control_discrepancy": maximum_control_discrepancy,
    "quarter_point_numerical_curvature": quarter_row[0],
    "quarter_point_certified_curvature_midpoint": certified_quarter_curvature,
    "quarter_point_relative_error": quarter_relative_error,
    "evaluator_stable_enough_for_sign_claim": False,
    "reason_unresolved": "step/depth control changes sign and misses certified quarter-point curvature",
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-source-loewner-diagonal-curvature-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
